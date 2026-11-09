
document.addEventListener('click',function(e){
  var t=e.target.closest('[data-yt]'); if(!t) return;
  e.preventDefault();
  var f=document.createElement('iframe');
  f.src='https://www.youtube-nocookie.com/embed/'+t.getAttribute('data-yt')+'?autoplay=1&rel=0';
  f.allow='autoplay; encrypted-media; fullscreen; picture-in-picture';
  f.allowFullscreen=true; f.title='video';
  t.innerHTML=''; t.removeAttribute('data-yt'); t.appendChild(f);
});
