# Packshot e produto em cena

Carregue quando tiver produto na imagem: na mão, na mesa, packshot, rótulo,
ícone de benefício. Complementa o checklist de packshot do `PLAYBOOK.md` §6.
Última revisão: 2026-10-19.

---

## 1. As 3 leis

1. **Produto real ou produto nenhum.** Sem a foto oficial do produto, não tem produto
   na cena. A engine inventa rótulo, simplifica a arte e cria verso que não existe.
2. **Base sem produto, produto no 2º passo.** Gere a pessoa/cena com a mão ou a mesa
   prontas e insira a foto oficial depois, com referência.
3. **Composição ruim não se conserta encolhendo.** Produto gigante, duplicado ou
   torto → volte à base limpa e reinsira.

## 2. Escala em número (sempre em % da altura da imagem)

| Produto | Na mão | Na mesa |
|---|---|---|
| Pote de cápsula/gummy padrão | 22–25% | 20–23% |
| Pote de gummy em selfie de perto | 25–35% | — |
| Frasco conta-gotas 30–60 ml | 12–16% | 10–14% |

- Ficou pequeno: reedite com `40 percent larger than it is now`.
- Frasco pequeno dominante, "cara de packshot" ou duplicado = reprovado.
- Conta-gotas "perto do peito" = baixo, na altura da clavícula. Encostou em lábio,
  bochecha ou olho, virou prop de selfie de beleza: reprovado.

## 3. Preparar a base

Mão:
```
The hands are empty and natural near chest level with a relaxed C-shaped grip
ready to hold a cylinder, but holding nothing visible.
```
Mesa:
```
A kitchen counter is clearly visible in the lower center foreground, clean and
empty, with enough tabletop space for a bottle to be added later.
```
Mesa cortada ou rente à borda = regere a base. Nada de cilindro branco de
placeholder, a não ser que peçam (e ele nunca pode sobrar no final).

## 4. Inserir o produto (comece curto)

**1ª tentativa, curta** (funciona na maioria; Nano Banana 2.1 edit ou GPT Image 2 edit):
```
Make the woman holding the bottle, she is showing it to the viewer, keep the text
perfect, match the shadows of the bottle into the scene seamlessly. Keep only the
person holding the bottle with the bottle text visible. The size of the bottle is
medium. Use the exact product from image 2.
```

**Escalada** (só se pegada, escala ou rótulo falharem): prompt detalhado em
`exemplos-aprovados.md` (E5, na mão; E6, na mesa). Depois de 1 falha no mesmo
problema, mude a tática em vez de reescrever o mesmo prompt.

**Referência tirada de vídeo em que outra pessoa segura o produto:**
`Use the exact bottle from image 2 and ignore the hand, face, body and background
in image 2.` Só use frame de vídeo se o rótulo estiver legível e você tiver certeza
de que é o produto certo.

## 5. Física da pegada

O que separa "segurando" de "colado":
- polegar de um lado, indicador e médio do outro
- pontas dos dedos cobrindo a borda; frasco parcialmente atrás dos dedos
- pressão de contato visível, leve compressão da pele
- sombra de contato sob CADA dedo
- `holding with one hand` (senão o produto fica grudado num dedo)

Palma aberta atrás do frasco = reprovado.

## 6. Pessoa segurando o produto (persona falando)

Não use `phone` nem `grip` no prompt da persona: a mão mexe demais e o produto é
lido como celular. Descreva o estado final:
```
pouch already in her left hand at chest height, label forward; she lifts it once
and holds still
```

## 7. Rótulo e texto

- Rótulo sempre de frente. Nunca deixe o personagem girar o pote (a engine inventa o verso).
- Still que vai virar vídeo: `the main product name must be clean enough to survive animation`.
- Rótulo, tabela nutricional ou texto inventado no frame = descarte, sem exceção.
- Mesmo produto em todos os inserts da peça. Joia ou embalagem trocando de forma
  entre frames reprova a peça inteira.

## 8. Produto aparece antes da hora

Referência de produto anexada **vaza** pra cena. Em keyframe antes da revelação,
não anexe a referência do produto e descreva o estado:
`The gift is still hidden, the table holds only the cake and two cups.`

## 9. Ícone 3D de benefício (cards de edição)

GPT Image 2.5, fundo transparente, qualidade alta. Molde aplicado em vídeo aprovado:
```
A glossy 3D gold-and-glass open hand with relaxed fingers, floating, soft golden
rim light. Premium 3D render with a transparent background, centered, soft gold
rim light, clean icon only.
```
Troque só o objeto (`small calm flame resting inside a glass sphere, warm glow`,
`walking shoe mid-step`, `crescent moon with three small stars`) e mantenha o sufixo
igual pra família de ícones ficar coerente.

## 10. Macro de objeto (prova de mecanismo)

Funciona em qualquer engine de prosa:
- dimensão física em cm de cada objeto (`about 10 by 7 centimeters and only 6
  millimeters thick`)
- contagem exata (`a single sponge`, `one glass, one spoon, one hand`)
- cor travada contra o vizinho (`deep blood red, not pink, not orange`)
- esquerda e direita nomeadas (`new on the LEFT, old on the RIGHT`)
- quanto do quadro o objeto ocupa (`filling about 60 percent of the frame`)
- `soft contact shadow` sempre

Sequência START / ACTION / PAYOFF: 3 edições do MESMO still
(`Edit the reference photo. Keep the exact same camera angle, framing, counter,
glass, lighting and hand. Change only this: ...`). Geometria idêntica nos 3 quadros;
servem de primeiro e último frame de vídeo.

## 11. QA do produto antes de animar

- [ ] é o produto certo (asset oficial), um só, onde o briefing pede
- [ ] escala dentro da tabela §2
- [ ] pegada física, sombra de contato, luz do lado da cena
- [ ] rótulo de frente, legível, sem texto inventado
- [ ] rosto inalterado em relação à base
- [ ] nenhuma marca de terceiro legível (tênis, remédio, transportadora)
