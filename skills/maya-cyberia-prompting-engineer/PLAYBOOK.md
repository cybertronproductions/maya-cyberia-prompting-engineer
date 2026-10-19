# PLAYBOOK — referência profunda

Carregue só a seção que a tarefa pede.

> **Atenção, Soul 2.0:** os templates abaixo usam tokens de filename
> (`IMG_2985.HEIC`, `.CR2`...) e negativos. No **Higgsfield Soul 2.0** apague o token
> (vira texto impresso) e nunca escreva `no X` (modo positivo-only, veja `SKILL.md`).
> Versões atuais das engines: `references/engines-2026.md`.

---

## 1. Focal ↔ geometria do rosto

A focal define a GEOMETRIA do rosto. Errar isso = fake que negative
prompt nenhum conserta.

| Focal | Distância | Rosto | Use pra |
|-------|-----------|-------|---------|
| 24–28mm | braço esticado | leve alongamento, "cara de selfie" | selfie, UGC, vlog |
| 35mm | 1–1,5m | quase neutro, contexto visível | street, lifestyle |
| 50mm | 2m | neutro, olho humano | retrato casual |
| 85mm | 3–4m | comprimido, lisonjeiro, fundo desfocado | editorial, beauty |
| 135mm+ | longe | compressão forte | paparazzi, candid de longe |

Selfie com cara de 85mm = fake. Paparazzi com distorção de 24mm = fake.

## 2. Receitas de luz (fonte + direção + qualidade + temperatura)

```
single window light from camera left, overcast, soft wraparound shadows
bare ceiling bulb directly above, hard shadows under eyes, warm tungsten
phone screen glow from below, dark room, cold blue cast on face
golden hour sun low behind subject, rim light on hair, flare bottom-left
on-camera flash, hard frontal light, background falls to black, slight red-eye
windshield daylight from the front, overcast, soft even light   <- a mais crível pra UGC
```

Nunca: `cinematic lighting`, `perfect lighting`, `dramatic lighting` —
é pedido de beleza disfarçado.

## 3. Pele, textura e imperfeição de operador

**Pele por idade.** Poros e pelos finos favorecem sujeito até ~40 anos. Em 45+
viram veias e couro: use o Skin Lock do `SKILL.md` + luz difusa. No Soul 2.0,
nunca `natural skin`, `pores`, `visible texture`, `grain` (modo positivo-only).

Pele (até ~40 anos; escolha 2–4): `visible pores on nose and cheeks, slight oiliness
on the T-zone, faint dark circles, baby hairs at the hairline, lip lines`

Operador (escolha 2–3, nunca mais): `slightly tilted framing, subject
off-center, mild motion blur on the moving hand, focus missed to the
shoulder, cropped at the forehead`

Materiais: `fingerprints on the glass, lint on the sweater, scuffed
table edge, condensation drops on the bottle`

## 4. Biblioteca completa de hacks de câmera

Os tokens de filename são empurrão de estética, não metadata real, e **não valem
igual em todas as engines**: no **Soul 2.0 são proibidos** (saem como texto
impresso); em Nano Banana 2.1, GPT Image e Seedream são
"risky" (podem empurrar a estética ou virar texto: teste 1 imagem e prefira a
prosa equivalente). Dica pro: token (onde for seguro) + descrição do efeito
juntos = estética do dataset + controle fino. Sem token, só a descrição já
carrega a maior parte.

**RAW/câmera:** `IMG_4021.CR2`/`.CR3` (Canon) · `DSC_0231.NEF` (Nikon) ·
`DSC00412.ARW` (Sony) · `DSCF3302.RAF` (Fuji) · `L1004532.DNG` (Leica)

**Celular:** `IMG_2985.HEIC` (iPhone) · `+ flash on` · `night mode photo,
handheld` · `0.5x selfie, front ultrawide` · `PIC_20260731_142233.jpg`
(Android) · `Screenshot_20260731-214233.png`

**Dispositivos:** `GOPR0142.JPG` (GoPro) · `DJI_0412.JPG` (drone) ·
`dashcam footage still, timestamp` · `security camera still, high angle,
IR grain` · `laptop webcam frame, low resolution, backlit` ·
`trail camera photo, IR flash`

**Filme analógico:** `shot on Kodak Portra 400` (pele quente, o
queridinho) · `CineStill 800T` (noite, halation vermelho nos neons) ·
`Kodak Gold 200` (férias anos 90) · `Fuji Superia 400` (snapshot) ·
`disposable camera photo, flash` · `expired film, light leaks` ·
`instant film photo, white border` (polaroid)

**Cinema/imprensa:** `stills archive` · `film still, 35mm anamorphic,
subtle halation` · `press photograph, wire service crop` ·
`contact sheet scan`

**Objeto-imagem social:** `screenshot of an Instagram story, 23:47` ·
`FaceTime call screenshot` · `Zoom meeting screenshot` · `frame from a
vlog, YouTube compression` · `photobooth strip` · `scanned yearbook
photo, 1998` · `magazine scan, halftone dots`

## 5. Texto na imagem

- Texto sempre entre aspas: `the label reads "VITAFLOW"`
- Máx ~12 palavras por elemento; 1 elemento por vez quando der
- Tipografia como designer: `bold condensed sans-serif, white on red`
- Texto crítico → GPT Image 2.5 (ou Nano Banana 2.1/Pro). Melhor ainda: gerar
  imagem limpa e aplicar texto no editor (100% confiável)
- **Nunca confie em texto no Soul 2.0**: ele desenha texto falso (crachá,
  bordado, legenda) até quando o prompt proíbe. Limpe no GPT Image.
- Acentos (ą, ő, ç, ß): GPT Image ok; as outras erram — texto no editor

## 6. Packshot — produto que não flutua

- [ ] `soft contact shadow grounding the bottle` — sem isso, flutua
- [ ] `subtle reflection on the glossy surface` (se superfície brilha)
- [ ] `bottle the size of her palm, fingers wrapping naturally` — escala
- [ ] `label facing camera, slight curve distortion on the text`
- [ ] luz do produto = luz da cena (mesmo lado)

**Inserir produto real (2 passos):** 1) gere a cena com a mão em posição
(`hand raised, fingers curled as if holding a bottle`); 2) insira o
produto com Nano Banana 2.1 (ou Pro) / GPT Image 2.5 edit + foto de referência:
`Place the attached bottle in her hand. Match the window light, add
contact shadow, keep face and pose unchanged.` Nunca deixe a engine
inventar o rótulo de memória.

## 7. Templates DR (troque as variáveis {})

**UGC carro (o cavalo de batalha):**
```
{age}yo {ethnicity} woman, {hair}, sitting in her parked car, seatbelt
still on, talking to the front camera at arm's length, mid-sentence,
one hand gesturing, 26mm selfie distortion, windshield light from the
front, visible pores, slight under-eye shadows, slightly tilted
framing, IMG_2985.HEIC, 9:16
```

**Editorial de autoridade:**
```
editorial portrait of a {age}yo {profession}, {wardrobe}, seated at a
desk, looking off-camera mid-conversation, Canon EOS R5, 85mm f/1.4,
window light from camera left, natural skin texture, IMG_7203.CR2, 4:5
```

**Paparazzi:**
```
candid paparazzi outtake, {age}yo model leaving a café holding {prop},
caught mid-step looking away, 135mm long-lens compression, harsh midday
sun, slight motion blur on the far leg, press photograph framing,
IMG_8842.CR2, wire service crop, 3:2
```

**Story com texto (GPT Image 2.5):**
```
screenshot of an Instagram story, 9:16: casual mirror photo of a {age}yo
woman in gym clothes, bathroom lighting from above, unedited. Story text
overlay in Instagram's default white font reads "{claim, max 8 words}",
time stamp "07:42" top right, recompressed screenshot quality
```

**Talking head (vai virar vídeo):**
```
{age}yo woman in a white coat, clean modern clinic hallway, arms
relaxed, caught mid-explanation looking just off-camera, 50mm, waist-up,
ceiling panel light mixed with window daylight, visible skin texture,
9:16, first frame of a video
```
(`first frame of a video` = pose neutra, boca relaxada, pronto pra animar)

**Lifestyle noturno:**
```
{age}yo woman, oversized hoodie, sitting cross-legged on a hotel bed
scrolling her phone, warm tungsten lamp from the right, room falling
dark, slight grain in the shadows, lint on the hoodie, off-center
framing, PIC_20260731_214233.jpg, 9:16
```

## 8. Compliance de anúncio (o que derruba conta em nutra)

1. **Claim médico na imagem** — OCR das plataformas lê o texto DENTRO da
   arte. Overlay sempre em linguagem de experiência pessoal ("como eu me
   sinto às 7h"), nunca promessa clínica ("queima gordura", "cura X").
2. **Rosto de celebridade/autoridade real** sem autorização — detecção
   automática + denúncia de concorrente = conta caída. Use avatar próprio
   consistente.
3. **Before/after corporal explícito** — par de silhuetas comparadas é
   flag automática. O que passa: mesma pessoa, mesmo enquadramento,
   mudança de contexto/energia (cansada no sofá → ativa na cozinha).
