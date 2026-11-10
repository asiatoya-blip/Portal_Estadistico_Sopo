# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Sitio estático. Producción: Eleventy + librería `nxgov` + CDN GOV.CO v5 en Cloudflare Pages (ADR-001, ADR-005).
Propuesta de diseño 2026-11-10: HTML/CSS/JS estático sin dependencias, publicado en GitHub Pages para revisión del
cliente (pedido del usuario); se porta a Eleventy en la Etapa 2.

## Users

Por igual (confirmado 2026-11-10):
- **Ciudadanía**: vecinos, periodistas y estudiantes que buscan un dato rápido del municipio, a menudo desde el celular.
- **Funcionarios de la Alcaldía y concejales**: consultan indicadores para decidir y rendir cuentas, y exploran a fondo.

Lectura rápida arriba (cifras), exploración a fondo abajo (tableros).

## Product Purpose

Micrositio estadístico de la Alcaldía de Sopó (Cundinamarca, DANE 25758), enlazado desde la sede electrónica bajo un
dominio `.gov.co`. Reúne en una "ventana sencilla" las cifras clave del municipio y los tableros de Tableau Public que
publica la entidad. Éxito: el visitante encuentra la cifra o el tablero que busca, con fuente y fecha, sin perderse.

## Positioning

Es la fuente oficial del propio municipio: cada cifra sale de TerriData (DNP) con fuente y fecha de corte, y cada
tablero es el que publica la Alcaldía. Una cifra que el visitante no pueda rastrear hasta su fuente no se publica.

## Operating Context

- Se entra desde la sede electrónica de Sopó; convive con la barra superior, cabecera, pie y barra de accesibilidad
  del CDN GOV.CO v5, que no se modifican.
- Las gráficas son solo iframes de Tableau Public (ADR-011): contenido de terceros, no se puede estilizar ni hacer
  accesible por dentro.
- Las tarjetas salen del Excel de TerriData; al subir uno nuevo el sitio se regenera (GitHub Actions).
- Contenido editable por la entidad en Decap CMS.

## Capabilities and Constraints

- Secciones confirmadas (2026-11-10): **cifras + tableros**. Asistente IA y datos abiertos dejan de ser secciones de
  la página (enlace o franja pequeña). Pendiente de formalizar en un ADR.
- Libros de Tableau confirmados: `TerriData2026_sopo` (10 hojas, pestañas), `SopoDatosCuriosos2026` (6 hojas,
  pestañas), `EscenariosDeportivosyRecreativosdeSop2026` (1 hoja `Hoja1`, sin pestañas).
- "Acceso a Programas Sociales y Oferta Institucional": **oculto hasta que la entidad entregue la URL** (decisión
  2026-11-10). No se muestran textos de prueba de programas.
- CSP estricta: sin script ni style en línea, sin `eval`; Tableau solo por `frame-src`. Los códigos de inserción con
  `viz_v1.js` no se usan.
- Tableau Public no entrega datos por API (403) ni imágenes de vista previa útiles (1×1 px).
- Fuera de alcance: login, formularios con datos personales (se enlaza la PQRSD de la sede).

## Brand Commitments

- Kit UI GOV.CO 9.2 y CDN GOV.CO v5: chrome oficial sin modificar. Azul Cobalt `#0943B5` y tokens del Kit.
- Prohibidos los colores del mockup v4 (`#004884`, `#3366CC`), Tailwind, Font Awesome y el CDN v4.
- Logo oficial de la Alcaldía 2024–2027: `design_specs/logo_sopo_2024_2027_1x - copia.png`.
- Prefijo `nxgov-` + BEM en todo bloque propio (reglas Sogas, `vendor/nxgov/CLAUDE.md`).
- El cliente pidió una estructura parecida a la maqueta alpha (`mockup_gemini_alpha/`): tarjetas arriba y tableros
  por tema. Solo se toma la estructura, no su código ni sus colores.

## Evidence on Hand

- `data_base/TerriData25758f.xlsx` (5.961 filas, 932 indicadores) y `data/fixtures/terridata-sopo.json`.
- Inventario de libros y hojas: `tableau/inventario-libros.md`.
- No existen todavía: resúmenes en texto de las 17 hojas (los escribe la entidad), CSV por hoja de Tableau, URL de
  Programas Sociales, diseño para teléfono de las hojas de Tableau. No se inventan.

## Product Principles

1. Cada cifra con su fuente y su fecha, o no se publica.
2. Una sola ventana: lo que el visitante necesita cabe en una página; lo demás es un enlace.
3. Lo que vive dentro de Tableau tiene su equivalente en texto fuera de él.
4. Solo se muestra lo que la entidad ya entregó; lo pendiente no ocupa espacio.
5. Oficial antes que llamativo: convive con GOV.CO sin competir con su chrome.

## Accessibility & Inclusion

WCAG 2.1 AA y Resolución 1519 de 2020 (anexos 1 a 4). La barra de accesibilidad del CDN escribe `font-size` en línea:
tipografía en `rem`, sin alturas fijas en texto. Movimiento con `prefers-reduced-motion`. Interfaz en español; si se
mantiene inglés, los tableros se marcan `lang="es"`.
