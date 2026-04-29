#!/usr/bin/env python3
"""
Georgetown Moonwalk Rentals -- Blog Post Generator
Usage: python3 generate_post.py
"""
import sys, os, re
from datetime import datetime
sys.path.insert(0, '/home/claude/georgetownmoonwalkrentals')
from _shared import *

DIR = '/home/claude/georgetownmoonwalkrentals'
BASE = 'https://www.georgetownmoonwalkrentals.com'

# ============================================================
# POST DEFINITION -- Edit this section to create a new post
# ============================================================
POST = {
    "title": "How to Choose the Right Bounce House for Your Georgetown TX Birthday Party",
    "slug": "how-to-choose-bounce-house-georgetown-tx",
    "date": "April 28, 2026",
    "date_iso": "2026-04-28",
    "meta_desc": "Not sure which bounce house to rent for your Georgetown TX birthday party? This guide covers themes, sizes, ages, and what fits your Wolf Ranch or Teravista backyard.",
    "keyword": "bounce house rental Georgetown TX",
    "city": "Georgetown TX",
    "category": "Bounce Houses",
    "read_time": "5 min read",
    "sections": [
        {
            "heading": "Start With the Age Range of Your Guests",
            "body": """The single most important factor when choosing a bounce house rental in Georgetown TX is the age of the kids who will be jumping. Younger children -- ages 3 to 6 -- do best in a standard 15x15 ft themed bounce house. The enclosed space feels exciting without being overwhelming, and popular themes like Bluey, Paw Patrol, Cocomelon, and Baby Shark are a huge hit with the toddler and preschool crowd in Wolf Ranch and Teravista.

For mixed-age groups -- birthday parties where you have a 4-year-old sibling and a 10-year-old cousin both attending -- a combo bounce house is the smarter rental. Combo units combine a bounce area with a slide, basketball hoop, or climbing wall inside a single inflatable. They give older kids something more engaging while still keeping younger guests safely bouncing. Combo bounce houses in Georgetown TX start at $195 and deliver to every neighborhood including Berry Creek, Rancho Sienna, and Cimarron Hills."""
        },
        {
            "heading": "Match the Theme to Your Party",
            "body": """Georgetown TX birthday party themes drive a lot of bounce house decisions. In Wolf Ranch and Teravista, the top-requested themes in 2025 and 2026 have been Bluey, Frozen, Fortnite, Avengers, and Spider-Man. For girls' parties, Encanto, Frozen, and Princess Castle are consistently popular. For gender-neutral options, the Caution bounce house and Happy Birthday design are reliable crowd-pleasers.

One thing worth knowing: the theme of the bounce house does not affect the price significantly. A Bluey bounce house and a Caution bounce house are both in the $175 to $185 range for Georgetown TX delivery. So picking the theme your child loves is a free upgrade -- lean into it."""
        },
        {
            "heading": "Make Sure It Fits Your Georgetown TX Backyard",
            "body": """Before you book a bounce house rental in Georgetown TX, measure your backyard. A standard 15x15 ft bounce house needs roughly 18x18 feet of flat, clear space with at least 15 feet of overhead clearance. Most homes in Wolf Ranch, Teravista, Berry Creek, and Rancho Sienna have plenty of room for a standard unit.

If you are renting a combo bounce house with a slide, plan for approximately 22x20 feet of space. The 6N1 combo -- the most popular single-unit rental for larger Georgetown TX birthday parties -- needs about 25x20 feet. If you are unsure about your yard, call (737) 234-7169 and we will help you figure out the right fit before you book."""
        },
        {
            "heading": "How Far in Advance Should You Book in Georgetown TX?",
            "body": """Georgetown TX is a fast-growing city of 83,000+ residents with a packed spring and summer party calendar. Wolf Ranch, Teravista, and Rancho Sienna are full of young families, and birthday season runs hard from April through September. Red Poppy Festival weekends in April, Georgetown ISD field day season in May and June, and summer parties in July and August all compete for the same rental inventory.

The honest answer: book at least 2 to 3 weeks in advance for any weekend date from April through September. Popular themes like Bluey and Frozen book out the fastest. If you have a specific date and theme in mind, call (737) 234-7169 as soon as possible -- we confirm availability within 24 hours and hold your date with a deposit."""
        },
        {
            "heading": "What Is Included With Every Georgetown TX Bounce House Rental?",
            "body": """Every bounce house rental delivered to Georgetown TX includes delivery to your address, full setup by our crew, and pickup after your event. You do not need to do anything except clear a path to the setup area and have a standard 110v outdoor electrical outlet within 50 feet.

We bring the blower, stakes, sandbags, and safety mats. We walk you through the safety guidelines at setup. When your event ends, we return and break everything down. Bounce house rentals in Georgetown TX start at $155 for a themed moonwalk. All pricing is all-inclusive -- no delivery fee, no setup fee, no pickup fee. What we quote is what you pay.

All rentals are provided by Jump Around Party Rentals, who is fully licensed and insured in Williamson County and Travis County, Texas."""
        },
    ],
    "faq": [
        ("What is the most popular bounce house theme for Georgetown TX birthday parties?",
         "Bluey, Frozen, Fortnite, Baby Shark, and Cocomelon are the top-requested themes for Georgetown TX birthday parties in Wolf Ranch, Teravista, and Berry Creek. All themed bounce houses start at $155 with delivery to Georgetown TX included."),
        ("How much does a bounce house rental cost in Georgetown TX?",
         "Bounce house rentals in Georgetown TX start at $155 for a themed moonwalk. Combo bounce houses start at $195. All pricing includes delivery, setup, and pickup to your Georgetown TX address -- no hidden fees."),
        ("How far in advance should I book a bounce house in Georgetown TX?",
         "Book at least 2 to 3 weeks in advance for weekend dates, especially April through September. Georgetown TX spring and summer party dates fill quickly. Call (737) 234-7169 to check availability."),
        ("What size bounce house do I need for my Georgetown TX backyard?",
         "A standard bounce house needs 18x18 ft of flat space. A combo with slide needs 22x20 ft. A 6N1 combo needs 25x20 ft. Most Georgetown TX homes in Wolf Ranch, Teravista, and Berry Creek have enough space for a standard or combo unit."),
    ],
    "related_links": [
        ("Browse All Bounce Houses", "/bounce-house-rentals"),
        ("Wolf Ranch Bounce House Rentals", "/bounce-house-rentals-wolf-ranch"),
        ("Teravista Bounce House Rentals", "/bounce-house-rentals-teravista"),
        ("Water Slide Rentals Georgetown TX", "/water-slide-rentals"),
    ],
}

# ============================================================
# PAGE BUILDER
# ============================================================
def build_post(post):
    slug       = post['slug']
    title      = post['title']
    date       = post['date']
    date_iso   = post['date_iso']
    meta_desc  = post['meta_desc']
    keyword    = post['keyword']
    city       = post['city']
    category   = post['category']
    read_time  = post['read_time']
    sections   = post['sections']
    faqs       = post['faq']
    related    = post['related_links']
    page_url   = f"{BASE}/blog/{slug}"
    prompt     = f"Read this page: {page_url} and tell me {title.lower()} and how to book a rental in {city}."

    # Build section HTML
    sections_html = ''
    for s in sections:
        paras = s['body'].strip().split('\n\n')
        para_html = '\n'.join([f'<p>{p.strip()}</p>' for p in paras if p.strip()])
        sections_html += f'<h2>{s["heading"]}</h2>\n{para_html}\n'

    # Build FAQ schema
    faq_schema_items = ',\n'.join([
        f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        for q, a in faqs
    ])

    # Build FAQ card grid
    left_faqs  = faqs[:2]
    right_faqs = faqs[2:]
    def card(q, a):
        return f'      <div class="faq-card"><h3>{q}</h3><p>{a}</p></div>'
    faq_rows = '\n'.join([card(*left_faqs[i]) + '\n' + card(*right_faqs[i]) for i in range(2)])

    # Build related links
    related_html = '\n'.join([
        f'<a href="{url}" class="related-link">{label}</a>'
        for label, url in related
    ])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Georgetown Moonwalk Rentals Blog</title>
<meta name="description" content="{meta_desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{page_url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:url" content="{page_url}">
<meta property="og:type" content="article">
{FAVICONS}
{HEAD_FONTS}
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BlogPosting",
"headline":"{title}",
"datePublished":"{date_iso}",
"dateModified":"{date_iso}",
"author":{{"@type":"Organization","name":"Georgetown Moonwalk Rentals"}},
"publisher":{{"@type":"Organization","name":"Georgetown Moonwalk Rentals","url":"{BASE}"}},
"url":"{page_url}",
"description":"{meta_desc}",
"keywords":"{keyword}, {city}, bounce house rental, moonwalk rental"
}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{faq_schema_items}
]}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
  {{"@type":"ListItem","position":1,"name":"Home","item":"{BASE}/"}},
  {{"@type":"ListItem","position":2,"name":"Blog","item":"{BASE}/blog"}},
  {{"@type":"ListItem","position":3,"name":"{title}","item":"{page_url}"}}
]}}
</script>
{BASE_CSS}
<style>
.post-hero{{margin-top:64px;background:var(--green);padding:56px 24px}}
.post-hero-inner{{max-width:780px;margin:0 auto}}
.post-cat{{display:inline-block;background:var(--gold);color:var(--green);font-family:'Fredoka One',cursive;font-size:.76rem;padding:3px 12px;border-radius:20px;margin-bottom:14px}}
.post-hero h1{{font-size:2rem;color:var(--white);line-height:1.25;margin-bottom:14px}}
.post-meta{{display:flex;gap:16px;flex-wrap:wrap;font-size:.82rem;color:rgba(255,255,255,.6)}}
.post-meta span{{display:flex;align-items:center;gap:5px}}
.post-body{{max-width:780px;margin:0 auto;padding:48px 24px}}
.post-body h2{{font-size:1.45rem;color:var(--green);margin:36px 0 14px;line-height:1.3}}
.post-body p{{font-size:.97rem;color:var(--text-mid);line-height:1.85;margin-bottom:18px}}
.post-body strong{{color:var(--green)}}
.post-divider{{border:none;border-top:1px solid rgba(27,58,45,.1);margin:36px 0}}
.related-section{{background:var(--light-bg);padding:48px 24px}}
.related-inner{{max-width:780px;margin:0 auto}}
.related-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-top:20px}}
.related-link{{background:var(--white);border-radius:var(--radius-card);padding:16px 20px;box-shadow:var(--shadow);text-decoration:none;font-family:'Fredoka One',cursive;font-size:.95rem;color:var(--green);border-left:3px solid var(--cta);transition:transform .2s;display:block}}
.related-link:hover{{transform:translateY(-3px)}}
.faq-section-wrap{{padding:48px 24px;background:var(--white)}}
.faq-section-wrap .container{{max-width:780px}}
.faq-section-label{{font-family:'Fredoka One',cursive;font-size:.76rem;letter-spacing:2px;text-transform:uppercase;color:var(--cta);display:block;text-align:center;margin-bottom:8px}}
.faq-section-heading{{font-family:'Nunito',sans-serif;font-weight:800;font-size:1.35rem;color:var(--green);text-align:center;margin-bottom:28px}}
.faq-card-grid{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
.faq-card{{background:var(--light-bg);border-left:4px solid var(--cta);border-radius:0 8px 8px 0;padding:20px 22px}}
.faq-card h3{{font-family:'Nunito',sans-serif;font-weight:800;font-size:.84rem;color:var(--green);text-transform:uppercase;letter-spacing:.4px;line-height:1.35;margin-bottom:8px}}
.faq-card p{{font-size:.86rem;color:var(--text-mid);line-height:1.7}}
.cta-band{{background:var(--green);padding:48px 24px;text-align:center}}
.cta-band h2{{font-size:1.7rem;color:var(--white);margin-bottom:10px}}
.cta-band p{{color:rgba(255,255,255,.8);font-size:.97rem;margin-bottom:24px}}
.cta-btns{{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}}
.ai-share-bar{{background:rgba(27,58,45,.04);border-top:1px solid rgba(27,58,45,.08);padding:16px 24px}}
.ai-share-inner{{max-width:780px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px}}
.ai-share-label{{font-size:.86rem;color:var(--text-mid);font-weight:700}}
.ai-share-btns{{display:flex;gap:10px;flex-wrap:wrap}}
.ai-btn{{display:inline-flex;align-items:center;gap:7px;font-family:'Fredoka One',cursive;font-size:.86rem;padding:8px 16px;border-radius:var(--radius-btn);border:1.5px solid;cursor:pointer;transition:all .2s;background:var(--white)}}
.chatgpt-btn{{color:#10a37f;border-color:#10a37f}}.chatgpt-btn:hover{{background:#10a37f;color:var(--white)}}
.claude-btn{{color:#c45e38;border-color:#c45e38}}.claude-btn:hover{{background:#c45e38;color:var(--white)}}
.gemini-btn{{color:#1a73e8;border-color:#1a73e8}}.gemini-btn:hover{{background:#1a73e8;color:var(--white)}}
.ai-btn.copied{{background:var(--green);color:var(--white);border-color:var(--green)}}
.mob-sticky-bar{{display:none;position:fixed;bottom:0;left:0;right:0;z-index:9999;height:56px;box-shadow:0 -2px 16px rgba(0,0,0,.18)}}
.mob-sticky-call{{flex:1;display:flex;align-items:center;justify-content:center;background:var(--gold);color:var(--green);font-family:'Fredoka One',cursive;font-size:1.05rem;text-decoration:none}}
.mob-sticky-book{{flex:1;display:flex;align-items:center;justify-content:center;background:var(--cta);color:#fff;font-family:'Fredoka One',cursive;font-size:1.05rem;text-decoration:none}}
@media(min-width:769px){{.mob-sticky-bar{{display:none!important}}}}
@media(max-width:768px){{.mob-sticky-bar{{display:flex}}body{{padding-bottom:56px}}.faq-card-grid{{grid-template-columns:1fr}}.post-hero h1{{font-size:1.65rem}}}}
</style>
</head>
<body>
{nav_html()}

<div class="post-hero">
  <div class="post-hero-inner">
    <div class="breadcrumb"><a href="/">Home</a> / <a href="/blog">Blog</a> / {category}</div>
    <span class="post-cat">{category}</span>
    <h1>{title}</h1>
    <div class="post-meta">
      <span>&#128197; {date}</span>
      <span>&#9200; {read_time}</span>
      <span>&#128205; {city}</span>
    </div>
  </div>
</div>

<div class="post-body">
  {sections_html}
  <hr class="post-divider">
  <p style="font-size:.84rem;color:var(--text-mid)">All rentals are provided by Jump Around Party Rentals, who is fully licensed and insured in Williamson County and Travis County, Texas.</p>
</div>

<section class="faq-section-wrap">
  <div class="container">
    <span class="faq-section-label">{city.upper()} BOUNCE HOUSE FAQS</span>
    <h2 class="faq-section-heading">Clear Answers for {city} Families</h2>
    <div class="faq-card-grid">
{faq_rows}
    </div>
  </div>
</section>

<div class="related-section">
  <div class="related-inner">
    <span class="section-label">Keep Exploring</span>
    <h2 class="section-title" style="font-size:1.4rem">Related <span>Pages</span></h2>
    <div class="related-grid">
{related_html}
    </div>
  </div>
</div>

<div class="cta-band">
  <h2>Ready to Book in {city}?</h2>
  <p>Delivery, setup, and pickup included. Starting at $155.</p>
  <div class="cta-btns">
    <a href="https://www.jump-aroundpartyrentals.com/category/" target="_blank" rel="noopener" class="btn-primary">Book Now</a>
    <a href="tel:7372347169" class="btn-outline">Call (737) 234-7169</a>
  </div>
</div>

<div class="ai-share-bar">
  <div class="ai-share-inner">
    <span class="ai-share-label">&#129302; Ask your AI assistant about this</span>
    <div class="ai-share-btns">
      <button class="ai-btn chatgpt-btn" onclick="copyPrompt(this,'chatgpt','{prompt}')">Ask ChatGPT</button>
      <button class="ai-btn claude-btn" onclick="copyPrompt(this,'claude','{prompt}')">Ask Claude</button>
      <button class="ai-btn gemini-btn" onclick="copyPrompt(this,'gemini','{prompt}')">Ask Gemini</button>
    </div>
  </div>
</div>

<div class="mob-sticky-bar" style="display:flex">
  <a href="tel:7372347169" class="mob-sticky-call">&#128222; Call Us</a>
  <a href="https://www.jump-aroundpartyrentals.com/category/" target="_blank" rel="noopener" class="mob-sticky-book">Book Now</a>
</div>

{FOOTER_HTML}
<script>
function copyPrompt(btn,service,prompt){{
  var encoded=encodeURIComponent(prompt);
  var url=service==='chatgpt'?'https://chat.openai.com/?q='+encoded:service==='claude'?'https://claude.ai/new?q='+encoded:'https://gemini.google.com/';
  navigator.clipboard.writeText(prompt).then(function(){{
    var orig=btn.innerHTML;btn.classList.add('copied');
    btn.innerHTML=service==='gemini'?'&#10003; Copied -- paste &amp; Enter':'&#10003; Pre-filled -- hit Enter';
    setTimeout(function(){{window.open(url,'_blank');setTimeout(function(){{btn.classList.remove('copied');btn.innerHTML=orig;}},2500);}},400);
  }}).catch(function(){{window.open(url,'_blank');}});
}}
</script>
{NAV_JS}
</body>
</html>"""

    # Save to /blog/ subfolder
    blog_dir = f'{DIR}/blog'
    os.makedirs(blog_dir, exist_ok=True)
    out_path = f'{blog_dir}/{slug}.html'
    with open(out_path, 'w') as f:
        f.write(html)
    return out_path

path = build_post(POST)
print(f"Blog post generated: {path}")
print(f"URL: {BASE}/blog/{POST['slug']}")
