"""Genera prototipo/index.html desde portal.json (sin dependencias). Uso: python prototipo/build.py"""
import json
import re
from html import escape as e
from pathlib import Path

AQUI = Path(__file__).parent
D = json.loads((AQUI / "portal.json").read_text(encoding="utf-8"))
SEGURO = re.compile(r"^[A-Za-z0-9_]{1,80}$")  # libro y hoja: lista blanca (revisión de seguridad 2026-11-10)
CDN = "https://cdn.www.gov.co/layout-govco-v5"
HOJAS = {h["id"]: (g, h) for g in D["grupos"] for h in g["hojas"]}
ESTADO = {"mejora": "Mejora", "empeora": "Empeora", "estable": "Sin valoración"}
FLECHA = {"sube": "M12 19V5M5 12l7-7 7 7", "baja": "M12 5v14M5 12l7 7 7-7"}
# Íconos de trazo propios (24×24), uno por entrada del menú
ICONO = {
    "resumen": "M4 13h6V4H4zM14 20h6v-9h-6zM4 20h6v-4H4zM14 7h6V4h-6z",
    "Indicadores territoriales": "M4 20V10M10 20V4M16 20v-7M22 20H2",
    "Deporte y recreación": "M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11zM12 12.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5",
    "Datos curiosos": "M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z",
}


def svg(path, clase="nxgov-icon"):
    return f'<svg class="{clase}" aria-hidden="true" viewBox="0 0 24 24"><path d="{path}"/></svg>'


def url(h, embed):
    assert SEGURO.match(h["libro"]) and SEGURO.match(h["hoja"]), h
    base = f"https://public.tableau.com/views/{h['libro']}/{h['hoja']}"
    return base + ("?:showVizHome=no&:embed=y&:tabs=n&:toolbar=n&:language=es-ES" if embed else "?:language=es-ES")


def miles(v):
    return f"{v:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".").removesuffix(",0")


def tendencia(serie, w=160, h=44, pad=4):
    """Mini tendencia SVG de una serie anual de TerriData; devuelve (puntos, ultimo_xy, descripción)."""
    anos = sorted(serie)
    vals = [serie[a] for a in anos]
    lo, hi = min(vals), max(vals)
    rango = (hi - lo) or 1
    pts = [(pad + i * (w - 2 * pad) / (len(vals) - 1), pad + (hi - v) * (h - 2 * pad) / rango) for i, v in enumerate(vals)]
    desc = f"Tendencia {anos[0]}–{anos[-1]}: de {miles(vals[0])} a {miles(vals[-1])}; máximo {miles(hi)}."
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in pts), pts[-1], desc


# Autoverificación: el último punto queda al borde derecho y el máximo arriba
_p, (_x, _y), _d = tendencia({"2020": 1, "2021": 3, "2022": 2})
assert abs(_x - 156) < 0.01 and "máximo 3" in _d and _p.split()[1].endswith(",4.0")


def kpi(k):
    puntos, (lx, ly), desc = tendencia(k["serie"])
    area = f"4,44 {puntos} 156,44"
    sentido = "baja" if k["cambio"].startswith("−") else "sube"
    h = HOJAS[k["hoja"]][1]
    return f"""
          <a class="nxgov-kpi nxgov-kpi--{k['estado']}" href="#{h['id']}">
            <span class="nxgov-kpi__top"><span class="nxgov-kpi__label">{e(k['etiqueta'])}</span><span class="nxgov-kpi__chip">{ESTADO[k['estado']]}</span></span>
            <span class="nxgov-kpi__value">{e(k['valor'])}</span>
            <span class="nxgov-kpi__unit">{e(k['unidad'])}</span>
            <svg class="nxgov-kpi__trend" viewBox="0 0 160 44" preserveAspectRatio="none" role="img" aria-label="{e(desc)}"><polygon points="{area}"/><polyline points="{puntos}"/><circle cx="{lx:.1f}" cy="{ly:.1f}" r="3"/></svg>
            <span class="nxgov-kpi__change">{svg(FLECHA[sentido])}{e(k['cambio'])}</span>
            <span class="nxgov-kpi__source">{e(k['fuente'])} · <span class="nxgov-kpi__go">Ver tablero<span class="nxgov-sr-only"> de {e(h['titulo'])}</span></span></span>
          </a>"""


def iframe(h):
    return (f'<iframe class="nxgov-board__frame" src="{e(url(h, True))}" title="Tablero interactivo: {e(h["titulo"])}" lang="es" '
            f'loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox" '
            f'referrerpolicy="strict-origin" allow="fullscreen" allowfullscreen></iframe>')


def resumen(h):
    if h["resumen"]:
        return f'<p class="nxgov-view__summary">{e(h["resumen"])}</p>'
    return ('<p class="nxgov-view__summary nxgov-view__summary--pending">Resumen pendiente: la Alcaldía publicará '
            'aquí, en texto, lo que muestra este tablero.</p>')


def vista_hoja(g, h, i, lista):
    tabs = ""
    if len(lista) > 1:
        tabs = '<nav class="nxgov-tabs" aria-label="Tableros de ' + e(g["nombre"]) + '"><ul class="nxgov-tabs__list">' + "".join(
            f'<li><a class="nxgov-tabs__link" href="#{x["id"]}"{" aria-current=\"page\"" if x is h else ""}>{e(x["titulo"])}</a></li>'
            for x in lista) + "</ul></nav>"
    prev_h, next_h = lista[i - 1] if i else None, lista[i + 1] if i + 1 < len(lista) else None
    pager = ""
    if prev_h or next_h:
        pager = '<nav class="nxgov-pager" aria-label="Tablero anterior y siguiente">' + \
            (f'<a class="nxgov-pager__link" href="#{prev_h["id"]}"><span class="nxgov-pager__dir">← Anterior</span>{e(prev_h["titulo"])}</a>' if prev_h else "<span></span>") + \
            (f'<a class="nxgov-pager__link nxgov-pager__link--next" href="#{next_h["id"]}"><span class="nxgov-pager__dir">Siguiente →</span>{e(next_h["titulo"])}</a>' if next_h else "") + "</nav>"
    return f"""
        <section class="nxgov-view" id="{h['id']}" aria-labelledby="{h['id']}-h" data-nxgov-group="{e(g['nombre'])}">
          <header class="nxgov-view__head">
            <p class="nxgov-view__crumb"><a href="#resumen">Resumen</a> <span aria-hidden="true">/</span> {e(g['nombre'])}</p>
            <div class="nxgov-view__title-row">
              <h2 class="nxgov-view__title" id="{h['id']}-h">{e(h['titulo'])}</h2>
              <a class="nxgov-btn" href="{e(url(h, False))}" rel="noopener" target="_blank">Abrir en Tableau Public<span class="nxgov-sr-only"> (otra pestaña)</span></a>
            </div>
          </header>
          {tabs}
          <div class="nxgov-board">
            <div class="nxgov-board__info">{resumen(h)}<p class="nxgov-view__meta">Fuente: {e(h['fuente'])} · Corte: {e(D['corte'])}</p></div>
            <div class="nxgov-board__stage">{iframe(h)}</div>
          </div>
          {pager}
        </section>"""


def menu():
    out = f'<ul class="nxgov-nav__list"><li><a class="nxgov-nav__item" href="#resumen">{svg(ICONO["resumen"])}Resumen</a></li></ul>'
    for g in D["grupos"]:
        hijos = "".join(f'<li><a class="nxgov-nav__sub" href="#{h["id"]}">{e(h["titulo"])}</a></li>' for h in g["hojas"])
        out += (f'<details class="nxgov-nav__group" data-nxgov-group="{e(g["nombre"])}"><summary class="nxgov-nav__item">'
                f'{svg(ICONO[g["nombre"]])}<span class="nxgov-nav__label">{e(g["nombre"])}</span><span class="nxgov-nav__count">{len(g["hojas"])}</span></summary>'
                f'<ul class="nxgov-nav__sublist">{hijos}</ul></details>')
    return out


def colecciones():
    out = ""
    for g in D["grupos"]:
        primeros = "".join(f'<li><a href="#{h["id"]}">{e(h["titulo"])}</a></li>' for h in g["hojas"][:4])
        mas = f'<li class="nxgov-collection__more">y {len(g["hojas"]) - 4} más</li>' if len(g["hojas"]) > 4 else ""
        out += f"""
            <article class="nxgov-collection">
              <span class="nxgov-collection__icon">{svg(ICONO[g['nombre']])}</span>
              <h3 class="nxgov-collection__title"><a href="#{g['hojas'][0]['id']}">{e(g['nombre'])}</a></h3>
              <p class="nxgov-collection__meta">{len(g['hojas'])} {'tablero' if len(g['hojas']) == 1 else 'tableros'} · {e(g['fuente'])}</p>
              <ul class="nxgov-collection__list">{primeros}{mas}</ul>
            </article>"""
    return out


k = D["kpis"]
mejoran = sum(x["estado"] == "mejora" for x in k)
empeoran = sum(x["estado"] == "empeora" for x in k)
dest = HOJAS["demografia"][1]
vistas = "".join(vista_hoja(g, h, i, g["hojas"]) for g in D["grupos"] for i, h in enumerate(g["hojas"]))

pagina = f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' https://cdn.www.gov.co; style-src 'self' https://cdn.www.gov.co; font-src 'self' https://cdn.www.gov.co; img-src 'self' data: https://cdn.www.gov.co; frame-src https://public.tableau.com; object-src 'none'; base-uri 'self'; form-action 'self'">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <title>Portal Estadístico de Sopó</title>
  <meta name="description" content="¿Cómo va Sopó? Cifras oficiales y tableros de Sopó, Cundinamarca, con su fuente y su fecha de corte.">
  <link rel="stylesheet" href="{CDN}/all.css">
  <link rel="stylesheet" href="assets/portal.css">
  <script src="{CDN}/script.js" defer></script>
  <script src="assets/portal.js" defer></script>
</head>
<body class="nxgov-page">
  <a class="nxgov-skip" href="#contenido">Saltar al contenido</a>
  <div class="barra-superior-govco">
    <a href="https://www.gov.co/" target="_blank" rel="noopener" aria-label="Portal del Estado Colombiano - GOV.CO"></a>
  </div>
  <div class="nxgov-a11y">
    <div class="barra-accesibilidad-govco">
      <button class="contrast" type="button" aria-label="Cambiar contraste"><span class="govco-contrast"></span></button>
      <button class="decrease-font-size" type="button" aria-label="Disminuir letra" data-decrease-limit="-5"><span class="govco-font-minimize"></span></button>
      <button class="increase-font-size" type="button" aria-label="Aumentar letra" data-increase-limit="5"><span class="govco-font-maximize"></span></button>
    </div>
  </div>
  <header class="nxgov-header">
    <div class="nxgov-container nxgov-header__inner">
      <a class="nxgov-header__brand" href="#resumen"><img class="nxgov-header__logo" src="assets/logo-sopo.png" width="1080" height="589" alt="Alcaldía de Sopó"><span class="nxgov-header__name">Portal Estadístico</span></a>
      <p class="nxgov-header__cut"><span class="nxgov-header__dot" aria-hidden="true"></span>Datos a {e(D['corte'])}</p>
    </div>
  </header>
  <div class="nxgov-container nxgov-shell">
    <aside class="nxgov-nav">
      <details class="nxgov-nav__menu" open>
        <summary class="nxgov-nav__toggle">Menú de tableros</summary>
        <nav aria-label="Tableros">{menu()}</nav>
      </details>
      <p class="nxgov-nav__note">Fuentes: TerriData (DNP) y libros de la Alcaldía en Tableau Public.</p>
    </aside>
    <main class="nxgov-main" id="contenido">
      <section class="nxgov-view nxgov-view--home" id="resumen" aria-labelledby="resumen-h">
        <header class="nxgov-home__head">
          <h1 class="nxgov-home__title" id="resumen-h">¿Cómo va Sopó?</h1>
          <p class="nxgov-home__lead">Cifras oficiales del municipio con su fuente y su tendencia. Toca una cifra para ver su tablero.</p>
          <ul class="nxgov-pulse" aria-label="Estado frente al año anterior">
            <li class="nxgov-pulse__item nxgov-pulse__item--mejora"><strong>{mejoran}</strong> mejoraron</li>
            <li class="nxgov-pulse__item nxgov-pulse__item--empeora"><strong>{empeoran}</strong> empeoraron</li>
            <li class="nxgov-pulse__item"><strong>{len(k) - mejoran - empeoran}</strong> sin valoración</li>
          </ul>
        </header>
        <h2 class="nxgov-sr-only">Cifras principales</h2>
        <div class="nxgov-kpis">{''.join(kpi(x) for x in k)}
        </div>
        <section class="nxgov-feature" aria-labelledby="destacado-h">
          <div class="nxgov-section-head">
            <h2 class="nxgov-section-head__title" id="destacado-h">Tablero destacado: {e(dest['titulo'])}</h2>
            <a class="nxgov-link" href="#{dest['id']}">Abrir en el visor →</a>
          </div>
          <div class="nxgov-board nxgov-board--feature"><div class="nxgov-board__stage">{iframe(dest)}</div></div>
        </section>
        <section aria-labelledby="explorar-h">
          <div class="nxgov-section-head"><h2 class="nxgov-section-head__title" id="explorar-h">Explorar tableros</h2></div>
          <div class="nxgov-collections">{colecciones()}
          </div>
        </section>
      </section>{vistas}
    </main>
  </div>
  <div class="nxgov-totop"><button class="volver-arriba-govco" type="button" aria-label="Volver arriba"><span class="govco-expand_circle_up"></span></button></div>
  <footer class="pie-pagina-govco">
    <div class="first-section">
      <h4>Alcaldía Municipal de Sopó · Portal Estadístico</h4>
      <div class="logo-container">
        <span class="govco-logo-potencia"></span><span class="separator"></span><img class="nxgov-footer-logo" src="assets/logo-sopo.png" width="1080" height="589" alt="Alcaldía de Sopó">
      </div>
      <h5>Sede principal</h5>
      <ul class="contact-data-container">
        <li><p>Dirección: Carrera 3 # 2-45, Sopó, Cundinamarca</p></li>
        <li><p>Código postal: 251001</p></li>
        <li><p>Horario de atención: lunes a jueves</p><p>7:00 a.m. - 5:00 p.m.; viernes hasta 4:00 p.m.</p></li>
        <li><p>Teléfono conmutador: +57 (1) 587 6644</p></li>
        <li><p>Correo institucional: <a href="mailto:contactenos@sopo-cundinamarca.gov.co" class="btn-govco link-btn-govco">contactenos@sopo-cundinamarca.gov.co</a></p></li>
        <li><p>Correo de notificaciones judiciales: <a href="mailto:notificacionesjudiciales@sopo-cundinamarca.gov.co" class="btn-govco link-btn-govco">notificacionesjudiciales@sopo-cundinamarca.gov.co</a></p></li>
      </ul>
      <div class="end-links-container">
        <a href="https://www.sopo-cundinamarca.gov.co" class="btn-govco link-btn-govco" rel="noopener">Sede electrónica</a>
        <a href="https://www.sopo-cundinamarca.gov.co" class="btn-govco link-btn-govco" rel="noopener">PQRSD</a>
        <a href="https://www.sopo-cundinamarca.gov.co" class="btn-govco link-btn-govco" rel="noopener">Políticas</a>
        <a href="https://terridata.dnp.gov.co" class="btn-govco link-btn-govco" rel="noopener">Datos abiertos (TerriData)</a>
      </div>
    </div>
    <div class="second-section">
      <span class="govco-logo"></span><span class="separator"></span><span class="govco-co"></span>
    </div>
  </footer>
</body>
</html>
"""
(AQUI / "index.html").write_text(pagina, encoding="utf-8")
print("prototipo/index.html generado")
