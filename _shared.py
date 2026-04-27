# ============================================================
# SHARED CONSTANTS AND HELPERS FOR Georgetown Moonwalk Rentals
# ============================================================

SITE = {
    "domain": "georgetownmoonwalkrentals.com",
    "url": "https://www.georgetownmoonwalkrentals.com",
    "name": "Georgetown Moonwalk Rentals",
    "phone_display": "(737) 234-7169",
    "phone_raw": "7372347169",
    "phone_href": "tel:7372347169",
    "email": "info@georgetownmoonwalkrentals.com",
    "operator": "Jump Around Party Rentals",
    "insurance": "All rentals are provided by Jump Around Party Rentals, who is fully licensed and insured in Williamson County and Travis County, Texas.",
    "rating": "4.8",
    "reviews": "914",
    "year": "2025",
    "booking_url": "https://www.jump-aroundpartyrentals.com/category/",
    "address": "3616 Bass Loop, Round Rock TX 78665",
    "geo_lat": "30.6333",
    "geo_lng": "-97.6778",
    "zip_codes": "78626, 78628, 78633",
    "county": "Williamson County",
    "isd": "Georgetown ISD",
}

COLORS = {
    "primary": "#1b3a2d",       # deep forest green
    "cta": "#c45e38",           # warm copper / red poppy
    "cta_hover": "#a34d2e",
    "gold": "#c8912a",
    "gold_hover": "#a87520",
    "footer": "#0e1e16",
    "light_bg": "#f4f7f4",
    "white": "#ffffff",
    "text_dark": "#1b3a2d",
    "text_mid": "#445c4e",
}

NEIGHBORHOODS = [
    {
        "slug": "wolf-ranch",
        "name": "Wolf Ranch",
        "label": "Georgetown's Hill Country flagship community",
        "zip": "78628",
        "schools": "Wolf Ranch Elementary, Tippit Middle School, East View High School",
        "isd": "Georgetown ISD",
        "facts": "Wolf Ranch is Georgetown's premier master-planned community, built along the San Gabriel River with Hill Country views. Developed by Hillwood, the community features Wolf Ranch Elementary on-site, the Wolf Ranch Town Center retail district, and trail systems along the river.",
        "landmarks": "Wolf Ranch Town Center, San Gabriel River, Wolf Ranch Elementary School",
    },
    {
        "slug": "berry-creek",
        "name": "Berry Creek",
        "label": "Established gated golf community in northeast Georgetown",
        "zip": "78628",
        "schools": "Annie Purl Elementary, Charles Forbes Middle School, Georgetown High School",
        "isd": "Georgetown ISD",
        "facts": "Berry Creek is one of Georgetown's most established master-planned communities, anchored by the Berry Creek Country Club and an 18-hole golf course. It is a gated community in the northeast section of Georgetown with mature trees and established streets.",
        "landmarks": "Berry Creek Country Club, Georgetown High School, SH-195",
    },
    {
        "slug": "teravista",
        "name": "Teravista",
        "label": "Golf course community between Georgetown and Round Rock",
        "zip": "78626",
        "schools": "Carver Elementary, Douglas Benold Middle School, East View High School",
        "isd": "Georgetown ISD",
        "facts": "Teravista is a vibrant master-planned golf course community located in the Rolling Hills between Georgetown and Round Rock. With an 18-hole golf course, trails, parks, and a residents' clubhouse, it sits 24 miles from downtown Austin and 17 miles from The Domain.",
        "landmarks": "Teravista Golf Course, I-35, Teravista Recreation Center",
    },
    {
        "slug": "sun-city",
        "name": "Sun City",
        "label": "Del Webb's premier 55+ community in Georgetown TX",
        "zip": "78633",
        "schools": "Georgetown ISD (children of visiting guests)",
        "isd": "Georgetown ISD",
        "facts": "Sun City Georgetown is one of the largest Del Webb active-adult communities in Texas with over 7,500 homes. Located in north Georgetown, the community spans thousands of acres with multiple clubhouses, golf courses, pools, and activity centers.",
        "landmarks": "Sun City Community Center, Del Webb Blvd, Georgetown Municipal Airport",
    },
    {
        "slug": "rancho-sienna",
        "name": "Rancho Sienna",
        "label": "540-acre master-planned community on Ronald Reagan Blvd",
        "zip": "78628",
        "schools": "Rancho Sienna Elementary, Liberty Hill Middle School, Liberty Hill High School",
        "isd": "Liberty Hill ISD",
        "facts": "Rancho Sienna spans 540 acres at the corner of Ronald Reagan Boulevard and Highway 29. The community will house approximately 1,400 families at completion, with a resort pool, splash pad, the Sienna House clubhouse, fitness center, four miles of trails, and nine parks.",
        "landmarks": "Sienna House Clubhouse, Ronald Reagan Blvd, Hwy 29, Rancho Sienna Elementary",
    },
    {
        "slug": "cimarron-hills",
        "name": "Cimarron Hills",
        "label": "Private golf and country club community in Georgetown",
        "zip": "78628",
        "schools": "Rancho Sienna Elementary or Pickett Elementary, Georgetown ISD/Liberty Hill ISD",
        "isd": "Georgetown ISD",
        "facts": "Cimarron Hills is Georgetown's premier private golf and country club community, featuring a Jack Nicklaus Signature Course and resort-style amenities. Homes range from $410,000 to $2.6 million with monthly HOA dues that include full club membership.",
        "landmarks": "Cimarron Hills Country Club, Jack Nicklaus Signature Golf Course",
    },
    {
        "slug": "morningstar",
        "name": "Morningstar",
        "label": "Growing master-planned community in northwest Georgetown",
        "zip": "78628",
        "schools": "Rancho Sienna Elementary, Liberty Hill Middle, Liberty Hill High School",
        "isd": "Liberty Hill ISD",
        "facts": "Morningstar is a newer master-planned community in northwest Georgetown featuring Hill Country-inspired homes, resort-style amenities, and community parks. The neighborhood offers easy access to Ronald Reagan Boulevard and Highway 29.",
        "landmarks": "Ronald Reagan Blvd, Hwy 29, Wolf Ranch Town Center",
    },
    {
        "slug": "serenada",
        "name": "Serenada",
        "label": "Established wooded neighborhood in north Georgetown",
        "zip": "78628",
        "schools": "Mitchell Elementary, Forbes Middle School, Georgetown High School",
        "isd": "Georgetown ISD",
        "facts": "Serenada is one of Georgetown's most established neighborhoods, known for its mature oak trees, large lots, and quiet streets north of downtown. The neighborhood includes Serenada East, Serenada West, and Serenada Country Estates.",
        "landmarks": "SH-195, Georgetown Municipal Airport, Inner Loop Road",
    },
    {
        "slug": "georgetown-square",
        "name": "Georgetown Square",
        "label": "Georgetown's historic downtown and courthouse district",
        "zip": "78626",
        "schools": "Village Elementary, Benold Middle School, Georgetown High School",
        "isd": "Georgetown ISD",
        "facts": "Georgetown Square is the historic heart of Georgetown, centered on the Williamson County Courthouse built in 1911. The area features the famous Red Poppy Festival each April, boutique shopping, local restaurants, and Southwestern University just blocks away.",
        "landmarks": "Williamson County Courthouse, Georgetown Square, Southwestern University, Red Poppy Festival",
    },
    {
        "slug": "water-oak",
        "name": "Water Oak",
        "label": "New master-planned community near Lake Georgetown",
        "zip": "78628",
        "schools": "Mitchell Elementary, Forbes Middle School, Georgetown High School",
        "isd": "Georgetown ISD",
        "facts": "Water Oak is a newer master-planned community in Georgetown offering modern homes near Lake Georgetown and the San Gabriel River. The community provides easy access to outdoor recreation and is growing rapidly with new construction.",
        "landmarks": "Lake Georgetown, Cedar Breaks Park, San Gabriel River",
    },
    {
        "slug": "fountainwood",
        "name": "Fountainwood",
        "label": "Wooded estate community in northwest Georgetown",
        "zip": "78628",
        "schools": "Mitchell Elementary, Forbes Middle School, Georgetown High School",
        "isd": "Georgetown ISD",
        "facts": "Fountainwood is a heavily wooded community on the northwest outskirts of Georgetown featuring estate-sized lots, brick and stone facades, and mature trees. It is known for its serene atmosphere and large private yards.",
        "landmarks": "Ronald Reagan Blvd, Inner Loop Road, Northwest Georgetown",
    },
    {
        "slug": "lakeside",
        "name": "Lakeside at Lake Georgetown",
        "label": "One of the few neighborhoods directly on Lake Georgetown",
        "zip": "78633",
        "schools": "Mitchell Elementary, Forbes Middle School, Georgetown High School",
        "isd": "Georgetown ISD",
        "facts": "Lakeside at Lake Georgetown is one of Georgetown's most unique neighborhoods, situated directly on the shores of Lake Georgetown. Residents enjoy lake access, trails, scenic views, and community events throughout the year.",
        "landmarks": "Lake Georgetown, Cedar Breaks Park, Jim Hogg Road",
    },
]

CATEGORIES = [
    {
        "slug": "bounce-house-rentals",
        "name": "Bounce House Rentals",
        "short": "Bounce Houses",
        "icon": "🏰",
        "start_price": "$155",
        "desc": "Themed moonwalks and bounce houses starting at $155. Bluey, Frozen, Fortnite, Cocomelon, Avengers, and 20+ more themes.",
        "cta": "See Bounce Houses",
    },
    {
        "slug": "water-slide-rentals",
        "name": "Water Slide Rentals",
        "short": "Water Slides",
        "icon": "🌊",
        "start_price": "$245",
        "desc": "Single lane, double lane, slip n slides, and mega slides up to 32ft. Starting at $245.",
        "cta": "See Water Slides",
    },
    {
        "slug": "combo-bounce-house-rentals",
        "name": "Combo Bounce House Rentals",
        "short": "Combo Bounce Houses",
        "icon": "🎪",
        "start_price": "$195",
        "desc": "Inflatables with bounce area plus slide, basketball hoop, or climbing wall. Starting at $195.",
        "cta": "See Combos",
    },
    {
        "slug": "obstacle-course-rentals",
        "name": "Obstacle Course Rentals",
        "short": "Obstacle Courses",
        "icon": "🏁",
        "start_price": "$365",
        "desc": "Single-piece 34ft courses to 160ft 5-piece mega runs. Starting at $365.",
        "cta": "See Obstacle Courses",
    },
]

GISD_SCHOOLS = "Georgetown High School, East View High School, Douglas Benold Middle School, Charles Forbes Middle School, James Tippit Middle School, George Wagner Middle School, Wolf Ranch Elementary, Carver Elementary, Cooper Elementary, Ford Elementary, Frost Elementary, McCoy Elementary, Mitchell Elementary, Purl Elementary, Village Elementary, Williams Elementary"

CSS_VARS = """
  :root {
    --green: #1b3a2d;
    --cta: #c45e38;
    --cta-hover: #a34d2e;
    --gold: #c8912a;
    --gold-hover: #a87520;
    --footer-bg: #0e1e16;
    --white: #ffffff;
    --light-bg: #f4f7f4;
    --text-dark: #1b3a2d;
    --text-mid: #445c4e;
    --radius-card: 16px;
    --radius-btn: 50px;
    --radius-sm: 8px;
    --shadow: 0 8px 32px rgba(27,58,45,0.13);
  }
"""

NAV_LINKS_HTML = """    <li><a href="/index.html">Home</a></li>
    <li><a href="/bounce-house-rentals.html">Bounce Houses</a></li>
    <li><a href="/water-slide-rentals.html">Water Slides</a></li>
    <li><a href="/combo-bounce-house-rentals.html">Combos</a></li>
    <li><a href="/obstacle-course-rentals.html">Obstacle Courses</a></li>
    <li><a href="/service-area.html">Service Area</a></li>
    <li><a href="/faq.html">FAQ</a></li>
    <li><a href="tel:7372347169" class="nav-phone">(737) 234-7169</a></li>
    <li><a href="https://www.jump-aroundpartyrentals.com/category/" target="_blank" rel="noopener" class="nav-cta">Book Now</a></li>"""

MOB_LINKS_HTML = """    <li><a href="/index.html">Home</a></li>
    <li><a href="/bounce-house-rentals.html">Bounce Houses</a></li>
    <li><a href="/water-slide-rentals.html">Water Slides</a></li>
    <li><a href="/combo-bounce-house-rentals.html">Combos</a></li>
    <li><a href="/obstacle-course-rentals.html">Obstacle Courses</a></li>
    <li><a href="/service-area.html">Service Area</a></li>
    <li><a href="/faq.html">FAQ</a></li>
    <li><a href="/about.html">About</a></li>
    <li><a href="/contact.html">Contact</a></li>"""

def nav_html(active=""):
    return f"""<nav>
  <a href="/index.html" class="nav-logo" style="display:flex;align-items:center;text-decoration:none;"><img src="/images/logo.png" alt="Georgetown Moonwalk Rentals logo"></a>
  <ul class="nav-links">
{NAV_LINKS_HTML}
  </ul>
  <button class="hamburger" id="hamburger" aria-label="Open menu"><span></span><span></span><span></span></button>
</nav>
<div class="mobile-menu" id="mobileMenu">
  <ul>
{MOB_LINKS_HTML}
  </ul>
  <div class="mob-btns">
    <a href="tel:7372347169" class="mob-call">&#128222; (737) 234-7169</a>
    <a href="https://www.jump-aroundpartyrentals.com/category/" target="_blank" rel="noopener" class="mob-cta">Book Now</a>
  </div>
</div>"""

BASE_CSS = """<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
""" + CSS_VARS + """
body{font-family:'Nunito',sans-serif;font-size:16px;color:var(--text-dark);background:var(--white);line-height:1.7}
h1,h2,h3,h4,nav a{font-family:'Fredoka One',cursive}
nav{position:fixed;top:0;left:0;right:0;z-index:1000;background:var(--green);display:flex;align-items:center;justify-content:space-between;padding:0 24px;height:64px;box-shadow:0 2px 16px rgba(0,0,0,.25)}
.nav-logo img{height:44px;width:auto}
.nav-links{display:flex;gap:16px;list-style:none}
.nav-links a{color:rgba(255,255,255,.85);text-decoration:none;font-size:.88rem;font-family:'Fredoka One',cursive;transition:color .2s}
.nav-links a:hover{color:var(--gold)}
.nav-cta{background:var(--cta);color:var(--white)!important;padding:7px 16px;border-radius:var(--radius-btn)}
.nav-cta:hover{background:var(--cta-hover)!important}
.nav-phone{color:var(--gold)!important}
.hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;background:none;border:none;padding:4px}
.hamburger span{display:block;width:26px;height:2.5px;background:var(--white);border-radius:2px}
.mobile-menu{display:none;position:fixed;top:64px;left:0;right:0;background:var(--green);z-index:999;padding:16px 24px 24px;border-top:1px solid rgba(255,255,255,.1)}
.mobile-menu.open{display:block}
.mobile-menu ul{list-style:none;display:flex;flex-direction:column;gap:4px}
.mobile-menu a{display:block;padding:10px 0;color:rgba(255,255,255,.85);text-decoration:none;font-family:'Fredoka One',cursive;font-size:1.05rem;border-bottom:1px solid rgba(255,255,255,.08)}
.mobile-menu a:hover{color:var(--gold)}
.mob-btns{display:flex;flex-direction:column;gap:10px;margin-top:16px}
.mob-call{display:block;background:var(--gold);color:var(--green)!important;text-align:center;padding:12px;border-radius:var(--radius-btn);font-family:'Fredoka One',cursive;font-size:1.05rem;text-decoration:none}
.mob-cta{display:block;background:var(--cta);color:var(--white)!important;text-align:center;padding:12px;border-radius:var(--radius-btn);font-family:'Fredoka One',cursive;font-size:1.05rem;text-decoration:none}
.page-hero{margin-top:64px;background:var(--green);padding:60px 24px;text-align:center}
.page-hero h1{font-size:2.3rem;color:var(--white);margin-bottom:12px;line-height:1.15}
.page-hero h1 span{color:var(--gold)}
.page-hero p{color:rgba(255,255,255,.8);font-size:1rem;max-width:640px;margin:0 auto}
.breadcrumb{font-size:.82rem;color:rgba(255,255,255,.55);margin-bottom:14px}
.breadcrumb a{color:rgba(255,255,255,.65);text-decoration:none}
.breadcrumb a:hover{color:var(--gold)}
section{padding:60px 24px}
.container{max-width:1100px;margin:0 auto}
.section-label{font-family:'Fredoka One',cursive;font-size:.78rem;letter-spacing:1.5px;text-transform:uppercase;color:var(--cta);display:block;margin-bottom:8px}
.section-title{font-size:1.95rem;color:var(--green);line-height:1.2;margin-bottom:14px}
.section-title span{color:var(--cta)}
.section-sub{font-size:.97rem;color:var(--text-mid);max-width:680px;margin-bottom:32px;line-height:1.75}
.btn-primary{display:inline-block;background:var(--cta);color:var(--white);font-family:'Fredoka One',cursive;font-size:1rem;padding:12px 26px;border-radius:var(--radius-btn);text-decoration:none;transition:background .2s;border:none;cursor:pointer}
.btn-primary:hover{background:var(--cta-hover)}
.btn-gold{display:inline-block;background:var(--gold);color:var(--green);font-family:'Fredoka One',cursive;font-size:1rem;padding:12px 26px;border-radius:var(--radius-btn);text-decoration:none;transition:background .2s}
.btn-gold:hover{background:var(--gold-hover)}
.btn-outline{display:inline-block;background:transparent;color:var(--white);font-family:'Fredoka One',cursive;font-size:1rem;padding:11px 26px;border-radius:var(--radius-btn);text-decoration:none;border:2px solid rgba(255,255,255,.45);transition:all .2s}
.btn-outline:hover{border-color:var(--gold);color:var(--gold)}
.trust-bar{background:var(--green);padding:18px 24px;border-top:1px solid rgba(255,255,255,.08)}
.trust-bar .container{display:flex;justify-content:center;flex-wrap:wrap;gap:28px}
.trust-item{display:flex;align-items:center;gap:8px;color:rgba(255,255,255,.88);font-size:.88rem;font-weight:700}
.insurance-block{background:rgba(200,145,42,.08);border:1px solid rgba(200,145,42,.3);border-radius:var(--radius-card);padding:16px 20px;margin-top:24px;font-size:.88rem;color:var(--text-mid)}
.page-nav-block{background:var(--green);border-radius:var(--radius-card);padding:26px 30px;margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between}
.page-nav-block p{color:rgba(255,255,255,.85);font-size:.97rem;font-weight:700}
.page-nav-links{display:flex;flex-wrap:wrap;gap:8px}
.page-nav-links a{font-family:'Fredoka One',cursive;font-size:.86rem;color:var(--white);background:rgba(255,255,255,.1);padding:6px 14px;border-radius:var(--radius-btn);text-decoration:none;border:1px solid rgba(255,255,255,.15);transition:background .2s,color .2s}
.page-nav-links a:hover{background:var(--gold);color:var(--green);border-color:var(--gold)}
.faq-list{display:flex;flex-direction:column;gap:10px;margin-top:24px}
.faq-item{background:var(--white);border-radius:var(--radius-card);box-shadow:var(--shadow);overflow:hidden}
.faq-question{width:100%;text-align:left;background:none;border:none;padding:18px 22px;font-family:'Fredoka One',cursive;font-size:.98rem;color:var(--green);cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:12px}
.faq-question:hover{color:var(--cta)}
.faq-chevron{font-size:.95rem;transition:transform .3s;flex-shrink:0;color:var(--gold)}
.faq-item.open .faq-chevron{transform:rotate(180deg)}
.faq-answer{max-height:0;overflow:hidden;transition:max-height .35s ease}
.faq-item.open .faq-answer{max-height:400px}
.faq-answer-inner{padding:0 22px 18px;font-size:.92rem;color:var(--text-mid);line-height:1.7;border-top:1px solid rgba(27,58,45,.07);padding-top:14px}
footer{background:var(--footer-bg);color:rgba(255,255,255,.7);padding:48px 24px 24px}
.footer-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:32px;max-width:1100px;margin:0 auto 40px}
.footer-col h4{font-family:'Fredoka One',cursive;color:var(--white);font-size:1.02rem;margin-bottom:14px}
.footer-col p,.footer-col a{font-size:.86rem;color:rgba(255,255,255,.6);text-decoration:none;line-height:2.1;display:block}
.footer-col a:hover{color:var(--gold)}
.footer-bottom{text-align:center;font-size:.78rem;color:rgba(255,255,255,.3);border-top:1px solid rgba(255,255,255,.07);padding-top:20px;max-width:1100px;margin:0 auto}
@media(max-width:900px){.nav-links{display:none}.hamburger{display:flex}}
@media(max-width:768px){.section-title{font-size:1.65rem}section{padding:44px 20px}.page-nav-block{flex-direction:column;align-items:flex-start}}
@media(max-width:480px){.page-hero h1{font-size:1.8rem}}
</style>"""

HEAD_FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">"""

FAVICONS = """<link rel="icon" type="image/x-icon" href="/images/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="96x96" href="/images/favicon-96x96.png">
<link rel="apple-touch-icon" sizes="180x180" href="/images/favicon-180x180.png">
<link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192x192.png">
<link rel="icon" type="image/png" sizes="512x512" href="/images/favicon-512x512.png">"""

FOOTER_HTML = f"""<footer>
  <div class="footer-grid">
    <div class="footer-col">
      <h4>Georgetown Moonwalk Rentals</h4>
      <p>Bounce house, moonwalk, water slide, combo, and obstacle course rentals serving Georgetown TX and Williamson County.</p>
      <p style="margin-top:10px;color:var(--gold);">(737) 234-7169</p>
    </div>
    <div class="footer-col">
      <h4>Our Rentals</h4>
      <a href="/bounce-house-rentals.html">Bounce Houses</a>
      <a href="/water-slide-rentals.html">Water Slides</a>
      <a href="/combo-bounce-house-rentals.html">Combo Bounce Houses</a>
      <a href="/obstacle-course-rentals.html">Obstacle Courses</a>
      <a href="/contact.html">Get a Quote</a>
    </div>
    <div class="footer-col">
      <h4>Neighborhoods</h4>
      <a href="/neighborhood-wolf-ranch.html">Wolf Ranch</a>
      <a href="/neighborhood-berry-creek.html">Berry Creek</a>
      <a href="/neighborhood-teravista.html">Teravista</a>
      <a href="/neighborhood-rancho-sienna.html">Rancho Sienna</a>
      <a href="/neighborhood-cimarron-hills.html">Cimarron Hills</a>
      <a href="/service-area.html">All Neighborhoods</a>
    </div>
    <div class="footer-col">
      <h4>Company</h4>
      <a href="/about.html">About Us</a>
      <a href="/service-area.html">Service Area</a>
      <a href="/faq.html">FAQ</a>
      <a href="/contact.html">Contact</a>
    </div>
  </div>
  <div class="footer-bottom">
    <p>All rentals are provided by Jump Around Party Rentals, who is fully licensed and insured in Williamson County and Travis County, Texas.</p>
    <p style="margin-top:8px;">&copy; {SITE['year']} Georgetown Moonwalk Rentals. All rights reserved.</p>
  </div>
</footer>"""

NAV_JS = """<script>
  document.getElementById('hamburger').addEventListener('click',()=>{document.getElementById('mobileMenu').classList.toggle('open')});
  document.querySelectorAll('.faq-question').forEach(btn=>{btn.addEventListener('click',()=>{const item=btn.parentElement;const isOpen=item.classList.contains('open');document.querySelectorAll('.faq-item').forEach(i=>i.classList.remove('open'));if(!isOpen)item.classList.add('open')})});
</script>"""

print("Shared module loaded -- all constants ready")
