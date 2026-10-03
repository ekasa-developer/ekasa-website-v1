(function(){
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;

  // scroll reveal (auto-staggered inside .stag containers)
  document.querySelectorAll('.stag').forEach(function(g){
    Array.prototype.forEach.call(g.children,function(c,i){c.classList.add('rv');c.style.setProperty('--i',i)});
  });
  var els=document.querySelectorAll('.rv,.steps');
  if(!('IntersectionObserver' in window)||reduce){els.forEach(function(e){e.classList.add('in')})}
  else{
    var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}})},{threshold:.15,rootMargin:'0px 0px -6% 0px'});
    els.forEach(function(e){io.observe(e)});
  }

  // count-up numbers
  function count(el){
    var to=parseFloat(el.dataset.to),suf=el.dataset.suf||'',t0=null,d=1600;
    if(reduce){el.textContent=to+suf;return}
    function f(t){if(!t0)t0=t;var p=Math.min((t-t0)/d,1),e=1-Math.pow(1-p,4);el.textContent=Math.round(to*e)+suf;if(p<1)requestAnimationFrame(f)}
    requestAnimationFrame(f);
  }
  var cs=document.querySelectorAll('[data-to]');
  if('IntersectionObserver' in window){
    var co=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){count(x.target);co.unobserve(x.target)}})},{threshold:.6});
    cs.forEach(function(e){co.observe(e)});
  }else cs.forEach(function(e){e.textContent=e.dataset.to+(e.dataset.suf||'')});

  // nav: shrink on scroll, hide on scroll down, show on scroll up
  var nav=document.querySelector('.nav'),last=0;
  addEventListener('scroll',function(){
    var y=scrollY;nav.classList.toggle('scrolled',y>20);
    var open=document.querySelector('.nav ul.open');
    nav.classList.toggle('hide',y>last&&y>400&&!open);last=y;
  },{passive:true});

  // mobile menu
  var mb=document.querySelector('.menu-btn'),ul=document.querySelector('.nav ul');
  if(mb)mb.addEventListener('click',function(){var o=ul.classList.toggle('open');mb.setAttribute('aria-expanded',o)});
  if(ul)ul.addEventListener('click',function(e){if(e.target.tagName==='A'){ul.classList.remove('open');mb.setAttribute('aria-expanded',false)}});

  // accordion (one open at a time)
  document.querySelectorAll('.acc-q').forEach(function(b){
    b.addEventListener('click',function(){
      var it=b.parentElement,was=it.classList.contains('open');
      document.querySelectorAll('.acc-item.open').forEach(function(o){o.classList.remove('open');o.querySelector('.acc-q').setAttribute('aria-expanded',false)});
      if(!was){it.classList.add('open');b.setAttribute('aria-expanded',true)}
    });
  });

  // mood check
  var mbs=document.querySelectorAll('.mood-btn'),box=document.getElementById('mood-resp'),txt=document.getElementById('mood-text');
  var msg={
    calm:"Good to hear. A calm moment is still worth understanding, an EKASA assessment can help you build on it.",
    overwhelmed:"That's a lot to carry. EKASA Dost is a space to talk it through, at your own pace.",
    stressed:"Stress builds up quietly. A conversation with EKASA Dost can help you find where it's coming from.",
    confused:"Confusion is often the start of clarity. An EKASA assessment can help you see your own patterns.",
    hopeful:"That's worth holding onto. EKASA Dost can help you build on it, one conversation at a time.",
    low:"Thank you for naming that. EKASA Dost is here to listen, whenever you're ready."
  };
  mbs.forEach(function(b){b.addEventListener('click',function(){
    mbs.forEach(function(x){x.classList.remove('active');x.setAttribute('aria-pressed',false)});
    b.classList.add('active');b.setAttribute('aria-pressed',true);
    txt.textContent=msg[b.dataset.mood]||'';box.classList.add('show');
  })});

  var f=document.getElementById('enquiry');
  if(f)f.addEventListener('submit',function(e){
    var endpoint=f.dataset.endpoint,ok=document.getElementById('ok');
    if(!endpoint){e.preventDefault();ok.textContent='Online enquiries are not connected yet. Please call +91 9694300555 or email contact@ekasa.in.';ok.classList.add('show');return}
    e.preventDefault();
    var submit=f.querySelector('button[type="submit"]');
    submit.disabled=true;
    fetch(endpoint,{method:'POST',body:new FormData(f),headers:{Accept:'application/json'}})
      .then(function(r){if(!r.ok)throw new Error('Request failed');ok.textContent='Thanks. Your enquiry has been sent. We will reply within a day.';ok.classList.add('show');f.reset()})
      .catch(function(){ok.textContent='We could not send your enquiry. Please call +91 9694300555 or email contact@ekasa.in.';ok.classList.add('show')})
      .finally(function(){submit.disabled=false});
  });
})();

// glass layer: slow parallax on blobs + gentle tilt on glass panels
(function(){
  if(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  var bl=[].slice.call(document.querySelectorAll('.blob')),t=false;
  function upd(){t=false;var h=innerHeight;bl.forEach(function(b){var r=b.parentNode.getBoundingClientRect();if(r.bottom<0||r.top>h)return;b.style.transform='translate3d(0,'+((r.top+r.height/2-h/2)*parseFloat(b.dataset.speed||0)).toFixed(1)+'px,0)'})}
  addEventListener('scroll',function(){if(!t){t=true;requestAnimationFrame(upd)}},{passive:true});addEventListener('resize',upd);upd();
  if(!matchMedia('(hover:hover)').matches)return;
  document.querySelectorAll('.tilt').forEach(function(el){
    el.addEventListener('pointermove',function(e){var r=el.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;el.style.transform='perspective(900px) rotateY('+(x*5).toFixed(2)+'deg) rotateX('+(-y*5).toFixed(2)+'deg)'});
    el.addEventListener('pointerleave',function(){el.style.transform=''});
  });
})();
