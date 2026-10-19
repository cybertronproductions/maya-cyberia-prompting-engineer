# Engines de imagem em 2026 — o que mudou e como escrever pra cada uma

Última verificação: 2026-10-19. Fontes no fim. Tudo que não deu pra confirmar
em página oficial está marcado **(não confirmado)**. Engine muda de nome e
de regra rápido: antes de gastar lote grande, teste 1 imagem.

Legenda das colunas do "metadata hack" (filename tipo `IMG_2985.HEIC`):
- **sim** = funciona como empurrão de estética
- **risky** = pode funcionar, pode virar texto impresso na imagem; teste antes
- **não** = vira texto impresso. Nunca usar

Regra que vale pra todas: o filename NÃO cria EXIF real. É só um empurrão de
estética, e em engine que desenha texto bem ele pode virar texto visível.
Na dúvida, use a versão em prosa (`unedited smartphone photo, HEIC compression`).

---

## Resumo rápido

| Engine | Versão atual | Negativo? | Metadata hack | Texto na imagem | Refs |
|---|---|---|---|---|---|
| Nano Banana (Google) | **2.1** `gemini-nano-banana-2.1` (GA 2026-10-06) | sem campo; descreva em positivo | risky | forte | até 14 |
| GPT Image (OpenAI) | **2.5** (`-flare` rápido, `-sunburst` precisão) | sem campo; positivo | risky | muito forte | várias (limite não confirmado) |
| Higgsfield Soul | **2.0** | **NÃO. Modo positivo-only** | **não** | fraco: desenha texto falso | Soul ID / referência |
| Seedream (ByteDance) | **5.0 Pro** (5.0 Lite desde fev/2026) | sem campo; positivo | risky | bom, multilíngue | até 14 |

---

## 1. Nano Banana 2.1 (Google)

- **Versão atual:** Nano Banana 2.1, model id `gemini-nano-banana-2.1`,
  liberado como GA em 2026-10-06. É a atualização do Nano Banana 2
  (Gemini 3.1 Flash Image) mantendo velocidade/custo de Flash.
- **Família (ids):** 2.1 = `gemini-nano-banana-2.1` · 2 = `gemini-3.1-flash-image`
  (anterior; docs recomendam 2.1 em projeto novo) · 2 Lite =
  `gemini-3.1-flash-lite-image` (mais rápido/barato, só 1K, fraco em multi-ref) ·
  legado `gemini-2.5-flash-image`. Existe um Pro (`gemini-3-pro-image`), mas **não usamos:
  tudo roda no Nano Banana 2.1**.
- **Melhor uso:** trabalho-cavalo (geração + edição conversacional), consistência
  de personagem entre turnos, texto/infográfico, edição com foto de referência
  (inserir produto real).
- **Dialeto:** prosa narrativa, frase completa. Molde oficial fotorrealista:
  `A photorealistic [shot type] of [subject] in [setting]. [Lighting]. Shot from
  [camera angle] with [lens].` Fórmula do guia de Cloud: sujeito + ação + local +
  composição + estilo.
- **Negativo:** não existe campo. O guia do Google manda descrever o que DEVE
  aparecer ("empty street", não "no cars"). Use positivo.
- **Metadata hack:** risky. Modelo lê prosa; o token de arquivo é empurrão fraco
  e não foi reconfirmado na 2.1. Prefira `unedited smartphone photo`.
- **Texto na imagem:** forte (2.1 melhorou texto e layout de infográfico). Texto
  exato entre aspas + descrição da fonte. Texto longo e crítico: GPT Image.
- **Referências:** até 14 imagens no total. Consistência de até 4 personagens e
  fidelidade de até 10 objetos (2.1/2). Diga o papel de cada
  imagem ("image 1 = identidade, image 2 = pose, image 3 = produto").
- **Detalhes de API:** saída 1K (padrão), 2K, 4K (maiúsculo: `2K`). Pensamento
  sempre ligado; níveis `minimal` / `medium` (padrão) / `high`. `seed`, `topK`,
  `temperature`, `topP` dão erro se enviados. Toda imagem leva SynthID. Pode usar
  grounding de busca web/imagem.
- **Exemplo:**
```
A photorealistic candid photo of a 27-year-old woman with a messy bun sitting in
her parked car, seatbelt on, talking to the front camera at arm's length. Overcast
windshield light from the front, soft even shadows, faint under-eye shadows,
slightly tilted framing, unedited smartphone photo look. Shot with a 26mm
front-camera lens, 9:16.
```

## 2. GPT Image 2 / 2.5 (OpenAI)

- **Versão atual:** `gpt-image-2` saiu em 2026-04-21 (API e Codex; ChatGPT
  "Images 2.0" no dia seguinte). A página oficial de geração de imagem da OpenAI
  hoje documenta **`gpt-image-2.5-flare`** (rápido, uso diário) e
  **`gpt-image-2.5-sunburst`** (precisão de edição). Data de anúncio do 2.5:
  2026-09-08 (só fonte de terceiros, não confirmado).
- **Melhor uso:** texto exato e layout (rótulo, headline, story com legenda),
  edição com referência ("keep identical"), consertar defeito de outra engine
  (ex.: texto falso que o Soul desenhou), troca de fundo, PNG transparente.
- **Dialeto:** seções estruturadas, instrução direta. Pode refinar em vários
  turnos (Responses API). Máscara é guiada por prompt, não é exata.
- **Negativo:** sem campo. Escreva em positivo; negação em prosa às vezes funciona
  mas é menos confiável que descrever o resultado.
- **Metadata hack:** risky. Como desenha texto muito bem, o filename tem mais
  chance de sair impresso. Use prosa.
- **Texto na imagem:** o melhor da lista (multilíngue, texto pequeno, UI). A
  própria OpenAI avisa que ainda pode errar posição/nitidez de texto: confira.
- **Referências:** o 2 aceitou até 16 imagens por chamada (fonte de terceiros);
  a página oficial não fixa o limite do 2.5 (não confirmado).
- **API:** tamanhos livres múltiplos de 16, proporção entre 1:3 e 3:1, lado máx.
  3840 px (acima de 2560x1440 é experimental). Qualidade `low` a `max` (2.5 tem
  `xhigh` e `max`). `background: "transparent"` com PNG/WebP.
- **Exemplo:**
```
Create a photorealistic image.
Subject: a 30-year-old woman holding a supplement bottle at kitchen-counter height.
Scene: bright apartment kitchen, morning light from the right.
Text: the bottle label reads "VITAFLOW" in bold condensed sans-serif, white on green.
Realism: unedited smartphone photo, soft contact shadow under the bottle.
Format: 4:5.
```

## 3. Higgsfield Soul 2.0

- **Versão atual:** Soul 2.0 (o Soul original continua em Image > Soul).
  Recursos de produto: presets (uma review de fev/2026 lista 20; ex.: Subtle
  Flash, Y2K Street, Digital Camera), Moodboard, Soul HEX (paleta), Soul ID
  (treina com 20 a 80 fotos de um rosto e fica preso ao modelo em que foi
  treinado) e imagem de referência.
- **Melhor uso:** avatar/UGC com estética de rede social, look de moda,
  influencer. Escolha o preset ANTES e escreva o prompt dentro da estética dele.
- **Dialeto:** frase curta + keywords de estética, tudo em **positivo**.
- **Negativo:** **NÃO.** O Soul 2.0 lê a negação como o próprio objeto. "no text"
  desenha texto. (Fonte: doutrina da casa, testada em produção; a página oficial
  de ajuda não foi encontrada para confirmar. Não confirmado em doc oficial.)
- **Metadata hack:** **não.** `IMG_2985.HEIC` e similares saem como texto
  impresso na imagem. Nunca usar no Soul 2.0.
- **Texto na imagem:** fraco e perigoso. Desenha texto falso (crachá, bordado,
  legenda) mesmo quando o prompt proíbe. Se aparecer, limpe o still escolhido
  com GPT Image (referência + "keep identical").
- **Referências:** anexar imagem de referência desativa o campo de prompt
  (modo referência OU modo prompt). Rosto fixo = Soul ID.
- **Regras de ouro no Soul:** modo positivo-only, lista de tokens proibidos, Skin
  Lock em quem tem 45+, Pose Lock em lote. Tudo em `SKILL.md` (seção Soul 2.0).
- **Exemplo (positivo-only):**
```
Vertical 9:16 single photograph of an adult woman, 32, wavy brown hair, soft
closed-mouth smile, eyes on the lens. Cream knit sweater. POSE: both arms relaxed
down at her sides, hands out of frame. Real domestic kitchen, clean uncluttered
surfaces, only one person in the scene. Chest-height medium close-up, slight
handheld tilt, off-center. Ordinary wide phone lens rendering, soft even front
light, mixed white balance, authentic still-photo look. One single adult woman,
exactly two hands with five fingers each, clean simple composition.
```

## 4. Seedream (ByteDance)

- **Versão atual:** **Seedream 5.0 Pro** (data disputada: 23/jun ou 12/ago de 2026,
  não confirmado) e **5.0 Lite** (fev/2026, raciocina antes de renderizar e usa
  busca na web). Saída 1K/2K (4K no Lite é upscale por IA). Seedance 2.5 é
  vídeo, não confunda.
- **Melhor uso:** colocar pessoa real em cena nova mantendo o rosto, integração
  de luz e fundo, infográfico e layout, edição local precisa.
- **Dialeto:** prosa narrativa em inglês. Para edição, abrir com a ação:
  `Place the man from this image into a new scene...`.
- **Negativo:** sem campo útil; descreva em positivo.
- **Metadata hack:** risky (não confirmado).
- **Texto na imagem:** bom e multilíngue (Pro).
- **Referências:** até 14 por requisição (via OpenRouter, terceiros).
  Lição de campo: **uma mudança grande por passada**; 5 refs de personagem de
  uma vez bagunçou.
- **Exemplo:**
```
Place the woman from this image into a new scene: a dim hotel hallway at night,
warm wall sconces, her jacket exactly as in the original (matte black leather).
Keep her face, hair and expression unchanged. Mid-key lighting, not pitch black.
```

---

## Fontes

- Google, modelos Nano Banana e ids: https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1
- Google, guia de geração de imagem (Gemini API): https://ai.google.dev/gemini-api/docs/image-generation
- Google Cloud, guia de prompt Nano Banana: https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana
- Lançamento do Nano Banana 2.1 (data): https://letsdatascience.com/news/google-rolls-out-nano-banana-21-image-model-c6ac3b89
- OpenAI, guia de imagem (2.5 flare/sunburst): https://developers.openai.com/api/docs/guides/image-generation
- gpt-image-2 (lançamento, terceiros): https://neurohive.io/en/news/chatgpt-images-2-0-openai-launches-image-generation-model-with-reasoning-2k-resolution-and-multilingual-text/
- GPT Image 2.5 (terceiros): https://muapi.ai/playground/gpt-image-2.5-text-to-image
- Higgsfield Soul 2.0 (terceiros): https://creatify.ai/blog/higgsfield-soul-prompts-for-product-ads
- Seedream 5.0 Pro (OpenRouter): https://openrouter.ai/bytedance-seed/seedream-5-0-pro-20260812
- Seedream 5.0 Lite: https://www.newsquawk.com/headlines/-bytedance-launches-seedream-50-lite-image-generation-model-which-is-first-with-online-search-capability

Última verificação: 2026-10-19.
