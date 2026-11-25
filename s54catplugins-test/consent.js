(function(){
var C=window.S54||{},KEY='s54_consent',TTL=365*864e5,loaded=false;
function get(){try{var v=JSON.parse(localStorage.getItem(KEY)||'null');if(v&&Date.now()-v.t<TTL)return v.a}catch(e){}return null}
function set(a){try{localStorage.setItem(KEY,JSON.stringify({a:a,t:Date.now()}))}catch(e){}}
window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}
gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied'});
function track(n,p){if(loaded&&get()==='yes'){p=p||{};p.transport_type='beacon';gtag('event',n,p)}}
function load(){
  if(!C.ga||loaded)return;loaded=true;window['ga-disable-'+C.ga]=false;
  var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id='+encodeURIComponent(C.ga);document.head.appendChild(s);
  gtag('js',new Date());gtag('consent','update',{analytics_storage:'granted'});
  gtag('config',C.ga,{allow_google_signals:false,allow_ad_personalization_signals:false});
  var b=document.body.dataset;
  if(b.product){var it={item_id:b.product,item_name:b.name};if(b.price){it.price=+b.price}gtag('event','view_item',{currency:'EUR',value:b.price?+b.price:0,items:[it]})}
}
function wipe(){
  if(C.ga){window['ga-disable-'+C.ga]=true}
  if(loaded)gtag('consent','update',{analytics_storage:'denied'});
  var h=location.hostname,parts=h.split('.'),ds=[h,'.'+h];if(parts.length>2)ds.push('.'+parts.slice(-2).join('.'));
  document.cookie.split(';').forEach(function(c){var n=c.split('=')[0].trim();if(n.indexOf('_ga')===0){
    ds.forEach(function(d){document.cookie=n+'=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/;domain='+d});
    document.cookie=n+'=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/'}});
  loaded=false;
}
var box=null;
function close(){if(box){box.remove();box=null}}
function show(){
  close();box=document.createElement('div');box.className='cc';box.setAttribute('role','dialog');box.setAttribute('aria-label','Cookie settings');
  var cur=get(),root=document.querySelector('link[rel=stylesheet]').getAttribute('href').replace('style.css','');
  box.innerHTML='<h2>Cookies</h2><p>We would like to use analytics cookies (Google Analytics) to see which pages and buttons people use, so we can make the site better. Nothing is set unless you accept. <a href="'+root+'cookies/">Cookie policy</a></p><div class="row"><button type="button" class="btn ghost" data-r>Reject</button><button type="button" class="btn ghost" data-a>Accept</button></div>';
  box.querySelector('[data-r]').onclick=function(){set('no');wipe();close()};
  box.querySelector('[data-a]').onclick=function(){set('yes');load();close()};
  document.body.appendChild(box);
}
document.addEventListener('click',function(e){
  if(e.target.closest('[data-cookie-settings]')){show();return}
  var t=e.target.closest('[data-ev]');if(!t)return;
  var p={},it=t.getAttribute('data-item'),v=t.getAttribute('data-value'),l=t.getAttribute('data-label');
  if(it)p.items=[{item_name:it}];if(v){p.value=+v;p.currency='EUR'}if(l)p.label=l;
  track(t.getAttribute('data-ev'),p);
});
document.addEventListener('toggle',function(e){var d=e.target;if(d.tagName==='DETAILS'&&d.open){var s=d.querySelector('summary');track('faq_open',{label:s?s.textContent.trim():''})}},true);
function init(){var c=get();if(c==='yes')load();else if(c===null)show()}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
