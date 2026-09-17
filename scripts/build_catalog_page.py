#!/usr/bin/env python3
"""Generate catalog.html — a self-contained visual browse page for the catalog.

Reads data/catalog.json and writes catalog.html at the repo root. The catalog
data is inlined into the page, so the file works opened locally or served from
any static host (GitHub Pages included) with no fetch, no CORS, no build step.

Run after any change to data/catalog.json:

    python3 scripts/build_catalog_page.py
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "catalog.json"
OUT_PATH = ROOT / "catalog.html"

# Display name + order for each outcome category. Skills first, collections last.
CATEGORY_ORDER = [
    ("customer-market-intelligence", "Customer & market intelligence"),
    ("positioning-competitive", "Positioning & competitive strategy"),
    ("product-portfolio", "Product & portfolio strategy"),
    ("go-to-market-growth", "Go-to-market & growth"),
    ("pricing-monetization", "Pricing & monetization"),
    ("executive-decisions", "Executive decisions & operating systems"),
    ("measurement-experimentation", "Measurement & experimentation"),
    ("execution-systems", "Execution systems"),
    ("collections-discovery", "Collections & discovery"),
]

STATUS_LABEL = {
    "petrichor-original": "Petrichor Original",
    "reviewed": "Reviewed",
    "collection": "Collection",
}

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Awesome Strategy Skills — browse the catalog</title>
<meta name="description" content="Browse the curated Awesome Strategy Skills catalog by outcome, status, publisher, and license.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#0B0E14; --panel:#141A21; --panel-2:#1B222C; --border:#252E3A; --border-2:#3A4553;
  --ink:#D8DEE6; --ink-soft:#B9C3CE; --muted:#9FB0C3; --faint:#71818F;
  --clay:#D97757; --clay-deep:#C2663F;
  --teal:#3BA89B; --teal-bg:#12211F;
  --sans:"IBM Plex Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --display:"Archivo",var(--sans); --mono:"IBM Plex Mono",ui-monospace,monospace;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);line-height:1.5;
  -webkit-font-smoothing:antialiased;padding:0 clamp(16px,4vw,56px)}
a{color:var(--clay);text-decoration:none}
a:hover{text-decoration:underline}
.wrap{max-width:1180px;margin:0 auto}

header.top{padding:clamp(40px,7vw,88px) 0 28px;border-bottom:1px solid var(--border)}
.eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--clay);margin:0 0 14px}
h1{font-family:var(--display);font-weight:800;font-size:clamp(34px,6vw,60px);line-height:1.02;
  letter-spacing:-.02em;margin:0 0 16px}
.lede{font-size:clamp(16px,2.2vw,19px);color:var(--ink-soft);max-width:60ch;margin:0 0 26px}
.stats{display:flex;flex-wrap:wrap;gap:26px;margin-top:8px}
.stat .n{font-family:var(--display);font-weight:700;font-size:26px;color:var(--ink)}
.stat .l{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--faint)}

.controls{position:sticky;top:0;z-index:20;background:rgba(11,14,20,.9);
  backdrop-filter:blur(10px);border-bottom:1px solid var(--border);
  padding:11px 0 12px;margin-bottom:26px}
.controls .row{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
#q{flex:1 1 240px;min-width:200px;background:var(--panel);border:1px solid var(--border-2);
  color:var(--ink);font-family:var(--sans);font-size:14px;padding:8px 13px;border-radius:9px}
#q::placeholder{color:var(--faint)}
#q:focus{outline:none;border-color:var(--clay)}
.chips{display:flex;flex-wrap:wrap;gap:7px}
.chip{font-family:var(--mono);font-size:11.5px;letter-spacing:.02em;background:var(--panel);
  border:1px solid var(--border-2);color:var(--muted);padding:5px 10px;border-radius:999px;cursor:pointer;
  transition:all .12s}
.chip:hover{border-color:var(--faint);color:var(--ink-soft)}
.chip[aria-pressed="true"]{background:var(--clay);border-color:var(--clay);color:#160b06;font-weight:600}
.count-note{font-family:var(--mono);font-size:12px;color:var(--faint);margin-left:auto}

section.cat{margin:0 0 40px;scroll-margin-top:96px}
.cat-head{display:flex;align-items:baseline;gap:12px;margin:0 0 16px;
  padding-bottom:10px;border-bottom:1px solid var(--border)}
.cat-head h2{font-family:var(--display);font-weight:700;font-size:22px;letter-spacing:-.01em;margin:0}
.cat-head .c{font-family:var(--mono);font-size:12px;color:var(--faint)}

.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:14px}
.card{background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:18px 18px 16px;
  display:flex;flex-direction:column;gap:9px;transition:border-color .12s,transform .12s}
.card:hover{border-color:var(--border-2);transform:translateY(-2px)}
.card .name{font-family:var(--display);font-weight:600;font-size:17px;line-height:1.2}
.card .desc{font-size:14px;color:var(--ink-soft);margin:0}
.card .why{font-size:12.5px;color:var(--muted);border-left:2px solid var(--border-2);
  padding-left:10px;margin:2px 0 0}
.meta{display:flex;flex-wrap:wrap;gap:7px;align-items:center;margin-top:auto;padding-top:6px}
.badge{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;
  padding:3px 8px;border-radius:6px;border:1px solid var(--border-2);color:var(--muted)}
.badge.s-petrichor-original{background:#241206;border-color:var(--clay-deep);color:var(--clay)}
.badge.s-reviewed{background:var(--teal-bg);border-color:#1f4a44;color:var(--teal)}
.badge.s-collection{background:var(--panel-2);border-color:var(--border-2);color:var(--muted)}
.pub{font-family:var(--mono);font-size:11.5px;color:var(--faint)}
.pub .lic{color:var(--muted)}
.card .rev{font-family:var(--mono);font-size:10.5px;color:var(--faint)}
.empty{display:none;color:var(--faint);font-family:var(--mono);font-size:14px;padding:30px 0}

footer{border-top:1px solid var(--border);margin-top:26px;padding:28px 0 60px;
  color:var(--faint);font-size:13px}
footer a{color:var(--muted)}
.legend{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:14px;font-family:var(--mono);font-size:11px;color:var(--faint)}
.legend span::before{content:"";display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:6px;vertical-align:middle}
.legend .lp::before{background:var(--clay)} .legend .lr::before{background:var(--teal)} .legend .lc::before{background:var(--border-2)}
</style>
</head>
<body>
<div class="wrap">
<header class="top">
  <p class="eyebrow">Awesome Strategy Skills</p>
  <h1>Browse the catalog</h1>
  <p class="lede">Curated AI-agent skills for decisions that survive contact with reality. Reviewed for evidence discipline, decision utility, and maintenance — not scraped, not a prompt dump.</p>
  <div class="stats">
    <div class="stat"><div class="n">__N_SKILLS__</div><div class="l">Skills</div></div>
    <div class="stat"><div class="n">__N_COLL__</div><div class="l">Collections</div></div>
    <div class="stat"><div class="n">__N_CAT__</div><div class="l">Categories</div></div>
    <div class="stat"><div class="n">__N_PUB__</div><div class="l">Publishers</div></div>
  </div>
</header>

<div class="controls">
  <div class="row" style="margin-bottom:10px">
    <input id="q" type="search" placeholder="Search name, description, publisher…" autocomplete="off">
    <span class="count-note" id="countNote"></span>
  </div>
  <div class="chips" id="catChips"></div>
  <div class="chips" id="statusChips" style="margin-top:8px"></div>
</div>

<div class="legend">
  <span class="lp">Petrichor Original</span>
  <span class="lr">Reviewed</span>
  <span class="lc">Collection</span>
</div>

<main id="cats"></main>
<p class="empty" id="empty">No skills match those filters.</p>

<footer>
  <p>Generated from <a href="data/catalog.json">data/catalog.json</a> · __TODAY__ · <a href="https://github.com/Petrichor-Projects/awesome-strategy-skills">Repository</a> · <a href="README.md">README</a></p>
  <p>Status: <strong>Petrichor Original</strong> — maintainer-created, ownership disclosed. <strong>Reviewed</strong> — source, scope, and license manually inspected. <strong>Collection</strong> — a discovery source; individual items not automatically endorsed. A link is not a security audit.</p>
</footer>
</div>

<script>
const CATALOG = __DATA__;
const CATS = __CATS__;
const STATUS = __STATUS__;
const state = {q:"", cat:"all", status:"all"};

const norm = s => (s||"").toLowerCase();
function matches(e){
  if(state.cat!=="all" && e.category!==state.cat) return false;
  if(state.status!=="all" && e.status!==state.status) return false;
  if(state.q){
    const hay = norm(e.name+" "+e.description+" "+e.why_included+" "+e.publisher+" "+e.license);
    if(!hay.includes(state.q)) return false;
  }
  return true;
}
function esc(s){return (s||"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));}

function card(e){
  const rev = e.last_reviewed ? `<div class="rev">reviewed ${esc(e.last_reviewed)}</div>` : "";
  const why = e.why_included ? `<p class="why">${esc(e.why_included)}</p>` : "";
  return `<article class="card">
    <div class="name"><a href="${esc(e.url)}" target="_blank" rel="noopener">${esc(e.name)}</a></div>
    <p class="desc">${esc(e.description)}</p>
    ${why}
    <div class="meta">
      <span class="badge s-${esc(e.status)}">${esc(STATUS[e.status]||e.status)}</span>
      <span class="pub">${esc(e.publisher)} · <span class="lic">${esc(e.license)}</span></span>
    </div>
    ${rev}
  </article>`;
}

function render(){
  const host = document.getElementById("cats");
  let html="", shown=0;
  for(const [key,label] of CATS){
    const items = CATALOG.filter(e=>e.category===key && matches(e))
      .sort((a,b)=>a.name.localeCompare(b.name));
    if(!items.length) continue;
    shown += items.length;
    html += `<section class="cat" id="cat-${key}">
      <div class="cat-head"><h2>${esc(label)}</h2><span class="c">${items.length}</span></div>
      <div class="grid">${items.map(card).join("")}</div>
    </section>`;
  }
  host.innerHTML = html;
  document.getElementById("empty").style.display = shown? "none":"block";
  const total = CATALOG.length;
  document.getElementById("countNote").textContent = shown===total ? `${total} entries` : `${shown} of ${total}`;
}

function buildChips(){
  const cc = document.getElementById("catChips");
  const mk = (val,label,pressed)=>`<button class="chip" role="button" aria-pressed="${pressed}" data-k="cat" data-v="${val}">${label}</button>`;
  cc.innerHTML = mk("all","All outcomes",true) + CATS.map(([k,l])=>{
    const n = CATALOG.filter(e=>e.category===k).length;
    return n? mk(k,`${l} <span style="opacity:.6">${n}</span>`,false):"";
  }).join("");
  const sc = document.getElementById("statusChips");
  sc.innerHTML = `<span class="pub" style="align-self:center;margin-right:4px">status:</span>` +
    mk2("all","All") + Object.keys(STATUS).map(s=>{
      const n = CATALOG.filter(e=>e.status===s).length;
      return n? mk2(s,`${STATUS[s]} <span style="opacity:.6">${n}</span>`):"";
    }).join("");
  function mk2(val,label){return `<button class="chip" role="button" aria-pressed="${val==='all'}" data-k="status" data-v="${val}">${label}</button>`;}
}

document.addEventListener("click",e=>{
  const c = e.target.closest(".chip"); if(!c) return;
  const k=c.dataset.k, v=c.dataset.v;
  state[k]=v;
  document.querySelectorAll(`.chip[data-k="${k}"]`).forEach(b=>b.setAttribute("aria-pressed", b.dataset.v===v));
  render();
});
document.getElementById("q").addEventListener("input",e=>{state.q=norm(e.target.value);render();});

buildChips();
render();
</script>
</body>
</html>
"""


def main() -> int:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    entries = catalog["entries"]

    n_skills = sum(1 for e in entries if e["kind"] == "skill")
    n_coll = sum(1 for e in entries if e["kind"] == "collection")
    n_pub = len({e["publisher"] for e in entries})
    n_cat = len({e["category"] for e in entries})

    html = TEMPLATE
    html = html.replace("__DATA__", json.dumps(entries, ensure_ascii=False))
    html = html.replace("__CATS__", json.dumps(CATEGORY_ORDER, ensure_ascii=False))
    html = html.replace("__STATUS__", json.dumps(STATUS_LABEL, ensure_ascii=False))
    html = html.replace("__N_SKILLS__", str(n_skills))
    html = html.replace("__N_COLL__", str(n_coll))
    html = html.replace("__N_CAT__", str(n_cat))
    html = html.replace("__N_PUB__", str(n_pub))
    html = html.replace("__TODAY__", date.today().isoformat())

    OUT_PATH.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT_PATH.relative_to(ROOT)} — {len(entries)} entries "
          f"({n_skills} skills, {n_coll} collections, {n_cat} categories, {n_pub} publishers)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
