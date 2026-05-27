/**
 * POST /api/child-story/page
 *
 * Genera UNA pagina de la historia personalizada del nino en el universo Pax.
 * Disenado para llamarse N veces secuencialmente desde el frontend.
 * Cada request dura ~30-45s, dentro del timeout de 120s de Vercel Free.
 *
 * Body (JSON):
 *   - characterSheetBase64: string  (data URL del character sheet del nino)
 *   - childName: string
 *   - childAge: number (3-14)
 *   - superpower: string
 *   - pageNumber: number            (1-10 storybook, 1-6 comic)
 *   - format: "storybook" | "comic"
 *   - totalPages: number            (10 para storybook, 6 para comic)
 *
 * Returns: { ok: true, pageNum, title, text, imageBase64 }
 */

import { NextRequest, NextResponse } from "next/server";
import OpenAI from "openai";

export const runtime = "nodejs";
export const maxDuration = 120;

// ---------------------------------------------------------------------------
// Superpowers
// ---------------------------------------------------------------------------

interface SuperpowerDef {
  escena: string;
  desc: string;
}

const SUPERPOWERS: Record<string, SuperpowerDef> = {
  "hacer reir": {
    escena:
      "{NAME} empieza a hacer caras graciosas frente al cristal. Jiggy se rie tanto que se cae, y el cristal tiembla un poco.",
    desc: "alegrar a otros cuando todo parece gris",
  },
  "ser valiente": {
    escena:
      '{NAME} se acerca al cristal aunque le da un poco de miedo, apoya las dos manos y dice: "No te voy a dejar solo."',
    desc: "enfrentar lo que da miedo para cuidar a otro",
  },
  "ser generoso": {
    escena:
      '{NAME} se quita su pulsera favorita y la apoya contra el cristal. "Toma, te la presto."',
    desc: "dar sin esperar nada a cambio",
  },
  "ser curioso": {
    escena:
      '{NAME} se agacha, mira el cristal de cerca y pregunta: "Que necesitas? Dime y lo busco."',
    desc: "preguntar antes de asumir",
  },
  "ser amable": {
    escena:
      '{NAME} se sienta junto al cristal y le habla bajito: "No pasa nada. Estoy aqui."',
    desc: "acompanar sin pedir nada",
  },
  "cuidar a otros": {
    escena:
      "{NAME} nota que KZ tiene frio y le pasa su chaqueta. El cristal ve el gesto y pulsa suavemente.",
    desc: "cuidar al de al lado antes de pensar en ti",
  },
};

// ---------------------------------------------------------------------------
// Storybook templates (10 pages)
// ---------------------------------------------------------------------------

interface PageDef {
  title: string;
  text: string;
  visualPrompt: string;
  useJiggyRef: boolean;
}

function getStorybookPage(
  pageNum: number,
  name: string,
  age: number,
  superpower: string
): PageDef | null {
  const sp = SUPERPOWERS[superpower] || SUPERPOWERS["ser valiente"];

  const pages: Record<number, PageDef> = {
    1: {
      title: "La llegada",
      text: `${name} tiene ${age} anos y hoy es un dia especial. Una luz suave, entre verde y dorada, brilla debajo de su cama. Se agacha y descubre una grieta que late como un corazon. Sin pensarlo, mete la mano... y cae flotando entre raices luminosas y cristales que zumban. Aterriza de pie en un lugar imposible: el Uray Pacha.`,
      visualPrompt: `A child character (Pax-style: ONE cyclops eye, pointed elf ears, chibi proportions, purple tribal headband, cream vest with purple trim) landing softly inside a spectacular underground cavern. Giant magenta and cyan crystals illuminate basalt walls. God rays from a crack above. The child is seen from behind, arms spread in wonder. 3D Pixar render, cinematic lighting, children's book illustration.`,
      useJiggyRef: false,
    },
    2: {
      title: "Jiggy aparece",
      text: `"Otro humano? No puede ser!" grita alguien con voz aguda. Un ser de piel verde turquesa, un solo ojo enorme y una sonrisa traviesa aparece de un salto. "Soy Jiggy. Vivimos aqui abajo desde hace mucho. Y tu llegaste justo cuando te necesitamos." ${name} no entiende nada todavia, pero siente algo calido en el pecho.`,
      visualPrompt: `Image 1 is the character reference for Jiggy (turquoise jade skin, ONE large cyclops eye, mischievous grin, brown leather vest, explorer bag). Image 2 is the character sheet for ${name}. Generate: Jiggy meeting the child inside an underground crystal cavern. Jiggy is excited, pointing at the child. The child looks amazed. Warm crystal lighting. 3D Pixar render, children's book illustration.`,
      useJiggyRef: true,
    },
    3: {
      title: "El cristal enfermo",
      text: `Jiggy lleva a ${name} corriendo por un tunel lleno de raices luminosas. Al final se abre una camara circular. En el centro hay un cristal enorme, pero su luz parpadea debil. "Este cristal alimenta toda esta zona" explica Jiggy preocupado. "Si se apaga, todo se oscurece." El cristal emite un pulso debil. ${name} lo siente en el pecho.`,
      visualPrompt: `Image 1 is Jiggy's character reference. Image 2 is ${name}'s character sheet. Generate: circular underground chamber with a GIANT crystal flickering weakly with dim magenta light. The child and Jiggy look at it worried. Stalactites of crystal around. Tense atmosphere. 3D Pixar render, children's book illustration.`,
      useJiggyRef: true,
    },
    4: {
      title: "Un superpoder secreto",
      text: `${name} mira el cristal y siente algo raro, como si el cristal le pidiera algo. Jiggy dice: "Los humanos tienen algo que nosotros no: superpoderes del corazon." ${name} no sabe que eso significa todavia, pero recuerda algo que siempre le sale bien: ${sp.desc}. Tal vez eso sea su superpoder.`,
      visualPrompt: `Image 1 is Jiggy's reference. Image 2 is ${name}'s character sheet. Generate: the child touching their chest with a thoughtful expression, standing in front of the dim crystal. Jiggy beside them explaining something with animated gestures. A faint glow starting around the child's hands. 3D Pixar render, children's book illustration, warm magical lighting.`,
      useJiggyRef: true,
    },
    5: {
      title: "Primer intento",
      text: `${name} se acerca al cristal e intenta con todas sus fuerzas activar su superpoder. Aprieta los ojos, tensa los brazos... y no pasa nada. Bueno, casi nada: una chispita diminuta se enciende y se apaga. Jiggy intenta no reirse pero no puede. ${name} tambien se rie. "Estuvo cerca" dice Jiggy secandose una lagrima de risa.`,
      visualPrompt: `Image 1 is Jiggy. Image 2 is ${name}'s character sheet. Generate: the child straining comically in front of the crystal, eyes squeezed shut, arms tense. A TINY spark appears and fades. Jiggy behind trying not to laugh but failing. Humorous scene. 3D Pixar render, children's book illustration, warm lighting.`,
      useJiggyRef: true,
    },
    6: {
      title: "El secreto de Jiggy",
      text: `Jiggy se sienta junto a ${name}. "El truco es que no es un truco" dice. "Los cristales no responden a la fuerza. Responden a lo genuino. No intentes ser super. Solo se tu." ${name} se queda pensando un momento. Respira hondo. Se acerca al cristal, pero esta vez sin apretar nada.`,
      visualPrompt: `Image 1 is Jiggy. Image 2 is ${name}'s character sheet. Generate: Jiggy and the child sitting together on a crystal formation, having a quiet heart-to-heart conversation. Soft warm lighting from nearby crystals. Intimate, emotional moment. 3D Pixar render, children's book illustration.`,
      useJiggyRef: true,
    },
    7: {
      title: "anuraK despierta",
      text: `${sp.escena.replace(/\{NAME\}/g, name)} Y en ese instante, el cristal empieza a brillar. No de a poquito — de golpe, como un corazon que vuelve a latir. Magenta, cian, dorado. "Eso es anuraK!" grita Jiggy. "La energia que nace cuando alguien hace algo bueno de verdad." El cristal late al mismo ritmo que el corazon de ${name}.`,
      visualPrompt: `Image 1 is Jiggy. Image 2 is ${name}'s character sheet. Generate: GRAND VISUAL MOMENT. The massive crystal FULLY AWAKENED, radiating brilliant magenta-cyan-golden light. Waves of luminous energy climbing cavern walls. The child bathed in light, expression of awe and joy. Jiggy celebrating, jumping with excitement. Brilliant particles floating. Epic magical atmosphere. 3D Pixar render, children's book illustration.`,
      useJiggyRef: true,
    },
    8: {
      title: "La tribu celebra",
      text: `La noticia vuela por los tuneles. De todas partes llegan Pax: Wiz, el viejo sabio de barba blanca. Byte con sus auriculares de luces. Luxa, que se rie tan fuerte que tiemblan las estalactitas. Y Onyx, enorme y silencioso, que saluda a ${name} con la mano en el pecho. Alguien empieza a tocar musica. Los cristales pulsan al compas. Todos bailan.`,
      visualPrompt: `Image 2 is ${name}'s character sheet. Generate: celebration in a large underground Pax cavern. Many small Pax tribe characters (turquoise jade skin, ONE cyclops eye each, pointed ears, tribal outfits) dancing and celebrating. The child dancing in the center. Crystals pulsing with festive lights. Colorful, warm, joyful atmosphere. 3D Pixar render, children's book illustration.`,
      useJiggyRef: false,
    },
    9: {
      title: "Un recuerdo especial",
      text: `Wiz, el mas viejo de la tribu, se acerca a ${name}. En sus manos tiene un cristal pequeno, del tamano de una canica, que brilla con un pulso suave y constante. "Este cristal es tuyo" dice Wiz. "Va a brillar cada vez que hagas algo bueno, arriba o abajo. Y nosotros lo vamos a sentir." ${name} lo aprieta en la mano. Esta tibio.`,
      visualPrompt: `Image 2 is ${name}'s character sheet. Generate: An old wise Pax character (white mineral beard, purple robe, crystal staff) giving a small glowing crystal to the child. The crystal glows warm magenta-cyan in the child's hands. Other Pax tribe members watching warmly from behind. Emotional, intimate moment. 3D Pixar render, children's book illustration.`,
      useJiggyRef: false,
    },
    10: {
      title: "De vuelta a casa",
      text: `${name} sube por la grieta, aterriza en su cuarto, y todo esta igual que antes. Excepto una cosa: en su mano hay un cristal pequeno que brilla cada vez que siente esa cosquilla en el pecho. Y ahora sabe lo que es. Se llama anuraK. Y cada vez que brilla, en algun lugar debajo del mundo, un Pax sonrie.`,
      visualPrompt: `Image 2 is ${name}'s character sheet. Generate: a child lying in bed at night, looking at a small crystal glowing softly in their open palm. The crystal casts gentle magenta-cyan light on their face. Warm cozy bedroom. Subtle overlay or reflection showing Jiggy and the Pax world below. Emotional, warm closing scene. 3D Pixar render, children's book illustration, soft lighting.`,
      useJiggyRef: false,
    },
  };

  return pages[pageNum] || null;
}

// ---------------------------------------------------------------------------
// Comic templates (6 pages, 4 panels each)
// ---------------------------------------------------------------------------

function getComicPage(
  pageNum: number,
  name: string,
  age: number,
  superpower: string
): PageDef | null {
  const sp = SUPERPOWERS[superpower] || SUPERPOWERS["ser valiente"];
  const comicStyle =
    "Comic book page layout, 4 panels in a 2x2 grid, sequential storytelling, speech bubbles with text, dynamic angles, 3D Pixar style with neon-magic lighting.";

  const pages: Record<number, PageDef> = {
    1: {
      title: "La llegada + Jiggy",
      text: `${name} (${age} anos) descubre una grieta luminosa bajo su cama y cae al Uray Pacha. Alli conoce a Jiggy, un ser turquesa con un solo ojo enorme y una sonrisa traviesa. "Llegaste justo cuando te necesitamos!"`,
      visualPrompt: `${comicStyle} Image 1 is Jiggy's character reference. Image 2 is ${name}'s character sheet. PAGE 1 of a children's comic: Panel 1: ${name} discovers a glowing crack under the bed. Panel 2: Falls through into a crystal cavern. Panel 3: Meets Jiggy who jumps excitedly. Panel 4: Jiggy welcomes the child with open arms. Speech bubbles in Spanish. 3D Pixar render, magical underground setting.`,
      useJiggyRef: true,
    },
    2: {
      title: "El cristal enfermo",
      text: `Jiggy lleva a ${name} a una camara donde un cristal gigante parpadea debil. "Si se apaga, todo se oscurece." El cristal emite un pulso que ${name} siente en el pecho. Algo tiene que hacer.`,
      visualPrompt: `${comicStyle} Image 1 is Jiggy. Image 2 is ${name}'s character sheet. PAGE 2: Panel 1: Running through luminous tunnels. Panel 2: Arriving at a chamber with a giant dim crystal. Panel 3: Jiggy explains the crystal is dying, worried face. Panel 4: The child feels the crystal's pulse, hand on chest. Speech bubbles in Spanish. 3D Pixar render.`,
      useJiggyRef: true,
    },
    3: {
      title: "Superpoder + primer intento",
      text: `${name} descubre que tiene un superpoder del corazon: ${sp.desc}. Intenta usarlo con todas sus fuerzas... y falla comicamente. Solo sale una chispita. Jiggy se rie tanto que se cae. "Estuvo cerca!"`,
      visualPrompt: `${comicStyle} Image 1 is Jiggy. Image 2 is ${name}'s character sheet. PAGE 3: Panel 1: Jiggy tells the child about heart superpowers. Panel 2: The child strains comically trying to activate power, eyes squeezed. Panel 3: A tiny spark appears and fades, both look surprised. Panel 4: Both laughing, Jiggy fell over. Speech bubbles in Spanish. Humorous scene. 3D Pixar render.`,
      useJiggyRef: true,
    },
    4: {
      title: "Jiggy ensena + anuraK",
      text: `"No intentes ser super. Solo se tu" dice Jiggy. ${name} respira hondo y se acerca al cristal sin forzar nada. ${sp.escena.replace(/\{NAME\}/g, name)} El cristal explota en luz. "Eso es anuraK!" grita Jiggy.`,
      visualPrompt: `${comicStyle} Image 1 is Jiggy. Image 2 is ${name}'s character sheet. PAGE 4: Panel 1: Jiggy and child sitting, having a heart-to-heart. Panel 2: Child approaches crystal calmly, genuine expression. Panel 3: EXPLOSION of magenta-cyan-golden light from the crystal. Panel 4: Jiggy celebrating, crystal fully alive. Speech bubbles in Spanish. 3D Pixar render, epic lighting in panel 3.`,
      useJiggyRef: true,
    },
    5: {
      title: "La tribu celebra",
      text: `La noticia vuela por los tuneles. Llegan Wiz, Byte, Luxa, Onyx y mas Pax. Todos quieren conocer al humano que encendio el cristal. Empieza la musica, los cristales pulsan al compas. ${name} baila con la tribu.`,
      visualPrompt: `${comicStyle} Image 2 is ${name}'s character sheet. PAGE 5: Panel 1: Many Pax tribe members arriving through tunnels excitedly. Panel 2: Old wise Wiz character greets the child with reverence. Panel 3: Full celebration scene with dancing, glowing crystals pulsing. Panel 4: The child dancing happily surrounded by Pax friends. Speech bubbles in Spanish. 3D Pixar render, festive colorful lighting.`,
      useJiggyRef: false,
    },
    6: {
      title: "De vuelta + cristal de recuerdo",
      text: `Wiz le da a ${name} un cristal pequeno que brilla con un pulso suave. "Va a brillar cada vez que hagas algo bueno." ${name} vuelve a su cuarto con el cristal en la mano. Ahora sabe lo que es esa cosquilla. Se llama anuraK.`,
      visualPrompt: `${comicStyle} Image 2 is ${name}'s character sheet. PAGE 6: Panel 1: Wise old Pax gives the child a small glowing crystal. Panel 2: Child says goodbye to Jiggy and the tribe, waving. Panel 3: Back in bedroom at night, looking at the crystal glowing in hand. Panel 4: Close-up of the crystal with a warm glow, the child smiling. Speech bubbles in Spanish. 3D Pixar render, emotional closing.`,
      useJiggyRef: false,
    },
  };

  return pages[pageNum] || null;
}

// ---------------------------------------------------------------------------
// Load Jiggy reference PNG
// ---------------------------------------------------------------------------

async function loadJiggyBuffer(): Promise<Buffer> {
  // In Vercel prod, public/ files are on the CDN, not the lambda filesystem.
  // Try filesystem first (dev), then fetch from public URL.
  try {
    const { readFile } = await import("fs/promises");
    const { join } = await import("path");
    const jiggyPath = join(
      process.cwd(),
      "_lore",
      "personajes",
      "jiggy.png"
    );
    return await readFile(jiggyPath);
  } catch {
    // Fallback: try public/ path
    try {
      const { readFile } = await import("fs/promises");
      const { join } = await import("path");
      const publicPath = join(
        process.cwd(),
        "public",
        "images",
        "personajes",
        "jiggy.png"
      );
      return await readFile(publicPath);
    } catch {
      // Last resort for Vercel: fetch from own URL
      const base = process.env.VERCEL_URL
        ? `https://${process.env.VERCEL_URL}`
        : "http://localhost:3000";
      const resp = await fetch(`${base}/images/personajes/jiggy.png`);
      if (!resp.ok) throw new Error("Failed to load Jiggy reference image");
      return Buffer.from(await resp.arrayBuffer());
    }
  }
}

// ---------------------------------------------------------------------------
// Handler
// ---------------------------------------------------------------------------

export async function POST(req: NextRequest) {
  const t0 = Date.now();

  try {
    let body: Record<string, unknown>;
    try {
      body = (await req.json()) as Record<string, unknown>;
    } catch {
      return NextResponse.json(
        { ok: false, error: "Body JSON invalido." },
        { status: 400 }
      );
    }

    const characterSheetBase64 =
      typeof body.characterSheetBase64 === "string"
        ? body.characterSheetBase64.trim()
        : "";
    const childName =
      typeof body.childName === "string" ? body.childName.trim() : "";
    const childAge = typeof body.childAge === "number" ? body.childAge : 0;
    const superpower =
      typeof body.superpower === "string"
        ? body.superpower.trim().toLowerCase()
        : "";
    const pageNumber =
      typeof body.pageNumber === "number" ? body.pageNumber : 0;
    const format =
      typeof body.format === "string" ? body.format.trim() : "storybook";
    const totalPages =
      typeof body.totalPages === "number" ? body.totalPages : 0;

    // Validate
    if (!characterSheetBase64 || !characterSheetBase64.startsWith("data:")) {
      return NextResponse.json(
        { ok: false, error: "characterSheetBase64 requerido (data URL)." },
        { status: 400 }
      );
    }
    if (!childName || childName.length > 50) {
      return NextResponse.json(
        { ok: false, error: "childName requerido (max 50 chars)." },
        { status: 400 }
      );
    }
    if (childAge < 3 || childAge > 14) {
      return NextResponse.json(
        { ok: false, error: "childAge debe estar entre 3 y 14." },
        { status: 400 }
      );
    }
    if (!SUPERPOWERS[superpower]) {
      return NextResponse.json(
        {
          ok: false,
          error: `superpower invalido. Opciones: ${Object.keys(SUPERPOWERS).join(", ")}`,
        },
        { status: 400 }
      );
    }
    if (format !== "storybook" && format !== "comic") {
      return NextResponse.json(
        { ok: false, error: 'format debe ser "storybook" o "comic".' },
        { status: 400 }
      );
    }
    const maxPages = format === "storybook" ? 10 : 6;
    if (pageNumber < 1 || pageNumber > maxPages) {
      return NextResponse.json(
        {
          ok: false,
          error: `pageNumber debe estar entre 1 y ${maxPages} para formato ${format}.`,
        },
        { status: 400 }
      );
    }
    if (totalPages !== maxPages) {
      return NextResponse.json(
        {
          ok: false,
          error: `totalPages debe ser ${maxPages} para formato ${format}.`,
        },
        { status: 400 }
      );
    }

    // API key
    const apiKey = process.env.OPENAI_API_KEY;
    if (!apiKey) {
      console.error("[child-story/page] OPENAI_API_KEY no seteada");
      return NextResponse.json(
        { ok: false, error: "Servicio no disponible temporalmente." },
        { status: 500 }
      );
    }

    // Get page definition
    const pageDef =
      format === "storybook"
        ? getStorybookPage(pageNumber, childName, childAge, superpower)
        : getComicPage(pageNumber, childName, childAge, superpower);

    if (!pageDef) {
      return NextResponse.json(
        { ok: false, error: `Pagina ${pageNumber} no definida.` },
        { status: 400 }
      );
    }

    // Prepare character sheet buffer
    const base64Match = characterSheetBase64.match(
      /^data:[^;]+;base64,(.+)$/
    );
    if (!base64Match) {
      return NextResponse.json(
        { ok: false, error: "Formato data URL invalido." },
        { status: 400 }
      );
    }
    const charSheetBuffer = Buffer.from(base64Match[1], "base64");

    // Build image references for OpenAI edit
    const openai = new OpenAI({ apiKey });

    console.log(
      `[child-story/page] Generando ${format} pagina ${pageNumber}/${totalPages} para "${childName}"...`
    );

    let imageFiles: File[];

    if (pageDef.useJiggyRef) {
      // Pages with Jiggy: 2 reference images (Jiggy + child character sheet)
      const jiggyBuffer = await loadJiggyBuffer();
      const jiggyFile = new File(
        [new Uint8Array(jiggyBuffer)],
        "jiggy-ref.png",
        { type: "image/png" }
      );
      const charFile = new File(
        [new Uint8Array(charSheetBuffer)],
        "character-sheet.png",
        { type: "image/png" }
      );
      imageFiles = [jiggyFile, charFile];
    } else {
      // Pages without Jiggy: only child character sheet
      const charFile = new File(
        [new Uint8Array(charSheetBuffer)],
        "character-sheet.png",
        { type: "image/png" }
      );
      imageFiles = [charFile];
    }

    const response = await openai.images.edit({
      model: "gpt-image-1",
      image: imageFiles,
      prompt: pageDef.visualPrompt,
      size: format === "comic" ? "1024x1536" : "1536x1024",
      quality: "high",
    });

    const imageData = response.data?.[0];
    const tookMs = Date.now() - t0;

    if (!imageData || !imageData.b64_json) {
      console.warn(
        `[child-story/page] Pagina ${pageNumber} sin imagen (${tookMs}ms)`
      );
      return NextResponse.json({
        ok: true,
        pageNum: pageNumber,
        title: pageDef.title,
        text: pageDef.text,
        imageBase64: "",
        tookMs,
      });
    }

    console.log(
      `[child-story/page] Pagina ${pageNumber} lista en ${tookMs}ms`
    );

    return NextResponse.json({
      ok: true,
      pageNum: pageNumber,
      title: pageDef.title,
      text: pageDef.text,
      imageBase64: `data:image/png;base64,${imageData.b64_json}`,
      tookMs,
    });
  } catch (err) {
    const e = err as Error;
    console.error("[child-story/page] Error:", e.message);

    if (
      e.message?.includes("safety") ||
      e.message?.includes("content_policy")
    ) {
      return NextResponse.json(
        {
          ok: false,
          error:
            "Imagen rechazada por politica de contenido. Intenta con otra foto.",
        },
        { status: 400 }
      );
    }

    return NextResponse.json(
      { ok: false, error: "Error al generar la pagina. Intenta de nuevo." },
      { status: 500 }
    );
  }
}
