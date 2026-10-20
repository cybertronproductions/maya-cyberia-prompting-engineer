# Biblioteca de prompts (text-to-image)

Prompts de imagem que rodaram em produção, organizados por caso de uso. Complementa
`exemplos-aprovados.md` (que traz os moldes de character sheet 3x3, inserção de produto
detalhada, estilos animados e cenário vazio) e os templates do `PLAYBOOK.md`: aqui entram
os casos que ainda não estavam lá. Prompt em inglês, literal; explicação em português.
Troque só o que está em `[colchetes]`.

**Status.** APROVADO = escolhido pelo diretor/cliente · USADO = entrou em peça ou episódio
entregue · MOLDE = estrutura validada, remontada com blocos aprovados (sem imagem aprovada
registrada para esse texto exato).

**Engines.** Só as quatro: Nano Banana 2.1, GPT Image (ChatGPT), Higgsfield Soul 2.0,
Seedream 5.0. Soul 2.0 é positivo-only: nenhum "no ..." no prompt.

**Trava anti-grão (GPT Image).** Todo prompt de GPT Image termina com:
`Clean natural photographic surface, low ISO, smooth tonal transitions, natural skin. No added film grain, sensor noise, crackle or oversharpening.`

---

## 1. UGC selfie

### 1.1 · Soul 2.0 · selfie de base, sem produto (futuro avatar) · MOLDE
Objetivo: base de pessoa para depois inserir produto ou animar. Adaptado do template de
lote que rodou em centenas de bases, convertido para positivo-only.
```
IMG_2985.HEIC, realistic iPhone front-camera portrait of a 41-year-old woman with a soft brown bob and a few flyaway hairs, average build, wearing a grey crewneck sweatshirt, standing in her real kitchen with a window on her left, relaxed shoulders, genuine slight smile, looking directly into the lens. Camera at natural arm length, front-camera POV, relaxed handheld framing. Her hands rest open near her chest in a loose C-shaped grip, empty and natural. Natural pores, subtle facial asymmetry, tiny flyaway hairs, slight front-camera distortion, compressed smartphone detail, believable window shadows, natural room light. 28mm equivalent, vertical 9:16, ordinary phone photo, even natural skin.
```
Por que funciona
- Abre com nome de arquivo de câmera (`IMG_2985.HEIC`) e `front-camera POV`, em vez de "RAW iPhone photo", que chama interface.
- Não descreve onde o celular está (celular descrito aparece no quadro); só o ponto de vista.
- Mão "vazia em C" já prepara o grip para a inserção do produto depois.

### 1.2 · Soul 2.0 · UGC com pet, centro seguro de 4:5 · MOLDE
Objetivo: still de depoimento com cachorro, rosto e pet inteiros no recorte do feed.
```
Candid vertical smartphone photo of a 47-year-old man with short grey-brown hair and a trimmed beard, wearing a faded green flannel shirt, sitting on a living-room sofa with his golden retriever resting its head on his knee, both centered in the frame, front-facing phone-camera POV, warm relieved expression, looking toward the lens. Late-afternoon window light mixed with one warm table lamp, uneven automatic exposure, slightly irregular window shadows on the wall, mild perspective distortion from a wide phone lens. Real lived-in room, throw blanket slightly crumpled, natural skin texture.
```
Por que funciona
- Casting específico (idade, cabelo, roupa gasta) em vez de "pessoa bonita".
- Luz mista com causa física (janela + abajur) e dois defeitos só: exposição irregular e distorção de lente.
- Rosto e pet no centro do quadro: sobrevive ao crop 4:5.

### 1.3 · GPT Image · selfie no carro, fala no meio da frase · MOLDE
Objetivo: o "cavalo de batalha" do UGC, a pessoa conversando com a câmera no carro.
```
Single unedited vertical smartphone photo, one continuous camera frame. A 38-year-old Latina woman with dark wavy hair in a loose clip, sitting in her parked car with the seatbelt still on, talking to the front camera at arm's length, mid-sentence, one hand gesturing, 26mm selfie distortion, windshield daylight from the front, visible pores, slight under-eye shadows, slightly tilted framing, IMG_2985.HEIC, 9:16. Shot on iPhone 14 Pro front camera, natural HDR disabled, realistic phone photo, not cinematic, not beauty retouched. Clean natural photographic surface, low ISO, smooth tonal transitions, natural skin. No added film grain, sensor noise, crackle or oversharpening.
```
Por que funciona
- Primeira frase fecha o formato: foto única, sem print, sem colagem.
- Ação congelada (meio da frase, mão em gesto) em vez de pose; cinto de segurança dá contexto físico.
- Ficha de câmera com "not cinematic, not retouched" empurra para foto de celular, e a trava fecha o grão.

### 1.4 · Seedream 5.0 · UGC em quarto de hotel, luz quente · MOLDE
Objetivo: cena noturna casual, pessoa no celular, sem cara de estúdio.
```
Candid vertical photo of a 29-year-old woman in an oversized hoodie sitting cross-legged on a hotel bed, looking down at her phone with a soft half-smile, warm tungsten lamp from the right, the room falling into darkness behind her, lint on the hoodie, rumpled bed linen, slightly off-center framing, mild shadow noise only in the darkest corners, handheld photo from the foot of the bed, PIC_20260731_214233.jpg, 9:16, not a fashion editorial, natural skin tone.
```
Por que funciona
- Uma fonte de luz com direção e temperatura (tungstênio da direita) e queda de exposição no fundo.
- Imperfeições com causa: fiapo no tecido, cama amassada, ruído só na sombra.
- Nome de arquivo de câmera empurra para foto de rolo, não de banco de imagem.

---

## 2. Avatar consistente e continuidade de elenco

### 2.1 · Nano Banana 2.1 · duas referências, papéis separados (rosto + elenco) · USADO
Objetivo: manter a protagonista e uma coadjuvante entre planos, numa época diferente. A
ref 1 manda no rosto da protagonista; a ref 2 manda na coadjuvante e no figurino das duas.
```
One photorealistic 16:9 landscape cinematic historical first frame, a coastal village in Java, 1883. Reference 1 is authoritative for the heroine's exact adult face: green eyes, burgundy hair and bangs, facial landmarks, natural age. Reference 2 is authoritative for the SAME adult Javanese woman and both women's wardrobe and props: the heroine wears a modest charcoal long-sleeved linen blouse, dark practical skirt and brown crossbody satchel; the companion wears a cream kebaya, indigo patterned sarong and low black bun, carrying a small wooden medicine box. Preserve identity and period wardrobe exactly. Sharp readable faces, clean natural skin, no synthetic grain, restrained cinema lighting. Landscape visual storytelling; no visible camera or phone, no interface, subtitles, text, logos, watermark, modern buildings or vehicles. Earlier that morning in a village open-air market, side-on medium two-shot. The heroine at left holds the free end of a coil of coarse hemp rope while the companion at right gathers the rope with her medicine box under her arm. Woven baskets and cotton hanging from a timber stall create foreground depth. A few sparse ash specks on one cloth; the light has become overcast. No destroyed buildings. Both faces recognizable and hands physically coherent.
```
Por que funciona
- "Authoritative for" dá a cada referência um papel e evita misturar rostos.
- Figurino e props descritos por item e repetidos em todo plano: o pior vilão de continuidade é a roupa que muda.
- Estado da cena explícito (cinzas esparsas, luz nublada) para a linha do tempo da história bater.

### 2.2 · Nano Banana 2.1 · continuidade de objeto removido (o colar que sumiu) · USADO
Objetivo: plano posterior à perda de um adereço; o prompt grita o que NÃO existe mais.
```
One photorealistic 16:9 landscape cinematic historical first frame, Java near the Sunda Strait, 1883. Reference 1 is authoritative for the heroine's exact adult face. Reference 2 is authoritative for her companion and both women's wardrobe and props. Preserve identity and period wardrobe exactly. Sharp readable faces, clean natural skin, no synthetic grain, restrained cinema lighting. Both women have reached a high muddy ledge, moving away from its edge. Waist-up medium shot, the exhausted heroine in the foreground left and the companion on the right, crouched with an intact wooden medicine box. The heroine has NO necklace, NO pendant, NO chain: she gave it up in the previous scene. All other costume and facial identity unchanged. Wind blows her burgundy hair, dust on the clothes, dark grey sky. Far below in the background, a massive surge of foamy sea water covers the coastal plain among palms. No bodies, no graphic injuries. A protective human moment after a frightening escape.
```
Por que funciona
- Estado de continuidade dito em maiúsculas pontuais (`NO necklace`) para o adereço não reaparecer.
- Mantém "tudo o mais inalterado" e muda só o estado; o estado anterior vem da ficha de cena.
- Perigo ao fundo, momento humano em primeiro plano: o rosto lidera a leitura.

### 2.3 · Nano Banana 2.1 · elenco animado, ângulos do mesmo cenário com refs · USADO
Objetivo: plano de ação com os dois personagens já travados nas referências (master do casal + ângulo do cenário).
```
HIM walking in through the kitchen doorway toward camera, relaxed; HER in the foreground with her back to camera, unpacking a grocery bag on the counter. No jewelry box or card visible. HER: a woman in her early 30s, light brown hair in a ponytail, plain red T-shirt, blue jeans. HIM: a man in his early 30s, short beard, plain light blue golf shirt, blue jeans, brown cap. Same people, clothes and kitchen as the reference images, daytime. Stylized 3D animated feature-film look, high-end CG animation studio render quality, rounded appealing shapes, big easy-to-read faces, soft subsurface skin, warm soft daytime light. Vertical 9:16. No text, no captions, no logos anywhere.
```
Por que funciona
- A descrição fixa (roupa de cada um) é repetida em TODO plano, mesmo com referência anexada.
- `HIM`/`HER` + posição no quadro (porta, bancada) dão blocking claro; objeto que não deve aparecer é dito.
- O bloco de estilo é idêntico entre os planos: um preset por lote.

---

## 3. Character sheet

### 3.1 · Nano Banana 2.1 · sheet de vilã (close + 3 vistas) · USADO
Objetivo: personagem antagonista de drama, fundo branco, mesma pessoa em todas as vistas.
```
Character reference sheet, left side a front-face close-up, right side three equal-height full-body views side by side showing front, 90-degree side, and back; same character in all views, full body in frame, neutral A-pose, tops of heads and soles of feet aligned; woman around forty, tall and slim, upright posture with chin slightly raised; angular face, sharp cheekbones, thin arched brows, a narrow cool gaze, lips pressed in a faint smirk; sleek platinum-blonde bob; fitted white linen dress, oversized tortoiseshell sunglasses pushed up on the head, gold hoop earrings; the face, hairstyle, and clothing of the close-up and the three views are completely identical; pure white background, soft even lighting, cinematic quality
```
Por que funciona
- Layout descrito com precisão (close à esquerda, três vistas à direita, alturas iguais).
- Personalidade vira traço físico (queixo erguido, sorriso de canto, olhar estreito).
- Frase "completamente idênticos" trava rosto, cabelo e roupa entre painéis.

### 3.2 · Nano Banana 2.1 · sheet de mentora (mesmo molde, outro arquétipo) · USADO
```
Character reference sheet, left side a front-face close-up, right side three equal-height full-body views side by side showing front, 90-degree side, and back; same character in all views, full body in frame, neutral A-pose, tops of heads and soles of feet aligned; woman in her late thirties, slim toned build, relaxed open stance; round face, bright hazel eyes, easy wide smile, light smile lines; curly dark-brown hair to the shoulders; rust-orange fitted sweater, black leggings, white sneakers, silver smartwatch; the face, hairstyle, and clothing of the close-up and the three views are completely identical; pure white background, soft even lighting, cinematic quality
```
Por que funciona
- Contraste de silhueta e cor com a vilã (aberta/quente × rígida/fria): elenco legível mesmo em miniatura.
- Postura e sorriso descritos, não só roupa.

### 3.3 · Nano Banana 2.1 · master de casal animado no cenário real · USADO
Objetivo: referência única de dois personagens no cenário onde a cena acontece.
```
Character reference of a married couple standing side by side in a bright suburban kitchen in the daytime: light wood cabinets, white counters, a window with blinds over the sink, a stove with a cupboard beside it, three brown paper grocery bags and some groceries on the counter, full body, both facing camera, friendly. HER: a woman in her early 30s, light brown hair in a ponytail, plain red T-shirt, blue jeans. HIM: a man in his early 30s, short beard, plain light blue golf shirt, blue jeans, brown cap. Eye-level, steady camera. Stylized 3D animated feature-film look, high-end CG animation studio render quality, rounded appealing shapes, big easy-to-read faces, soft subsurface skin, warm soft daytime light. Vertical 9:16. No text, no captions, no logos anywhere.
```
Por que funciona
- Elenco e cenário na mesma referência: o modelo aprende os dois ao mesmo tempo.
- Roupas lisas e cores primárias (vermelho, azul, bege): fáceis de repetir sem deriva.

### 3.4 · Nano Banana 2.1 · plano vazio em ângulo reverso (mesmo cenário) · USADO
Objetivo: variações do mesmo cenário para continuidade de câmera, sem personagens.
```
Same kitchen, reverse angle: camera from the doorway side looking at the counter with the grocery bags, the window with blinds and the stove and cupboard behind, nobody in frame. A bright suburban kitchen in the daytime: light wood cabinets, white counters, a window with blinds over the sink, a stove with a cupboard beside it, three brown paper grocery bags and some groceries on the counter. Eye-level. Stylized 3D animated feature-film look, high-end CG animation studio render quality, rounded appealing shapes, big easy-to-read faces, soft subsurface skin, warm soft daytime light. Vertical 9:16. No text, no captions, no logos anywhere.
```
Por que funciona
- `Same kitchen` + a lista fixa de objetos repetida = o modelo reconstrói o mesmo espaço em outro ângulo.
- `nobody in frame` e posição da câmera explícita (lado da porta).

---

## 4. Packshot e produto na mão

### 4.1 · Nano Banana 2.1 / GPT Image (edit) · inserção rápida do frasco · APROVADO
Objetivo: pôr o frasco real na mão de uma base aprovada. Imagem 1 = base, imagem 2 = frasco.
```
Make the woman holding the bottle, she is showing it to the viewer, keep the text perfect, match the shadows of the bottle into the scene seamlessly, remove any text/UI from the first image reference. Keep only the person holding the bottle with the bottle text visible. The size of the bottle is medium. Use the exact product from IMAGE 2.
```
Por que funciona
- Curto: a engine de edição preserva rosto e cena sozinha; prompt longo só entra se este falhar.
- `Use the exact product from IMAGE 2` impede a engine de inventar o rótulo.
- Pede explicitamente a limpeza de texto/interface herdada da base.
- GPT Image: acrescente a trava anti-grão no fim.

### 4.2 · Nano Banana 2.1 / GPT Image (edit) · frasco tirado de vídeo com outra mão · MOLDE
Objetivo: quando a referência do produto é um recorte onde outra pessoa segura o frasco.
```
Make the man holding the bottle, he is showing it to the viewer, normal size bottle, with the right hand, don't change the face, keep the rest the same. Use the exact supplement bottle from IMAGE 2 and ignore the hand, face, body and background in IMAGE 2.
```
Por que funciona
- `ignore the hand, face, body and background` corta o vazamento de identidade da ref do produto.
- Mão especificada (direita) evita grip aleatório.

### 4.3 · Soul 2.0 · base com mesa livre para o frasco entrar depois · MOLDE
Objetivo: pessoa com mesa limpa visível no quadro; o produto é inserido numa segunda etapa.
```
IMG_2985.HEIC, realistic iPhone front-camera portrait of a 52-year-old man with short salt-and-pepper hair, wearing a navy polo, sitting at a wooden kitchen table in a real home with soft morning window light. A clean empty section of the wooden tabletop is clearly visible in the lower left foreground with open space for an object. Camera at natural arm length, relaxed handheld framing, authentic calm expression, looking directly into the lens. Natural skin texture, subtle asymmetry, slight front-camera distortion, believable shadows, ordinary room light, vertical 9:16, even natural skin.
```
Por que funciona
- Reserva espaço físico para o produto dentro do quadro (mesa visível, longe da borda).
- Nada de frasco, rótulo ou texto na base: o produto real entra depois, nunca inventado.

### 4.4 · GPT Image · frasco em contexto, sem pedestal · MOLDE
Objetivo: still de produto que parece parte da cena, ancorado na ação.
```
Use the attached official product reference as immutable product DNA: preserve the exact bottle silhouette, cap, material, colorway and label layout; do not invent or alter the branding. Vertical 9:16 editorial still. Scene: a lived-in stone kitchen worktop with whole ingredients, a cutting board and an open notebook turned away from the camera; the supplement bottle is placed naturally next to a used teaspoon. First read: the preparation. Second read: the bottle as a clue. Third read: ingredient texture and a handwritten page that stays unreadable. Contrast: polished bottle surface against raw ingredients. 85mm editorial macro, raking side window light. Knife marks, powder dust, stone pores, soft contact shadow grounding the bottle. Clean natural photographic surface, low ISO, smooth tonal transitions, natural skin. No added film grain, sensor noise, crackle or oversharpening.
```
Por que funciona
- Referência oficial como "DNA imutável": a engine copia o rótulo em vez de recriá-lo.
- Três leituras (ação, produto, textura) e um contraste dão hierarquia visual.
- Contact shadow aterra o frasco, que não flutua.

---

## 5. Lifestyle (produto dentro da vida real)

Todos abaixo: GPT Image, vertical, uma referência oficial do frasco anexada, usado em lote
real de 200 imagens. Prefixo comum (cole antes da cena):
`Use the attached official product reference as immutable product DNA: preserve the exact jar silhouette, lid geometry, material, colorway and label layout. Do not invent or alter branding. Generate a vertical 9:16 editorial still for a DTC creative.`
Sufixo comum: `No new text, no watermark, no fake certification, no extra product variants, no distorted hands or labels.` + a trava anti-grão.

### 5.1 · Cozinha de manhã, preparo real · USADO
```
Scene: early morning kitchen counter, open ingredient drawer, a pair of adult hands measuring a real ingredient beside the supplement jar; steam from coffee crosses the foreground. First read: the practical ritual in motion. Second: the jar beside the action. Third: spoon dust, counter scratches and window condensation. Contrast: warm sunrise against cool stone. Camera: low 35mm documentary angle. Lighting: hard morning window plus soft kitchen bounce. Physical realism: fingerprints on the lid, worn wood grain, small spills, fabric sleeve folds.
```
Por que funciona
- Abre pela ação e pelo ritual, não pelo objeto.
- Contraste de temperatura (nascer do sol quente × pedra fria) cria dimensão sem efeito.
- Lista de imperfeições com causa física (digital, risco, vapor).

### 5.2 · Mesa à noite, tensão limpa · USADO
```
Scene: dark dining table after rain, the supplement jar partly concealed by a folded linen napkin and a glass of water; an adult hand enters only at the edge to reach for it. First read: ritual and anticipation. Second: the jar. Third: rain reflections on the tabletop. Contrast: intimate amber practical light against blue window rain. Camera: 50mm close three-quarter. Lighting: one warm lamp and cold ambient. Physical realism: wet window, glass rings, crumpled linen, subtle crumbs.
```
Por que funciona
- Produto parcialmente escondido cria curiosidade; a mão entra só na borda.
- Duas luzes com papéis: lâmpada quente (íntima) e ambiente frio (chuva).

### 5.3 · Despensa, gesto de escolha · USADO
```
Scene: an adult hand pulls the supplement jar from a real pantry shelf between dry ingredients and ceramic bowls. First read: hand and gesture. Second: the jar. Third: the depth and material order of the pantry. Contrast: domestic calm against sharp direct flash. Camera: 28mm close handheld documentary framing. Lighting: direct flash with warm shelf ambient. Physical realism: paper labels blurred and unreadable, shelf dust, natural finger pressure.
```
Por que funciona
- Flash direto + ambiente quente dá o visual de foto de celular de verdade.
- "Rótulos de papel borrados e ilegíveis" evita texto falso no fundo.

### 5.4 · Mesa de madeira, domingo · USADO
```
Scene: a sunlit wooden dining table, the supplement jar among a simple breakfast spread and a folded newspaper with no visible readable text; an adult hand adjusts a glass. First read: a lived-in Sunday atmosphere. Second: the jar. Third: dust in sunlight and wood grain. Contrast: soft domestic warmth against one crisp flash highlight. Camera: 50mm eye-level editorial. Lighting: window sun plus controlled flash. Physical realism: crumbs, smudged glass, linen weave, imperfect shadows.
```
Por que funciona
- Jornal "sem texto legível" é a defesa contra letras inventadas.
- Um único highlight de flash dá ponto focal sem virar packshot.

### 5.5 · Bolsa e mesa de trabalho · USADO
```
Scene: a real desk at home with a closed laptop, a tote bag open and an adult hand setting the supplement jar beside keys and a notebook. First read: the transition between places. Second: the jar. Third: motion blur from the hand and a scratched desktop. Contrast: work pressure against a personal ritual. Camera: 28mm direct-flash editorial. Lighting: hard flash with late-afternoon side light. Physical realism: paper edges, fabric bag texture, fingerprints, cable disorder.
```
Por que funciona
- Motion blur só na mão (causa física) em vez de borrar o quadro todo.
- Bagunça de cabos e papéis dá "vida real" sem sujeira gratuita.

### 5.6 · Janela, chuva, pausa · USADO
```
Scene: the supplement jar on a kitchen sill beside a glass and a small ingredient bowl; an adult silhouette is out of focus beyond a rain-covered window. First read: rain and silhouette. Second: the jar. Third: droplets and window reflection. Contrast: protected interior against hostile weather. Camera: 85mm shallow focus. Lighting: blue rain ambience with a small warm practical. Physical realism: condensation, imperfect glass, water trails, stone sill texture.
```
Por que funciona
- Foco raso separa o frasco nítido da silhueta desfocada.
- Interior quente contra exterior azul: contraste emocional claro.

---

## 6. Paparazzi e editorial

### 6.1 · GPT Image · editorial de tensão controlada, flash contra concreto molhado · USADO
Objetivo: still editorial original (sem marca) para criativo de nicho beleza/saúde.
```
Original editorial, vertical. Controlled menace: an anonymous adult woman in soaked black tailoring stands motionless under an orange underpass light, a tiny unbranded red vial partly hidden in her cuff; first read the face, second the product clue, third the amber rain reflections. Paparazzi flash against wet concrete, Leica 35mm, real pores, rain and fabric, no text, no logo, no watermark. Clean natural photographic surface, low ISO, smooth tonal transitions, natural skin. No added film grain, sensor noise, crackle or oversharpening.
```
Por que funciona
- Emoção primeiro ("controlled menace"), objeto depois; três leituras em ordem.
- Flash de paparazzi contra superfície molhada: contraste duro e reflexo, sem neon.
- Uma câmera nomeada (Leica 35mm) em vez de pilha de lentes.

### 6.2 · GPT Image · ritual de moda, acesso proibido · USADO
```
Original fashion ritual, vertical. Forbidden access: a cropped adult hand in a black leather glove parts heavy blue velvet, briefly revealing a tiny blank cobalt glass bottle; first read the curtain and gesture, second the bottle, third a flash of silver powder. Canon R5 50mm, hard flash, tactile velvet, dust and glass, no text, no logo, no watermark. Clean natural photographic surface, low ISO, smooth tonal transitions, natural skin. No added film grain, sensor noise, crackle or oversharpening.
```
Por que funciona
- Mão recortada + cortina cria narrativa em um quadro, sem rosto.
- Garrafa "blank" (sem rótulo) elimina texto e marca de uma vez.

### 6.3 · GPT Image · cinema cultural, parada em movimento · USADO
```
Original cultural cinema, vertical. Defiant stillness: an anonymous adult in a graphite coat stands on a rain-slick platform while a train becomes a violent lateral light smear; a tiny unbranded device is glimpsed inside the coat. Low 28mm documentary flash, real wet asphalt, wind and fabric, no text, no logo, no watermark. Clean natural photographic surface, low ISO, smooth tonal transitions, natural skin. No added film grain, sensor noise, crackle or oversharpening.
```
Por que funciona
- Contraste imóvel × movimento (pessoa nítida, trem em rastro) é a ideia inteira.
- Câmera baixa 28mm + flash = linguagem de reportagem, não de estúdio.

### 6.4 · Soul 2.0 · paparazzi de rua, enquadre quase errado · MOLDE
Objetivo: foto "roubada" de celebridade fictícia saindo de um café, positivo-only.
```
Candid paparazzi outtake of a 31-year-old woman with a sleek dark ponytail leaving a corner café holding a takeaway cup, caught mid-step and looking away to her left, long-lens compression from across the street, harsh midday sun, slight motion softness on the far leg, slightly missed framing with a passer-by partly crossing the edge, wire-service documentary composition, vertical 3:2 crop, IMG_8842.CR2, natural skin.
```
Por que funciona
- Cues aprovados de paparazzi: `outtake`, `slightly missed framing`, `ambient crowd occlusion`.
- Sujeito não olha para a lente: é isso que vende o "flagra".
- Sem fonte falsa (nada de nome de agência): o resultado não ganha marca d'água.

---

## 7. Cena histórica e cinematográfica (Nano Banana 2.1)

Aprendizado de episódio longo: estrutura fixa `Camera + sujeito/ação + Setting + bloco de
realismo`, o bloco de cenário idêntico em todo plano da mesma locação, e o bloco de
realismo idêntico em todos. 303 keyframes 16:9 geraram com as referências da heroine
anexadas nos planos em que ela aparece.

Bloco de realismo repetido (cole no fim de todo plano):
`Photorealistic film still filling the entire 16:9 frame edge to edge with no black bars, no letterbox, natural light, real skin texture, documentary realism, [época e ano], historically plausible linen clothing, no modern objects, no text, no letters, no watermark, no logos.`

### 7.1 · Plano de abertura (estabelecimento) · USADO
```
Photorealistic wide establishing shot, a limestone quarry on the east bank of a great river at sunrise, around 2560 BC, white limestone cliffs, workers in white linen kilts with wooden levers and ropes, white dust in golden light, across the river a nearly finished great pyramid gleaming white. Cinematic documentary realism, 16:9, no text.
```
Por que funciona
- Local, época, hora e três elementos de escala (falésia, trabalhadores, pirâmide) numa frase.
- Cor dominante dita (branco, dourado) para o episódio inteiro herdar a paleta.

### 7.2 · Selfie de vlog no passado, com referência de rosto · USADO
```
Selfie vlog framing: the heroine holds the camera at arm's length herself, the phone is not visible. Camera: selfie close-up, wide-angle. The heroine (exactly the woman in the attached reference images: same face, pale green eyes, long straight dark-burgundy hair with blunt bangs, thin gold headband, geometric tattoo on the left side of her neck, turquoise-and-gold broad collar, ivory linen wrap dress, gold arm cuffs) sits on a huge white limestone block, looks into the lens with a dry half-smile, workers and ropes behind her. Setting: a limestone quarry on the east bank of the river at sunrise, white limestone cliffs, dozens of workers in white linen kilts with wooden levers and ropes, white dust in warm golden light. Photorealistic film still filling the entire 16:9 frame edge to edge with no black bars, no letterbox, natural light, real skin texture, documentary realism, Old Kingdom Egypt around 2560 BC, historically plausible linen clothing, no modern objects, no text, no letters, no watermark, no logos.
```
Por que funciona
- Descrição fixa da personagem (cabelo, tatuagem, joias) em TODO plano que a inclui, além da referência.
- "Holds the camera herself, the phone is not visible": selfie coerente sem celular no quadro.
- Gancho de personalidade (meio sorriso seco) sem pedir texto.

### 7.3 · Drone aéreo, empurrão lento · USADO
```
Camera: aerial drone, slow push. Aerial view from the quarry across the flooded river to the great pyramid, cargo boats on the water. Setting: the wide flooded river in the afternoon, flooded fields and palm groves, the plateau with the great pyramid gleaming white on the western horizon. Photorealistic film still filling the entire 16:9 frame edge to edge with no black bars, no letterbox, natural light, real skin texture, documentary realism, Old Kingdom Egypt around 2560 BC, historically plausible linen clothing, no modern objects, no text, no letters, no watermark, no logos.
```
Por que funciona
- Movimento de câmera dito na primeira linha, como o primeiro quadro de um vídeo.
- Camadas de profundidade (barcos, campos, palmeiras, horizonte) numa descrição enxuta.

### 7.4 · Close de personagem secundário em ação · USADO
```
Camera: close-up. A stern work-gang boss about 45 years old, shaved head, short black beard, white linen kilt, holding a long wooden staff, ties a thin linen cord with three knots around the heroine's wrist. Setting: a limestone quarry on the east bank of the river at sunrise, white limestone cliffs, dozens of workers in white linen kilts with wooden levers and ropes, white dust in warm golden light. Photorealistic film still filling the entire 16:9 frame edge to edge with no black bars, no letterbox, natural light, real skin texture, documentary realism, Old Kingdom Egypt around 2560 BC, historically plausible linen clothing, no modern objects, no text, no letters, no watermark, no logos.
```
Por que funciona
- Personagem secundário com idade, cabeça, barba, roupa e adereço: nenhum rosto genérico.
- Ação com objeto pequeno (cordão com três nós) entrega um beat de história.

### 7.5 · Noite à luz de tocha, câmera nervosa · USADO
```
Camera: handheld, fast, different angle. Torchlit night: a rope strains as men pull a sledge, flames swinging. Setting: a sand haul road at night lit by torches, a white limestone block on a wooden sledge pulled by two lines of men with ropes, the dark great pyramid ahead. Photorealistic film still filling the entire 16:9 frame edge to edge with no black bars, no letterbox, natural light, real skin texture, documentary realism, Old Kingdom Egypt around 2560 BC, historically plausible linen clothing, no modern objects, no text, no letters, no watermark, no logos.
```
Por que funciona
- Luz motivada (tochas na cena) em vez de "dramatic lighting".
- Tensão física (corda esticada, chamas balançando) conta a cena.

### 7.6 · Macro de prova de época (inserto) · USADO
```
Camera: close-up slow push. Red ochre gang marks painted on rough white limestone blocks. Setting: a wooden log track running from the white quarry down to the river bank, a large white limestone block on a wooden sledge, ropes, workers in white kilts. Photorealistic film still filling the entire 16:9 frame edge to edge with no black bars, no letterbox, natural light, real skin texture, documentary realism, Old Kingdom Egypt around 2560 BC, historically plausible linen clothing, no modern objects, no text, no letters, no watermark, no logos.
```
Por que funciona
- Inserto de detalhe (marcas de ocre na pedra) é B-roll que dá credibilidade histórica.
- O fundo de cenário continua o mesmo, então o corte combina com os planos amplos.

### 7.7 · Plano de multidão com ação coletiva · USADO
```
Camera: wide. A crew of about forty boatmen loading white stone into a boat. Setting: the river bank below the quarry, wooden cargo boats moored at a stone landing, papyrus reeds, workers loading stone. Photorealistic film still filling the entire 16:9 frame edge to edge with no black bars, no letterbox, natural light, real skin texture, documentary realism, Old Kingdom Egypt around 2560 BC, historically plausible linen clothing, no modern objects, no text, no letters, no watermark, no logos.
```
Por que funciona
- Número concreto ("about forty") dá escala sem descrever cada pessoa.
- Verbo de ação coletiva (carregando pedra) evita figurantes em pose.

### 7.8 · Primeiro quadro de cena de perigo, selfie com companheira · USADO
```
Photorealistic cinematic 16:9 historical adventure first frame. The attached portrait is authoritative for the exact adult face of the heroine: green eyes, burgundy hair and bangs, facial landmarks and natural age. Preserve her recognizable face. Wardrobe: modest charcoal long-sleeve linen blouse, practical dark skirt, brown leather crossbody satchel. A steep muddy hillside above a strait, Java, August 1883. The heroine fills the left foreground in a coherent handheld selfie shot, one arm out of view holding the invisible camera; her other hand reaches back toward her companion, a fictional adult Javanese woman wearing a cream cotton kebaya and an indigo batik sarong, black hair in a low bun, carrying a small wooden medicine box, climbing toward her. In the right background far below, tsunami surf sweeps through palms and a small timber settlement. No bodies or graphic injury. Ash-dark afternoon with a readable horizon, natural skin, sharp faces, clean textures without grain. Physically credible hands and perspective. No text, subtitles, UI, phone, visible camera or watermark. The camera begins before the two grip hands. Scary but human, not a fantasy painting.
```
Por que funciona
- Primeiro plano = rosto e emoção; catástrofe fica no fundo, em escala menor.
- Limites de conteúdo escritos (sem corpos, sem ferimento gráfico) e "scary but human, not a fantasy painting" trava o tom.
- Momento exato da câmera ("antes de apertarem as mãos") prepara a animação do vídeo.

---

## 8. Criativo de anúncio com texto na imagem

Regra geral: texto na imagem só em GPT Image (ou Nano Banana 2.1). Máximo ~12 palavras,
sempre entre aspas. Claim em linguagem de experiência pessoal, nunca promessa clínica.
Para texto crítico, gere a imagem limpa e aplique o texto no editor.

### 8.1 · GPT Image · story com texto sobreposto · MOLDE
Objetivo: estética de story espontâneo, com texto curto de experiência pessoal.
```
Screenshot of an Instagram story, 9:16: a casual mirror photo of a 34-year-old woman in a grey gym set, bathroom lighting from above, unedited, phone held low. Story text overlay in the default white font reads "Day 14 of my new routine", time stamp "07:42" at the top right, recompressed screenshot quality. Clean natural photographic surface, low ISO, smooth tonal transitions, natural skin. No added film grain, sensor noise, crackle or oversharpening.
```
Por que funciona
- Único caso em que a palavra "Instagram" é usada de propósito: o formato é o screenshot.
- Texto curto, entre aspas, em primeira pessoa (nada de promessa).
- Hora e "recomprimido" dão o acabamento de print real.

### 8.2 · Nano Banana 2.1 / GPT Image · capa 9:16 de reel, rosto medido · USADO (estrutura)
Objetivo: key art para grid de feed. Imagem 1 = contact sheet de 4 fotos da mesma pessoa; imagem 2 = logo.
```
Image 1 is a contact sheet of four photos of the SAME real adult man: use it only as the face authority. Image 2 shows the logo: copy its shape, colors and lettering exactly, add no extra letters. FULL-BLEED: the picture fills the entire frame edge to edge, no black bars, no letterbox, no borders, no margins and no mirrored or blurred reflection bands. Vertical 9:16 key art, readable from far away on a phone grid. The man looks into the camera with a confident calm expression, his eyes sit at exactly 30 percent of the frame height from the top, shoulders squared, hands closed or out of frame. Behind him a dark charcoal studio wall with a soft silver rim light from camera left. The top fifth of the frame is atmosphere only, with no lettering. Bold condensed sans-serif title "AI EDITING" in white at the lower third, small logo at the bottom center. No other people and no second copy of the man. Skin tone natural, never airbrushed, never reddish.
```
Por que funciona
- Papéis numerados por imagem e `use it only as the face authority`.
- Medida do rosto (30% da altura) e quinto superior livre: sobrevive ao recorte do feed.
- Anti-duplicação do herói e trava de tom de pele contra o color grade.

### 8.3 · GPT Image · rótulo legível num frasco fictício · MOLDE
Objetivo: quando não há foto oficial, gerar a embalagem com texto correto (marca fictícia).
```
Studio-quality product photo on a warm white surface: a white supplement bottle with a matte finish and a sage-green cap, the label facing camera with a slight curve distortion on the text, the label reads "NORTHLEAF" in bold condensed sans-serif, dark green on white, and below it "Daily Greens" in a lighter weight; no other text on the label. Soft contact shadow grounding the bottle, soft window light from the left, shallow depth of field, bottle fully inside the frame with a clear margin from every edge. Clean natural photographic surface, low ISO, smooth tonal transitions, natural skin. No added film grain, sensor noise, crackle or oversharpening.
```
Por que funciona
- Cada texto em aspas, com tipografia descrita como um designer; "no other text" fecha o resto.
- Distorção de curvatura no rótulo e sombra de contato são o que o torna físico.
- Substitua o nome fictício por um real somente depois, no pós, com o rótulo oficial.

### 8.4 · GPT Image · cena com telas ao fundo, sem letras inventadas · MOLDE
Objetivo: cenário de escritório com monitores, evitando texto ilegível de IA.
```
A candid vertical photo of a 36-year-old man in a rolled-sleeve shirt standing in a modern open office, a wall of monitors and a whiteboard behind him slightly out of focus; every screen, card, sign and panel in the scene shows only abstract icons and shapes, never any words, letters or numbers. He looks off-camera mid-conversation, window light from camera left mixed with ceiling panel light, 35mm, waist-up. Clean natural photographic surface, low ISO, smooth tonal transitions, natural skin. No added film grain, sensor noise, crackle or oversharpening.
```
Por que funciona
- A frase "abstract icons and shapes, never any words" é a trava de texto para qualquer tela ao fundo.
- Fundo desfocado + sujeito nítido mantém o foco no rosto.

---

## Checklist rápido antes de rodar

- Abertura fecha o formato (foto única de celular, plano de cinema, sheet).
- Uma câmera, uma luz principal com direção, 2 a 3 imperfeições com causa física.
- Referência com papel por imagem; descrição fixa repetida em todo plano.
- Soul 2.0: só positivo. GPT Image: trava anti-grão no fim. Texto: aspas e curto.
- Produto sempre de referência oficial, nunca recriado de memória.
