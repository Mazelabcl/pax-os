/**
 * POST /api/child-story
 *
 * Genera una historia personalizada de 7 paginas con imagenes del universo Pax.
 * Recibe el character sheet generado por /api/paxearte + datos del nino.
 *
 * Body (JSON):
 *   - characterSheetUrl: string (URL relativa de la imagen generada)
 *   - childName: string
 *   - childAge: number (5-10)
 *   - superpower: string (uno de los 6 disponibles)
 *
 * Devuelve: { ok: true, pages: [{ pageNum, title, text, imageUrl }] }
 *
 * NOTA: genera 7 imagenes secuencialmente (~2-3 min total). MVP sincrono.
 */

import { NextRequest, NextResponse } from "next/server";
import OpenAI from "openai";

export const runtime = "nodejs";
export const maxDuration = 300; // 5 min max for 7 sequential image generations

// ---------------------------------------------------------------------------
// Superpowers definitions
// ---------------------------------------------------------------------------

interface SuperpowerDef {
  escena: string;
  desc: string;
}

const SUPERPOWERS: Record<string, SuperpowerDef> = {
  "ser generoso": {
    escena: "{NOMBRE} se quita su pulsera favorita — la que lleva siempre — y la apoya suavemente contra el cristal. \"Toma, te la presto. Tal vez te haga sentir mejor.\"",
    desc: "dar sin esperar nada a cambio",
  },
  "ser valiente": {
    escena: "{NOMBRE} se acerca al cristal aunque le da un poco de miedo, apoya las dos manos y dice con voz firme: \"No te voy a dejar solo.\"",
    desc: "enfrentar lo que da miedo para cuidar a otro",
  },
  "hacer reir": {
    escena: "{NOMBRE} empieza a hacer caras graciosas frente al cristal, hasta que Jiggy se rie tanto que se cae. Y por alguna razon, el cristal tambien tiembla.",
    desc: "alegrar a otros cuando todo parece gris",
  },
  "ser curioso": {
    escena: "{NOMBRE} se agacha, mira el cristal de cerca y pregunta: \"Que necesitas? Dime y lo busco.\"",
    desc: "preguntar antes de asumir",
  },
  "ser amable": {
    escena: "{NOMBRE} se sienta junto al cristal y le habla bajito, como a un amigo triste: \"No pasa nada. Estoy aqui.\"",
    desc: "acompanar sin pedir nada",
  },
  "cuidar a otros": {
    escena: "{NOMBRE} nota que KZ tiene frio y le pasa su chaqueta. El cristal ve el gesto y pulsa.",
    desc: "cuidar al de al lado antes de pensar en ti",
  },
};

// ---------------------------------------------------------------------------
// Page definitions (visual prompts for each page)
// ---------------------------------------------------------------------------

interface PageTemplate {
  pageNum: number;
  title: string;
  textTemplate: string;
  visualPrompt: string;
}

function getPageTemplates(name: string, age: number, superpower: string): PageTemplate[] {
  const sp = SUPERPOWERS[superpower] || SUPERPOWERS["ser valiente"];

  return [
    {
      pageNum: 1,
      title: "La llegada",
      textTemplate: `${name} tiene ${age} anos y hoy es un dia especial. Mientras juega en su cuarto, nota algo raro: una luz suave, entre verde y dorada, brilla debajo de su cama. Se agacha a mirar y descubre una grieta en el piso que antes no estaba ahi. La grieta late como un corazon diminuto. Sin pensarlo dos veces, ${name} mete la mano... y el piso se abre. Cae suave, como flotando, entre raices luminosas y cristales que zumban bajito. Aterriza de pie en un lugar imposible: una caverna enorme donde todo brilla con luz propia. Bienvenido al Uray Pacha.`,
      visualPrompt: `A child character (Pax-style: ONE cyclops eye, pointed elf ears, chibi proportions, purple tribal headband, cream vest with purple trim, turquoise arm tattoos) landing softly inside a spectacular underground cavern. Giant magenta and cyan crystals illuminate basalt walls. God rays falling from a crack in the ceiling above. The child is seen from behind in silhouette, arms slightly spread in wonder. Luminous mineral formations everywhere. 3D Pixar render, cinematic lighting, magical atmosphere. Children's book illustration style.`,
    },
    {
      pageNum: 2,
      title: "Jiggy y KZ",
      textTemplate: `"Otro humano? No puede ser!" grita alguien con voz aguda. Un ser pequeno de piel verde turquesa, un solo ojo enorme y una sonrisa traviesa aparece de un salto. Lleva una bandana purpura y parece que siempre esta a punto de tropezar. "Soy Jiggy. Y este de aca es KZ." Detras de Jiggy asoma otro ser, mas bajito, con ojos brillantes llenos de curiosidad. KZ le hace un gesto timido con la mano. "Somos Pax. Vivimos aqui abajo desde hace... bueno, mucho tiempo. Y tu llegaste justo cuando te necesitamos." ${name} no entiende nada todavia. Pero siente algo calido en el pecho, como una cosquilla suave.`,
      visualPrompt: `Two small Pax tribe characters meeting a child in an underground crystal cavern. JIGGY: turquoise jade skin, ONE large cyclops eye, wide mischievous grin, purple headband with geometric patterns, cream vest, dynamic enthusiastic pose pointing at the viewer. KZ: smaller, turquoise skin, ONE cyclops eye, shy expression, peeking from behind a crystal formation. The child character (Pax-style with ONE cyclops eye, pointed ears, human skin tone, purple headband) facing them with amazement. Warm crystal lighting. 3D Pixar render, children's book illustration.`,
    },
    {
      pageNum: 3,
      title: "Algo se apaga",
      textTemplate: `Jiggy lleva a ${name} corriendo por un tunel estrecho lleno de raices luminosas. KZ los sigue de cerca. Al final del tunel se abre una camara circular. En el centro hay un cristal enorme — del tamano de ${name} — pero algo no esta bien. Su luz parpadea debil, como una vela a punto de morir. "Este cristal alimenta toda esta zona del Uray Pacha" explica KZ con voz preocupada. "Si se apaga, las plantas de cristal se marchitan, los tuneles se oscurecen..." "Probamos de todo" dice Jiggy. "Cantar, bailar, contar chistes. Nada funciona." El cristal emite un pulso debil. ${name} lo siente en el pecho.`,
      visualPrompt: `Circular underground chamber with a GIANT crystal in the center that is flickering weakly with dim magenta light, like a candle about to die. Stalactites and stalagmites of crystal around the chamber. A child character (Pax-style: ONE cyclops eye, pointed ears, human skin, purple headband, cream tribal vest) looking at the crystal with empathy. Jiggy and KZ (small turquoise-skinned Pax characters with cyclops eyes) standing to the side looking worried. Tense but not dark atmosphere. Irregular light pulses from the dying crystal. 3D Pixar render, children's book illustration.`,
    },
    {
      pageNum: 4,
      title: "El superpoder",
      textTemplate: `${name} se queda mirando el cristal un momento largo. Jiggy y KZ se miran entre ellos sin saber que hacer. Entonces ${name} hace algo que nadie esperaba. ${sp.escena.replace(/\{NOMBRE\}/g, name)} No es magia. No es un truco. Es simplemente lo que ${name} sabe hacer mejor: ${sp.desc}. Y en ese instante, algo cambia.`,
      visualPrompt: `Intimate moment: a child character (Pax-style: ONE cyclops eye, pointed ears, human skin tone, purple tribal headband, cream vest with purple trim) standing in front of a large crystal, making a gentle gesture toward it. Jiggy and KZ (small turquoise Pax characters with cyclops eyes) watching from behind, surprised expressions. A FIRST SPARK of light beginning to glow inside the previously dim crystal. The child's face illuminated by this new spark. Emotional, hopeful lighting. 3D Pixar render, children's book illustration.`,
    },
    {
      pageNum: 5,
      title: "anuraK",
      textTemplate: `El cristal empieza a brillar. No de a poquito — de golpe, como un corazon que vuelve a latir. Magenta profundo, destellos de cian, olas de luz dorada que suben por las paredes de la caverna como raices vivas. "Eso es anuraK!" grita KZ, saltando. "Anu-que?" pregunta ${name}. "anuraK" explica Jiggy, todavia con la boca abierta. "La energia que nace cuando alguien hace algo bueno de verdad. Llevamos semanas intentando encender este cristal y tu lo lograste en un minuto." La cosquilla en el pecho de ${name} ahora es calida, grande, luminosa. El cristal late al mismo ritmo que su corazon.`,
      visualPrompt: `GRAND VISUAL MOMENT: A massive crystal FULLY AWAKENED, radiating brilliant magenta-cyan-golden light. Waves of luminous energy climbing up the cavern walls like living roots. A child character (Pax-style: ONE cyclops eye, pointed ears, human skin, purple headband) standing in front of the crystal, bathed in light, expression of awe and pure joy. Jiggy and KZ (turquoise Pax characters) celebrating behind, jumping with excitement. Brilliant particles floating in the air. Magical, climactic atmosphere. 3D Pixar render, children's book illustration, epic lighting.`,
    },
    {
      pageNum: 6,
      title: "Fiesta en el Uray Pacha",
      textTemplate: `La noticia vuela por los tuneles. De todas partes llegan Pax que ${name} no conocia: Wiz, el viejo sabio de barba mineral y sonrisa lenta. Byte, con sus auriculares de luces verdes. Luxa, que se rie tan fuerte que hace temblar las estalactitas. Y Onyx, enorme y silencioso, que le hace a ${name} un saludo solemne con la mano en el pecho. Todos quieren conocer al humano que encendio el cristal. Alguien empieza a tocar musica. Los cristales pulsan al compas. Los Pax bailan. ${name} tambien. Y en medio de la fiesta, Wiz se acerca y le dice algo al oido: "Sabiamos que vendrias. Solo no sabiamos cuando."`,
      visualPrompt: `Celebration scene in a large underground Pax cavern. Many small Pax tribe characters (turquoise jade skin, ONE cyclops eye each, pointed ears, tribal outfits) celebrating and dancing. Crystals all around pulsing with festive light in rhythm. A child character (Pax-style with human skin, cyclops eye, purple headband) dancing with Jiggy and KZ in the center. An old wise Pax character (WIZ: white mineral beard, gentle smile) watching from the side. Colorful crystal lights like a party. Warm, joyful, festive atmosphere. 3D Pixar render, children's book illustration.`,
    },
    {
      pageNum: 7,
      title: "De vuelta a casa",
      textTemplate: `Cuando es hora de volver, Jiggy acompana a ${name} hasta la grieta por donde llego. "No te preocupes" dice Jiggy. "Cada vez que hagas algo bueno por alguien, arriba o abajo, un cristal va a brillar. Y nosotros lo vamos a sentir." KZ se acerca corriendo con algo en las manos: un pequeno cristal, del tamano de una canica, que brilla con un pulso suave y constante. "Para que no te olvides" dice KZ. ${name} lo aprieta en la mano. Esta tibio. Sube por la grieta, aterriza en su cuarto, y todo esta igual que antes. Excepto una cosa: en su mano hay un cristal pequeno que brilla cada vez que ${name} siente esa cosquilla en el pecho. Y ahora sabe lo que es. Se llama anuraK.`,
      visualPrompt: `Dual scene - split composition. TOP HALF: A child (Pax-style: ONE cyclops eye, pointed ears, human skin, purple headband) lying in bed at night in their bedroom, looking at a small crystal glowing softly in their open palm. The crystal casts a gentle magenta-cyan light on their face. Warm, cozy bedroom. BOTTOM HALF or subtle overlay: Jiggy and KZ (turquoise Pax characters with cyclops eyes) looking upward from the Uray Pacha underground world, smiling warmly. Emotional, warm closing scene. 3D Pixar render, children's book illustration, soft lighting.`,
    },
  ];
}

// ---------------------------------------------------------------------------
// Handler
// ---------------------------------------------------------------------------

export async function POST(req: NextRequest) {
  const tStart = Date.now();

  try {
    // 1) Parse body
    let body: Record<string, unknown>;
    try {
      body = (await req.json()) as Record<string, unknown>;
    } catch {
      return NextResponse.json(
        { ok: false, error: "Body JSON invalido." },
        { status: 400 }
      );
    }

    const characterSheetUrl = typeof body.characterSheetUrl === "string" ? body.characterSheetUrl.trim() : "";
    const childName = typeof body.childName === "string" ? body.childName.trim() : "";
    const childAge = typeof body.childAge === "number" ? body.childAge : 0;
    const superpower = typeof body.superpower === "string" ? body.superpower.trim().toLowerCase() : "";

    // 2) Validate — accept base64 data URL or legacy path
    if (!characterSheetUrl) {
      return NextResponse.json({ ok: false, error: "characterSheetUrl es requerido (base64 data URL o path)." }, { status: 400 });
    }
    if (!childName || childName.length > 50) {
      return NextResponse.json({ ok: false, error: "childName es requerido (max 50 chars)." }, { status: 400 });
    }
    if (childAge < 3 || childAge > 14) {
      return NextResponse.json({ ok: false, error: "childAge debe estar entre 3 y 14." }, { status: 400 });
    }
    if (!SUPERPOWERS[superpower]) {
      const valid = Object.keys(SUPERPOWERS).join(", ");
      return NextResponse.json(
        { ok: false, error: `superpower invalido. Opciones: ${valid}` },
        { status: 400 }
      );
    }

    // 3) Verify API key
    const apiKey = process.env.OPENAI_API_KEY;
    if (!apiKey) {
      console.error("[child-story] OPENAI_API_KEY no esta seteada");
      return NextResponse.json(
        { ok: false, error: "Servicio no disponible temporalmente." },
        { status: 500 }
      );
    }

    // 4) Load character sheet image as reference (base64 data URL or legacy file path)
    let charSheetBuffer: Buffer;
    if (characterSheetUrl.startsWith("data:")) {
      // Extract base64 from data URL
      const base64Match = characterSheetUrl.match(/^data:[^;]+;base64,(.+)$/);
      if (!base64Match) {
        return NextResponse.json(
          { ok: false, error: "Formato de data URL invalido para character sheet." },
          { status: 400 }
        );
      }
      charSheetBuffer = Buffer.from(base64Match[1], "base64");
    } else {
      // Legacy: try reading from filesystem (works in dev, not in Vercel prod)
      const { readFile } = await import("fs/promises");
      const { join } = await import("path");
      const charSheetPath = join(process.cwd(), "public", characterSheetUrl.replace(/^\//, ""));
      try {
        charSheetBuffer = await readFile(charSheetPath);
      } catch {
        return NextResponse.json(
          { ok: false, error: "Character sheet no encontrado. Genera uno primero con /api/paxearte." },
          { status: 400 }
        );
      }
    }

    const charSheetFile = new File([new Uint8Array(charSheetBuffer)], "character-sheet.png", {
      type: "image/png",
    });

    // 5) Generate 7 pages sequentially (return base64, no disk writes)
    const openai = new OpenAI({ apiKey });
    const pages = getPageTemplates(childName, childAge, superpower);
    const results: Array<{ pageNum: number; title: string; text: string; imageBase64: string }> = [];

    for (const page of pages) {
      console.log(`[child-story] Generando pagina ${page.pageNum}/7 para "${childName}"...`);
      const pageT0 = Date.now();

      try {
        const response = await openai.images.edit({
          model: "gpt-image-1",
          image: charSheetFile,
          prompt: `Using the character from this reference image as the main child character in the scene:\n\n${page.visualPrompt}`,
          size: "1536x1024", // Landscape for book pages
          quality: "high",
        });

        const imageData = response.data?.[0];
        if (!imageData || !imageData.b64_json) {
          console.warn(`[child-story] Pagina ${page.pageNum} sin imagen, usando placeholder`);
          results.push({
            pageNum: page.pageNum,
            title: page.title,
            text: page.textTemplate,
            imageBase64: "",
          });
          continue;
        }

        const pageTook = Date.now() - pageT0;
        console.log(`[child-story] Pagina ${page.pageNum} lista en ${pageTook}ms`);

        results.push({
          pageNum: page.pageNum,
          title: page.title,
          text: page.textTemplate,
          imageBase64: `data:image/png;base64,${imageData.b64_json}`,
        });
      } catch (pageErr) {
        const pe = pageErr as Error;
        console.error(`[child-story] Error en pagina ${page.pageNum}:`, pe.message);
        results.push({
          pageNum: page.pageNum,
          title: page.title,
          text: page.textTemplate,
          imageBase64: "",
        });
      }
    }

    const totalMs = Date.now() - tStart;
    console.log(`[child-story] Historia completa para "${childName}" en ${totalMs}ms`);

    return NextResponse.json({
      ok: true,
      childName,
      superpower,
      pages: results,
      tookMs: totalMs,
    });
  } catch (err) {
    const e = err as Error;
    console.error("[child-story] Error general:", e.message);
    return NextResponse.json(
      { ok: false, error: "Error al generar la historia. Intenta de nuevo." },
      { status: 500 }
    );
  }
}
