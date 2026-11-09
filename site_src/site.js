/* Shane 54: site script = (1) soft page navigation so the audio never stops,
   (2) global podcast player: dock + full sheet + media session (lock screen), (3) YouTube facades */
(function () {
  'use strict';
  var SCRIPT = document.currentScript.src;
  var BASE = SCRIPT.replace(/assets\/site\.js.*$/, '');
  var BASEPATH = new URL(BASE).pathname;
  var TXT = {
    hu: { now: 'ÉPPEN SZÓL', eps: 'epizód', close: 'Bezár', soon: 'Az archívum hamarosan feltöltődik.', open: 'Lejátszó megnyitása' },
    en: { now: 'NOW PLAYING', eps: 'episodes', close: 'Close', soon: 'The archive is coming soon.', open: 'Open player' }
  };
  function L() { return TXT[(document.documentElement.lang || 'hu').slice(0, 2)] || TXT.hu; }
  var $ = function (s, r) { return (r || document).querySelector(s); };

  /* ---------- YouTube facades ---------- */
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-yt]'); if (!t) return;
    e.preventDefault();
    if (P.a && !P.a.paused) P.a.pause();
    var f = document.createElement('iframe');
    f.src = 'https://www.youtube-nocookie.com/embed/' + t.getAttribute('data-yt') + '?autoplay=1&rel=0';
    f.allow = 'autoplay; encrypted-media; fullscreen; picture-in-picture'; f.allowFullscreen = true; f.title = 'video';
    t.innerHTML = ''; t.removeAttribute('data-yt'); t.appendChild(f);
  });

  /* ---------- icons ---------- */
  var IC = {
    play: '<svg viewBox="0 0 24 24" width="26" height="26"><path fill="currentColor" d="M8 5v14l11-7z"/></svg>',
    pause: '<svg viewBox="0 0 24 24" width="26" height="26"><path fill="currentColor" d="M6 5h4v14H6zm8 0h4v14h-4z"/></svg>',
    prev: '<svg viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M6 6h2v12H6zm3.5 6 8.5 6V6z"/></svg>',
    next: '<svg viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M16 6h2v12h-2zM6 18l8.5-6L6 6z"/></svg>',
    back: '<svg viewBox="0 0 24 24" width="26" height="26"><path fill="currentColor" d="M12 5V2L7 6l5 4V7a5 5 0 1 1-5 5H5a7 7 0 1 0 7-7z"/><text x="12" y="16.5" text-anchor="middle" font-size="6.5" font-weight="700" fill="currentColor" font-family="Inter,Arial">15</text></svg>',
    fwd: '<svg viewBox="0 0 24 24" width="26" height="26"><path fill="currentColor" d="M12 5V2l5 4-5 4V7a5 5 0 1 0 5 5h2a7 7 0 1 1-7-7z"/><text x="12" y="16.5" text-anchor="middle" font-size="6.5" font-weight="700" fill="currentColor" font-family="Inter,Arial">30</text></svg>',
    down: '<svg viewBox="0 0 24 24" width="26" height="26"><path fill="currentColor" d="M7.4 8.6 12 13.2l4.6-4.6L18 10l-6 6-6-6z"/></svg>'
  };

  /* ---------- player ---------- */
  var P = { a: new Audio(), eps: [], cur: -1, si: 0, speeds: [1, 1.25, 1.5, 2], loaded: null, demo: false };
  var A = P.a; A.preload = 'metadata'; A.setAttribute('playsinline', '');
  var LOGO = BASE + 'assets/img/id_logo.png';
  var dock, sheet, seeking = false, built = false, lastPos = 0;

  function fmt(s) { if (!isFinite(s) || s < 0) return '0:00'; s = Math.floor(s); var h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60), x = s % 60;
    return (h ? h + ':' + (m < 10 ? '0' : '') + m : m) + ':' + (x < 10 ? '0' : '') + x; }
  function art(e) { return (e && e.art) || LOGO; }

  function parse(j) {
    var base = j.base || ('https://archive.org/download/' + j.ia + '/');
    return (j.episodes || []).map(function (e) {
      return { title: e.title, sub: e.sub || '', tracks: e.tracks || [], dur: e.dur || 0, art: e.art ? BASE + 'assets/' + e.art : null,
        src: base + e.file.split('/').map(encodeURIComponent).join('/') };
    });
  }
  function loadEps(demo) {
    if (P.loaded && P.demo === demo) return P.loaded;
    P.demo = demo;
    if (demo) {
      var s = BASE + 'assets/demo/demo.wav';
      P.eps = [{ title: 'Episode title one', sub: 'demo', dur: 14, src: s }, { title: 'Episode title two', sub: 'demo', dur: 14, src: s }, { title: 'Episode title three', sub: 'demo', dur: 14, src: s }];
      return (P.loaded = Promise.resolve(P.eps));
    }
    if (!document.querySelector('meta[name="s54-episodes"]')) return (P.loaded = Promise.resolve([]));
    return (P.loaded = fetch(BASE + 'assets/episodes.json').then(function (r) { if (!r.ok) throw 0; return r.json(); })
      .then(function (j) { P.eps = parse(j); return P.eps; }).catch(function () { return []; }));
  }

  function build() {
    if (built) return; built = true;
    dock = $('#dock'); sheet = $('#sheet');
    dock.innerHTML = '<div class="dk-prog"><i></i></div><div class="dk-row"><button class="dk-info" aria-label="' + L().open + '"><img class="dk-art" alt=""><span class="dk-t"><b></b><s></s></span></button>' +
      '<button class="ib dk-play" aria-label="Play/Pause"></button><button class="ib dk-next" aria-label="Next">' + IC.next + '</button></div>';
    sheet.innerHTML = '<div class="sh-head"><button class="ib sh-close" aria-label="' + L().close + '">' + IC.down + '</button><small>' + L().now + '</small><span style="width:44px"></span></div>' +
      '<div class="sh-main"><img class="sh-art" alt=""><h3 class="sh-title"></h3><span class="sh-sub"></span>' +
      '<input class="pl-bar" type="range" min="0" max="1000" value="0" step="1" aria-label="Seek"><div class="pl-times"><span class="sh-cur">0:00</span><span class="sh-dur">0:00</span></div>' +
      '<div class="sh-ctl"><button class="sh-spd" aria-label="Speed">1×</button><button class="ib sh-prev" aria-label="Previous">' + IC.prev + '</button><button class="ib sh-b15" aria-label="-15s">' + IC.back + '</button>' +
      '<button class="ib main sh-play" aria-label="Play/Pause"></button><button class="ib sh-f30" aria-label="+30s">' + IC.fwd + '</button><button class="ib sh-next" aria-label="Next">' + IC.next + '</button></div></div>' +
      '<details class="sh-tr"><summary>Tracklist</summary><ol></ol></details><div class="sh-list"></div>';
    $('.dk-info', dock).onclick = openSheet;
    $('.dk-play', dock).onclick = toggle; $('.dk-next', dock).onclick = next;
    $('.sh-close', sheet).onclick = closeSheet;
    $('.sh-play', sheet).onclick = toggle; $('.sh-next', sheet).onclick = next; $('.sh-prev', sheet).onclick = prev;
    $('.sh-b15', sheet).onclick = function () { seekBy(-15); }; $('.sh-f30', sheet).onclick = function () { seekBy(30); };
    $('.sh-spd', sheet).onclick = function () { P.si = (P.si + 1) % P.speeds.length; A.playbackRate = P.speeds[P.si]; this.textContent = P.speeds[P.si] + '×'; };
    var bar = $('.pl-bar', sheet);
    bar.oninput = function () { seeking = true; if (A.duration) A.currentTime = A.duration * bar.value / 1000; bar.style.setProperty('--p', (bar.value / 10) + '%'); };
    bar.onchange = function () { seeking = false; };
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !sheet.hidden) closeSheet(); });
  }
  function openSheet() { sheet.hidden = false; document.documentElement.classList.add('sheet-open'); renderList($('.sh-list', sheet)); sync(); }
  function closeSheet() { sheet.hidden = true; document.documentElement.classList.remove('sheet-open'); }

  function seekBy(d) { if (A.duration) A.currentTime = Math.max(0, Math.min(A.duration, A.currentTime + d)); }
  function toggle() { if (P.cur < 0) { play(0); } else if (A.paused) { A.play().catch(function () {}); } else { A.pause(); } }
  function next() { if (P.cur + 1 < P.eps.length) play(P.cur + 1); }
  function prev() { if (A.currentTime > 3 || P.cur <= 0) { A.currentTime = 0; } else { play(P.cur - 1); } }
  function play(i, paused, at) {
    if (i < 0 || i >= P.eps.length) return;
    build(); P.cur = i; var e = P.eps[i];
    A.src = e.src; A.playbackRate = P.speeds[P.si];
    if (at) { A.addEventListener('loadedmetadata', function f() { A.removeEventListener('loadedmetadata', f); try { A.currentTime = at; } catch (x) {} }); }
    dock.hidden = false; document.documentElement.classList.add('has-dock');
    if ('mediaSession' in navigator) {
      var u = art(e);
      navigator.mediaSession.metadata = new MediaMetadata({ title: e.title, artist: 'Shane 54', album: 'International Departures', artwork: [{ src: u, sizes: '512x512', type: /\.png/i.test(u) ? 'image/png' : 'image/jpeg' }] });
    }
    if (!paused) A.play().catch(function () {});
    sync(); save();
  }

  function renderList(c) {
    if (!c) return;
    c.innerHTML = '';
    P.eps.forEach(function (e, i) {
      var b = document.createElement('button'); b.className = 'ep'; b.setAttribute('data-i', i);
      b.innerHTML = '<img loading="lazy" alt=""><span class="t"><b></b><s></s></span><span class="d"></span>';
      b.querySelector('img').src = art(e); b.querySelector('b').textContent = e.title; b.querySelector('s').textContent = e.sub;
      b.querySelector('.d').textContent = e.dur ? fmt(e.dur) : '';
      b.onclick = function () { if (i === P.cur) { toggle(); } else { play(i); } };
      c.appendChild(b);
    });
  }

  function sync() {
    if (!built) return;
    var e = P.eps[P.cur], playing = !A.paused;
    if (e) {
      $('.dk-art', dock).src = art(e); $('.dk-t b', dock).textContent = e.title; $('.dk-t s', dock).textContent = e.sub;
      $('.sh-art', sheet).src = art(e); $('.sh-title', sheet).textContent = e.title; $('.sh-sub', sheet).textContent = e.sub;
    }
    var tr = $('.sh-tr', sheet);
    if (tr) {
      var ol = $('ol', tr), tk = (e && e.tracks) || [];
      if (ol.getAttribute('data-i') !== String(P.cur)) {
        ol.setAttribute('data-i', P.cur); ol.innerHTML = '';
        tk.forEach(function (x) {
          var li = document.createElement('li'), b = document.createElement('button');
          b.innerHTML = '<i></i><span></span>'; b.firstChild.textContent = x.t == null ? '' : fmt(x.t); b.lastChild.textContent = x.n;
          if (x.t == null) b.disabled = true; else b.onclick = function () { if (A.duration || true) A.currentTime = x.t; };
          li.appendChild(b); ol.appendChild(li);
        });
      }
      tr.hidden = !tk.length;
    }
    $('.dk-play', dock).innerHTML = playing ? IC.pause : IC.play;
    $('.sh-play', sheet).innerHTML = playing ? IC.pause : IC.play;
    document.documentElement.classList.toggle('playing', playing);
    var rows = document.querySelectorAll('.ep');
    for (var i = 0; i < rows.length; i++) {
      var on = +rows[i].getAttribute('data-i') === P.cur;
      rows[i].classList.toggle('on', on); rows[i].classList.toggle('pl', on && playing);
    }
    tick();
  }
  function tick() {
    if (!built) return;
    var d = A.duration || (P.eps[P.cur] && P.eps[P.cur].dur) || 0, p = d ? A.currentTime / d : 0;
    $('.dk-prog i', dock).style.width = (p * 100) + '%';
    if (!sheet.hidden) {
      var bar = $('.pl-bar', sheet); bar.style.setProperty('--p', (p * 100) + '%'); if (!seeking) bar.value = Math.round(p * 1000);
      $('.sh-cur', sheet).textContent = fmt(A.currentTime); $('.sh-dur', sheet).textContent = fmt(d);
    }
    if ('mediaSession' in navigator && navigator.mediaSession.setPositionState && A.duration && isFinite(A.duration)) {
      var n = Date.now(); if (n - lastPos > 1000) { lastPos = n; try { navigator.mediaSession.setPositionState({ duration: A.duration, position: Math.min(A.currentTime, A.duration), playbackRate: A.playbackRate }); } catch (x) {} }
    }
  }
  var lastSave = 0;
  function save(force) {
    if (P.demo || P.cur < 0) return; var n = Date.now(); if (!force && n - lastSave < 4000) return; lastSave = n;
    try { localStorage.setItem('s54_pl', JSON.stringify({ i: P.cur, t: Math.floor(A.currentTime) })); } catch (x) {}
  }
  A.addEventListener('timeupdate', function () { tick(); save(); });
  A.addEventListener('loadedmetadata', tick);
  A.addEventListener('play', sync); A.addEventListener('pause', function () { sync(); save(true); });
  A.addEventListener('ended', function () { if (P.cur + 1 < P.eps.length) play(P.cur + 1); else sync(); });
  window.addEventListener('pagehide', function () { save(true); });
  if ('mediaSession' in navigator) {
    var ms = navigator.mediaSession, set = function (n, f) { try { ms.setActionHandler(n, f); } catch (x) {} };
    set('play', function () { A.play(); }); set('pause', function () { A.pause(); });
    set('previoustrack', prev); set('nexttrack', next);
    set('seekbackward', function (d) { seekBy(-(d && d.seekOffset || 15)); }); set('seekforward', function (d) { seekBy(d && d.seekOffset || 30); });
    set('seekto', function (d) { if (d && isFinite(d.seekTime)) A.currentTime = d.seekTime; });
  }

  /* ---------- per-page init ---------- */
  var restored = false;
  function init() {
    var c = $('#idlist');
    if (c) {
      var demo = !!c.getAttribute('data-demo');
      loadEps(demo).then(function () { if (!P.eps.length) return; build(); renderList(c); sync(); });
    } else if (!restored) {
      loadEps(false).then(function () { restoreOnce(); });
    }
    if (c) restoreOnce();
    build(); sync();
  }
  function restoreOnce() {
    if (restored) return; restored = true;
    if (!P.eps.length || P.cur >= 0 || P.demo) return;
    try { var s = JSON.parse(localStorage.getItem('s54_pl') || 'null'); if (s && P.eps[s.i] && s.t > 5) { play(s.i, true, s.t); } } catch (x) {}
  }

  /* ---------- soft navigation (keeps the audio alive) ---------- */
  function go(url, push) {
    fetch(url).then(function (r) { if (!r.ok) throw 0; return r.text(); }).then(function (html) {
      var d = new DOMParser().parseFromString(html, 'text/html'), app = d.getElementById('app'); if (!app) throw 0;
      $('#app').innerHTML = app.innerHTML;
      document.title = d.title; document.documentElement.lang = d.documentElement.lang || 'hu';
      document.body.setAttribute('style', d.body.getAttribute('style') || '');
      if (push) history.pushState({}, '', url);
      var h = new URL(url, location.href).hash, t = h && document.getElementById(h.slice(1));
      if (t) t.scrollIntoView(); else window.scrollTo(0, 0);
      init();
    }).catch(function () { location.href = url; });
  }
  document.addEventListener('click', function (e) {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var a = e.target.closest('a[href]'); if (!a || a.target || a.hasAttribute('download')) return;
    var u = new URL(a.href, location.href);
    if (u.origin !== location.origin || u.pathname.indexOf(BASEPATH) !== 0) return;
    if (u.pathname === location.pathname && u.search === location.search) return;
    if (/\.(jpe?g|png|webp|zip|pdf|mp3)$/i.test(u.pathname)) return;
    e.preventDefault(); go(u.href, true);
  });
  window.addEventListener('popstate', function () { go(location.href, false); });

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();

  // newsletter form: submit in place, show the thank-you text
  document.addEventListener('submit', function (ev) {
    var f = ev.target;
    if (!f || !f.closest || !f.closest('.club')) return;
    ev.preventDefault();
    var btn = f.querySelector('button'); if (btn) btn.disabled = true;
    var ok = function () { var p = document.createElement('p'); p.className = 'done'; p.textContent = f.getAttribute('data-ok') || 'OK'; f.replaceWith(p); };
    fetch(f.action, { method: 'POST', body: new FormData(f), mode: 'no-cors' }).then(ok, function () { f.submit(); });
  });

  // "Join the club" sheet, reachable from every page
  function clubSheet(open) {
    var s = document.getElementById('clubsheet'); if (!s) return;
    s.hidden = !open; document.documentElement.classList.toggle('club-open', !!open);
    if (open) { var i = s.querySelector('input[type=email]'); if (i) setTimeout(function () { i.focus(); }, 50); }
  }
  document.addEventListener('click', function (ev) {
    var t = ev.target;
    if (t.closest && t.closest('[data-club]')) { ev.preventDefault(); clubSheet(true); }
    else if (t.id === 'clubsheet' || (t.closest && t.closest('.cs-x'))) { clubSheet(false); }
  });
  document.addEventListener('keydown', function (ev) { if (ev.key === 'Escape') clubSheet(false); });
})();
