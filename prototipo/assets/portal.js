// Mejora progresiva: sin JS todas las vistas se ven apiladas y los enlaces del riel llevan a cada tablero.
(function () {
  'use strict';
  document.documentElement.classList.add('nxgov-js');
  var views = Array.prototype.slice.call(document.querySelectorAll('.nxgov-view'));
  var links = Array.prototype.slice.call(document.querySelectorAll('.nxgov-rail__link'));
  var menu = document.querySelector('.nxgov-rail__menu');
  var narrow = window.matchMedia('(max-width: 64rem)');
  if (!views.length) return;

  function show(hash, animate) {
    var id = (hash || '').replace(/^#/, '');
    var target = (id && document.getElementById(id)) || views[0];
    var view = target.closest('.nxgov-view') || views[0];
    views.forEach(function (v) { v.classList.toggle('nxgov-is-hidden', v !== view); });
    links.forEach(function (a) {
      if (a.getAttribute('href') === '#' + view.id) a.setAttribute('aria-current', 'true');
      else a.removeAttribute('aria-current');
    });
    if (animate && view.classList.contains('nxgov-view--home')) {
      view.classList.remove('nxgov-is-entering');
      void view.offsetWidth;
      view.classList.add('nxgov-is-entering');
    }
    document.title = (view.id === 'resumen' ? '' : view.querySelector('h2').textContent + ' · ') + 'Portal Estadístico de Sopó';
    document.dispatchEvent(new CustomEvent('nxgov:views:change', { detail: { vista: view.id } }));
    return view;
  }

  document.addEventListener('click', function (ev) {
    var a = ev.target.closest('a[href^="#"]');
    if (!a || a.classList.contains('nxgov-skip')) return;
    var id = a.getAttribute('href');
    if (!document.getElementById(id.slice(1))) return;
    ev.preventDefault();
    history.pushState(null, '', id);
    var view = show(id, true);
    if (narrow.matches && menu) menu.open = false;
    window.scrollTo(0, 0);
    var heading = view.querySelector('h1, h2');
    if (heading) { heading.setAttribute('tabindex', '-1'); heading.focus({ preventScroll: true }); }
  });

  window.addEventListener('popstate', function () { show(location.hash, false); });
  if (menu && narrow.matches) menu.open = false;
  show(location.hash, true);
})();
