// Mejora progresiva: sin JS todos los temas y tableros se ven apilados y "Abrir en Tableau Public" funciona.
(function () {
  'use strict';
  document.documentElement.classList.add('nxgov-js');
  var TABLEAU = /^https:\/\/public\.tableau\.com\/views\/[A-Za-z0-9_]+\/[A-Za-z0-9_]+\?[^#@\\]*$/;
  var links = Array.prototype.slice.call(document.querySelectorAll('.nxgov-themes__link'));
  var panels = Array.prototype.slice.call(document.querySelectorAll('.nxgov-theme'));
  if (!links.length || !panels.length) return;

  function emit(name, detail) {
    document.dispatchEvent(new CustomEvent('nxgov:' + name, { detail: detail }));
  }

  // Tema activo: el hash puede ser un tema (#finanzas) o una hoja (#finanzas-finanzasidf)
  function resolve(hash) {
    var id = (hash || '').replace(/^#/, '');
    var target = id && document.getElementById(id);
    if (!target) return { panel: panels[0], sheet: null };
    var panel = target.closest('.nxgov-theme');
    if (!panel) return { panel: panels[0], sheet: null };
    return { panel: panel, sheet: target.classList.contains('nxgov-viz') ? target : null };
  }

  function showSheet(panel, index) {
    panel.querySelectorAll('.nxgov-viz').forEach(function (v) {
      v.classList.toggle('nxgov-is-hidden', v.getAttribute('data-nxgov-sheet') !== String(index));
    });
    panel.querySelectorAll('.nxgov-sheets__btn').forEach(function (b) {
      b.setAttribute('aria-pressed', b.getAttribute('data-nxgov-sheet') === String(index) ? 'true' : 'false');
    });
  }

  function activate(state, animate) {
    panels.forEach(function (p) { p.classList.toggle('nxgov-is-hidden', p !== state.panel); });
    links.forEach(function (a) {
      if (a.getAttribute('href') === '#' + state.panel.id) a.setAttribute('aria-current', 'true');
      else a.removeAttribute('aria-current');
    });
    showSheet(state.panel, state.sheet ? state.sheet.getAttribute('data-nxgov-sheet') : '0');
    if (animate) {
      state.panel.classList.remove('nxgov-is-entering');
      void state.panel.offsetWidth;
      state.panel.classList.add('nxgov-is-entering');
    }
    emit('themes:change', { tema: state.panel.id });
  }

  links.forEach(function (a) {
    a.addEventListener('click', function (ev) {
      ev.preventDefault();
      var id = a.getAttribute('href');
      history.replaceState(null, '', id);
      var state = resolve(id);
      activate(state, true);
      // En pantallas angostas el panel queda debajo de la barra: llevar al visitante a él
      if (state.panel.getBoundingClientRect().top > window.innerHeight * 0.6) {
        var calm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        state.panel.scrollIntoView({ behavior: calm ? 'auto' : 'smooth', block: 'start' });
      }
    });
  });

  document.querySelectorAll('.nxgov-sheets__btn').forEach(function (b) {
    b.addEventListener('click', function () {
      var panel = b.closest('.nxgov-theme');
      var index = b.getAttribute('data-nxgov-sheet');
      showSheet(panel, index);
      var sheet = panel.querySelector('.nxgov-viz[data-nxgov-sheet="' + index + '"]');
      if (sheet) history.replaceState(null, '', '#' + sheet.id);
    });
  });

  // El iframe de Tableau se crea solo cuando el visitante lo pide (privacidad y peso)
  document.querySelectorAll('.nxgov-viz__load').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var src = btn.getAttribute('data-nxgov-src');
      if (!TABLEAU.test(src)) return;
      var ev = new CustomEvent('nxgov:action:load-viz', { cancelable: true, detail: { src: src } });
      if (!document.dispatchEvent(ev)) return;
      var stage = btn.closest('.nxgov-viz__stage');
      var frame = document.createElement('iframe');
      frame.className = 'nxgov-viz__frame';
      frame.src = src;
      frame.title = btn.getAttribute('data-nxgov-title');
      frame.setAttribute('lang', 'es');
      frame.setAttribute('sandbox', 'allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox');
      frame.setAttribute('referrerpolicy', 'strict-origin');
      frame.setAttribute('allow', 'fullscreen');
      frame.setAttribute('allowfullscreen', '');
      stage.replaceChildren(frame);
      stage.classList.add('nxgov-is-loaded');
      frame.focus();
      emit('viz:loaded', { src: src });
    });
  });

  window.addEventListener('hashchange', function () { activate(resolve(location.hash), true); });
  activate(resolve(location.hash), false);
})();
