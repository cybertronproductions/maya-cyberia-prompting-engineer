# Avatar, influencer e personagem recorrente

Carregue quando o pedido for avatar, influencer de IA, persona de anúncio,
character sheet, "o mesmo rosto em várias cenas" ou still que vai virar avatar
falante. Última revisão: 2026-10-19.

---

## 1. Qual engine pra quê

| Tarefa | Engine | Por quê |
|---|---|---|
| Casting de persona UGC nova | Higgsfield Soul 2.0 | estética de rede social; mesmo texto em 3 seeds, escolhe-se 1 |
| Character sheet a partir de selfie | GPT Image 2 / ChatGPT | mais fiel à geometria do rosto; gere FORA da ferramenta de vídeo |
| Pessoa real (com autorização) em cena nova | Seedream 5.0 Pro (2K) | ganhou de Nano Banana e Grok num teste de campo (2026-10) |
| Still novo do mesmo personagem (edição) | Nano Banana 2.1 com **1** referência | 2 referências de pessoas diferentes puxam o rosto da 2ª |
| Limpar still escolhido (texto falso, fundo) | GPT Image 2 | `keep everything identical` + só a mudança |

⚠ Em avatar humano hiper-real de cliente, Nano Banana teve rosto reprovado de cara
(2026-10). Use Nano Banana 2.1 pra keyframe, objeto, cenário, estilizado e edição
pontual; o casting do rosto fica com Soul 2.0, Seedream ou GPT Image.

## 2. Âncora canônica (a regra que mais custou)

- Personagem recorrente = **1 still canônico aprovado**. Todo take, toda cena nova,
  parte DELE.
- Nunca encadeie "último frame do take anterior" pra manter identidade: num anúncio,
  no 6º take a modelo estava irreconhecível e o anúncio inteiro foi reprovado.
- Exceção provada: **a mesma ação física contínua** em vários takes (B-roll) pode
  partir do último frame aprovado. Talking head e casting, nunca.
- Não use referência com legenda queimada nem vídeo como referência de identidade
  (puxa cenário junto).
- Still novo: compare o rosto **lado a lado** com o aprovado antes de animar.

## 3. Trava de identidade no prompt

Texto por personagem que passou no QA de identidade de um lote inteiro:
```
Reference image defines the man: same 62-year-old face, short silver hair, grey
trimmed stubble and build; only one person is in the room and both hands in frame
are attached to his own arms.
```

Edição do mesmo still, mantendo o rosto (Nano Banana 2.1, 1 referência):
```
Edit this exact photo. Keep identical: <rosto, barba, cabelo, roupa>, the room,
<objetos fixos>, lighting, the exact framing and the exact camera distance
(do not zoom in or crop, same face size in the frame). Do not change his identity.
Changes: 1) ... 2) ...
```
A cláusula `exact camera distance ... same face size in the frame` entrou depois
que um still novo mudou rosto e enquadramento. Use sempre.

## 4. Character sheet

**A partir de selfie (GPT Image 2, 3x3):** prompt completo em
`exemplos-aprovados.md` (E3). QA antes de usar:
- olhos, nariz, boca, mandíbula, linha do cabelo iguais à selfie
- mesma idade e mesma pele, sem embelezar
- perfil esquerdo e direito apontando pra lados **opostos**
- roupa e cabelo idênticos em todos os painéis

Falhou? Regere no GPT Image. Nunca "corrija depois" na ferramenta de vídeo.

**Do zero, corpo inteiro (drama/anúncio):** esquerda close frontal; direita 3 vistas
de corpo inteiro (frente, 90° lateral, costas), mesma altura, A-pose neutra, fundo
branco, luz chapada, sem prop, sem texto. Consistência vale mais que beleza.
Prompt em `exemplos-aprovados.md` (E4).

**Óculos que cobrem os olhos:** pelo menos 3 painéis SEM óculos, pra conferir os olhos.

**Uso:** anexe selfie (ref 1) + sheet (ref 2) da MESMA pessoa. Gere uma still limpa por
cena e anime a still, nunca a sheet. Rosto mudou? Suba 2 a 3 painéis da sheet como
referência e repita.

## 5. Corpo e pele da persona

- Personalidade vira postura visível: "fria" → `steady gaze, lips pressed, barely smiles`.
- Figurino descrito separado do rosto, pelo nome do material
  (`matte black leather jacket`, `heather-grey henley`).
- Busto: `big bust with deep cleavage`. Nunca `heavy`, `heavy breasts`,
  `full natural breasts` (renderiza veia e pele caída). `full, natural bust` já sai
  grande no Soul; não reforce.
- "Mais shape" com armadura ou roupa: aumente carcaça e ombro, não a anatomia.
- 45+: Skin Lock do `SKILL.md` e luz suave frontal. Abajur duro expõe veia.

## 6. Mãos

- Toda mão em quadro pertence ao avatar e está presa ao braço dele. Mão entrando
  pelo lado da câmera reprova ("can't have 2 hands here").
  Engine com negativo: `only one person, nobody behind the camera, no hands enter
  from the camera side, both hands attached to his own arms`.
  Positivo-only: `one single adult man, exactly two hands with five fingers each,
  both hands attached to his own arms`.
- Key art e capa: `either fully closed fists or hidden, never long spread fingers`.
- Still que vai pra avatar falante (HeyGen e similares): mãos em repouso definido
  (`hands relaxed in lap`). Mão solta no still vira "mão fantasma" e "hand is moving
  too much" no vídeo.

## 7. Still pronto pra avatar falante

- Meio corpo, sentado ou em pé, rosto no terço superior, nada no primeiro plano
  (`clean unobstructed view ... nothing in the foreground`).
- Expressão de quem fala sem boca torta: `serious caring expression with a slight
  reassuring look`; no Soul prefira `soft closed-mouth smile, lips together`.
- Vai pra greenscreen? Fundo verde chapado `#00B140`, trocado no MESMO passo da
  limpeza no GPT Image 2 (uma passada a menos = rosto preservado). O recorte por
  chroma key + despill fica limpo até no cabelo.
- Foto em 4:5 ou 1:1 que precisa virar 9:16: outpaint no Seedream e **cole os pixels
  originais por cima** do resultado. O rosto fica 100% original; só a borda é gerada.

## 8. Lote de personas

- Varie o que o briefing não trava: origem, idade, cabelo, roupa, altura da câmera,
  posição no cômodo, temperatura da luz, intensidade da emoção.
- Fixe o que o briefing trava: cômodo, horário, enquadramento, direção do olhar.
- Não reaproveite o mesmo rosto em marcas diferentes sem pedido explícito.
- Casting por **arquétipo** (autoridade, idade, cenário, tom), nunca copiando uma
  pessoa real de anúncio concorrente.
- Um rosto por gate: sem selfie mestre + sheet aprovados e um still limpo, não escale.
  Rode 1 canário antes do lote pago.
