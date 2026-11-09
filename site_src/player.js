/* Shane 54 podcast player: streams from the Internet Archive (or demo files) */
(function () {
  var el = document.getElementById('idplayer'); if (!el) return;
  var IA = el.getAttribute('data-ia'), DEMO = el.getAttribute('data-demo'), ROOT = el.getAttribute('data-root') || '';
  var LBL = { now: el.getAttribute('data-now') || 'NOW PLAYING', load: el.getAttribute('data-load') || 'Loading…', err: el.getAttribute('data-err') || 'Could not load the episodes.' };
  var eps = [], cur = -1, a = new Audio(), speeds = [1, 1.25, 1.5, 2], si = 0, seeking = false;
  a.preload = 'metadata';
  var ICON = {
    play: '<svg viewBox="0 0 24 24" width="28" height="28"><path fill="currentColor" d="M8 5v14l11-7z"/></svg>',
    pause: '<svg viewBox="0 0 24 24" width="28" height="28"><path fill="currentColor" d="M6 5h4v14H6zm8 0h4v14h-4z"/></svg>',
    prev: '<svg viewBox="0 0 24 24" width="26" height="26"><path fill="currentColor" d="M6 6h2v12H6zm3.5 6 8.5 6V6z"/></svg>',
    next: '<svg viewBox="0 0 24 24" width="26" height="26"><path fill="currentColor" d="M16 6h2v12h-2zM6 18l8.5-6L6 6z"/></svg>'
  };
  el.innerHTML =
    '<img class="pl-logo" src="' + ROOT + 'assets/img/id_logo.png" alt="International Departures with Shane 54"><div class="pl-meta"><small>' + LBL.now + '</small><h3 class="pl-title">—</h3><span class="pl-sub"></span></div>' +
    '<input class="pl-bar" type="range" min="0" max="1000" value="0" step="1" aria-label="Seek">' +
    '<div class="pl-times"><span class="pl-cur">0:00</span><span class="pl-dur">0:00</span></div>' +
    '<div class="pl-ctl"><button class="pl-spd" aria-label="Speed">1×</button><button class="pl-prev" aria-label="Previous">' + ICON.prev + '</button>' +
    '<button class="pl-play" aria-label="Play">' + ICON.play + '</button><button class="pl-next" aria-label="Next">' + ICON.next + '</button><span class="pl-spacer"></span></div>' +
    '<div class="pl-list"><p class="pl-msg">' + LBL.load + '</p></div>';
  var $ = function (s) { return el.querySelector(s); };
  var bar = $('.pl-bar'), playB = $('.pl-play'), list = $('.pl-list');

  function fmt(s) { if (!isFinite(s)) return '0:00'; s = Math.floor(s); var h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60), x = s % 60;
    return (h ? h + ':' + (m < 10 ? '0' : '') + m : m) + ':' + (x < 10 ? '0' : '') + x; }
  function paint() { var p = a.duration ? a.currentTime / a.duration : 0; bar.style.setProperty('--p', (p * 100) + '%'); if (!seeking) bar.value = Math.round(p * 1000);
    $('.pl-cur').textContent = fmt(a.currentTime); $('.pl-dur').textContent = fmt(a.duration || (eps[cur] && eps[cur].dur)); }
  function render() {
    list.innerHTML = '';
    eps.forEach(function (e, i) {
      var b = document.createElement('button'); b.className = 'pl-row' + (i === cur ? ' on' : '');
      b.innerHTML = '<span class="pl-n">' + (i + 1) + '</span><span class="pl-t"><b></b><s></s></span><span class="pl-d">' + (e.dur ? fmt(e.dur) : '') + '</span>';
      b.querySelector('b').textContent = e.title; b.querySelector('s').textContent = e.sub || '';
      b.onclick = function () { load(i, true); }; list.appendChild(b);
    });
  }
  function load(i, go) {
    if (i < 0 || i >= eps.length) return; cur = i; var e = eps[i];
    a.src = e.src; a.playbackRate = speeds[si];
    $('.pl-title').textContent = e.title; $('.pl-sub').textContent = e.sub || '';
    render(); paint();
    if ('mediaSession' in navigator) { navigator.mediaSession.metadata = new MediaMetadata({ title: e.title, artist: 'Shane 54', album: 'International Departures' }); }
    if (go) a.play();
  }
  function toggle() { if (cur < 0) { load(0, true); } else if (a.paused) { a.play(); } else { a.pause(); } }
  playB.onclick = toggle;
  $('.pl-prev').onclick = function () { if (a.currentTime > 3) { a.currentTime = 0; } else { load(cur - 1, !a.paused); } };
  $('.pl-next').onclick = function () { load(cur + 1, !a.paused || true); };
  $('.pl-spd').onclick = function () { si = (si + 1) % speeds.length; a.playbackRate = speeds[si]; this.textContent = speeds[si] + '×'; };
  bar.oninput = function () { seeking = true; if (a.duration) { a.currentTime = a.duration * bar.value / 1000; } bar.style.setProperty('--p', (bar.value / 10) + '%'); };
  bar.onchange = function () { seeking = false; };
  a.addEventListener('timeupdate', paint); a.addEventListener('loadedmetadata', paint);
  a.addEventListener('play', function () { playB.innerHTML = ICON.pause; el.classList.add('playing'); });
  a.addEventListener('pause', function () { playB.innerHTML = ICON.play; el.classList.remove('playing'); });
  a.addEventListener('ended', function () { if (cur + 1 < eps.length) load(cur + 1, true); });
  if ('mediaSession' in navigator) {
    navigator.mediaSession.setActionHandler('play', function () { a.play(); }); navigator.mediaSession.setActionHandler('pause', function () { a.pause(); });
    navigator.mediaSession.setActionHandler('nexttrack', function () { load(cur + 1, true); }); navigator.mediaSession.setActionHandler('previoustrack', function () { load(cur - 1, true); });
  }
  function start(list_) { eps = list_; if (!eps.length) { list.innerHTML = '<p class="pl-msg">' + LBL.err + '</p>'; return; } load(0, false); }

  if (DEMO) {
    var src = ROOT + 'assets/demo/demo.wav';
    start([{ title: 'Episode title one', sub: '2012 · demo', src: src, dur: 14 }, { title: 'Episode title two', sub: '2012 · demo', src: src, dur: 14 }, { title: 'Episode title three', sub: '2013 · demo', src: src, dur: 14 }]);
  } else {
    fetch('https://archive.org/metadata/' + encodeURIComponent(IA)).then(function (r) { return r.json(); }).then(function (m) {
      var files = (m.files || []).filter(function (f) { return /\.mp3$/i.test(f.name) && f.source !== 'derivative'; });
      if (!files.length) files = (m.files || []).filter(function (f) { return /\.mp3$/i.test(f.name); });
      files.sort(function (x, y) { return x.name.localeCompare(y.name, undefined, { numeric: true }); });
      start(files.map(function (f) {
        return { title: f.title || f.name.replace(/\.mp3$/i, '').replace(/[_]+/g, ' '), sub: f.creator || '', dur: parseFloat(f.length) || 0,
          src: 'https://archive.org/download/' + encodeURIComponent(IA) + '/' + f.name.split('/').map(encodeURIComponent).join('/') };
      }));
    }).catch(function () { start([]); });
  }
})();
