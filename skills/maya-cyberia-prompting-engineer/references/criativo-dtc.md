# Criativo DTC: anúncio, capa, key art e cena de prova

Carregue quando a imagem for peça de anúncio (UGC still, cena de prova de
mecanismo, capa de reel, key art, cenário de drama). Complementa os templates DR e o
compliance do `PLAYBOOK.md` §7–8. Última revisão: 2026-10-19.

---

## 1. Imagem = fala = público

- Fala de dor, dieta ou exercício → pessoa compatível com a dor (ex.: sobrepeso).
  Pessoa magra só em resultado ou desejo.
- Ingrediente mostrado = ingrediente da oferta.
- Número ou data na cena que contradiz a promessa: mascare na edição.
- Casting por arquétipo do mercado (autoridade, idade, cenário, tom), personagem
  ORIGINAL. Rosto de anúncio concorrente é inteligência, não licença.

## 2. Still de anúncio não leva texto

- Sem legenda, CTA ou overlay no still. Lettering entra na edição.
- Rosto, pet e produto dentro do centro seguro do crop 4:5 (o 9:16 é recortado no feed).
- Telas, placas e cards no fundo: `every card, screen, sign and panel in the scene
  shows only abstract icons and shapes, never any words, letters or numbers`.
  Sem essa trava, todo painel vira texto ilegível de IA.

## 3. Compliance que derruba conta

1. Claim médico escrito na imagem (o OCR da plataforma lê). Use experiência pessoal.
2. Antes/depois no mesmo frame. Separe no tempo.
3. Pele ou barriga em destaque; nudez dispara revisão. Maquete anatômica passou com
   `clinical educational demonstration` no fim do prompt.
4. Marca de terceiro visível (tênis, remédio, transportadora, rótulo de vinho).
   Confira logo em cada still: um "N" de tênis apareceu numa geração e a foto caiu.
5. Frasco âmbar genérico lê como "pare seu remédio". Use frasco branco sem rótulo.
6. Nicho sensível (desempenho masculino): enquadre da cintura pra cima, roupa larga;
   produto na altura do peito tira o foco do decote.
7. Documento ou exame em cena: marcas abstratas ilegíveis. Nunca nome de paciente,
   médico, clínica, ID, QR ou código de barras.

Compliance também é por cliente: alguns liberam marca de terceiro ou celebridade com
jurídico próprio. Confira o perfil do cliente antes de bloquear.

## 4. Cena de prova (demo de mecanismo)

Edite um still aprovado em vez de gerar outro:
```
Edit this exact photo. Keep the exact same man with the identical face, beard, hair
and <roupa>, the exact same room, <objetos fixos>, framing and lighting. Do not
change his identity. Only two changes: 1) ... 2) ... Photorealistic, sharp focus,
clinical educational demonstration.
```
Exemplo completo e aprovado: `exemplos-aprovados.md` (E8).

## 5. Multi-referência com papel por imagem

Dê o papel de cada imagem e diga o que IGNORAR dela:
```
Image 1 is the exact camera position, framing and location: keep this exact shot,
identical angle, identical crop, identical daylight. ... the man from image 2: same
face, same short dark hair and beard, wearing the same <roupa> as in image 3.
```
- `ignore the backgrounds, the salute pose and the coat` (o que não copiar da ref)
- `Remove every person ...` quando a ref de locação tem gente
- Feche com a textura da ref de locação: `Same slight phone-camera softness and
  grain as image 1`. Sujeito e fundo ficam da mesma câmera.
- Uma mudança grande por passada. Personagens extras entram numa 2ª passada.

## 6. Integração sujeito ↔ fundo

A frase que fez a pessoa parecer fotografada no lugar:
```
He must look photographed in the same room: same light direction, shadows, haze,
color grade and grain as the background.
```
E `mid-key and realistic, the room is clearly visible, not pitch black`: cena escura
"cinematográfica" esconde a integração ruim e o cliente reprova.

## 7. Capa e key art 9:16

Estrutura que passou num lote de 60 capas (portável pra GPT Image 2):
- `FULL-BLEED: the picture fills the entire frame edge to edge, no black bars, no
  letterbox, no borders, no margins and no mirrored or blurred reflection bands`
- `readable from far away on a phone grid`
- papéis numerados: `Image 1 is a contact sheet of four photos of the SAME real man`
  (uma contact sheet com 4 fotos do rosto vale mais que 4 refs soltas); `Image 3
  shows the logo: copy its shape, colors and lettering exactly, add no extra letters`
- rosto em posição medida: `His eyes sit at exactly 30 percent of the frame height
  from the top`; o quinto superior só atmosfera, sem letra (título no topo é cortado
  pelo grid 4:5)
- anti-duplicação do herói: `no other people and no second copy of the man`
- trava de tom de pele contra o grade: `never airbrushed, never reddish`
- mãos fechadas ou escondidas

Em lote, varie composição, ação, enquadramento e cenário por capa. 40 capas no mesmo
layout foram aprovadas pela velocidade e criticadas como repetitivas.

## 8. Cenário vazio (plate) pra continuidade

```
Fixed-camera wide-angle shot, a clear establishing shot, <local>, <horário>;
foreground: ...; midground: ...; background: ...; floor: ...; walls: ...;
<2 a 4 peças em posição fixa>; spatial structure continuous and self-consistent;
<luz com direção e temperatura>; No people in the scene, empty scene
```
Cenário = local + horário (a cozinha à noite é outro plate). Zero pessoas, nem
silhueta, reflexo ou foto na parede. Exemplos em `exemplos-aprovados.md` (E9).

## 9. "Historinha" pra cobrir trecho de VSL

Sem stock bom pra um trecho de história: imagem com a cena completa (quem, onde,
emoção, luz, câmera/lente, 9:16), 4 opções, pegue a primeira boa, anime com zoom
leve na edição. Prompt visual direto: só o que aparece, sem explicar o roteiro nem
a intenção do anúncio.

## 10. Estilo animado (remake de anúncio)

Descreva os traços do estilo. Nunca escreva nome de estúdio, desenho ou marca de
brinquedo no prompt. Moldes travados em `exemplos-aprovados.md` (E10).
Pra realismo 3D sem virar super-herói: `grounded cinematic 3D realism, natural
proportions, realistic materials, documentary lighting, restrained performance`.
Um preset de estilo por lote.
