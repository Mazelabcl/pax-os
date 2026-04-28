# Pax web app — instrucciones project-level

App de visualización + feedback para el proyecto Pax (mini-serie animada). Sin IA en backend — aldot procesa feedback localmente.

## Contexto del proyecto Pax

Lee al iniciar:
- `C:\Users\aldot\.claude\projects\C--Users-aldot--gemini-antigravity-scratch-pax-miniserie\memory\pax_project.md`
- `C:\Users\aldot\.claude\projects\C--Users-aldot--gemini-antigravity-scratch-pax-miniserie\memory\pax_webapp_decisions.md`
- `C:\Users\aldot\.claude\projects\C--Users-aldot--gemini-antigravity-scratch-pax-miniserie\memory\pipez_collaborator.md`
- `C:\Users\aldot\.gemini\antigravity\scratch\pax-miniserie\next_session_plan.md`

## Scope

App es read-only + copy-friendly. NO chat con IA, NO tools de acción, NO Agent Studio, NO form de feedback (Pipez usa WhatsApp). Lee `pax_webapp_decisions.md` sección "Scope final v1" antes de proponer features.

## Stack

Next.js 15 App Router + TypeScript + Tailwind + shadcn/ui + react-markdown. Vercel Password Protection. Sin backend de IA, sin DB, sin form.

## Idioma UI

Español. Mobile-first.

## Source of truth

`content/` en este repo. La carpeta `pax-miniserie` (afuera) es snapshot histórico.

## Cuando recibo feedback de Pipez

Llega vía WhatsApp a aldot. Aldot lo procesa localmente (Claude Code en este repo) usando los agentes Pax disponibles (`~/.claude/agents/pax-*.md`). Editar `content/*.md`, commit, push. Vercel auto-deploya.
