# Erros e correções comprovados

Cada linha aconteceu em produção, com imagem reprovada e correção que passou.
Formato: **sintoma → causa → correção**. Consulte antes de reescrever um prompt que
falhou. Lições gerais (regra · por quê) ficam em `lessons.md`.
Última revisão: 2026-10-19.

---

## Texto, UI e objetos que não deviam estar lá

| Sintoma | Causa | Correção |
|---|---|---|
| Soul 2.0 bordou texto falso no jaleco (crachá, bordado) em 2 rodadas | O prompt dizia `no badge, no embroidery, no lanyard ... No text anywhere`: no Soul, nomear é pedir | Não regere. Escolha o still bom e limpe no GPT Image 2 (referência + `keep everything identical`), trocando o fundo pra `#00B140` no mesmo passo se for chroma. Pra próxima: `a plain blank white lab coat with a smooth, clean, unmarked chest` |
| Barra de usuário, selo, ícone de som, moldura de celular | `story`, `TikTok`, `camera roll`, `testimonial`, `RAW iPhone photo`; ou lista de `no app interface, no username bar...` no Soul | Corte as palavras de plataforma. No Soul, abra com `single unedited vertical smartphone photo, one continuous camera frame` e feche com `clean simple composition` |
| Nome de arquivo (`IMG_2985.HEIC`) escrito na imagem | Token de filename no Soul 2.0 | Use a prosa: `unedited smartphone photo` |
| Celular aparece no quadro | `phone propped on the counter` | Não descreva o aparelho; use `front-facing phone-camera POV` |
| Segundo celular, ou produto lido como celular | `phone` repetido, `adjusts her grip` | `filming herself at arm's length`; mão livre com posição definida |
| Telas e placas do fundo cheias de texto ilegível | Nenhuma trava pra painel | `every card, screen, sign and panel ... shows only abstract icons and shapes` |
| Logo de terceiro legível (tênis) | Engine completa marca famosa sozinha | QA de logo em cada still; descarte |
| UI só nas bordas | — | Crop só se não perder rosto e mãos e o still não for animado (crop muda o enquadramento e quebra o vídeo). Senão regere 1x; repetiu, reporte |

## Rosto e identidade

| Sintoma | Causa | Correção |
|---|---|---|
| Nano Banana 2.1 trouxe o homem da 2ª referência | 2 refs de pessoas/frames diferentes | 1 ref (o frame aprovado) + a mudança descrita em texto |
| Still novo por take mudou rosto e enquadramento; objeto some e volta | Gerar still do zero a cada take | Edite o still aprovado; `exact camera distance (do not zoom in or crop, same face size in the frame)` |
| Modelo irreconhecível no 6º take | Encadear último frame de take em take | Todo take parte do still canônico. Last frame só pra mesma ação física contínua |
| Rosto mudou e ganhou grão ao longo das versões | Cadeia longa de regeração (edição da edição) | Volte ao aprovado e faça uma passada só |
| Seedream direto na foto crua: roupa fina, fundo não trocou | Mudança grande demais numa passada | Base intermediária com a roupa já aprovada; depois a cena |
| 5 personagens numa passada bagunçaram o rosto | Muitas refs de identidade de uma vez | Uma mudança grande por passada; extras na 2ª |
| Editor redesenhou a roupa e granulou a pele | Palavra `refine` | Peça a mudança específica, sem `refine` |
| Character sheet com rosto "parecido" | Sheet gerada dentro da ferramenta de vídeo, ou corrigida depois | Gere no GPT Image 2 com a selfie como única identidade; falhou, regere lá |
| Referência com pele danificada contaminou o resultado; `no grain` repetido não limpou | A ref suja controlava rosto e pele | Ref limpa = rosto e pele; ref danificada = só layout, pose e roupa (E13 em `exemplos-aprovados.md`) |

## Pele, corpo e mãos

| Sintoma | Causa | Correção |
|---|---|---|
| Veias, couro, envelhecimento em 45+ | `natural skin pores`, `visible texture`, `grain`, luz de abajur dura | Skin Lock + `soft even front light` |
| Peito vascular ou caído | `heavy`, `heavy breasts`, `full natural breasts` | `big bust with deep cleavage`; descreva a roupa e a silhueta |
| Pele de estúdio, encerada | Filtro de beleza implícito ou prompt de "flawless" | Variação sutil de tom e luz, sem cera, sem poro gravado, sem grão |
| "Fake demais": cabeça torta, mão com bug | Falta de imperfeição física, pose posada | Ação interrompida, 2–3 imperfeições com causa, mãos declaradas |
| Grão demais (4 reprovações num mês) | Cue de filme/filename no ChatGPT; regeração encadeada | Trava anti-grain no ChatGPT; grão leve só na edição |
| Mão de alguém entrando pelo lado da câmera | Engine "completa" quem está filmando | `only one person, nobody behind the camera, both hands attached to his own arms` |
| Mão fantasma e olho fechando no avatar falante | Mão solta no still de partida | Still com mãos em repouso definido (`hands relaxed in lap`) |
| Mesma pose em todo o lote | `hand on chest` / `touching collarbone` | Pose Lock A–F do `SKILL.md` |
| Sorriso largo num médico que devia passar seriedade | Expressão não especificada | `serious caring expression with a slight reassuring look` |
| Poste e objetos no primeiro plano | Cena aberta sem trava | `clean unobstructed view ... nothing in the foreground` |

## Produto

| Sintoma | Causa | Correção |
|---|---|---|
| Rótulo simplificado, verso inventado | A engine desenhou o produto de memória | Produto só com foto oficial; rótulo de frente |
| Frasco pequeno saiu gigante ou duplicado | Escala sem número | Refaça da base sem produto + PNG oficial + escala em % (`packshot-produto.md` §2) |
| Produto colado num dedo | Sem descrição de pegada | `holding with one hand` + física da pegada |
| Produto flutua | Sem sombra de contato | `soft contact shadow`, luz do lado da cena |
| Produto aparece antes da revelação | Referência de produto anexada no keyframe | Não anexe; descreva o estado sem o produto |
| Mesa ignorada na inserção | Posição vaga | 1 retry com `lower center foreground, fully inside the image, not cropped by the edge`; falhou, mude pra na mão |
| Joia ou embalagem diferente em cada frame | Cada insert gerado do zero | A mesma referência de produto em todos |

## Composição e processo

| Sintoma | Causa | Correção |
|---|---|---|
| Persona UGC voltou como thumbnail bonita | Pedido sem formato de captura | `candid vertical smartphone photo`, selfie ou vlog explícito |
| Título da capa cortado no grid | Texto no topo do 9:16 | Rosto a ~1/3 do topo; quinto superior sem letra |
| 40 capas iguais | Mesmo layout em todas | Varie composição, ação, enquadramento e cenário |
| Cena escura, pessoa "colada" no fundo | `cinematic`, `dark moody` | `mid-key, not pitch black` + frase de integração sujeito ↔ fundo |
| Locação muda entre cenas | Cada keyframe sem ref de locação | Keyframe da locação como 2ª ref + `Same room and set as the second reference image` |
| 1º item do lote trava | Ferramenta "esquenta" no primeiro job | Item descartável primeiro (`A plain grey studio backdrop, soft light.`) |
| Prompt longo de inserção falhou à toa | Detalhe demais na 1ª tentativa | Comece pelo prompt curto; escale só no que falhou |
| Filtro de conteúdo recusou demo anatômica | Termo ambíguo | `clinical educational demonstration, no nudity` no fim; ou troque o sujeito |
| Lote histórico com arquitetura moderna e UI falsa | Gate de still pulado | Still limpo aprovado antes de animar; lote reprovado não anima |
| Imagem "completed" tratada como aprovada | Status técnico ≠ QA | Reporte separado: geradas / baixadas / aprovadas / reprovadas |
