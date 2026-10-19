---
name: maya-cyberia-prompting-engineer
description: >
  Engenharia de prompt de imagem hiper-realista, atualizada pra 2026 — Nano Banana 2.1
  (e Pro), GPT Image 2/2.5, Higgsfield Soul 2.0 (modo positivo-only), FLUX.2, Seedream 5.0.
  Use quando pedirem prompt de imagem realista, avatar/influencer, packshot,
  criativo de anúncio, foto estilo iPhone/paparazzi, trabalho com imagem de referência
  (identidade, produto), ou "maya cyberia" / "prompt de imagem". Prompt final sempre em inglês.
---

# MAYA CYBERIA PROMPTING ENGINEER

**A regra que muda tudo: não peça beleza, descreva imperfeição.**
`8k, masterpiece, flawless, perfect skin` = cara de IA na hora.
Câmera com física + luz com direção + 2–3 defeitos de foto real = realismo.

Antes de escrever: **qual é a engine?** Engine sem negativo (Soul 2.0) muda as regras
inteiras. Versões e dialetos atuais: `references/engines-2026.md`.

## Os 7 blocos (todo prompt tem)

1. **Sujeito** — idade + etnia + 2 traços: `24yo italian-latina, dark wavy hair, bright blue eyes`
2. **Cena** — com desgaste/época: `cramped kitchen, 90s tile, magnets on the fridge`
3. **Ação candid** — nunca "posing": `caught mid-laugh reaching for a mug, eyes off-camera`
4. **Câmera** — focal coerente: selfie = 24–28mm; editorial = 85mm; paparazzi = 135mm
5. **Luz** — fonte + direção + qualidade: `window light from the left, overcast, soft shadows`
6. **Imperfeição** — 2 a 3, nunca mais: `visible pores, slight motion blur, tilted framing`
7. **Formato** — aspect + estética de captura: `9:16, unedited smartphone photo`

Blocos 5 e 6 carregam 70% do realismo. (Poros: só até ~40 anos, veja Pele madura.)

## Hacks de câmera — NÃO funcionam igual em todas as engines

Tokens de filename (`IMG_2985.HEIC`) são empurrão de estética, não metadata real.

| Engine | Filename/metadata token |
|---|---|
| **Soul 2.0** | **PROIBIDO.** Sai como texto impresso na imagem |
| Nano Banana, GPT Image, FLUX.2, Seedream | risky: pode empurrar a estética, pode virar texto (GPT Image desenha texto bem, risco maior). Teste 1 imagem; prefira a prosa equivalente |

Versão em prosa (segura em qualquer engine): `unedited smartphone photo, HEIC
compression, computational HDR look`.

| Look | Token ou prosa |
|------|----------------|
| iPhone real | `unedited smartphone photo` (+ `IMG_2985.HEIC` só onde não for Soul; com flash: `+ flash on`) |
| RAW Canon / Nikon / Sony | `Canon EOS R5, 85mm f/1.4` (+ `IMG_9854.CR2` onde não for Soul) |
| Fuji film simulation | `Fujifilm film-simulation colors` (+ `DSCF3302.RAF`) |
| Cinema / still de filme | `film still, 35mm anamorphic, subtle halation` |
| Foto de imprensa | `press photograph, wire service crop` |
| Filme analógico | `shot on Kodak Portra 400` (pele) / `CineStill 800T` (noite neon) |
| Festa crua | `disposable camera photo, flash` |
| Print social | `screenshot of an Instagram story, 23:47` (cuidado: no Soul vira UI) |
| Paparazzi | `long-lens compression, 135mm, press photograph` |

Lista completa (drone, CCTV, dashcam, webcam, polaroid, magazine scan...) no `PLAYBOOK.md`.

## Qual engine (out/2026)

| Tarefa | Engine |
|--------|--------|
| Avatar/UGC com estética de rede social | Higgsfield Soul 2.0 — preset ANTES, prompt positivo-only |
| Texto exato na imagem (rótulo, headline) | GPT Image 2.5 (`flare` rápido / `sunburst` precisão), texto entre aspas, ≤12 palavras |
| Editar imagem / inserir produto real / consistência multi-turno | Nano Banana 2.1 (`gemini-nano-banana-2.1`); peça premium → Nano Banana Pro (`gemini-3-pro-image`) |
| Manter o rosto da referência em cena nova (só com autorização da pessoa) | Seedream 5.0 Pro ou Nano Banana 2.1 |
| Lote barato / cor exata / prompt JSON | FLUX.2 (`flex` pra tipografia) |
| Consertar texto falso desenhado por outra engine | GPT Image com referência + `keep identical` |

Imagen 4 foi aposentado na API do Google: migre pra Nano Banana 2.1.
Dialeto: Nano/Seedream = prosa narrativa · GPT Image = seções estruturadas ·
Soul = frase + keywords positivas · FLUX = descritivo ou JSON.

## Soul 2.0 — Modo Positivo-Only (obrigatório)

O Soul 2.0 não entende negativo: lê "no X" como X. Padrão 9:16. Estas regras valem
também pra qualquer engine marcada como sem negativo.

**1. Tokens proibidos (renderizam artefato visível):**
`no text, text, caption, subtitle, legend, watermark, logo, no phone frame, frame,
app interface, UI, overlay, player, views, metadata, IMG_0000.HEIC, EXIF, video still,
mid-sentence, talking to the camera, speaking`

Troque: `video still` → `single photograph` · `UGC testimonial` → `single photograph
of an adult woman` + `unedited home-video feel` · `mid-sentence` → `soft closed-mouth
smile, lips together, eyes on the lens`.

**2. Tokens de pele proibidos** (viram veia, couro, envelhecimento; pior em 45+):
`heavy, heavy breasts, natural skin, natural skin pores, mature skin texture, real age
detail, visible texture, fine hairs, grain, sensor noise, oversharpening, etched wrinkles`.
Busto grande: `big bust with deep cleavage`, nunca `heavy`.

**3. Restrições viram afirmação positiva:** `one single adult woman, exactly two hands
with five fingers each, clean simple composition`. Nomear o proibido é pedir o proibido.

**4. Skin Lock — obrigatório em sujeito 45+:**
`Smooth even skin tone across the face, neck and chest, soft clear skin surface, uniform
complexion, clean retouched photographic finish, soft diffused front light wrapping the
chest, gentle shadow transitions.` Luz dura de abajur expõe veias: use luz suave frontal.

**5. Pose Lock (lote):** nunca `hand on chest` / `touching collarbone` (o modelo repete
em todo o lote). Declare os dois braços e as duas mãos e gire uma pose por variante:
A braços relaxados, mãos fora do quadro · B um braço estendido, o outro relaxado ·
C uma mão ajeitando o cabelo · D mão no quadril, peso em uma perna · E duas mãos numa
caneca · F um braço com o telefone baixo.

**6. Ordem:** `Vertical 9:16 single photograph of an adult woman, <idade>, <papel>` →
rosto/cabelo (+ Skin Lock se 45+) → roupa → `POSE: <A–F>` → cena doméstica limpa, só uma
pessoa → enquadramento (altura do peito, leve tilt) → lente de celular grande-angular →
luz suave, balanço de branco misto → fecho de restrição positiva.

**7. Texto falso aparece mesmo assim** (crachá, bordado)? Pare de reescrever. Escolha o
still e limpe com GPT Image (referência + `keep everything identical`).

## Pele madura (45+) em qualquer engine

Poros e pelos finos favorecem só quem tem menos de ~40. Em 45+ trocam por Skin Lock +
luz difusa. Padrão limpo e natural: grão, ruído e rugas esculpidas não são realismo
automático. Mantenha a idade e as linhas normais de expressão, sem suavizar a ponto de
rejuvenescer.

## Identidade (trabalho com referência)

- Rotule cada imagem: identidade, alvo de edição, cena, produto ou estilo.
- **Rosto vem só da referência de identidade.** Referência de roupa/estilo nunca empresta
  rosto, olho, idade ou proporção corporal.
- Descreva marcos estáveis (olho, sobrancelha, nariz, lábios, maçã, mandíbula, linha do
  cabelo, assimetria característica); não dependa só de "parece a fulana".
- Em edição, repita o que pode mudar e o que fica fixo (`keep face, pose, clothing identical`).
- Referência com pele danificada: não grite "no grain". Troque a estratégia (referência
  limpa = rosto e pele; a danificada = só layout, pose e roupa).
- Aprove o still ANTES de animar; still reprovado não semeia vídeo pago.

## Saiu com cara de IA? (pare no 1º que resolver)

1. Palavra de elogio no prompt? → deleta todas
2. Luz sem fonte/direção? → luz física (`bare ceiling bulb`, não "cinematic lighting")
3. Sujeito posando? → ação interrompida, olhar fora do frame
4. Liso demais? → +2 imperfeições específicas (45+: Skin Lock, não mais poros)
5. Rosto estranho? → focal errada pro enquadramento (bloco 4)
6. Veio texto/UI inesperado? → você usou token proibido (filename, "no text"); tire
7. Nada resolveu? → engine errada pra tarefa

## Ferramentas

- `PLAYBOOK.md` — focal↔rosto, receitas de luz, biblioteca de hacks, templates DR,
  packshot, compliance de anúncio. **Só carregue quando a tarefa pedir.**
- `references/engines-2026.md` — por engine: versão, ids, dialeto, negativo, hack de
  metadata, texto, referências, exemplo. **Leia antes de escolher engine.**
- `references/lessons.md` — lições de campo ("regra · por quê").
- `references/realism-cues.md` — biblioteca de cues por lane.
- `scripts/forge.py` — gera o prompt pronto (7 receitas × 4 dialetos):
  `python3 scripts/forge.py --recipe ugc-selfie --engine soul`
  Lote: `--json scripts/briefs.example.json --out prompts.txt` · Ver tudo: `--list`

## Regras fixas

- Prompt final sempre em inglês
- Saída pra engine sem negativo: só o prompt, sem bloco `Negative prompt`
- Nunca pessoa real identificável sem autorização
- Criativo de anúncio: zero claim médico no texto da imagem (OCR das plataformas lê
  tudo) — detalhes no PLAYBOOK.md
- Não afirme que um token é comando secreto garantido: é empurrão de estética
