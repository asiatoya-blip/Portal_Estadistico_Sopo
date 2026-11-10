"""Genera prototipo/index.html desde temas.json (sin dependencias). Uso: python prototipo/build.py"""
import json
import re
from html import escape as e
from pathlib import Path

AQUI = Path(__file__).parent
DATOS = json.loads((AQUI / "temas.json").read_text(encoding="utf-8"))
SEGURO = re.compile(r"^[A-Za-z0-9_]{1,80}$")  # libro y hoja: lista blanca (revisión de seguridad 2026-11-10)
FLECHA = {
    "sube": '<svg class="nxgov-stat__icon" aria-hidden="true" viewBox="0 0 24 24"><path d="M12 19V5M5 12l7-7 7 7"/></svg>',
    "baja": '<svg class="nxgov-stat__icon" aria-hidden="true" viewBox="0 0 24 24"><path d="M12 5v14M5 12l7 7 7-7"/></svg>',
}


def url(h, embed):
    assert SEGURO.match(h["libro"]) and SEGURO.match(h["hoja"]), h
    base = f"https://public.tableau.com/views/{h['libro']}/{h['hoja']}"
    return base + ("?:showVizHome=no&:embed=y&:tabs=n&:toolbar=n&:language=es-ES" if embed else "?:language=es-ES")


def cifra(c):
    if not c:
        return ""
    verdict = f'<span class="nxgov-stat__verdict">{e(c["valoracion"].capitalize())}</span>' if c["valoracion"] else ""
    mod = f' nxgov-stat__change--{c["valoracion"]}' if c["valoracion"] else ""
    return f"""
        <figure class="nxgov-stat">
          <figcaption class="nxgov-stat__label">{e(c['etiqueta'])}</figcaption>
          <p class="nxgov-stat__value">{e(c['valor'])} <span class="nxgov-stat__unit">{e(c['unidad'])}</span></p>
          <p class="nxgov-stat__change{mod}">{FLECHA[c['direccion']]}<span>{e(c['cambio'])}</span>{verdict}</p>
          <p class="nxgov-stat__source">Fuente: {e(c['fuente'])}</p>
        </figure>"""


def hoja(t, h, i):
    ident = f"{t['id']}-{h['hoja'].lower()}"
    resumen = (f'<p class="nxgov-viz__summary">{e(h["resumen"])}</p>' if h["resumen"] else
               '<p class="nxgov-viz__summary nxgov-viz__summary--pending">Resumen pendiente: la Alcaldía '
               'publicará aquí, en texto, lo que muestra este tablero.</p>')
    return f"""
          <article class="nxgov-viz" id="{ident}" data-nxgov-sheet="{i}" aria-labelledby="{ident}-h">
            <div class="nxgov-viz__head">
              <h3 class="nxgov-viz__title" id="{ident}-h">{e(h['titulo'])}</h3>
              <a class="nxgov-viz__open" href="{e(url(h, False))}" rel="noopener" target="_blank">Abrir en Tableau Public<span class="nxgov-sr-only">: {e(h['titulo'])} (se abre en otra pestaña)</span></a>
            </div>
            {resumen}
            <p class="nxgov-viz__meta">Fuente: {e(h['fuente'])} · Corte: {e(DATOS['corte'])}</p>
            <div class="nxgov-viz__stage">
              <div class="nxgov-viz__gate">
                <button class="nxgov-viz__load" type="button" data-nxgov-src="{e(url(h, True))}" data-nxgov-title="Tablero interactivo: {e(h['titulo'])}">Cargar el tablero<span class="nxgov-sr-only"> de {e(h['titulo'])}</span></button>
                <p class="nxgov-viz__notice">Se carga desde Tableau Public, un servicio externo que puede usar cookies. El resto del portal no las usa.</p>
              </div>
            </div>
          </article>"""


def tema(t):
    selector = ""
    if len(t["hojas"]) > 1:
        botones = "".join(
            f'<button class="nxgov-sheets__btn" type="button" data-nxgov-sheet="{i}" aria-pressed="{"true" if i == 0 else "false"}">{e(h["titulo"])}</button>'
            for i, h in enumerate(t["hojas"]))
        selector = f'<div class="nxgov-sheets" role="group" aria-label="Tableros de {e(t["nombre"])}">{botones}</div>'
    otra = f'<p class="nxgov-theme__note">{e(t["otra"])}</p>' if t["otra"] else ""
    hojas = "".join(hoja(t, h, i) for i, h in enumerate(t["hojas"]))
    return f"""
      <section class="nxgov-theme{' nxgov-theme--multi' if len(t['hojas']) > 1 else ''}" id="{t['id']}" aria-labelledby="{t['id']}-h">
        <div class="nxgov-theme__facts">
          <h2 class="nxgov-theme__title" id="{t['id']}-h">{e(t['nombre'])}</h2>{cifra(t['cifra'])}
          {otra}
        </div>
        <div class="nxgov-theme__boards">
          {selector}{hojas}
        </div>
      </section>"""


nav = "".join(
    f'<li><a class="nxgov-themes__link" href="#{t["id"]}"><span class="nxgov-themes__name">{e(t["nombre"])}</span>'
    f'<span class="nxgov-themes__value">{e(t["pestana"])}</span></a></li>' for t in DATOS["temas"])

pagina = f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; font-src 'self'; img-src 'self'; frame-src https://public.tableau.com; object-src 'none'; base-uri 'self'; form-action 'self'">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <title>Portal Estadístico de Sopó</title>
  <meta name="description" content="Cifras oficiales y tableros de Sopó, Cundinamarca, con su fuente y su fecha de corte.">
  <link rel="stylesheet" href="assets/portal.css">
  <script src="assets/portal.js" defer></script>
</head>
<body>
  <a class="nxgov-skip" href="#contenido">Saltar al contenido</a>
  <div class="nxgov-govbar"><div class="nxgov-wrap"><a class="nxgov-govbar__brand" href="https://www.gov.co">GOV.CO</a></div></div>
  <header class="nxgov-header">
    <div class="nxgov-wrap nxgov-header__inner">
      <a class="nxgov-header__brand" href="./"><img class="nxgov-header__logo" src="assets/logo-sopo.png" width="1080" height="589" alt="Alcaldía de Sopó"><span class="nxgov-header__name">Portal Estadístico</span></a>
      <nav class="nxgov-header__links" aria-label="Enlaces de la Alcaldía"><a href="https://www.sopo-cundinamarca.gov.co" rel="noopener">Sede electrónica</a><a href="https://terridata.dnp.gov.co" rel="noopener">Datos abiertos en TerriData (DNP)</a></nav>
    </div>
  </header>
  <main id="contenido" class="nxgov-wrap">
    <div class="nxgov-intro">
      <div>
        <h1 class="nxgov-intro__title">Portal Estadístico de Sopó</h1>
        <p class="nxgov-intro__lead">Elige un tema: verás su cifra principal, con fuente, y el tablero para explorarla.</p>
      </div>
      <p class="nxgov-intro__cut">Datos a {e(DATOS['corte'])}</p>
    </div>
    <nav class="nxgov-themes" aria-label="Temas"><ul class="nxgov-themes__list">{nav}</ul></nav>
    <div class="nxgov-themes__panels">{''.join(tema(t) for t in DATOS['temas'])}
    </div>
  </main>
  <footer class="nxgov-footer">
    <div class="nxgov-wrap nxgov-footer__inner">
      <p><strong>Alcaldía Municipal de Sopó</strong>, Cundinamarca · Código DANE 25758</p>
      <p>Las cifras salen de TerriData (DNP) y de los tableros que publica la Alcaldía en Tableau Public. <a href="https://www.sopo-cundinamarca.gov.co" rel="noopener">Sede electrónica y PQRSD</a></p>
    </div>
    <div class="nxgov-govbar"><div class="nxgov-wrap"><a class="nxgov-govbar__brand" href="https://www.gov.co">GOV.CO</a></div></div>
  </footer>
</body>
</html>
"""
(AQUI / "index.html").write_text(pagina, encoding="utf-8")
print("prototipo/index.html generado")
