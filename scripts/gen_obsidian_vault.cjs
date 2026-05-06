// Genera storyboards.md (indice) + cap-1..12.md en el vault Obsidian Pax,
// usando URLs absolutas a Vercel para las imagenes (no duplica PNGs).
// Idempotente: sobrescribe en cada corrida.
const fs = require("node:fs");
const path = require("node:path");

const VERCEL = "https://pax-os.vercel.app";
const REPO = path.resolve(__dirname, "..");
const VAULT = "C:/Users/aldot/.gemini/antigravity/scratch/pax";

const OUTLINE = fs.readFileSync(
  path.join(REPO, "content", "episodios-12-outline.md"),
  "utf8",
);

// 1) Parse outline en bloques por episodio
const lines = OUTLINE.split(/\r?\n/);
const blocks = {};
let cur = null;
let body = [];
for (const line of lines) {
  const m = /^##\s+Episodio\s+(\d+)\s*[—\-]\s*(.+)$/.exec(line);
  if (m) {
    if (cur) blocks[cur.n] = { titulo: cur.titulo, body: body.join("\n") };
    cur = { n: parseInt(m[1], 10), titulo: m[2].trim() };
    body = [];
  } else if (cur) {
    body.push(line);
  }
}
if (cur) blocks[cur.n] = { titulo: cur.titulo, body: body.join("\n") };

function field(text, label) {
  const re = new RegExp(
    "\\*\\*" + label + "[^:]*:\\*\\*\\s*([\\s\\S]*?)(?=\\n\\*\\*|$)",
  );
  const m = text.match(re);
  return m ? m[1].trim() : "";
}

// 2) Indice principal
const indexLines = [
  "---",
  'title: "Storyboards — Pax temporada 1"',
  'description: "Indice de los 12 capitulos con sus shots y pagina comic"',
  "---",
  "",
  "# Storyboards — Pax (12 episodios)",
  "",
  "Cada capitulo tiene 7-15 shots + 1 pagina comic compilada.",
  "Las imagenes se sirven desde Vercel (`pax-os.vercel.app`); este vault solo guarda el grafo de notas.",
  "",
  "## Capitulos",
  "",
];

for (let n = 1; n <= 12; n++) {
  const b = blocks[n];
  if (!b) continue;
  indexLines.push(
    "- [[cap-" + n + "]] — Episodio " + n + " — " + b.titulo,
  );
}
indexLines.push(
  "",
  "---",
  "",
  "Volver a [[episodios-12-outline]] para el outline narrativo completo.",
);

fs.writeFileSync(
  path.join(VAULT, "storyboards.md"),
  indexLines.join("\n"),
  "utf8",
);

// 3) Pagina por cap
for (let n = 1; n <= 12; n++) {
  const b = blocks[n];
  if (!b) continue;

  const logline = field(b.body, "Logline");
  const hook = field(b.body, "Hook");
  const tono = field(b.body, "Tono dominante");
  const locacion = field(b.body, "Locación principal");
  const cliff = field(b.body, "Cliffhanger");

  const dir = path.join(REPO, "content", "storyboards", "cap-" + n);
  let shots = [];
  try {
    shots = fs
      .readdirSync(dir)
      .filter((f) => f.endsWith(".md"))
      .sort();
  } catch {
    // sin md companion — solo PNG. dejamos shots vacio.
  }

  const out = [];
  out.push("---");
  out.push('title: "Cap ' + n + " — " + b.titulo + '"');
  out.push("cap: " + n);
  out.push("---");
  out.push("");
  out.push("# Episodio " + n + " — " + b.titulo);
  out.push("");
  if (logline) {
    out.push("**Logline.** " + logline);
    out.push("");
  }
  if (tono) {
    out.push("**Tono.** " + tono);
    out.push("");
  }
  if (locacion) {
    out.push("**Locacion.** " + locacion);
    out.push("");
  }
  if (hook) {
    out.push("## Hook (0:00–0:08)");
    out.push("");
    out.push(hook);
    out.push("");
  }

  const comicUrl =
    VERCEL +
    "/images/storyboards/cap-" +
    n +
    "/cap-" +
    n +
    "-comic-page.png";
  out.push("## Pagina comic (compilado del cap)");
  out.push("");
  out.push("![Pagina comic cap " + n + "](" + comicUrl + ")");
  out.push("");

  if (shots.length > 0) {
    out.push("## Shots");
    out.push("");
    for (const f of shots) {
      const slug = f.replace(/\.md$/, "");
      if (/-comic-page$/.test(slug)) continue;
      const m = /^cap-\d+-shot-(\d+)-(.+)$/.exec(slug);
      if (!m) continue;
      const num = m[1];
      const titleSlug = m[2].replace(/-/g, " ");
      const imgUrl =
        VERCEL +
        "/images/storyboards/cap-" +
        n +
        "/" +
        slug +
        ".png";
      out.push("### Shot " + num + " — " + titleSlug);
      out.push("");
      out.push("![Shot " + num + "](" + imgUrl + ")");
      out.push("");
    }
  }

  if (cliff) {
    out.push("## Cliffhanger");
    out.push("");
    out.push(cliff);
    out.push("");
  }
  out.push("---");
  out.push("");
  out.push(
    "Volver al [[storyboards|indice de storyboards]] · [[episodios-12-outline|outline temporada]]",
  );

  fs.writeFileSync(
    path.join(VAULT, "cap-" + n + ".md"),
    out.join("\n"),
    "utf8",
  );
}

console.log("OK — escritos storyboards.md + cap-1..12.md en " + VAULT);
