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
| FLUX (BFL) | **FLUX.2** (pro/flex/dev/max/klein); FLUX 3 anunciado | não (descreva o que quer) | risky | bom (flex = tipografia) | até ~10 |
| Seedream (ByteDance) | **5.0 Pro** (5.0 Lite desde fev/2026) | sem campo; positivo | risky | bom, multilíngue | até 14 |
| Midjourney | **V8.1/V8.2** | `--no` (suporte em V8.x: não confirmado) | risky | melhorou (texto entre aspas) | `--oref` só V7 (não confirmado em V8) |
| Imagen (Google) | **aposentado** (Imagen 4 desligado na API) | — | — | — | migrar pra Nano Banana |

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

## 4. FLUX.2 (Black Forest Labs)

- **Versão atual:** FLUX.2 em variantes `[pro]` (produção), `[flex]` (controle
  máximo de parâmetros e tipografia), `[dev]` (open weights, experimento), `[max]`
  e `klein` (leve). **FLUX 3** foi anunciado em 2026-07-23 (multimodal), mas só
  Video e Action estavam em acesso antecipado; **FLUX 3 Image sem disponibilidade
  confirmada** em outubro (não confirmado).
- **Melhor uso:** volume em lote, edição multi-referência, controle de cor exata
  (hex), prompt estruturado.
- **Dialeto:** descritivo, em ordem (sujeito primeiro). Aceita **prompt em JSON**
  (sujeitos, composição, luz, câmera) e cor por hex (`color #E4572E`).
- **Negativo:** fontes de terceiros dizem que o FLUX não usa negative prompt;
  descreva o que quer (não confirmado em doc BFL).
- **Metadata hack:** risky (herança do FLUX.1/SD, não reconfirmado no FLUX.2).
- **Texto na imagem:** bom; `[flex]` é a indicada pra tipografia. Acento e
  caractere raro ainda falham: aplique no editor.
- **Referências:** até ~10 imagens (edição, estilo, identidade; fonte de terceiros).
- **Exemplo:**
```
Candid 35mm street photo of a 28-year-old woman in a denim jacket walking toward
the camera on a downtown crosswalk, looking at something off-frame left. Open
shade, cool soft light, sunlit storefronts behind, pedestrians motion-blurred.
Slightly rushed framing, documentary look. 3:2.
```

## 5. Seedream (ByteDance)

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

## 6. Midjourney (V8.x)

- **Versão atual:** V8.0 Alpha em 2026-03-17; **V8.1 em 2026-04-30** (docs oficiais:
  mais rápido, 2K HD nativo); **V8.2 padrão desde 2026-07-24** (só fonte de
  terceiros, não confirmado em docs oficiais). Sem `--v`, o prompt roda na padrão.
  V8.1 exige perfil de personalização global liberado.
- **Melhor uso:** estética, mood, arte e editorial. Pior em instrução precisa e
  edição do que Nano Banana/GPT Image.
- **Dialeto:** sujeito primeiro, frase natural curta + cauda de parâmetros
  (`--ar 9:16 --v 8.1`).
- **Negativo:** `--no` existe historicamente; suporte na V8.x tem fontes em
  conflito (não confirmado). Prefira positivo.
- **Metadata hack:** risky (não confirmado).
- **Texto na imagem:** melhorou; texto entre aspas rende mais certo. Ainda perde
  pra GPT Image e Nano Banana em texto/edição segundo reviews de terceiros.
- **Referências:** `--sref` (estilo) ok; `--oref` (omni reference) é V7; a versão V8
  está em treino segundo fontes de terceiros (não confirmado).
- **Nota da casa:** em 2026-07 o Midjourney foi deixado FORA do fluxo padrão
  desta skill. Mantido aqui só como referência.
- **Exemplo:**
```
candid portrait of a woman laughing at a diner counter at night, neon sign
reflected in the window, shot on CineStill 800T, shallow depth of field
--ar 4:5 --v 8.1
```

## 7. Imagen (Google)

- **Status:** a página oficial de geração de imagem da Gemini API já lista Imagen
  como "legacy (shut down)". Fontes de terceiros dizem que os endpoints Imagen 4
  (`imagen-4.0-generate-001`, `-ultra-`, `-fast-`) saíram do ar na Gemini API em
  2026-08-17 (data não confirmada pelo Google); a doc do Firebase manda migrar
  pra Nano Banana. Tutorial de setembro ainda os descreve como ativos no Vertex:
  fontes em conflito, **(não confirmado)** se ainda existe em algum canal.
- **O que fazer:** projeto novo = Nano Banana 2.1. Prompt de Imagen migra quase
  direto (prosa), mas reteste: a saída muda.
- Não há versão "Imagen 5" confirmada.

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
- FLUX.2 (Together): https://docs.together.ai/docs/quickstart-flux-2
- FLUX.2 (Prodia): https://docs.prodia.com/models/flux-2/
- FLUX 3: https://datanorth.ai/news/black-forest-labs-releases-flux-3
- Seedream 5.0 Pro (OpenRouter): https://openrouter.ai/bytedance-seed/seedream-5-0-pro-20260812
- Seedream 5.0 Lite: https://www.newsquawk.com/headlines/-bytedance-launches-seedream-50-lite-image-generation-model-which-is-first-with-online-search-capability
- Midjourney, modelos: https://docs.midjourney.com/docs/models
- Midjourney V8.1 review: https://vidmuse.ai/blog/midjourney-v8-1-review
- Imagen, migração Firebase: https://firebase.google.com/docs/ai-logic/imagen-models-migration
- Imagen 4, fim da API: https://unifically.com/blogs/imagen-4-api-shutdown

Última verificação: 2026-10-19.
