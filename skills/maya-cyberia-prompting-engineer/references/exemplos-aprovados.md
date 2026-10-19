# Exemplos aprovados (prompts literais)

Prompts rodados em produção, copiados como foram enviados. Use como molde: troque
sujeito, cena e produto, mantenha a estrutura.

Status: **APROVADO** = escolhido pelo diretor ou cliente · **USADO** = entrou numa
peça entregue · **MOLDE** = estrutura validada, sem aprovação registrada da imagem.
Engine indicada em cada um. Prompt com bloco negativo ou filename não vai pro Soul 2.0.
Última revisão: 2026-10-19.

---

## E1 · Soul 2.0 · figurante UGC, homem 62 · APROVADO
2K, 9:16, mesmo texto em 3 seeds; escolhida a opção 1.
```
Candid vertical smartphone photo of a 62-year-old American man with short silver hair, grey trimmed stubble and kind weathered eyes, wearing a heather-grey henley and dark jeans, standing in a sunlit family kitchen, three-quarter length from head to knees, relaxed posture, both hands visible at his sides, looking toward the camera with a calm expression, natural window light, real lived-in home, natural skin texture.
```

## E2 · Soul 2.0 · figurante UGC, mulher 58 · APROVADO
```
Candid vertical smartphone photo of a 58-year-old American woman with shoulder-length wavy silver-blonde hair, soft smile lines and warm hazel eyes, wearing a cream cardigan over a white tee and blue jeans, standing in a bright kitchen with a window behind her, three-quarter length from head to knees, relaxed posture, both hands visible, looking at the camera with a gentle expression, natural window light, real lived-in home, natural skin texture.
```
Nota: `natural skin texture` passou aqui em 55–65 anos com luz de janela suave. Se
aparecer veia ou couro, troque pelo Skin Lock.

## E3 · GPT Image 2 / ChatGPT · character sheet 3x3 a partir de selfie · MOLDE
Gere fora da ferramenta de vídeo. Selfie anexada = única identidade.
```
Using the attached portrait as the sole identity reference, create one clean
vertical 9:16 photorealistic character-consistency sheet of this exact person.

Build a balanced 3x3 grid with nine coherent views:
1) front-facing neutral close-up,
2) front-facing subtle natural smile,
3) left three-quarter view,
4) right three-quarter view,
5) left profile,
6) right profile,
7) medium shot speaking with one restrained hand gesture,
8) waist-up neutral posture,
9) serious attentive expression.

Preserve the exact facial geometry, eye shape and spacing, eyebrows, nose, lips,
cheekbones, jawline, ears, skin tone and texture, hairline, hairstyle, age,
characteristic asymmetries and body proportions from the reference. Keep the
same simple neutral clothing in every panel. Soft even daylight, plain warm-gray
background, realistic skin and hair, consistent camera and color response.

No beautification, no face redesign, no generic-model look, no change of
ethnicity or age, no makeup enhancement, no extra people, no labels, no text,
no logos, no watermark, no interface and no decorative layout.
```
Variante de ação: troque os quadros 7–9 por corpo inteiro (frente, base atlética,
largada). Mantenha os 6 faciais. No ChatGPT, feche com a trava anti-grain do `SKILL.md`.

## E4 · Character sheet corpo inteiro, do zero (drama/anúncio) · MOLDE
```
Character reference sheet, left side a front-face close-up, right side three equal-height full-body views side by side showing front, 90-degree side, and back; same character in all views, full body in frame, neutral A-pose, tops of heads and soles of feet aligned; woman in her mid-thirties, average height, soft build carrying some extra weight at the waist, shoulders slightly rounded; oval face, warm brown eyes with faint dark circles, light freckles across the nose, small mole above the left lip; shoulder-length chestnut hair in a loose low ponytail with face-framing strands; oversized sage-green knit cardigan over a plain white tee, dark straight-leg jeans, white sneakers, thin gold necklace; the face, hairstyle, and clothing of the close-up and the three views are completely identical; pure white background, soft even lighting, cinematic quality
```

## E5 · Inserção de produto na mão, versão detalhada · MOLDE
Nano Banana 2.1 edit ou GPT Image 2 edit. Use depois que o prompt curto
(`packshot-produto.md` §4) falhar.
```
Use IMAGE 1 as the locked base portrait and IMAGE 2 as the exact product reference.

IDENTITY LOCK: preserve the exact same face, eyes, nose, mouth, skin texture, hairline, body proportions, clothing, background, camera angle, lighting, and iPhone UGC look. Do not beautify, age-change, slim, reshape, or regenerate the person.

LOCAL EDIT ONLY: edit only the hand, fingers, wrist, and the small product contact area required for a believable grip.

TASK: replace the empty grip with the exact [PRODUCT] bottle. The subject must be physically holding and showing it to the camera at [PLACEMENT].

PHYSICAL GRIP: thumb wraps around one side of the bottle, index and middle fingers wrap around the opposite side, fingertips partly cover the bottle edge, the bottle sits partly behind fingers and palm, with natural knuckle angles and visible contact pressure.

INTEGRATION: add correct finger occlusion, contact shadows under every touching finger, subtle skin compression at contact points, matching room light, matching lens blur, realistic glass/plastic highlights, correct perspective, and matching depth of field.

SCALE: [regra de escala em % da altura da imagem]. Keep the product readable but not oversized.

NEGATIVE: no floating product, no sticker look, no hovering in front of the palm, no detached fingers, no unchanged open palm behind the product, no extra bottle, no face change, no text overlays, no social UI, no watermark.

OUTPUT: one single candid smartphone photo.
```

## E6 · Inserção de produto na mesa · MOLDE
```
Use IMAGE 1 as the locked base portrait and IMAGE 2 as the exact [PRODUCT] bottle reference.

Preserve the exact same person, face, skin texture, clothing, room, table, camera angle, lighting, and phone-photo realism. Do not beautify, reshape, age-change, or regenerate the person.

Place the exact [PRODUCT] bottle upright on [SURFACE] at [PLACEMENT]. The bottle must be fully inside the image, front-facing to camera, not cropped, not cut off, with clear margin from all edges. It should sit on the surface, not float.

Scale: [SCALE RULE]. The label must be sharp and readable, especially [MAIN PRODUCT NAME] and key label text.

Integration: realistic contact shadow on the surface, correct perspective matching the tabletop angle, matching warm/cool room light, matching blur/noise/grain, subtle table reflection if natural, realistic depth of field.

The subject is not holding the bottle. No app interface, no screenshot, no collage, no text overlays, no watermark, no extra products, no face change.
```

## E7 · Multi-referência · câmera escondida · APROVADO
Image 1 = locação, image 2 = rosto, image 3 = roupa.
```
Image 1 is the exact camera position, framing and location: keep this exact shot of the outdoor blue and red jiu-jitsu mat, the stone tiles, the hedge and the palm trees, identical angle, identical crop, identical daylight. Add a small square teak table standing on the stone tiles at the near edge of the mat, slightly right of center, with a clear plastic water bottle and a small white tub of powder with a scoop on it. Standing barefoot on the mat right behind the table is the man from image 2: same face, same short dark hair and beard, wearing the same white jiu-jitsu gi with brown belt as in image 3. He is alone, looking down at the table, one hand reaching for the bottle, not looking at the camera. His full body is visible, natural scale for the distance. Soft overcast daylight matching image 1, soft contact shadow under him and the table. Same slight phone-camera softness and grain as image 1.
```

## E8 · Nano Banana 2.1 · cena de prova editando o still aprovado · USADO
1 referência (o still aprovado do personagem).
```
Edit this exact photo. Keep the exact same man with the identical face, beard, hair and navy shirt, the exact same room, bookshelves, wall lamp, light stone countertop, glass bowl, spoon, framing and lighting. Do not change his identity. Only two changes: 1) the entire open cut interior of the pink anatomical model he holds is now completely filled with smooth matte solid black paste, no pale pink tissue visible inside, the pink outer shell unchanged; 2) his free hand now lifts a clear 60 ml syringe filled with dark red liquid beside the model. Photorealistic, sharp focus, clinical educational demonstration.
```
Versão seguinte da mesma técnica acrescentou a trava que faltava:
`... the exact framing and the exact camera distance (do not zoom in or crop, same face size in the frame).`

## E9 · Cenários vazios (plates) pra continuidade · MOLDE
Dia:
```
Fixed-camera wide-angle shot, a clear establishing shot, suburban American backyard birthday party, bright early afternoon; foreground: the corner of a white folding table with a pastel tablecloth and a stack of paper plates; midground: a green lawn with string lights hung between two wooden posts, a long buffet table against a white fence; background: a beige two-story house with a sliding glass door on the right of the frame, tall hedges along the left; floor: freshly cut grass with a stone path leading to the sliding door; walls: white picket fence, beige siding; pastel balloons tied to the right post, a cooler beside the buffet table; spatial structure continuous and self-consistent; warm direct sun from the upper left, soft shadows, cheerful saturated colors; No people in the scene, empty scene, cinematic quality
```
Noite:
```
Fixed-camera wide-angle shot, a clear establishing shot, lived-in suburban kitchen, late night; foreground: the edge of a marble island with a half-empty glass of wine; midground: the island in the center, a fridge covered in kids' drawings on the left; background: a dark window over the sink, a doorway to a dim hallway on the right of the frame; floor: light oak planks; walls: white subway tile, pale grey paint; a pendant lamp hangs over the island, a bowl of fruit at the island's far end, a phone face down near the wine glass; spatial structure continuous and self-consistent; single warm pendant light over the island, the rest falling into cool blue shadow, high contrast, quiet intimate mood; No people in the scene, empty scene, cinematic quality
```

## E10 · Nano Banana 2.1 · estilos animados travados · APROVADO (remake animado, nota 9)
Ação/cena + lente, depois `Same room and set as the second reference image.`, depois o estilo.
Referências: personagem e locação (produto só depois da revelação).
```
Stylized 3D animated feature-film look, high-end CG animation studio render quality, rounded appealing shapes, large expressive eyes, soft subsurface skin, rich cinematic colour and lighting. Same [CHARACTERS] and the same [PROPS] as the references. Vertical 9:16. No captions, no subtitles.
```
```
Flat 2D hand-drawn TV cartoon style, lemon-yellow skin, big round white eyes with small black pupils, thick clean black outlines, flat bright cel colours. Same [CHARACTERS] and the same [PROPS] as the references. Vertical 9:16. No captions, no subtitles.
```
```
Toy brick minifigure stop-motion style, macro photography of glossy ABS plastic toy figures with printed faces and claw hands, brick-built sets with visible studs, tiny-scale shallow depth of field, cinematic miniature lighting. Same [CHARACTERS] and the same [PROPS] as the references. Vertical 9:16. No logos, no captions, no subtitles.
```

## E11 · Seedream 5.0 Pro · pessoa real em cena nova · APROVADO
Base = foto da pessoa (com autorização dela) já com a roupa aprovada, não a foto crua.
Uma mudança grande por passada; personagens extras numa 2ª passada.
```
Place the man from this image into a new scene. Keep his face, hair, beard, expression, round dark sunglasses and head angle exactly identical.

Armor: keep the same heavy, bulky silhouette and the same organic integration into his body from the original image — broad massive shoulders, thick chest, a body that looks like a weapon. Replace only the small scales with large, thick, sculpted armor plates layered over each other, following the anatomy of his chest, shoulders and neck, with real volume and depth between the layers. Material: matte black carbon composite with a slightly organic, chitin-like finish — not shiny steel, not iron, not chrome. Between the plates, deep oxblood red synthetic muscle fibers, thick and powerful, visible in the gaps. Oxblood inlays along the edges of the plates and a dim oxblood glow deep inside the seams — like dried blood, not bright red, not neon. Segmented thick plates over the throat. At the base of the neck the armor fuses into his real skin with irregular edges, small surgical scars and red irritated skin. Realistic wear: scratches, dust, scuffed edges.

A small "Z9" engraved in the center of the chest plate, same black as the armor, only catching the light on its edges — not printed, not bold.

Thick black cables plugged into metal ports at the back of his skull and the nape of his neck, curving out behind his head and shoulders and running back toward the machines in the lab. Skin slightly red and scarred around the ports.

New background: a real high-tech cybernetics lab. Behind him, a row of tall glass containment tubes filled with murky liquid, each one holding a different dormant cyborg — different body types, some half-built with exposed metal skeletons, some with human faces and metal jaws, cables plugged into their spines, heads bowed. Steel grating floor, cable trays on the ceiling with bundles of black cables, server racks, robotic arms, concrete and dark grey walls. Softly out of focus, he is the sharpest thing in the frame.

Lighting: mid-key and realistic, the lab is clearly visible, not pitch black. Soft white overhead lab panels, soft key light on his face from the front-left. Deep oxblood red light glowing from the base of each tube, backlighting the cyborgs and leaving a thin red rim on his shoulders and red reflections on his armor. He must look photographed in the same room: same light direction, shadows, haze, color grade and grain as the background. No neon, no blue, no purple, no holograms.

50mm lens, chest-up, real skin pores, subtle sensor grain, documentary photo. DSC00412.ARW
```
O que copiar daqui: material travado por comparação (`not shiny steel, not iron,
not chrome`; `like dried blood, not bright red`), marca gravada sem virar estampa
(`same black as the armor, only catching the light on its edges — not printed`),
frase de integração sujeito ↔ fundo e `mid-key, not pitch black`.

## E12 · Soul 2.0 · médico pra avatar falante · USADO, com ressalva
Pose e expressão aprovadas; o still escolhido virou o avatar. Mas o texto falso no
jaleco apareceu nas 2 rodadas e precisou de limpeza no GPT Image 2. O prompt original
tinha negativos (`no badge...`, `No text anywhere`), que no Soul chamam o objeto.
Versão corrigida em positivo-only (troque antes de rodar):
```
Photorealistic raw iPhone front-camera UGC still, 9:16, clean unobstructed view. A 46-year-old white British man, male gastroenterologist, short dark brown hair slightly receding, light stubble, bare face. Wearing a plain blank white lab coat with a smooth, clean, unmarked chest and pockets, over plain navy blue scrubs. Sitting on a chair, half-body framing from mid-thigh up, facing camera, serious caring expression with a slight reassuring look, lips together, hands relaxed in lap. Real consultation office behind him, softly out of focus: light blue-grey wall and a window with sheer curtains. Soft even natural window light from the side, smooth even skin tone, gentle shadow transitions, natural phone exposure. Face centered in the upper third. Clean simple composition, one single adult man, exactly two hands with five fingers each.
```
(A versão corrigida ainda não rodou; a original é a que tem registro de uso.)

## E13 · Limpeza de referência danificada · MOLDE
Rosto e pele vêm do retrato limpo; a cena com pele danificada dá só layout.
```
Clean portraits are the authority for facial identity, apparent age and natural skin rendering. The scene reference controls only composition, pose and wardrobe; do not copy its damaged skin texture. Preserve facial landmarks. Natural tonal transitions, restrained mature expression lines, neutral attentive expression. No added grain, synthetic crackle, etched wrinkle mesh, exaggerated pores, oversharpening or waxy smoothing.
```

## E14 · GPT Image 2 · limpeza de still escolhido + fundo chroma · MOLDE
Descrição do passo que funcionou (o texto exato não foi guardado):
```
Keep everything identical: the man's face, hair, expression, pose, clothing and framing. Only two changes: remove the embroidered text and badge from the lab coat chest so it is plain white fabric, and replace the background with a flat solid chroma green (#00B140), evenly lit, no shadows on the backdrop.
```
2 tentativas, escolhida a melhor, direto pro avatar falante.
