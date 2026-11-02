import re
h=open("index.html").read()
hd=h[:h.index("</head>")+7]
a=h.index('<header class="top"');b=h.index('<main id="main">')
hdr=h[a:b].replace('href="#','href="index.html#')
c=h.index('<section class="on-plum contact"');d=h.index("</section>",c)+10
foot=h[c:d].replace('href="#','href="index.html#')
def head(title,desc):
    x=re.sub(r"<title>.*?</title>",f"<title>{title} · Taverna Racilor Cluj</title>",hd)
    x=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',x)
    x=re.sub(r'<meta property="og:title" content="[^"]*">',f'<meta property="og:title" content="{title} · Taverna Racilor Cluj">',x)
    x=re.sub(r'<meta property="og:description" content="[^"]*">',f'<meta property="og:description" content="{desc}">',x)
    return x
ARROW='<i>→</i>'
def card(img,alt,title,text,href,label):
    return f'''      <a class="ocard" href="{href}">
        <figure><img src="assets/{img}" alt="{alt}" loading="lazy" decoding="async" onerror="this.remove()"></figure>
        <div class="obody"><h3>{title}</h3><p>{text}</p><span class="olink">{label} {ARROW}</span></div>
      </a>
'''
READY='''    <div class="ready rv">
      <h2>Pentru mai multe informații</h2>
      <p>Scrie-ne sau sună-ne și îți răspundem cu detalii despre meniuri, disponibilitate și valoarea estimată.</p>
      <div class="ready-btns">
        <a class="rbtn" data-link="mail" data-val="email" data-keep href="index.html#form">Scrie-ne un e-mail <i>→</i></a>
        <a class="rbtn" data-link="tel" data-val="phone" data-keep href="index.html#form">Sună-ne <i>→</i></a>
        <a class="rbtn" href="index.html#form">Trimite-ne detaliile <i>→</i></a>
      </div>
    </div>'''
def page(fn,title,desc,hero,alt,h1,paras,cards,pack,pre=''):
    ps="".join(f"      <p>{p}</p>\n" for p in paras)
    body=f'''{head(title,desc)}
<body>
<a class="skip" href="#main">Sari la conținut</a>

{hdr}<main id="main">

<figure class="pghero"><img src="assets/{hero}" alt="{alt}" fetchpriority="high"></figure>

<section class="sec" style="padding-bottom:0">
  <div class="wrap">
    <div class="evintro rv">
      <h1 class="pgh1">{h1}</h1>
{ps}    </div>
{pre}    <div class="ocards">
{cards}    </div>
{READY}
  </div>
</section>

{foot}
</main>

<script src="assets/config.js"></script>
<script src="assets/site.js"></script>
</body>
</html>
'''
    open(fn,"w").write(body)

def opts(pack):
    return (card("oyster-event.jpg","Oyster bar la un eveniment, cu stridii pe gheață","Oyster Bar &amp; Caviar","Stridii proaspete pe gheață, cu lămâie și sosuri, alături de caviar. Un început elegant pentru recepția de bun venit.","oyster-bar.html","Descoperă")
      +card("pkg-boil.jpg","Seafood Boil turnat pe masă","Seafood Boil","Experiența semnătură a casei: conținutul oalei este turnat direct pe masă, în fața întregii echipe.","seafood-boil.html","Descoperă")
      +card("pkg-clasic.jpg","Fel principal de pește servit individual","Meniu clasic","Gustare de bun venit, ciorbă pescărească, fel principal individual de pește și desert, cu preț fix pe persoană.","index.html#pachete","Vezi pachetele"))

TYPES=(card("event-private.jpg","Petrecere de sezon la Taverna Racilor","Petreceri de vară și de Crăciun","Cina de Crăciun sau petrecerea de vară a echipei, cu preț fix pe persoană și zonă separată pentru grup.","petreceri.html","Descoperă")
      +card("event-corporate.jpg","Sală pregătită pentru o conferință","Conferințe și seminarii","Pauze de cafea, prânzuri de lucru și cine pentru participanți, servite la timp și fără întreruperi.","conferinte.html","Descoperă"))
PRE_TYPES='    <div class="rv" style="margin-top:clamp(30px,5vw,50px)"><span class="kicker">Tipuri de evenimente</span><h2>Alege ocazia</h2><span class="rule"></span></div>\n'
PRE_OPT='    <div class="rv" style="margin-top:clamp(30px,5vw,50px)"><span class="kicker">Formule de meniu</span><h2>Alege experiența</h2><span class="rule"></span></div>\n'
page("corporate.html","Corporate","Evenimente de firmă la Taverna Racilor Cluj: cine de gală, mese de echipă și petreceri de sfârșit de an, cu zonă separată pentru grup.",
 "event-corporate.jpg","Sală pregătită pentru un eveniment de firmă","Evenimente corporate",
 ["La Taverna Racilor, Iulius Mall Cluj, organizăm evenimente de firmă cu aceeași grijă pentru detalii pe care o avem în restaurant: de la mese de echipă și cine de gală la petreceri de sfârșit de an și recepții.",
  "Știm că evenimentele de firmă au termene strânse și așteptări mari. De aceea fiecare meniu se adaptează echipei, invitaților și ocaziei, iar grupul are o zonă separată, pregătită și servită de o echipă dedicată.",
  "Alegeți ocazia și formula de meniu de mai jos, iar noi revenim cu propunerea finală de meniu și valoarea estimată."],TYPES+'    </div>\n'+PRE_OPT+'    <div class="ocards">\n'+opts("c"),"",pre=PRE_TYPES)
page("private.html","Private","Cine intime, petreceri și aniversări la Taverna Racilor Cluj, în zona dedicată grupurilor.",
 "event-private.jpg","Masă lungă pregătită pentru un eveniment privat","Evenimente private",
 ["O cină intimă, o aniversare sau o petrecere între prieteni merită o seară fără griji. La Taverna Racilor, Iulius Mall Cluj, ne ocupăm de tot, ca voi să vă bucurați de oamenii dragi.",
  "Abordarea noastră e personală: adaptăm meniul la invitați, la preferințe alimentare și la ocazie, iar grupul are o zonă separată, servită de o echipă dedicată.",
  "Alegeți una dintre formulele de mai jos și revenim cu o propunere pe măsura serii voastre."],opts("p"),"")
page("nunti.html","Nunți","Mâncare excelentă și servire impecabilă pentru o zi de neuitat, la Taverna Racilor Cluj.",
 "event-nunti.jpg","Discurs la masa mirilor într-un restaurant luminat cald","Nunți",
 ["O nuntă e o zi pe care n-o veți uita. La Taverna Racilor, Iulius Mall Cluj, punem accent pe mâncare excelentă și servire atentă, ca voi să vă bucurați de fiecare moment.",
  "Meniul se adaptează nevoilor voastre, invitaților și preferințelor alimentare, iar grupul are o zonă separată, pregătită și servită de o echipă dedicată.",
  "Alegeți una dintre formulele de mai jos și revenim cu o propunere gândită pentru ziua voastră."],opts("n"),"")
page("petreceri.html","Petreceri de vară și de Crăciun","Petreceri de vară și cine de Crăciun pentru echipe, la Taverna Racilor Cluj.",
 "event-private.jpg","Echipă la o petrecere elegantă","Petreceri de vară și de Crăciun",
 ["Fie că sărbătoriți vara sau închideți anul împreună, o petrecere de firmă reușită îi face pe colegi să se simtă apreciați. La Taverna Racilor, Iulius Mall Cluj, ne ocupăm de mâncare, servire și atmosferă, ca voi să vă bucurați de seară.",
  "De la gustarea de bun venit până la desert, meniul se adaptează echipei, invitaților și bugetului, cu preț fix pe persoană. Grupul are o zonă separată, pregătită și servită de o echipă dedicată.",
  "Pentru sezonul de iarnă, locurile se alocă în ordinea confirmărilor, iar evenimentele de luni până joi primesc un upgrade gratuit."],opts("p"),"")
page("conferinte.html","Conferințe și seminarii","Mese și pauze de cafea pentru conferințe și seminarii, la Taverna Racilor Cluj.",
 "event-corporate.jpg","Sală pregătită pentru un eveniment de firmă","Conferințe și seminarii",
 ["O conferință sau un seminar funcționează mai bine când participanții sunt bine hrăniți și nimeni nu pierde timp cu logistica. La Taverna Racilor, Iulius Mall Cluj, le oferim un loc unde se pot opri, mânca și continua ziua cu energie.",
  "Meniul se adaptează numărului de participanți, programului și preferințelor alimentare, anunțate cu cel puțin 3 zile înainte, iar grupul are o zonă separată, servită de o echipă dedicată.",
  "Spuneți-ne data, numărul de participanți și formula dorită, iar noi revenim cu propunerea finală și valoarea estimată."],opts("c"),"")
# oyster bar page
def ocard2(img,alt,title,text):
    return f'''      <div class="ocard">
        <figure><img src="assets/{img}" alt="{alt}" loading="lazy" decoding="async" onerror="this.remove()"></figure>
        <div class="obody"><h3>{title}</h3><p>{text}</p></div>
      </div>
'''
oy=ocard2("oyster-bar-curved.jpg","Bar curbat cu stridii pe gheață","Oyster Bar","Stridii proaspete, deschise și servite pe gheață, cu lămâie și sosuri. Un colț de bar care devine punctul de întâlnire al serii.")+ocard2("oyster-premium.jpg","Stridii premium servite pe gheață, cu lămâie și sos de șalotă","Stridii premium","O selecție de stridii servite pe gheață, cu lămâie și sos de șalotă, pentru invitații care apreciază gusturile rafinate.")+ocard2("oyster-caviar.jpg","Platou cu stridii, caviar și sos mignonette","Caviar","Caviar servit alături de stridii, pentru un moment de rafinament la recepție sau la masă.")
page("oyster-bar.html","Oyster Bar &amp; Caviar","Oyster Bar și caviar la evenimentele Taverna Racilor Cluj.",
 "oyster-event.jpg","Oyster bar la un eveniment elegant","Oyster Bar &amp; Caviar",
 ["Un serviciu premium, pentru evenimentele în care vreți ca fiecare detaliu să conteze. Stridii proaspete și caviar, servite elegant, ca introducere la cină sau ca punct de atracție la recepție.",
  "Se potrivește evenimentelor corporate, petrecerilor private și nunților. Detaliile, disponibilitatea și prețurile le stabilim împreună, în funcție de eveniment."],oy,"")

cat=(ocard2("event-private.jpg","Masă lungă pregătită pentru o aniversare","Aniversări","Zile de naștere și aniversări, în zona dedicată grupului: meniu ales împreună, servire atentă și o seară fără griji pentru gazdă.")
    +ocard2("event-nunti.jpg","Discurs la masa mirilor","Nunți","Mâncare excelentă și servire impecabilă pentru o zi pe care n-o veți uita, adaptate invitaților și dorințelor voastre.")
    +ocard2("event-private.jpg","Masă festivă pregătită pentru un botez","Botezuri","O masă festivă pentru familie și prieteni, cu meniu adaptat vârstelor și preferințelor alimentare ale invitaților.")
    +ocard2("event-corporate.jpg","Mese pregătite pentru un eveniment acasă","Evenimente acasă și petreceri","Aducem experiența Taverna Racilor la voi acasă sau în locația aleasă: meniu, preparare și servire, ca voi să vă bucurați de oaspeți."))
page("catering.html","Catering","Catering premium pentru aniversări, nunți, botezuri și evenimente acasă, de la Taverna Racilor Cluj.",
 "event-nunti.jpg","Masă festivă la un eveniment elegant","Catering premium",
 ["Cele mai importante momente merită o masă pe măsură. Cu cateringul Taverna Racilor, aducem bucătăria de restaurant și servirea atentă la evenimentul vostru, oriunde alegeți să-l sărbătoriți.",
  "Nimic standard: fiecare meniu se construiește împreună, în funcție de ocazie, invitați și preferințe alimentare, cu fructe de mare proaspete, prezentare îngrijită și o echipă care se ocupă de fiecare detaliu.",
  "Spuneți-ne data, locul și numărul de invitați, iar noi revenim cu propunerea finală de meniu și valoarea estimată."],cat+'    </div>\n'+PRE_OPT+'    <div class="ocards">\n'+opts("c"),"",pre='    <div class="rv" style="margin-top:clamp(30px,5vw,50px)"><span class="kicker">Ocazii</span><h2>Pentru orice sărbătoare</h2><span class="rule"></span></div>\n')
