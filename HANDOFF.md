# Taverna Racilor Cluj: predare proiect

Site static (HTML/CSS/JS, fără build), live pe Cloudflare Pages: https://tavernaracilorcluj.pages.dev
Repo: `bymarccc/tavernaracilorcluj`, branch `main` (orice push pe `main` se publică singur în ~1-3 min).

## Fișiere
- `index.html`: prima pagină (hero cu video, evenimente, meniuri, pachete cu slider pe mobil, hartă, formular, subsol)
- `corporate.html`, `private.html`, `nunti.html`, `catering.html`, `petreceri.html`, `conferinte.html`, `oyster-bar.html`: pagini de eveniment (generate cu `tools_gen_pages.py`, scriptul copiază header/subsol din `index.html`; după schimbări în header/subsol regenerează-le)
- `seafood-boil.html`: pagină scrisă manual, paleta găleții (albastru, portocaliu, galben, crem), formular „Rezervă-ți Boil-ul" la final
- `assets/style.css`: tot stilul; `assets/site.js`: comportamente; `assets/config.js`: valorile editabile
- `assets/`: poze, `logo.png`, `video-1.mp4`, `video-2.mp4`
- `CERINTE-MANAGER.md`: lista de întrebări pentru managerul restaurantului

## Valori (în `assets/config.js`, obiectul `SITE`)
Completat: prețuri pachete (Clasic 150, Platou 150, Seafood Boil 120 lei), minim participanți 50, capacitate 300, e-mail contact@tavernaracilorcluj.ro, Instagram și TikTok.
Lipsesc: prețuri băuturi (Soft, Vin și bere, Complet), comandă minimă vouchere, telefon, persoană de contact, linkuri LinkedIn și Facebook, `formEndpoint` (fără el, formularele deschid aplicația de e-mail a vizitatorului).

## De făcut / probleme cunoscute
- Poze lipsă: hero pagină Seafood Boil (poza cu crab și porumb, cu logo peste), Octopus (meniuri), Business lunch și Burgers (scoase din listă), pagini private/catering folosesc poze de eveniment refolosite.
- Videoclipurile 2 și 3 din rândul de 3 sunt casete negre cu play; `video-2.mp4` e tăiat înainte de logo-ul Pescobar.
- Textele paginilor tip London Kitchen sunt scrise de noi în română, nu traduse (domeniul lor era blocat în sesiune).
- Linkurile „Explorează" și butoanele de meniu: `SITE.links`, `SITE.menuUrl`.
- Nu s-a cerut încă PR; site-ul e publicat direct de pe `main`.

## Preferințe ale clientului
Aspect ca thelondonkitchen.com (culori prună `#552C3C`, crem `#F9F8F4`, salvie `#A5B788`, titluri Bebas Neue, text Lato, text mic, carduri plate), pagina Seafood Boil ca delmarvaseafoodboil.com dar cu desene și texte proprii. Tot textul public e în română. Nu copia logo-uri, desene sau texte ale altor firme. Verifică pe 390 px și 1440 px înainte de publicare.
