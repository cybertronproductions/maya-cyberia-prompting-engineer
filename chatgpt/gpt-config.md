# GPT Builder config: paste-ready

Everything below goes into ChatGPT > Explore GPTs > Create > Configure.

## Name

```
Maya Cyberia Prompting Engineer — by Z9
```

## Description (max 300 chars)

```
Engenheira de prompts de imagem hiper-realista. Descreve imperfeição, não beleza: câmera com física, luz com direção, prompt em inglês pronto pra Nano Banana, GPT Image, Soul 2.0 e Seedream. Saiu com cara de IA? Ela conserta. By Z9.
```

## Instructions

Paste the full content of `chatgpt/instructions.md` (limit is 8,000 characters; the file is kept under 7,800).

## Conversation starters (4, PT-BR)

```
Cria um prompt de selfie UGC: mulher de 32 anos no carro, estilo iPhone, 9:16
```
```
Quero um packshot do meu suplemento na mão de uma mulher, sem o frasco flutuar
```
```
Faz um prompt de foto paparazzi: modelo saindo de um café, lente longa 135mm
```
```
Meu prompt saiu com cara de IA. Vou colar aqui, conserta pra mim
```

## Knowledge (upload these 4 files)

- `chatgpt/knowledge/playbook.md`
- `chatgpt/knowledge/realism-cues.md`
- `chatgpt/knowledge/doctrine.md`
- `chatgpt/knowledge/engines-2026.md`

Re-upload when the repo changes. The instructions refer to these file names exactly, so do not rename them.

## Capabilities

| Capability | Setting | Why |
|---|---|---|
| Web Search | OFF | The doctrine and engine notes live in the knowledge files. Search makes answers drift and slower. Turn it ON only if you want live checks of engine updates, and then keep `engines-2026.md` as the tiebreaker. |
| Canvas | OFF | One copy-ready prompt per answer is enough. |
| Image generation | ON | Lets Maya render the prompt on request and validate the result with the fix ladder. |
| Code Interpreter & Data Analysis | OFF | Not needed. |

## Actions

None. No API, no privacy-policy URL needed.

## Category suggestion

Primary: **DALL-E** (image generation). Alternative if that category is not offered: **Productivity**.

## Sharing

Publish to **GPT Store** (public). Public GPTs require a verified builder profile (name or verified domain) in your ChatGPT settings.

## Profile picture prompt (English)

```
Square app-icon portrait of "Maya Cyberia": a young woman in her late twenties, sharp and calm expression, looking straight at the camera, short dark bob with a single thin neon-cyan streak, subtle cybernetic detail only as a thin glowing seam along one cheekbone and a small circuit-line earpiece, black technical jacket with a high collar. Photorealistic skin with natural texture, soft cyan and magenta rim light from the sides, dark navy background with faint bokeh of city neon, shallow depth of field, shot like a 85mm editorial portrait, face centered with generous margin so it survives a circular crop, no text, no logo, no watermark.
```

## Notes

- The "Instructions" field is plain text; the Markdown headers and tables inside render fine as text for the model.
- Keep the instructions file under 8,000 characters or the builder will refuse to save.
