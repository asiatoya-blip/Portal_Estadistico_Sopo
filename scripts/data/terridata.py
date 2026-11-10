"""Actualiza las cifras del portal desde TerriData (DNP) para Sopó (DANE 25758). Sin dependencias.

Uso: python scripts/data/terridata.py [--archivo ruta.txt.zip]
- Descarga la exportación en texto de TerriData (o usa --archivo), valida su estructura y guarda la instantánea en
  data_base/terridata/ (control de cambios en Git, ADR-002/011).
- Recalcula valor, cambio, estado y serie de cada tarjeta de prototipo/portal.json según su bloque "terridata".
- Sale con código 1 y sin escribir nada si la validación falla.
"""
import argparse
import csv
import datetime as dt
import email.utils
import io
import json
import sys
import urllib.request
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
URL = "https://terridata.dnp.gov.co/assets/docs/txt/entidades/TerriData25758.txt.zip"
ENTIDAD = "25758"
COLUMNAS = ["Código Departamento", "Departamento", "Código Entidad", "Entidad", "Dimensión", "Subcategoría", "Indicador",
            "Dato Numérico", "Dato Cualitativo", "Año", "Mes", "Fuente", "Unidad de Medida"]
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
PORTAL = RAIZ / "prototipo" / "portal.json"
INSTANTANEA = RAIZ / "data_base" / "terridata" / "TerriData25758.txt.zip"


def numero(texto):
    """'13.883,00' -> 13883.0 (formato colombiano de TerriData)."""
    return float(texto.strip().replace(".", "").replace(",", "."))


def es(v, dec):
    """Número con formato colombiano: miles con punto, decimales con coma."""
    return f"{v:,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def con_signo(v, dec):
    return ("+" if v >= 0 else "−") + es(abs(v), dec)


def leer(zbytes):
    z = zipfile.ZipFile(io.BytesIO(zbytes))
    txt = [n for n in z.namelist() if n.lower().endswith(".txt")]
    if len(txt) != 1:
        raise ValueError(f"se esperaba un .txt en el zip y hay {txt}")
    filas = list(csv.reader(io.StringIO(z.read(txt[0]).decode("utf-8-sig")), delimiter="|"))
    if filas[0] != COLUMNAS:
        raise ValueError(f"encabezado distinto al esperado: {filas[0]}")
    datos = filas[1:]
    if len(datos) < 1000:
        raise ValueError(f"muy pocas filas: {len(datos)}")
    malas = [i for i, f in enumerate(datos, 2) if len(f) != 13 or f[2] != ENTIDAD]
    if malas:
        raise ValueError(f"filas con columnas o entidad inválidas, p. ej. línea {malas[0]}")
    return datos


def serie(datos, regla, hasta):
    """Serie anual de un indicador; si un año se repite gana la última fila (como en el fixture)."""
    s = {}
    for f in datos:
        if f[6] != regla["indicador"] or not f[7].strip():
            continue
        if regla.get("dimension") and f[4] != regla["dimension"]:
            continue
        ano = int(f[9])
        if regla.get("desde", 0) <= ano <= hasta:
            s[ano] = numero(f[7])
    if len(s) < 2:
        raise ValueError(f"'{regla['indicador']}' tiene menos de dos años de datos")
    return dict(sorted(s.items()))


def tarjeta(k, s):
    r = k["terridata"]
    anos = list(s)
    ult, ant = anos[-1], anos[-2]
    v, w = s[ult], s[ant]
    fmt = {"entero": lambda x: es(x, 0), "decimal1": lambda x: es(x, 1), "porcentaje1": lambda x: es(x, 1) + " %",
           "billones": lambda x: "$" + es(x / 1000, 2) + " bill."}[r["formato"]]
    delta = v - w
    cambio = {"absoluto": f"{con_signo(delta, 0)} frente a {ant}", "absoluto1": f"{con_signo(delta, 1)} frente a {ant}",
              "puntos": f"{con_signo(delta, 1)} puntos frente a {ant}",
              "porcentual": f"{con_signo(delta / w * 100, 1)} % frente a {ant}"}[r["cambio"]]
    estado = "estable" if r["sentido"] == 0 or delta == 0 else ("mejora" if delta * r["sentido"] > 0 else "empeora")
    k.update(valor=fmt(v), unidad=r["unidad"].format(año=ult), cambio=cambio, estado=estado,
             serie={str(a): round(x, 2) for a, x in s.items()})


# Autoverificación de las reglas de formato y cálculo
assert numero("13.883,00") == 13883.0 and numero("61,39") == 61.39
_k = {"terridata": {"formato": "billones", "cambio": "porcentual", "sentido": 1, "unidad": "pesos, {año}"}}
tarjeta(_k, {2022: 1178.25, 2023: 1281.67})
assert _k["valor"] == "$1,28 bill." and _k["cambio"] == "+8,8 % frente a 2022" and _k["estado"] == "mejora", _k
_k = {"terridata": {"formato": "decimal1", "cambio": "absoluto1", "sentido": -1, "unidad": "{año}"}}
tarjeta(_k, {2024: 276.3, 2025: 277.5})
assert _k["cambio"] == "+1,2 frente a 2024" and _k["estado"] == "empeora", _k


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--archivo", help="usar un .txt.zip local en vez de descargar")
    args = ap.parse_args()
    if args.archivo:
        zbytes = Path(args.archivo).read_bytes()
        fecha = dt.date.today()
    else:
        req = urllib.request.Request(URL, headers={"User-Agent": "portal-estadistico-sopo/1.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            zbytes = resp.read()
            lm = resp.headers.get("Last-Modified")
            fecha = email.utils.parsedate_to_datetime(lm).date() if lm else dt.date.today()
    try:
        datos = leer(zbytes)
        portal = json.loads(PORTAL.read_text(encoding="utf-8"))
        hoy = dt.date.today().year
        for k in portal["kpis"]:
            tarjeta(k, serie(datos, k["terridata"], hoy))
    except ValueError as err:
        print(f"TerriData no válido, no se actualiza nada: {err}", file=sys.stderr)
        return 1
    portal["corte"] = f"{MESES[fecha.month - 1]} de {fecha.year}"
    INSTANTANEA.parent.mkdir(parents=True, exist_ok=True)
    INSTANTANEA.write_bytes(zbytes)
    PORTAL.write_text(json.dumps(portal, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for k in portal["kpis"]:
        print(f"{k['etiqueta']}: {k['valor']} ({k['cambio']}, {k['estado']})")
    print(f"Corte: {portal['corte']}; {len(datos)} filas validadas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
