import Link from "next/link";

export const metadata = {
  title: "Pax — Oráculo",
  description: "Lectura ancestral × Pax. Maya · Astral · Arquetipo del servicio.",
};

export default function HomePage() {
  return (
    <main className="min-h-screen bg-black text-white flex flex-col items-center justify-center px-6 text-center">
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500&display=swap');
        @font-face {
          font-family: 'Didot';
          src: url('https://db.onlinewebfonts.com/c/251039e6849ad977a8bfc40b564dce89?family=Didot') format('woff2');
          font-weight: normal;
          font-style: normal;
        }
        .home-serif { font-family: 'Didot', 'GFS Didot', Georgia, serif; }
        .home-sans { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }

        @keyframes anchor-pulse {
          0%, 100% { opacity: 0.7; filter: drop-shadow(0 0 6px rgba(180,63,255,0.7)); }
          50%      { opacity: 1; filter: drop-shadow(0 0 14px rgba(180,63,255,1)); }
        }
        .anchor { animation: anchor-pulse 3s ease-in-out infinite; }

        .home-btn {
          background: linear-gradient(to bottom, rgba(255,140,70,0.10), transparent);
          box-shadow: 0 4px 30px rgba(0,0,0,0.5),
                      inset 0 1px 0 rgba(255,140,70,0.5),
                      inset 0 0 0 1px rgba(255,255,255,0.1),
                      inset 0 -1px 2px rgba(0,0,0,0.8);
          transition: box-shadow 0.3s ease;
        }
        .home-btn:hover {
          box-shadow: 0 4px 30px rgba(0,0,0,0.5),
                      0 0 24px rgba(255,120,50,0.3),
                      inset 0 1px 0 rgba(255,140,70,0.7),
                      inset 0 0 0 1px rgba(255,255,255,0.15);
        }
      `}</style>

      <div
        className="anchor mb-8"
        style={{
          width: "16px",
          height: "16px",
          background: "linear-gradient(135deg, #B43FFF, #EC4899)",
          clipPath: "polygon(50% 0%, 80% 20%, 100% 60%, 75% 100%, 25% 100%, 0% 60%, 20% 20%)",
        }}
      />

      <p
        className="home-serif italic mb-5"
        style={{
          fontSize: "12px",
          letterSpacing: "0.35em",
          color: "#B43FFF",
          opacity: 0.7,
        }}
      >
        PAX · SISTEMA · GESTO
      </p>

      <h1
        className="home-serif italic"
        style={{
          fontSize: "clamp(40px, 8vw, 80px)",
          lineHeight: 1.05,
          letterSpacing: "-0.02em",
          maxWidth: "720px",
          marginBottom: "20px",
        }}
      >
        Cuando naciste, un cristal vibró.
      </h1>

      <p
        className="home-sans font-extralight"
        style={{
          fontSize: "clamp(15px, 2vw, 18px)",
          color: "#a3a3a3",
          maxWidth: "520px",
          lineHeight: 1.7,
          marginBottom: "40px",
          letterSpacing: "0.01em",
        }}
      >
        Una lectura ancestral cruzada con el arquetipo Pax del servicio.
        Maya · astral · tu energía única.
      </p>

      <Link
        href="/oraculo"
        className="home-sans home-btn relative px-10 py-4 rounded-full backdrop-blur-md"
        style={{
          background: "rgba(255,255,255,0.03)",
          color: "#e0e0e0",
          fontSize: "15px",
          fontWeight: 300,
          letterSpacing: "0.05em",
        }}
      >
        Conocer mi cristal
      </Link>

      <Link
        href="/docs"
        className="home-sans mt-12 text-xs uppercase tracking-widest opacity-50 hover:opacity-100 transition-opacity"
        style={{ color: "#7a7a7a" }}
      >
        Docs del proyecto →
      </Link>
    </main>
  );
}
