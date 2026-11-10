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


def url(h, embed):
    assert SEGURO.match(h["libro"]) and SEGURO.match(h["hoja"]), h
    base = f"https://public.tableau.com/views/{h['libro']}/{h['hoja']}"
    return base + ("?:showVizHome=no&:embed=y&:tabs=n&:toolbar=n&:language=es-ES" if embed else "?:language=es-ES")


def miles(v):
    return f"{v:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".").removesuffix(",0")


def tendencia(serie, w=160, h=44, pad=4):
    """Mini tendencia SVG de una serie anual de TerriData; devuelve (puntos, ultimo_x, ultimo_y, descripción)."""
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
    sentido = "baja" if k["cambio"].startswith("−") else "sube"
    g, h = HOJAS[k["hoja"]]
    return f"""
          <article class="nxgov-kpi nxgov-kpi--{k['estado']}">
            <div class="nxgov-kpi__top">
              <h3 class="nxgov-kpi__label">{e(k['etiqueta'])}</h3>
              <span class="nxgov-kpi__chip">{ESTADO[k['estado']]}</span>
            </div>
            <p class="nxgov-kpi__value">{e(k['valor'])}</p>
            <p class="nxgov-kpi__unit">{e(k['unidad'])}</p>
            <svg class="nxgov-kpi__trend" viewBox="0 0 160 44" role="img" aria-label="{e(desc)}"><polyline points="{puntos}"/><circle cx="{lx:.1f}" cy="{ly:.1f}" r="3.5"/></svg>
            <p class="nxgov-kpi__change"><svg class="nxgov-icon" aria-hidden="true" viewBox="0 0 24 24"><path d="{FLECHA[sentido]}"/></svg>{e(k['cambio'])}</p>
            <p class="nxgov-kpi__foot"><span>{e(k['fuente'])}</span><a href="#{h['id']}">Ver tablero<span class="nxgov-sr-only"> de {e(h['titulo'])}</span></a></p>
          </article>"""


def iframe(h, clase="nxgov-board__frame"):
    return (f'<iframe class="{clase}" src="{e(url(h, True))}" title="Tablero interactivo: {e(h["titulo"])}" lang="es" '
            f'loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox" '
            f'referrerpolicy="strict-origin" allow="fullscreen" allowfullscreen></iframe>')


def resumen(h):
    if h["resumen"]:
        return f'<p class="nxgov-board__summary">{e(h["resumen"])}</p>'
    return ('<p class="nxgov-board__summary nxgov-board__summary--pending">Resumen pendiente: la Alcaldía publicará '
            'aquí, en texto, lo que muestra este tablero.</p>')


def vista_hoja(g, h, i, lista):
    prev_h, next_h = lista[i - 1] if i else None, lista[i + 1] if i + 1 < len(lista) else None
    nav = ""
    if prev_h or next_h:
        nav = '<nav class="nxgov-pager" aria-label="Otros tableros de este grupo">' + \
              (f'<a class="nxgov-pager__link" href="#{prev_h["id"]}"><span class="nxgov-pager__dir">Anterior</span>{e(prev_h["titulo"])}</a>' if prev_h else "<span></span>") + \
              (f'<a class="nxgov-pager__link nxgov-pager__link--next" href="#{next_h["id"]}"><span class="nxgov-pager__dir">Siguiente</span>{e(next_h["titulo"])}</a>' if next_h else "") + "</nav>"
    return f"""
        <section class="nxgov-view" id="{h['id']}" aria-labelledby="{h['id']}-h">
          <header class="nxgov-view__head">
            <p class="nxgov-view__crumb">{e(g['nombre'])} · {e(g['fuente'])}</p>
            <div class="nxgov-view__title-row">
              <h2 class="nxgov-view__title" id="{h['id']}-h">{e(h['titulo'])}</h2>
              <a class="nxgov-btn nxgov-btn--ghost" href="{e(url(h, False))}" rel="noopener" target="_blank">Abrir en Tableau Public<span class="nxgov-sr-only"> (otra pestaña)</span></a>
            </div>
          </header>
          <div class="nxgov-board">
            <div class="nxgov-board__text">
              {resumen(h)}
              <p class="nxgov-board__meta">Fuente: {e(h['fuente'])} · Corte: {e(D['corte'])}</p>
            </div>
            <div class="nxgov-board__stage">{iframe(h)}</div>
          </div>
          {nav}
        </section>"""


def rail():
    grupos = ""
    for g in D["grupos"]:
        enlaces = "".join(f'<li><a class="nxgov-rail__link" href="#{h["id"]}">{e(h["titulo"])}</a></li>' for h in g["hojas"])
        grupos += f'<p class="nxgov-rail__group">{e(g["nombre"])} <span>{len(g["hojas"])}</span></p><ul class="nxgov-rail__list">{enlaces}</ul>'
    return f"""
    <aside class="nxgov-rail">
      <div class="nxgov-rail__brand">
        <img class="nxgov-rail__logo" src="assets/logo-sopo.png" width="1080" height="589" alt="Alcaldía de Sopó">
        <p class="nxgov-rail__name">Portal Estadístico</p>
      </div>
      <details class="nxgov-rail__menu" open>
        <summary class="nxgov-rail__toggle">Temas y tableros</summary>
        <nav aria-label="Temas y tableros">
          <ul class="nxgov-rail__list"><li><a class="nxgov-rail__link nxgov-rail__link--home" href="#resumen">¿Cómo va Sopó?</a></li></ul>
          {grupos}
        </nav>
      </details>
      <p class="nxgov-rail__note">Datos a {e(D['corte'])}. Fuentes: TerriData (DNP) y libros de la Alcaldía en Tableau Public.</p>
    </aside>"""


k = D["kpis"]
mejoran = sum(x["estado"] == "mejora" for x in k)
empeoran = sum(x["estado"] == "empeora" for x in k)
dest = HOJAS["demografia"][1]
gen = HOJAS["generaciones"][1]
esc = HOJAS["escenarios"][1]
vistas = "".join(vista_hoja(g, h, i, g["hojas"]) for g in D["grupos"] for i, h in enumerate(g["hojas"]))

pagina = f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' https://cdn.www.gov.co; font-src 'self' https://cdn.www.gov.co; img-src 'self' data: https://cdn.www.gov.co; frame-src https://public.tableau.com; object-src 'none'; base-uri 'self'; form-action 'self'">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <title>Portal Estadístico de Sopó</title>
  <meta name="description" content="¿Cómo va Sopó? Cifras oficiales y tableros de Sopó, Cundinamarca, con su fuente y su fecha de corte.">
  <link rel="stylesheet" href="{CDN}/all.css">
  <link rel="stylesheet" href="assets/portal.css">
  <script src="assets/portal.js" defer></script>
</head>
<body class="nxgov-page">
  <a class="nxgov-skip" href="#contenido">Saltar al contenido</a>
  <div class="barra-superior-govco">
    <a href="https://www.gov.co/" target="_blank" rel="noopener" aria-label="Portal del Estado Colombiano - GOV.CO"></a>
  </div>
  <div class="nxgov-shell">{rail()}
    <main class="nxgov-main" id="contenido">
      <section class="nxgov-view nxgov-view--home" id="resumen" aria-labelledby="resumen-h">
        <header class="nxgov-hero">
          <div>
            <h1 class="nxgov-hero__title" id="resumen-h">¿Cómo va Sopó?</h1>
            <p class="nxgov-hero__lead">Las cifras oficiales del municipio, con su fuente, su tendencia y los tableros para explorarlas.</p>
          </div>
          <p class="nxgov-hero__cut">Datos a {e(D['corte'])}</p>
        </header>
        <p class="nxgov-pulse" role="status">
          <span class="nxgov-pulse__item nxgov-pulse__item--mejora"><strong>{mejoran}</strong> indicadores mejoraron</span>
          <span class="nxgov-pulse__item nxgov-pulse__item--empeora"><strong>{empeoran}</strong> empeoraron</span>
          <span class="nxgov-pulse__item"><strong>{len(k) - mejoran - empeoran}</strong> sin valoración</span>
          <span class="nxgov-pulse__note">frente al año anterior</span>
        </p>
        <h2 class="nxgov-sr-only">Cifras principales</h2>
        <div class="nxgov-kpis">{''.join(kpi(x) for x in k)}
        </div>
        <div class="nxgov-feature">
          <article class="nxgov-card nxgov-card--board" aria-labelledby="destacado-h">
            <div class="nxgov-card__head">
              <div><h2 class="nxgov-card__title" id="destacado-h">{e(dest['titulo'])} de Sopó</h2><p class="nxgov-card__meta">Tablero destacado · TerriData (DNP)</p></div>
              <a class="nxgov-btn nxgov-btn--ghost" href="#demografia">Ver a pantalla completa</a>
            </div>
            <div class="nxgov-board__stage nxgov-board__stage--feature">{iframe(dest)}</div>
          </article>
          <div class="nxgov-feature__side">
            <article class="nxgov-card nxgov-card--fact" aria-labelledby="sabias-h">
              <h2 class="nxgov-card__title" id="sabias-h">¿Sabías que…?</h2>
              <p class="nxgov-fact__value">5.931</p>
              <p class="nxgov-fact__text">soposeños son de la Generación Z, la más numerosa del municipio. Les siguen los Millennials, con 5.599.</p>
              <a class="nxgov-btn" href="#{gen['id']}">Ver los 6 datos curiosos</a>
            </article>
            <article class="nxgov-card nxgov-card--map" aria-labelledby="mapa-h">
              <h2 class="nxgov-card__title" id="mapa-h">¿Dónde hacer deporte?</h2>
              <p>{e(esc['resumen'])}</p>
              <a class="nxgov-btn nxgov-btn--ghost" href="#{esc['id']}">Ver el mapa de escenarios</a>
            </article>
          </div>
        </div>
      </section>{vistas}
    </main>
  </div>
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
