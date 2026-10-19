# Realismo iPhone, UGC e paparazzi

Carregue quando o pedido for "foto de celular", selfie, UGC, vlog, candid,
paparazzi, câmera escondida ou "não pode parecer IA".
Última revisão: 2026-10-19. Tudo aqui saiu de geração real em produção.

---

## 1. Abertura do prompt (a primeira frase decide o formato)

| Quer | Abra com |
|---|---|
| Foto única de celular, sem print nem colagem | `Single unedited vertical smartphone photo, one continuous camera frame` |
| Persona UGC (não thumbnail) | `Candid vertical smartphone photo of a <idade> <origem> <homem/mulher> ...` |
| Selfie de braço esticado | `... filming herself at arm's length, front-facing phone-camera POV` |
| Foto tirada por outra pessoa | `Camera held by another person at eye level` |
| Câmera escondida / longe | `... like footage from a camera hidden inside the house` |

- **Peça UGC/selfie explicitamente.** Imagem "bonita" 16:9 sem essa instrução
  volta com cara de thumbnail e é reprovada.
- Em engine com negativo dá pra acrescentar `not a screenshot`. No Soul 2.0, não
  (positivo-only).

## 2. Palavras que chamam interface (corte na hora)

`camera roll`, `story`, `TikTok`, `Instagram`, `testimonial`, `RAW iPhone photo`,
`RAW natural iPhone camera-roll` → a engine desenha barra de usuário, selo de
verificado, ícone de som, controle de vídeo ou moldura de celular.

- Começou a aparecer UI? Tire essas palavras. Não fique testando variações.
- Exceção consciente: o template "story com texto" do `PLAYBOOK.md` usa
  `screenshot of an Instagram story` de propósito, só em GPT Image.

## 3. O celular não pode aparecer

- `phone propped on the counter` → o celular aparece no quadro (4 de 5 imagens
  num lote de Soul 2.0). Não descreva onde o aparelho está.
- `phone` repetido e `adjusts her grip` → aparece um segundo celular, ou o
  produto na mão é lido como celular (pouch preto retangular é o caso clássico).
- O que funciona: `front-facing phone-camera POV` e, em engine com negativo,
  `phone not visible`. Dê à mão livre uma posição: `left hand stays open on her knee`.

## 4. Ficha de câmera de celular

Engine com negativo (GPT Image, Seedream, Nano Banana em prosa):
```
Shot on iPhone 14 Pro front camera, 28mm equivalent, natural HDR disabled,
vertical 9:16, realistic phone photo, not cinematic, not studio lighting,
not fashion editorial, not beauty retouched.
```

Positivo-only (Soul 2.0), bloco de captura:
```
Ordinary wide phone lens, natural chest-height framing, slight handheld tilt,
mild perspective distortion, subtle focus inconsistency, realistic phone
compression, gentle motion softness, uneven automatic exposure, mixed white
balance, irregular window shadows, unedited domestic footage, authentic
still-photo look.
```

Cues extras de celular (escolha 2 a 6, nunca todos): `Smart HDR restraint` ·
`uneven automatic exposure` · `mixed automatic white balance` · `subtle focus
inconsistency` · `realistic smartphone compression` · `handheld framing with
imperfect symmetry` · `small exposure clipping in bright windows` · `realistic
mirror geometry and parallax`.

## 5. Fórmula de figurante UGC aprovada (Soul 2.0, 55–65 anos)

`Candid vertical smartphone photo` + idade e origem + cabelo e 2 traços + roupa
simples nomeada + cômodo iluminado + `three-quarter length from head to knees` +
`relaxed posture, both hands visible` + expressão calma + `natural window light,
real lived-in home, natural skin texture`.

Mesmo texto, 3 seeds, escolhe-se a melhor. Prompts literais em
`exemplos-aprovados.md` (E1, E2). Descarte comum: mancha na roupa, mão estranha.

## 6. Pele: limpa por padrão

- Grão, ruído, poro gravado, malha de rugas e oversharpening **não** são cue
  automático de realismo. Viraram reprovação 4 vezes num mês ("grain demais").
- Excesso de grão aparece em **cadeia longa de regeração**: a cada passada o
  rosto muda e ganha textura. Volte à imagem aprovada em vez de editar a edição.
- Pedido "pele mais realista" sem envelhecer: variação sutil de tom e luz, sem
  filtro de beleza, sem cera, sem poro gravado, sem grão.
- Imagem de IA com aspecto plástico: um overlay de grão fino **na edição**,
  depois da geração, resolve melhor que prompt. Valide na tela do celular.

## 7. Imperfeição com causa física

Cada defeito precisa de motivo na cena: vidro → digital; janela → estouro de
exposição; tecido → fiapo; mão em movimento → blur só nela. Sujeira, ruído e blur
espalhados no quadro todo viram estilo, não foto real. 2 a 3, nunca mais.

## 8. Paparazzi, editorial e câmera escondida

Cues que funcionam: `candid paparazzi outtake` · `editorial outtake between posed
frames` · `behind-the-scenes publicity still` · `slightly missed framing` ·
`ambient crowd occlusion` · `wire-service documentary composition` ·
`subject caught mid-expression`.

Câmera escondida (aprovado): `Slight grain, mild compression, long-lens feel,
like footage from a camera hidden inside the house` + o sujeito
`does not look at the camera`. Exemplo completo: `exemplos-aprovados.md` (E7).

Cinema (só quando pedem frame de filme, nunca misturado com celular):
`frame captured between lines of dialogue` · `practical lights visible in the
scene` · `motivated key light` · `naturalistic blocking`.

## 9. Fonte "secreta" é proibida

`Getty Images`, nome de estúdio, `warner bros .com`, título de filme, nome de
agência → gera marca d'água ou texto falso. Traduza: `studio publicity still
aesthetic`, `archival production still`, `big-budget film publicity photography`.

## 10. Óptica de câmera RAW (uma câmera por prompt)

`Canon EOS R5, RF 85mm f/1.2L at f/2` · `Leica SL2-S, Summilux-M 35mm f/1.4
character` · `Phase One IQ4 medium-format tonal detail`, mais 1 ou 2 de:
`true optical falloff`, `natural microcontrast`, `subtle chromatic aberration at
high-contrast edges`, `realistic highlight roll-off`, `unretouched RAW development`.
