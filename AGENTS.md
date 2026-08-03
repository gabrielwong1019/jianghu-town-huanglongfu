# OPC V0.1 Bilingual Competition Rules

This file governs only the OPC competition bilingual copy of **Jianghu Town:
Huanglongfu V0.1**. It is not a rule set for future V0.2 or long-term
development.

## Source and Rule Priority

Apply sources in this order:

1. The user's approved Round 1 instructions and this `AGENTS.md`.
2. The current runnable V0.1 source under `game/`, for actual plot, variables,
   choices, and reachable flow.
3. The Google Doc [《江湖小镇之凰龙府》游戏初始设定](https://docs.google.com/document/d/1HzkeoPlSS20hTymtIr9X9QNOrdqEIpzb6UjnTkubdx8/edit?tab=t.0), for worldbuilding, character identity, relationships, voice, and terminology.
4. Other project documents.

## Conflict Handling

- If the Google Doc conflicts with runnable V0.1 code, do not bring future
  settings into code. Translate only content that already exists and runs in
  V0.1.
- The Google Doc may guide English terminology and character voice, but must
  not add characters, plot, systems, or V0.2 features.
- `开庵镇` and `雷云峰` are canonical. Correct the deprecated runtime spellings
  `开安镇` and `雷云锋` when encountered; never alter image text.
- Old character data in source may clarify a line's context, but must not
  override formal setting when it conflicts with the Google Doc.

## Localization Principles

- **UI:** translate standard interface copy accurately, naturally, and concisely.
- **Canonical/Semantic:** preserve a stable, shared translation for canonical
  setting facts and terms. In this project, “ontology” means the semantic or
  world-concept system; a stable ID or term key is one node, not a complete
  ontology.
- **Narrative:** use literary localization rather than mechanical word-for-word
  translation. Preserve plot facts, relationships, information, emotion,
  humor, wuxia identity, and character voice without adding modern memes,
  promises, or plot.
- Do not code-ify whole dialogue lines or turn character speech into mechanical
  templates.
- Future Traditional Chinese and Vietnamese must localize from authoritative
  Simplified Chinese source text, not secondarily from English.

## Round 1 Scope

- Deliver only the English Round 1 sample; do not translate the full chapter.
- Do not introduce V0.2 content or change images, music, video, plot facts,
  gameplay, choices, or variables.
- Do not expose incomplete languages in the game.
- Do not create `deploy/web` or perform any Cloudflare action.

## Git and Delivery Limits

- Work only on `feature/bilingual`; never modify or switch `main`.
- Do not commit, push, publish a branch, or create a pull request.
