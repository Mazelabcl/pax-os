#!/usr/bin/env node
/**
 * Generate concept art images via OpenRouter (Nano Banana / Gemini 2.5 Flash Image).
 *
 * Usage:
 *   node scripts/generate-concept-arts.mjs --block A
 *   node scripts/generate-concept-arts.mjs --block A --force
 *   node scripts/generate-concept-arts.mjs --block A --only concept-cave-wide-dark
 *
 * Reads prompts from content/episodio-1/concept-arts.md and reference images
 * from public/. Writes generated PNGs to public/images/concepts/{id}.png.
 */

import { readFile, writeFile, mkdir, stat } from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");

const MODEL_ID = "google/gemini-2.5-flash-image";
const ENDPOINT = "https://openrouter.ai/api/v1/chat/completions";
const COST_PER_IMAGE = 0.039;
const OUT_DIR = path.join(ROOT, "public", "images", "concepts");
const CONCEPT_ARTS_MD = path.join(ROOT, "content", "episodio-1", "concept-arts.md");
const STYLE_GUIDE_MD = path.join(ROOT, "content", "style-guide.md");

// ---------------------------------------------------------------------------
// CLI args
// ---------------------------------------------------------------------------
function parseArgs(argv) {
  const args = { block: null, force: false, only: null, dryRun: false };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--block") args.block = argv[++i];
    else if (a === "--force") args.force = true;
    else if (a === "--only") args.only = argv[++i];
    else if (a === "--dry-run") args.dryRun = true;
  }
  return args;
}

// ---------------------------------------------------------------------------
// .env.local loader (no dotenv)
// ---------------------------------------------------------------------------
async function loadEnv(envPath) {
  try {
    const raw = await readFile(envPath, "utf8");
    const env = {};
    for (const line of raw.split(/\r?\n/)) {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith("#")) continue;
      const eq = trimmed.indexOf("=");
      if (eq < 0) continue;
      const key = trimmed.slice(0, eq).trim();
      let val = trimmed.slice(eq + 1).trim();
      if (
        (val.startsWith('"') && val.endsWith('"')) ||
        (val.startsWith("'") && val.endsWith("'"))
      ) {
        val = val.slice(1, -1);
      }
      env[key] = val;
    }
    return env;
  } catch (err) {
    if (err.code === "ENOENT") return {};
    throw err;
  }
}

// ---------------------------------------------------------------------------
// Markdown parsing
// ---------------------------------------------------------------------------
function extractStyleLock(styleGuide) {
  // First code block under "## Bloque de estilo reutilizable" or any first code block.
  const m = styleGuide.match(/```[a-zA-Z0-9_-]*\n([\s\S]*?)```/);
  return m ? m[1].trim() : "";
}

/**
 * Parse concept-arts.md and return [{ id, bloque, prompt, slots: [{ slot, refPath }] }, ...]
 *
 * Walks line by line, tracking current bloque (H1) and current concept (H2).
 */
function parseConceptArts(md) {
  const lines = md.split(/\r?\n/);
  let currentBloque = null;
  const items = [];
  let current = null;

  for (const line of lines) {
    const h1 = /^#\s+Bloque\s+([A-C])\s*[—\-]/i.exec(line);
    if (h1) {
      if (current) items.push(current);
      current = null;
      currentBloque = h1[1].toUpperCase();
      continue;
    }
    const idMatch =
      /^##\s+`((?:concept|first-frame|last-frame)[a-z0-9-]+)`/i.exec(line);
    if (idMatch && currentBloque) {
      if (current) items.push(current);
      current = { id: idMatch[1], bloque: currentBloque, body: [] };
      continue;
    }
    if (/^##\s/.test(line) && !idMatch) {
      if (current) items.push(current);
      current = null;
      continue;
    }
    if (/^#\s/.test(line) && !h1) {
      if (current) items.push(current);
      current = null;
      currentBloque = null;
      continue;
    }
    if (current) current.body.push(line);
  }
  if (current) items.push(current);

  return items.map((item) => {
    const body = item.body.join("\n");
    return {
      id: item.id,
      bloque: item.bloque,
      slots: parseSlotsTable(body),
      prompt: extractPromptBlock(body),
    };
  });
}

function parseSlotsTable(body) {
  const lines = body.split(/\r?\n/);
  let headerIdx = -1;
  for (let i = 0; i < lines.length; i++) {
    const l = lines[i].trim().toLowerCase();
    if (/^\|\s*slot\s*\|\s*imagen\s*\|\s*(path\s*\/\s*estado|path)\s*\|$/.test(l)) {
      headerIdx = i;
      break;
    }
  }
  if (headerIdx < 0) return [];
  const sepIdx = headerIdx + 1;
  if (sepIdx >= lines.length || !/^\|[-\s|:]+\|$/.test(lines[sepIdx].trim())) {
    return [];
  }
  const slots = [];
  for (let i = sepIdx + 1; i < lines.length; i++) {
    const line = lines[i].trim();
    if (!line.startsWith("|") || !line.endsWith("|")) break;
    const cells = line
      .slice(1, -1)
      .split("|")
      .map((c) => c.trim());
    if (cells.length < 3) continue;
    const slotCell = cells[0];
    const estadoCell = cells.slice(2).join(" | ").trim();

    const slotMatch = slotCell.match(/`?(@image\d+)`?/i);
    if (!slotMatch) continue;
    const slot = slotMatch[1].toLowerCase();

    const pngMatch = estadoCell.match(/`?(public\/[^\s`]+\.(?:png|jpg|jpeg|webp))`?/i);
    const hasCheck = /[✓✔]/.test(estadoCell);
    let refPath = null;
    if (pngMatch && hasCheck) {
      refPath = pngMatch[1]; // keep full "public/..." path for filesystem read
    }
    slots.push({ slot, refPath });
  }
  return slots;
}

function extractPromptBlock(body) {
  // Find "**Prompt Nano Banana**" then the first triple-backtick block after it.
  const idx = body.search(/\*\*Prompt Nano Banana\*\*/i);
  if (idx < 0) return null;
  const after = body.slice(idx);
  const m = after.match(/```[a-zA-Z0-9_-]*\n([\s\S]*?)```/);
  return m ? m[1].trim() : null;
}

// ---------------------------------------------------------------------------
// Image helpers
// ---------------------------------------------------------------------------
async function readImageAsDataUri(absPath) {
  const buf = await readFile(absPath);
  const ext = path.extname(absPath).toLowerCase();
  const mime =
    ext === ".png"
      ? "image/png"
      : ext === ".jpg" || ext === ".jpeg"
      ? "image/jpeg"
      : ext === ".webp"
      ? "image/webp"
      : "application/octet-stream";
  return `data:${mime};base64,${buf.toString("base64")}`;
}

function decodeDataUri(uri) {
  const m = /^data:([^;]+);base64,(.+)$/.exec(uri);
  if (!m) return null;
  return { mime: m[1], buffer: Buffer.from(m[2], "base64") };
}

// ---------------------------------------------------------------------------
// OpenRouter call
// ---------------------------------------------------------------------------
async function generateImage({ apiKey, prompt, styleLock, refImageDataUris }) {
  // Build the text content: style-lock + prompt body (replace placeholder).
  const promptText = prompt.replace(/\[Style-lock pegado arriba\]\s*\n?/i, "");
  const fullText =
    (styleLock ? `${styleLock}\n\n` : "") + promptText;

  const userContent = [
    { type: "text", text: fullText },
    ...refImageDataUris.map((url) => ({
      type: "image_url",
      image_url: { url },
    })),
  ];

  const body = {
    model: MODEL_ID,
    messages: [{ role: "user", content: userContent }],
    modalities: ["image", "text"],
  };

  const t0 = Date.now();
  const res = await fetch(ENDPOINT, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${apiKey}`,
      "HTTP-Referer": "https://pax-os.vercel.app",
      "X-Title": "pax-os",
    },
    body: JSON.stringify(body),
  });
  const elapsed = Date.now() - t0;

  const text = await res.text();
  let json = null;
  try {
    json = JSON.parse(text);
  } catch {
    // not JSON
  }

  if (!res.ok) {
    return {
      ok: false,
      status: res.status,
      elapsed,
      error: json?.error?.message || text.slice(0, 500),
      raw: json,
    };
  }

  // Extract image from choices[0].message.images[0].image_url.url
  const choice = json?.choices?.[0];
  const message = choice?.message;
  let imageUri = null;

  if (message?.images && Array.isArray(message.images) && message.images.length > 0) {
    const first = message.images[0];
    imageUri =
      first?.image_url?.url ||
      first?.url ||
      (typeof first === "string" ? first : null);
  }
  // Fallback: maybe content array with image_url
  if (!imageUri && Array.isArray(message?.content)) {
    for (const item of message.content) {
      if (item?.type === "image_url" && item?.image_url?.url) {
        imageUri = item.image_url.url;
        break;
      }
      if (item?.type === "image" && item?.url) {
        imageUri = item.url;
        break;
      }
    }
  }

  if (!imageUri) {
    // Capture finish reason / refusal / text content for debugging.
    const finish = choice?.finish_reason ?? choice?.native_finish_reason ?? null;
    const refusal = message?.refusal ?? null;
    const textContent = typeof message?.content === "string"
      ? message.content
      : Array.isArray(message?.content)
        ? message.content.filter((c) => c?.type === "text").map((c) => c.text).join(" ")
        : null;
    const debug = [finish && `finish=${finish}`, refusal && `refusal=${refusal}`, textContent && `text="${textContent.slice(0, 200)}"`]
      .filter(Boolean)
      .join("; ");
    return {
      ok: false,
      status: res.status,
      elapsed,
      error: `No image in response${debug ? " (" + debug + ")" : ""}`,
      raw: json,
    };
  }

  return { ok: true, status: res.status, elapsed, imageUri, raw: json };
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------
async function main() {
  const args = parseArgs(process.argv);
  if (!args.block) {
    console.error("ERROR: --block A is required");
    process.exit(1);
  }
  const blockLetter = args.block.toUpperCase();
  if (!["A", "B", "C"].includes(blockLetter)) {
    console.error(`ERROR: --block must be A, B, or C (got ${blockLetter})`);
    process.exit(1);
  }

  const env = await loadEnv(path.join(ROOT, ".env.local"));
  const apiKey = env.OPENROUTER_API_KEY || process.env.OPENROUTER_API_KEY;
  if (!apiKey) {
    console.error("ERROR: OPENROUTER_API_KEY not set in .env.local");
    process.exit(1);
  }

  const [conceptMd, styleMd] = await Promise.all([
    readFile(CONCEPT_ARTS_MD, "utf8"),
    readFile(STYLE_GUIDE_MD, "utf8").catch(() => ""),
  ]);
  const styleLock = extractStyleLock(styleMd);
  const items = parseConceptArts(conceptMd).filter((it) => it.bloque === blockLetter);

  console.log(`[parse] Found ${items.length} concept arts in Bloque ${blockLetter}`);
  if (items.length === 0) {
    console.error("ERROR: no items parsed for this block");
    process.exit(1);
  }

  await mkdir(OUT_DIR, { recursive: true });

  const results = [];
  for (const item of items) {
    if (args.only && item.id !== args.only) continue;
    const outPath = path.join(OUT_DIR, `${item.id}.png`);
    if (!args.force && existsSync(outPath)) {
      console.log(`[skip] ${item.id} (already exists)`);
      results.push({ id: item.id, status: "skipped" });
      continue;
    }
    if (!item.prompt) {
      console.log(`[fail] ${item.id} — no prompt parsed`);
      results.push({ id: item.id, status: "failed", error: "no prompt" });
      continue;
    }

    // Resolve reference images.
    const refUris = [];
    const refMisses = [];
    for (const slot of item.slots) {
      if (!slot.refPath) continue;
      const abs = path.join(ROOT, slot.refPath);
      if (!existsSync(abs)) {
        refMisses.push(slot.refPath);
        continue;
      }
      try {
        const uri = await readImageAsDataUri(abs);
        refUris.push(uri);
      } catch (err) {
        refMisses.push(`${slot.refPath} (${err.message})`);
      }
    }
    if (refMisses.length > 0) {
      console.log(
        `[warn] ${item.id} — missing refs: ${refMisses.join(", ")}`,
      );
    }

    if (args.dryRun) {
      console.log(
        `[dry-run] ${item.id} — refs:${refUris.length} promptLen:${item.prompt.length}`,
      );
      results.push({ id: item.id, status: "dry-run" });
      continue;
    }

    process.stdout.write(`[gen]  ${item.id} (refs:${refUris.length})... `);
    const r = await generateImage({
      apiKey,
      prompt: item.prompt,
      styleLock,
      refImageDataUris: refUris,
    });

    if (!r.ok) {
      console.log(`FAIL status=${r.status} (${r.elapsed}ms): ${r.error}`);
      results.push({
        id: item.id,
        status: "failed",
        error: `${r.status}: ${r.error}`,
      });
      // If it's a hard auth/model error, stop the batch
      if (
        r.status === 401 ||
        r.status === 403 ||
        r.status === 404
      ) {
        console.error(
          `\n[abort] Hard error (${r.status}). Stopping batch. Verify OPENROUTER_API_KEY and model id "${MODEL_ID}".`,
        );
        break;
      }
      continue;
    }

    const decoded = decodeDataUri(r.imageUri);
    if (!decoded) {
      console.log(`FAIL — could not decode data URI`);
      results.push({ id: item.id, status: "failed", error: "decode" });
      continue;
    }

    await writeFile(outPath, decoded.buffer);
    const sz = (await stat(outPath)).size;
    console.log(`OK ${(sz / 1024).toFixed(1)}KB (${r.elapsed}ms)`);
    results.push({ id: item.id, status: "ok", bytes: sz, elapsed: r.elapsed });
  }

  // Summary
  const ok = results.filter((r) => r.status === "ok");
  const failed = results.filter((r) => r.status === "failed");
  const skipped = results.filter((r) => r.status === "skipped");
  const totalBytes = ok.reduce((s, r) => s + (r.bytes || 0), 0);
  const cost = ok.length * COST_PER_IMAGE;

  console.log("\n=== summary ===");
  console.log(`generated: ${ok.length}`);
  console.log(`failed:    ${failed.length}`);
  console.log(`skipped:   ${skipped.length}`);
  console.log(`size:      ${(totalBytes / 1024 / 1024).toFixed(2)}MB`);
  console.log(`cost est.: $${cost.toFixed(3)} (${ok.length} x $${COST_PER_IMAGE})`);
  if (failed.length > 0) {
    console.log("\nFailed IDs:");
    for (const f of failed) console.log(`  - ${f.id}: ${f.error}`);
  }
}

main().catch((err) => {
  console.error("FATAL:", err);
  process.exit(1);
});
