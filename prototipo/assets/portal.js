// Mejora progresiva: sin JS todas las vistas se ven apiladas y los enlaces del menú llevan a cada tablero.
(function () {
  'use strict';
  document.documentElement.classList.add('nxgov-js');
  var views = Array.prototype.slice.call(document.querySelectorAll('.nxgov-view'));
  var navLinks = Array.prototype.slice.call(document.querySelectorAll('.nxgov-nav a'));
  var groups = Array.prototype.slice.call(document.querySelectorAll('.nxgov-nav__group'));
  var menu = document.querySelector('.nxgov-nav__menu');
  var narrow = window.matchMedia('(max-width: 64rem)');
  if (!views.length) return;

  function show(hash, animate) {
    var id = (hash || '').replace(/^#/, '');
    var target = (id && document.getElementById(id)) || views[0];
    var view = target.closest('.nxgov-view') || views[0];
    views.forEach(function (v) { v.classList.toggle('nxgov-is-hidden', v !== view); });
    navLinks.forEach(function (a) {
      if (a.getAttribute('href') === '#' + view.id) a.setAttribute('aria-current', 'page');
      else a.removeAttribute('aria-current');
    });
    // El grupo del tablero activo queda desplegado en el menú
    var group = view.getAttribute('data-nxgov-group');
    groups.forEach(function (g) { if (g.getAttribute('data-nxgov-group') === group) g.open = true; });
    if (animate && view.classList.contains('nxgov-view--home')) {
      view.classList.remove('nxgov-is-entering');
      void view.offsetWidth;
      view.classList.add('nxgov-is-entering');
    }
    // La pestaña activa queda a la vista dentro de la tira desplazable
    var tab = view.querySelector('.nxgov-tabs__link[aria-current]');
    if (tab) { var strip = tab.closest('.nxgov-tabs'); if (strip.scrollWidth > strip.clientWidth) strip.scrollLeft = Math.max(0, tab.offsetLeft - 24); }
    var heading = view.querySelector('h1, h2');
    document.title = (view.id === 'resumen' ? '' : heading.textContent + ' · ') + 'Portal Estadístico de Sopó';
    document.dispatchEvent(new CustomEvent('nxgov:views:change', { detail: { vista: view.id } }));
    return view;
  }

  document.addEventListener('click', function (ev) {
    var a = ev.target.closest('a[href^="#"]');
    if (!a || a.classList.contains('nxgov-skip')) return;
    var id = a.getAttribute('href');
    if (id.length < 2 || !document.getElementById(id.slice(1))) return;
    ev.preventDefault();
    history.pushState(null, '', id);
    var view = show(id, true);
    if (narrow.matches && menu) menu.open = false;
    var main = document.getElementById('contenido');
    if (main.getBoundingClientRect().top < 0) main.scrollIntoView({ block: 'start' });
    var heading = view.querySelector('h1, h2');
    if (heading) { heading.setAttribute('tabindex', '-1'); heading.focus({ preventScroll: true }); }
  });

  window.addEventListener('popstate', function () { show(location.hash, false); window.scrollTo(0, 0); });
  if (menu && narrow.matches) menu.open = false;
  // En teléfono, Tableau entrega su diseño para teléfono (lo genera solo si el libro no trae uno)
  if (window.matchMedia('(max-width: 40rem)').matches) {
    document.querySelectorAll('.nxgov-board__frame').forEach(function (f) { f.src = f.getAttribute('src') + '&:device=phone'; });
  }
  show(location.hash, true);
  // El ancla nativa saltaría por encima de la cabecera y la barra GOV.CO; el navegador la aplica tras 'load'
  if (location.hash) { window.scrollTo(0, 0); window.addEventListener('load', function () { window.scrollTo(0, 0); }); }
})();
