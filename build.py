import datetime
import json
YEAR = datetime.date.today().year
FP = "https://discover.ekasa.life/fp"
DOST = "https://discover.ekasa.life/dost"
OG_IMAGE = "img/ekasa-wordmark.png"
SITE_URL = "https://www.ekasa.life"
SESSIONS_COUNT = "1000+"
SESSIONS_VALUE = "1000"
MAP_EMBED = "https://www.google.com/maps?q=92/64+Patel+Marg+Sector+9+Mansarovar+Jaipur+302020&output=embed"
AR = '<i class="ar"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></i>'

def btn(t, href, cls="btn-primary", ar=True):
    return f'<a class="btn {cls}" href="{href}">{t}{AR if ar else ""}</a>'

PAGES = [("index", "Home"), ("about", "About"), ("faq", "FAQ"), ("resources", "Resources"), ("testimonials", "Testimonials"), ("contact", "Contact"), ("privacy", "Privacy"), ("terms", "Terms")]

BL = '<div class="blobs" aria-hidden="true"><i class="blob b1" data-speed=".07"></i><i class="blob b2" data-speed="-.05"></i><i class="blob b3" data-speed=".09"></i></div>'
BLB = '<div class="blobs" aria-hidden="true"><i class="blob b1" data-speed=".05"></i><i class="blob b2" data-speed="-.04"></i></div>'

def ic(p):
    return f'<span class="ico"><svg viewBox="0 0 24 24">{p}</svg></span>'
LOCK = '<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 018 0v3"/>'
TARGET = '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3.5"/>'
LOOP = '<path d="M4 12a8 8 0 0114-5.3L20 9M20 12a8 8 0 01-14 5.3L4 15M20 4v5h-5M4 20v-5h5"/>'

def shell(fn, title, desc, body, ctaTitle=None):
    links = "".join(f'<li><a href="{p}.html"{" aria-current=page" if p==fn else ""}>{n}</a></li>' for p, n in PAGES)
    canonical = f"{SITE_URL}/" if fn == "index" else f"{SITE_URL}/{fn}.html"
    og_title = "EKASA | Personality Development & Self-Discovery" if fn == "index" else title
    og_desc = "Holistic wellness, rooted in tradition and made for modern life. Personality assessments, counselling and workshops."
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index,follow">
<link rel="canonical" href="{canonical}">
<meta property="og:site_name" content="EKASA">
<meta property="og:type" content="website">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc if fn == "index" else desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{OG_IMAGE}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{OG_IMAGE}">
<meta name="theme-color" content="#FAF6EF">
<link rel="icon" href="img/ekasa-wordmark.png">
<link rel="preload" href="fonts/InterTight-Variable.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav" id="top"><div class="nav-in">
<a class="logo" href="index.html" aria-label="EKASA home"><img src="img/ekasa-wordmark.png" alt="EKASA" width="103" height="30"></a>
<nav aria-label="Primary"><ul>{links}</ul></nav>
<div class="nav-cta">{btn("Book assessment", FP, "btn-primary btn-sm")}<button class="menu-btn" aria-label="Menu" aria-expanded="false"><span></span></button></div>
</div></header>
<main id="main">
{body}
</main>
<footer><div class="foot">
<div class="fgrid">
<div class="fcell"><img class="flogo" src="img/ekasa-logo.png" alt="EKASA"><p>Guided self-discovery and confidential counselling, in one place. Know yourself, heal what hurts.</p>{btn("Book assessment", FP)}</div>
<div class="fcell"><h4>Not sure where to start? <em>Say hello.</em></h4><p>Tell us what feels off. We reply within a day.</p>{btn("Contact us", "contact.html", "btn-ghost")}</div>
<div class="fcell"><div class="flinks"><ul><li><b>Explore</b></li><li><a href="index.html">Home</a></li><li><a href="about.html">About</a></li><li><a href="faq.html">FAQ</a></li></ul><ul><li><b>More</b></li><li><a href="resources.html">Resources</a></li><li><a href="testimonials.html">Testimonials</a></li><li><a href="contact.html">Contact</a></li></ul><ul><li><b>Book</b></li><li><a href="{DOST}">EKASA Dost</a></li><li><a href="{FP}">EKASA Seed</a></li><li><a href="{FP}">EKASA Flower</a></li></ul></div></div>
<div class="fcell"><a class="ph" href="tel:+919694300555">+91 96943 00555</a><a href="https://wa.me/919694300555">WhatsApp</a><a href="mailto:contact@ekasa.in">contact@ekasa.in</a><p>Arch Point Wellness Pvt. Ltd., 92/64, Patel Marg, Sector 9, Mansarovar, Jaipur 302020</p><a class="chip" href="https://instagram.com/archpoint_wellness">Instagram &middot; archpoint_wellness</a></div>
<div class="fcell emerg"><b>Not for crisis situations.</b> Tele-MANAS: 14416 (24/7). Emergency: 112.</div>
</div>
<div class="fbar"><span>&copy; {YEAR} EKASA (powered by Arch Point Wellness Pvt. Ltd.). All rights reserved.</span><span class="ap"><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms</a><img src="img/arch-point-wellness-logo.png" alt="Arch Point Wellness"></span></div>
</div></footer>
<script src="js/main.js"></script>
</body>
</html>'''

def head(eb, h, lead):
    return f'<section class="page-head glassy">{BL}<div class="wrap"><span class="eyebrow fade-up d1">{eb}</span><h1 class="fade-up d2">{h}</h1><p class="lead fade-up d3">{lead}</p></div></section>'

def band(h, extra=""):
    return f'<section class="band-sec"><div class="wrap"><div class="band rv zoom">{BLB}<div class="gpanel tilt"><h2>{h}</h2><div class="row">{btn("Book assessment", FP, "btn-light")}{btn("Start counselling", DOST, "btn-gold", False)}</div>{extra}</div></div></div></section>'

def quote(q, n, r, cls="", av=None):
    a = f'<img src="img/{av}" alt="">' if av else n[0]
    return f'<div class="card {cls}"><span class="qm">&ldquo;</span><q>{q}</q><div class="by"><span class="av">{a}</span><span><b>{n}</b><small>{r}</small></span></div></div>'

# ---------------- HOME
tags = ["Get Clear", "Feel Heard", "Decide Better", "Move Forward"]
chips = "".join(f'<span class="chip{" gold" if i%2 else ""}">{t}</span>' for i,t in enumerate(tags*2))
home = f'''
<section class="hero glassy">{BL}<div class="wrap">
<span class="eyebrow fade-up d1">EKASA &middot; Arch Point Wellness</span>
<h1><span class="ln"><span>Discover who you <em>really are.</em></span></span></h1>
<p class="lead fade-up d3">Holistic wellness, rooted in tradition and made for modern life.</p>
<p class="hero-support fade-up d3">Science, Soul &amp; Self in Harmony. Personality development, self-discovery and counselling for anyone aged 5 and above.</p>
<div class="hero-actions fade-up d4">{btn("Begin Your Journey", FP)}{btn("Talk to EKASA Dost", DOST, "btn-ghost", False)}</div>
<div class="proof glass fade-up d5"><span>{SESSIONS_COUNT} sessions conducted</span></div>
<p class="trust-line fade-up d5">Private. Practical. Designed for everyday life.</p>
<div class="marq fade-up d6" aria-hidden="true"><div class="marq-track">{chips}{chips}</div></div>
<div class="tiles rv zoom">
<div class="tile photo"><img src="img/tanya.jpg" alt="Tanya Maniktala"><div class="cap"><b>Tanya Maniktala</b><small>Actress</small></div></div>
<div class="tile quote notch tilt">{BLB}<span class="qm">&ldquo;</span><p>EKASA helped me uncover my <b class="hl">strengths</b>, gain valuable personal insights, and truly understand my capabilities. Now I feel more empowered than ever to take on bigger things in life.</p><div class="who"><b>Tanya Maniktala</b><small>Actress</small></div></div>
</div>
<div class="stats glass rv"><div class="stat"><b data-to="{SESSIONS_VALUE}" data-suf="+">{SESSIONS_COUNT}</b><span>Sessions conducted</span></div><div class="stat"><b data-to="100" data-suf="%">100%</b><span>Confidential</span></div><div class="stat"><b data-to="98" data-suf="%">98%</b><span>Satisfaction rate</span></div></div>
</div></section>

<section class="alt"><div class="wrap">
<div class="head rv"><span class="eyebrow">Why choose EKASA</span><h2>Why choose <em>EKASA</em></h2><p class="lead">A thoughtful path to understanding yourself, built on ancient wisdom and modern science.</p></div>
<div class="grid g3 why-grid stag">
<div class="card"><span class="num">1</span><h3>Ancient wisdom, modern science</h3><p>We blend ancient sciences with modern psychological and neurological tools for a fuller picture of who you are.</p></div>
<div class="card"><span class="num">2</span><h3>For every stage of life</h3><p>Designed for anyone aged 5 and above: school students, college students, working professionals and parents.</p></div>
<div class="card"><span class="num">3</span><h3>{SESSIONS_COUNT} sessions conducted</h3><p>Individuals and families have used EKASA to find clarity in studies, career, relationships and everyday life. <!-- VERIFY: "individuals and families" is a soft estimate; adjust or remove --></p></div>
<div class="card"><span class="num">4</span><h3>Clear, practical reports</h3><p>A guided assessment of about one hour, with your personalised report ready in 2 to 3 working days.</p></div>
<div class="card"><span class="num">5</span><h3>Private and confidential</h3><p>Your sessions and results stay between you and EKASA (and a parent or guardian for a child).</p></div>
<div class="card"><span class="num">6</span><h3>Online and in person</h3><p>EKASA Dost counselling is available both online and in person, so support fits your life.</p></div>
</div>
<div style="text-align:center;margin-top:36px">{btn("Book your EKASA session", FP, "btn-primary")}</div>
</div></section>

<section><div class="wrap">
<div class="head rv"><span class="eyebrow">How it works</span><h2>Three steps, start to <em>finish</em></h2></div>
<div class="grid g3 steps stag">
<div class="card step"><span class="num">1</span><h3>Discover</h3><p>Book a one-hour assessment. Your report arrives in two to three working days.</p></div>
<div class="card step"><span class="num">2</span><h3>Talk</h3><p>Book a session with a trained counsellor whenever life needs more than a report can give.</p></div>
<div class="card step"><span class="num">3</span><h3>Grow</h3><p>Walk away with real clarity, decisions made from self-knowledge instead of guesswork.</p></div>
</div></div></section>

<section class="alt"><div class="wrap">
<div class="head rv"><span class="eyebrow">Programs</span><h2>Pick where you <em>start</em></h2><p class="lead">Two assessments, one counselling service. Every price is shared on enquiry.</p></div>
<div class="grid g3 stag">
<div class="card prog"><span class="tag">Assessment</span><h3>EKASA Seed</h3><p>Personality, brain dominance, learning style, and career fit. The foundation.</p><dl><div><dt>Duration</dt><dd>1 hour</dd></div><div><dt>Report</dt><dd>2&ndash;3 days</dd></div><div><dt>Price</dt><dd>On enquiry</dd></div></dl>{btn("Book EKASA Seed", FP, "btn-primary")}</div>
<div class="card prog accent"><span class="tag">Assessment</span><h3>EKASA Flower</h3><p>Everything in Seed, plus Astrology, Numerology, and Chakra Assessment.</p><dl><div><dt>Duration</dt><dd>1 hour</dd></div><div><dt>Report</dt><dd>2&ndash;3 days</dd></div><div><dt>Price</dt><dd>On enquiry</dd></div></dl>{btn("Book EKASA Flower", FP, "btn-light")}</div>
<div class="card prog"><span class="tag">Counselling</span><h3>EKASA Dost</h3><p>Confidential counselling for stress, relationships, career, and family.</p><dl><div><dt>Format</dt><dd>Online or in-person</dd></div><div><dt>Confidentiality</dt><dd>100%</dd></div><div><dt>Price</dt><dd>On enquiry</dd></div></dl>{btn("Start counselling", DOST, "btn-primary")}</div>
</div></div></section>

<section><div class="wrap">
<div class="head rv"><span class="eyebrow">Who it's for</span><h2>Who this is <em>for</em></h2></div>
<ul class="who-list stag">
<li><div>Students choosing a stream<span>- get it right the first time.</span></div></li>
<li><div>Professionals stuck in a role that drains them<span>- find out why.</span></div></li>
<li><div>Anyone burning out quietly<span>- talk before it breaks you.</span></div></li>
<li><div>Couples stuck in the same fight<span>- understand the pattern.</span></div></li>
</ul></div></section>

<section class="alt glassy">{BL}<div class="wrap">
<div class="head rv"><span class="eyebrow">Kind words</span><h2>What people <em>say</em></h2></div>
<div class="grid g3 stag">
{quote("A deeply enriching experience, from the assessment to the consultation that followed.", "Ms. Pratima Naithani", "Ex President, Laghu Udyog Bharti, Jaipur")}
{quote("I left the session feeling heard, understood, and lighter than when I walked in.", "Dhanshree", "Interior Designer", "accent")}
{quote("I finally have a space where I don't have to explain myself before being understood.", "Khusbu", "Design Expert")}
</div>
<div style="text-align:center;margin-top:36px" class="rv">{btn("Read more stories", "testimonials.html", "btn-ghost")}</div>
</div></section>

<section><div class="wrap">
<div class="head rv"><span class="eyebrow">Founder's message</span><h2>The people behind <em>EKASA</em></h2><p class="lead">Emotional &middot; Knowledge &middot; Aptitude &middot; Strength &middot; Awareness - the five words behind the name.</p></div>
<div class="grid g2 stag" style="max-width:820px;margin:0 auto">
<div class="person"><img src="img/founder-poonam.jpg" alt="Ar. Poonam Jain"><div class="cap"><b>Ar. Poonam Jain</b><span>Co-founder. Guided by emotional strength and purposeful clarity.</span></div></div>
<div class="person"><img src="img/founder-amit.png" alt="Ar. Amit Khandelwal"><div class="cap"><b>Ar. Amit Khandelwal</b><span>Co-founder. Helps people reconnect with themselves through guided assessments and healing.</span></div></div>
</div></div></section>

<section class="alt glassy">{BL}<div class="wrap"><div class="mood glass tilt rv zoom">
<span class="eyebrow">A small check-in</span><h2>How are you <em>feeling</em> today?</h2><p class="lead">No wrong answer. Just a starting point for a conversation.</p>
<div class="moods" role="group" aria-label="Mood">{"".join(f'<button class="mood-btn" data-mood="{m.lower()}" aria-pressed="false">{m}</button>' for m in ["Calm","Overwhelmed","Stressed","Confused","Hopeful","Low"])}</div>
<div class="mood-resp" id="mood-resp" aria-live="polite"><div><p id="mood-text"></p>{btn("Talk to EKASA Dost", DOST)}</div></div>
</div></div></section>

{band("Your clarity <em>starts</em> today.")}
'''

# ---------------- ABOUT
about = head("About us", "Why people <em>choose</em> EKASA", "Self-discovery and confidential counselling, from Jaipur.") + f'''
<section style="padding-top:0"><div class="wrap">
<div class="about-photos rv zoom"><div class="tile photo"><img src="img/founder-poonam.jpg" alt="Ar. Poonam Jain, founder" style="object-position:center 30%"><div class="cap"><b>Ar. Poonam Jain</b><small>Founder</small></div></div><div class="tile quote notch tilt">{BLB}<span class="qm">&ldquo;</span><p>EKASA was built on the belief that every individual already carries <b class="hl">powerful potential</b> within.</p><div class="who"><b>Ar. Poonam Jain</b><small>Founder</small></div></div></div>
<div class="stats rv"><div class="stat"><b data-to="2">2</b><span>Programs, one ecosystem</span></div><div class="stat"><b data-to="100" data-suf="%">100%</b><span>Confidential counselling</span></div><div class="stat"><b>Jaipur</b><span>Local practice in Mansarovar</span></div></div>
</div></section>

<section class="alt glassy">{BL}<div class="wrap">
<div class="grid vm stag">
<div class="card"><span class="eyebrow" style="align-self:flex-start">Our vision</span><h3 style="font-size:32px;letter-spacing:-.03em">Help people stop guessing about who they are and what they need.</h3></div>
<div class="card accent"><span class="eyebrow" style="align-self:flex-start;color:var(--ink)">Our mission</span><h3 style="font-size:32px;letter-spacing:-.03em">One ecosystem: self-discovery assessment and confidential counselling, in one place.</h3></div>
</div></div></section>

<section><div class="wrap">
<div class="head rv"><span class="eyebrow">The name</span><h2>Five words, one <em>method</em></h2></div>
<div class="pillars stag">
{"".join(f'<div class="pillar"><b>{a}</b><span>{b}</span></div>' for a,b in zip("EKASA",["Emotional","Knowledge","Aptitude","Strength","Awareness"]))}
</div></div></section>

<section class="alt"><div class="wrap">
<div class="head rv"><span class="eyebrow">Founder's message</span><h2>The people behind <em>EKASA</em></h2><p class="lead">Emotional &middot; Knowledge &middot; Aptitude &middot; Strength &middot; Awareness - the five words behind the name.</p></div>
<div class="grid g2 stag" style="max-width:820px;margin:0 auto">
<div class="person"><img src="img/founder-poonam.jpg" alt="Ar. Poonam Jain"><div class="cap"><b>Ar. Poonam Jain</b><span>Co-founder. Guided by emotional strength and purposeful clarity.</span></div></div>
<div class="person"><span class="init">AK</span><div class="cap"><b>Ar. Amit Khandelwal</b><span>Co-founder. Helps people reconnect with themselves through guided assessments and healing.</span></div></div>
</div></div></section>

<section><div class="wrap">
<div class="head rv"><span class="eyebrow">Find us</span><h2>Where we <em>are</em></h2></div>
<div class="grid g2 rv" style="align-items:stretch"><div class="map"><iframe title="EKASA location map" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="{MAP_EMBED}" style="width:100%;height:100%;min-height:260px;border:0;border-radius:inherit;"></iframe></div>
<div class="card"><h3>Arch Point Wellness Pvt. Ltd.</h3><p>92/64, Patel Marg, Sector 9, Mansarovar, Jaipur 302020</p><p>Use the map to find the clinic and book your visit with confidence.</p><div style="margin-top:auto">{btn("Get directions", "https://maps.google.com/?q=92/64+Patel+Marg+Sector+9+Mansarovar+Jaipur+302020", "btn-primary")}</div></div></div>
</div></section>
''' + band("Ready to <em>begin?</em>")

# ---------------- FAQ
with open("faq.json", encoding="utf-8") as faq_file:
    faqs = json.load(faq_file)
def faq_item(item, index):
    verify = f'<!-- VERIFY: {item["verify"]} -->' if item.get("verify") else ""
    return f'<details class="faq-item"{" open" if index == 0 else ""}><summary>{item["question"]}</summary><div><p>{item["answer"]}</p>{verify}</div></details>'
items = "".join(faq_item(item, i) for i, item in enumerate(faqs))
faq_schema = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": item["question"], "acceptedAnswer": {"@type": "Answer", "text": item["answer"]}} for item in faqs]}, ensure_ascii=False)
faq = head("FAQ", "Questions, <em>answered.</em>", "Everything about assessments and counselling. Tap a question to open it.") + f'''
<section style="padding-top:24px"><div class="wrap"><div class="faq-wrap">
<div class="faq-side rv left"><div class="card accent"><h3 style="font-size:30px;letter-spacing:-.03em">Still have questions?</h3><p>We reply within a day.</p><div style="margin-top:8px">{btn("Contact us", "contact.html", "btn-light")}</div></div></div>
<div class="faq-list stag">{items}</div></div></div></section>
<script type="application/ld+json">{faq_schema}</script>
'''

# ---------------- RESOURCES
def post(ic_, t, excerpt, cls=""):
    return f'<article class="card post {cls}"><div class="top"><svg viewBox="0 0 24 24">{ic_}</svg></div><div class="txt"><div class="meta">{"<span class=tag>Featured</span>" if cls else ""}<span class="tag" style="opacity:.8">Guide</span></div><h3>{t}</h3><p>{excerpt}</p></div></article>'
PEN = '<path d="M4 20l4-1L19 8a2.1 2.1 0 00-3-3L5 16l-1 4zM14 7l3 3"/>'
SEED = '<path d="M12 21v-9M12 12c0-4-3-6-7-6 0 4 3 6 7 6zM12 14c0-3 2.5-5 6-5 0 3-2.5 5-6 5z"/>'
FLAME = '<path d="M12 3c1 4 5 5 5 10a5 5 0 01-10 0c0-2 1-3 2-4 0 2 1 3 2 3 0-4-1-6 1-9z"/>'
CHAT = '<path d="M4 5h16v11H9l-5 4V5z"/>'
res = head("Resources", "Notes on getting <em>clear.</em>", "Practical reads on self-discovery, counselling, burnout, and decision-making.") + f'''
<section style="padding-top:24px"><div class="wrap"><div class="grid g3 stag">
{post(PEN, "What Your Report Actually Tells You", "A plain-language guide to reading the insights in your assessment and deciding what to do next.", "feature")}
{post(SEED, "Seed or Flower: How to Choose", "A simple comparison for people who want the right starting point for self-discovery.")}
{post(FLAME, "Burnout Doesn't Look Like You Think", "Early signs, hidden patterns, and the point where a conversation helps more than silence.")}
{post(CHAT, "Talking to Your Teenager About Strengths, Not Grades", "A better way to open a strengths-first conversation at home.")}
</div></div></section>
''' + band("Rather talk it <em>through?</em>")

# ---------------- TESTIMONIALS
tm = head("Stories", "Real people. <em>Real results.</em>", "Stories from people who used EKASA Seed, Flower, and Dost to find clarity.") + f'''
<section class="glassy" style="padding-top:24px">{BL}<div class="wrap"><div class="masonry stag">
{quote("EKASA helped me uncover my strengths and gain real clarity on my own capabilities. Now I feel more empowered to take on bigger things.", "Tanya Maniktala", "Actress", "accent", "tanya.jpg")}
{quote("From HRV and brain tapping to diet reading, the sessions were deeply enriching. I highly recommend EKASA.", "Ms. Pratima Naithani", "Ex President, Laghu Udyog Bharti, Jaipur")}
{quote("I was impressed by the blend of science, technology, and holistic techniques used for healing.", "Capt. Vineet Ranawat", "Manager, Kanha Shanti Vanam")}
{quote("I went in overwhelmed and left with a much clearer mind and a sense of calm. It genuinely helped me.", "Anushka Srivastava", "HR Executive")}
{quote("I left the session feeling heard, understood, and lighter than when I walked in.", "Dhanshree", "Interior Designer")}
{quote("I finally have a space where I don't have to explain myself before being understood.", "Khusbu", "Design Expert")}
</div></div></section>
''' + band("Your story could <em>start</em> here.")

# ---------------- CONTACT
IC = {
 "ph": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/>',
 "ml": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "pin": '<path d="M12 21s7-6.5 7-12a7 7 0 10-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
 "clk": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'}
contact = head("Contact", "Talk to <em>EKASA.</em>", "Call, WhatsApp, or send an enquiry. We reply within a day.") + f'''
<section style="padding-top:24px"><div class="wrap"><div class="contact-grid">
<div class="card rv left" style="padding:40px"><h3 style="font-size:30px;letter-spacing:-.03em">Book a consultation in Jaipur</h3>
<form id="enquiry">
<div class="frow"><label>Name<input name="name" required autocomplete="name"></label><label>Email<input type="email" name="email" required autocomplete="email"></label></div>
<div class="frow"><label>Phone number<input type="tel" name="phone" autocomplete="tel"></label><label>I'm interested in<select name="interest"><option>EKASA Assessment</option><option>EKASA Dost</option><option>General Enquiry</option></select></label></div>
<label>Message<textarea name="message"></textarea></label>
<button class="btn btn-primary" type="submit" style="align-self:flex-start">Send enquiry{AR}</button>
<p class="note">Prefer not to call? Use this form and we’ll reply by phone, WhatsApp, or email.</p>
<p class="ok" id="ok" role="status">Online enquiries are not connected yet. Please call +91 96943 00555 or email contact@ekasa.in.</p>
</form></div>
<div class="grid" style="gap:16px">
<div class="card rv" style="padding:12px 28px"><div class="crow">{ic(IC["ph"])}<div><b>Phone / WhatsApp</b><a href="tel:+919694300555">+91 96943 00555</a></div></div><div class="crow">{ic(IC["ml"])}<div><b>Email</b><a href="mailto:contact@ekasa.in">contact@ekasa.in</a></div></div><div class="crow">{ic(IC["pin"])}<div><b>Address</b><span>Arch Point Wellness Pvt. Ltd., 92/64, Patel Marg, Sector 9, Mansarovar, Jaipur 302020</span></div></div><div class="crow">{ic(IC["clk"])}<div><b>Hours</b><span>Mon&ndash;Sat, 11am&ndash;5pm</span></div></div></div>
<div class="map rv"><iframe title="EKASA contact map" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="{MAP_EMBED}" style="width:100%;height:100%;min-height:260px;border:0;border-radius:inherit;"></iframe></div>
</div></div></div></section>
''' + band("Your clarity, one message <em>away.</em>", '<p class="crisis" style="color:rgba(255,255,255,.8)"><b style="color:#fff">Not for crisis situations.</b> Call Tele-MANAS 14416 or 112.</p>')

privacy = head("Privacy", "Privacy <em>Policy.</em>", "How EKASA handles information shared through this website.") + '''
<section><div class="wrap legal-copy"><p><strong>Placeholder for review:</strong> This Privacy Policy is a plain-language placeholder and must be reviewed and completed by EKASA before publication.</p>
<h2>Information we receive</h2><p>When you contact EKASA, we may receive the details you choose to send, such as your name, email address, phone number and message.</p>
<h2>How we use it</h2><p>We use enquiry details to respond to requests, arrange services and provide support. We do not sell personal information.</p>
<h2>Questions</h2><p>For privacy questions, contact <a href="mailto:contact@ekasa.in">contact@ekasa.in</a>.</p></div></section>
'''
terms = head("Terms", "Terms <em>of Use.</em>", "Terms for using the EKASA website and enquiry links.") + '''
<section><div class="wrap legal-copy"><p><strong>Placeholder for review:</strong> These Terms are a plain-language placeholder and must be reviewed and completed by EKASA before publication.</p>
<h2>Website information</h2><p>Content on this website is general information and is not medical or psychological diagnosis, emergency care or a substitute for professional advice.</p>
<h2>Bookings</h2><p>Service details and pricing are confirmed on enquiry. Please use the booking links and contact details provided on this site.</p>
<h2>Contact</h2><p>Questions can be sent to <a href="mailto:contact@ekasa.in">contact@ekasa.in</a>.</p></div></section>
'''

out = {
 "index": ("EKASA Jaipur | Self-Discovery Assessments & Counselling", "Self-discovery assessments, confidential counselling, and practical clarity in Jaipur by EKASA (Arch Point Wellness Pvt. Ltd.).", home),
 "about": ("About EKASA Jaipur | Founders, Vision & Mission", "Meet the EKASA founders, understand the name, and see how our Jaipur practice combines self-discovery with confidential counselling.", about),
 "faq": ("EKASA FAQ | Seed, Flower & Dost", "Get answers about EKASA Seed, Flower, and Dost, including what to expect, confidentiality, pricing, and how the process works.", faq),
 "resources": ("EKASA Resources | Self-Discovery & Counselling Guides", "Practical guides on assessment, counselling, burnout, and self-awareness from EKASA Jaipur.", res),
 "testimonials": ("EKASA Testimonials | Stories from Self-Discovery & Counselling", "Read stories from people who used EKASA Seed, Flower, and Dost for clearer decisions and confidential support.", tm),
 "contact": ("Contact EKASA Jaipur | Book a Consultation", "Contact EKASA in Jaipur to book a self-discovery assessment or confidential counselling session. Call, WhatsApp, or send an enquiry.", contact),
 "privacy": ("EKASA Privacy Policy", "Read the EKASA privacy policy placeholder.", privacy),
 "terms": ("EKASA Terms of Use", "Read the EKASA terms of use placeholder.", terms),
}
for k, (t, d, b) in out.items():
    open(f"{k}.html", "w").write(shell(k, t, d, b))
open("404.html", "w", encoding="utf-8").write(shell("404", "Page not found | EKASA", "The page you requested could not be found.", head("404", "That page <em>moved.</em>", "Let's get you back to EKASA.") + f'<section><div class="wrap" style="text-align:center">{btn("Return home", "index.html")}</div></section>'))
urls = [f"{SITE_URL}/" if k == "index" else f"{SITE_URL}/{k}.html" for k in out]
open("sitemap.xml", "w", encoding="utf-8").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{url}</loc></url>\n' for url in urls) + '</urlset>\n')
open("robots.txt", "w", encoding="utf-8").write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
print("ok")
