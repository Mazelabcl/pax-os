/**
 * POST /api/paxearte
 *
 * Recibe una foto (multipart/form-data) y la transforma en un character sheet
 * estilo Pax humanizado o full-pax usando OpenAI gpt-image-1 (images.edit).
 *
 * Campos:
 *   - photo: File (imagen del usuario)
 *   - style: "humanized" (default) | "full-pax"
 *
 * Devuelve: { ok: true, imageUrl: string } o { ok: false, error: string }
 */

import { NextRequest, NextResponse } from "next/server";
import OpenAI from "openai";

export const runtime = "nodejs";
export const maxDuration = 120; // Image generation can take a while

// ---------------------------------------------------------------------------
// Prompts
// ---------------------------------------------------------------------------

const HUMANIZED_PROMPT = `Transform this person into a Pax tribe character sheet with 5 poses on a clean white background.

CRITICAL IDENTITY RULES:
- Keep their EXACT skin color and facial features recognizable
- Replace both eyes with ONE large cyclops eye centered on the face (this is non-negotiable)
- Add pointed elf ears
- Chibi proportions: head is 40% of total height, 3-3.5 heads tall total body

OUTFIT (mandatory on all poses):
- Purple tribal headband with white geometric diamond patterns, tied at the back
- Cream/beige sleeveless tribal vest with purple geometric trim and purple crystal pendant necklace
- Dark navy baggy pants with tribal wraps at ankles
- Leather sandals with ankle straps
- Multiple bronze/copper bracelets on both wrists
- Turquoise/jade geometric tribal tattoos on both arms and shoulders
- Purple crystal earring on one ear
- Brown leather belt with small pouches and crystal vials

5 POSES (arrange in character sheet layout):
1. TOP LEFT - Full body standing front pose, confident stance, one hand on hip
2. TOP RIGHT - Close-up portrait bust, friendly smile, showing headband and jewelry details
3. BOTTOM LEFT - Sitting cross-legged reading an ancient book with glowing pages
4. BOTTOM CENTER - Standing holding a crystal-topped wooden staff (purple crystal glowing)
5. BOTTOM RIGHT - Running/action pose, dynamic movement, crystal pendants swinging

STYLE: 3D Pixar-quality render, PBR materials, soft studio lighting, white background, clean character sheet layout with clear separation between poses.`;

const PIXAR_PROMPT = `Transform this child's photo into a 3D Pixar/Disney animated movie character.

CRITICAL — LIKENESS IS EVERYTHING:
- Keep the EXACT same face shape, nose, mouth, eyes, eyebrows, hair color, hair style, skin tone
- The person looking at this must immediately say "that's my kid!"
- Do NOT change proportions, do NOT add fantasy elements, do NOT change clothing significantly
- This is a STYLE TRANSFER only: real photo → 3D animated Pixar render

STYLE:
- 3D Pixar-quality render (like Coco, Inside Out, Turning Red)
- Soft ambient lighting, warm tones
- Slightly larger eyes (Pixar style) but keeping the same eye color and shape
- Smooth skin with subtle subsurface scattering
- Clean white/light gradient background
- Single portrait, chest-up, looking at camera with a natural smile
- High quality, 4K render feel`;

const FULL_PAX_PROMPT = `Transform this person into a FULL PAX tribe character sheet with 5 poses on a clean white background.

CRITICAL IDENTITY RULES:
- Replace their skin with TURQUOISE JADE mineral skin color (like polished jade stone)
- Keep facial structure recognizable but with jade-green skin
- Replace both eyes with ONE large cyclops eye centered on the face (this is non-negotiable)
- Add pointed elf ears
- Chibi proportions: head is 40% of total height, 3-3.5 heads tall total body

OUTFIT (mandatory on all poses):
- Purple tribal headband with white geometric diamond patterns, tied at the back
- Cream/beige sleeveless tribal vest with purple geometric trim and purple crystal pendant necklace
- Dark navy baggy pants with tribal wraps at ankles
- Leather sandals with ankle straps
- Multiple bronze/copper bracelets on both wrists
- Turquoise/jade geometric tribal tattoos on both arms and shoulders (slightly darker than skin)
- Purple crystal earring on one ear
- Brown leather belt with small pouches and crystal vials

5 POSES (arrange in character sheet layout):
1. TOP LEFT - Full body standing front pose, confident stance, one hand on hip
2. TOP RIGHT - Close-up portrait bust, friendly smile, showing headband and jewelry details
3. BOTTOM LEFT - Sitting cross-legged reading an ancient book with glowing pages
4. BOTTOM CENTER - Standing holding a crystal-topped wooden staff (purple crystal glowing)
5. BOTTOM RIGHT - Running/action pose, dynamic movement, crystal pendants swinging

STYLE: 3D Pixar-quality render, PBR materials, soft studio lighting, white background, clean character sheet layout with clear separation between poses.`;

// ---------------------------------------------------------------------------
// Handler
// ---------------------------------------------------------------------------

export async function POST(req: NextRequest) {
  try {
    // 1) Parse multipart form data
    const formData = await req.formData();
    const photo = formData.get("photo");
    const style = (formData.get("style") as string) || "humanized";

    if (!photo || !(photo instanceof File)) {
      return NextResponse.json(
        { ok: false, error: "Campo 'photo' requerido (imagen)." },
        { status: 400 }
      );
    }

    if (!["humanized", "full-pax", "pixar"].includes(style)) {
      return NextResponse.json(
        { ok: false, error: "Estilo debe ser 'humanized', 'full-pax' o 'pixar'." },
        { status: 400 }
      );
    }

    // Validate file type
    const validTypes = ["image/jpeg", "image/png", "image/webp", "image/gif"];
    if (!validTypes.includes(photo.type)) {
      return NextResponse.json(
        { ok: false, error: "Formato de imagen no soportado. Usa JPG, PNG, WebP o GIF." },
        { status: 400 }
      );
    }

    // Max 20MB
    if (photo.size > 20 * 1024 * 1024) {
      return NextResponse.json(
        { ok: false, error: "Imagen demasiado grande. Maximo 20MB." },
        { status: 400 }
      );
    }

    // 2) Verify API key
    const apiKey = process.env.OPENAI_API_KEY;
    if (!apiKey) {
      console.error("[paxearte] OPENAI_API_KEY no esta seteada");
      return NextResponse.json(
        { ok: false, error: "Servicio no disponible temporalmente." },
        { status: 500 }
      );
    }

    // 3) Call OpenAI
    const openai = new OpenAI({ apiKey });
    const prompt = style === "pixar" ? PIXAR_PROMPT : style === "full-pax" ? FULL_PAX_PROMPT : HUMANIZED_PROMPT;

    console.log(`[paxearte] Generando character sheet | style=${style} | photoSize=${photo.size}`);
    const t0 = Date.now();

    // Convert uploaded file to the format OpenAI expects
    const photoBuffer = Buffer.from(await photo.arrayBuffer());
    const photoFile = new File([new Uint8Array(photoBuffer)], photo.name || "photo.png", {
      type: photo.type,
    });

    const response = await openai.images.edit({
      model: "gpt-image-1",
      image: photoFile,
      prompt,
      size: "1024x1024",
      quality: "high",
    });

    const tookMs = Date.now() - t0;
    console.log(`[paxearte] OpenAI respondio en ${tookMs}ms`);

    // 4) Return image as base64 data URL (Vercel has read-only filesystem)
    const imageData = response.data?.[0];
    if (!imageData || !imageData.b64_json) {
      console.error("[paxearte] OpenAI no devolvio imagen");
      return NextResponse.json(
        { ok: false, error: "No se pudo generar la imagen. Intenta de nuevo." },
        { status: 502 }
      );
    }

    const imageBase64 = `data:image/png;base64,${imageData.b64_json}`;
    console.log(`[paxearte] Imagen generada (base64) | took=${tookMs}ms`);

    return NextResponse.json({
      ok: true,
      imageBase64,
      style,
      tookMs,
    });
  } catch (err) {
    const e = err as Error;
    console.error("[paxearte] Error:", e.message);

    // Handle OpenAI-specific errors
    if (e.message?.includes("safety") || e.message?.includes("content_policy")) {
      return NextResponse.json(
        { ok: false, error: "La imagen fue rechazada por la politica de contenido. Intenta con otra foto." },
        { status: 400 }
      );
    }

    return NextResponse.json(
      { ok: false, error: "Error al generar la imagen. Intenta de nuevo." },
      { status: 500 }
    );
  }
}
