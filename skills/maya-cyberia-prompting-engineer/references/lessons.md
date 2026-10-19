# Lições de campo (genéricas)

Regras aprendidas gerando imagem real em produção. Formato: **regra · por quê**.
Última verificação: 2026-10-19. Se uma engine mudar de versão, reteste antes de confiar.

## Engine e modo

- **Soul 2.0 é positivo-only: nunca escreva `no X`.** · O Soul lê a negação como o próprio objeto; "no text" desenha texto.
- **Não use filename/metadata (`IMG_2985.HEIC`, `EXIF`) no Soul 2.0.** · Sai impresso na imagem como texto. Em outras engines é empurrão fraco e às vezes também vira texto: na dúvida, use prosa (`unedited smartphone photo`).
- **Texto falso em roupa (crachá, bordado, legenda) aparece no Soul mesmo proibido, em 2 rodadas seguidas.** · Pare de reescrever o prompt. Escolha o still bom e limpe com GPT Image: passe o still como referência + `keep everything identical` e peça só a remoção.
- **Troque o fundo no mesmo passo da limpeza quando for usar chroma key.** · Evita uma segunda passada que degrada o rosto. Peça cor sólida (ex.: verde `#00B140`).
- **Pessoa real em cena nova mantendo o rosto: Seedream 5.0 Pro (2K) ganhou de Grok Imagine 2.0 e Nano Banana num teste de campo (2026-10).** · Mantém o rosto e integra luz e fundo.
- **Prompt de colocar pessoa em cena abre com a ação:** `Place the man from this image into a new scene...`. · Dá a hierarquia certa (imagem = identidade, texto = cena).
- **Evite a palavra `refine` em editor de imagem.** · Em alguns modelos ela faz redesenhar a roupa e acrescenta grão artificial.
- **Trave a roupa pelo nome do material** (`matte black leather jacket`), não por "a mesma roupa". · Modelo troca peça quando a descrição é vaga.
- **Uma mudança grande por passada.** · Cinco referências de personagem numa passada só bagunçaram identidade.
- **Limite de jobs simultâneos existe por plano (8 no plano Plus do Higgsfield em 2026-09).** · Além disso vem `rate_limit_reached`. Erro 503 esporádico: repita só o item que falhou, não o lote.

## Pele, realismo e imperfeição

- **Descreva imperfeição, nunca beleza.** · `8k, masterpiece, flawless` é o sinal mais forte de "cara de IA".
- **Poros e pelos finos só até ~40 anos.** · Em 45+ viram veias, couro e envelhecimento exagerado. Use o Skin Lock (`SKILL.md`) e luz suave e difusa.
- **Luz de abajur duro expõe veias; prefira `soft even front light`.** · Sombra dura revela relevo da pele.
- **ChatGPT/GPT Image: feche todo prompt com a trava anti-grain** (`Clean natural photographic surface, low ISO, smooth tonal transitions, natural skin. No added film grain, sensor noise, crackle or oversharpening.`). · O gerador do ChatGPT tende a granular e afiar demais; cue de filme ou filename piora.
- **Grão e ruído de sensor não são realismo automático.** · Pedir grão, rugas esculpidas ou nitidez extra gera pele corrompida. Padrão limpo e natural; grão só se a estética pedir.
- **Overlay de grão fino leve DEPOIS da geração tira o aspecto plástico de clipe de IA.** · Resolve em pós o que prompt não resolve. Valide em tela de celular.
- **Focal define a geometria do rosto.** · Selfie com cara de 85mm ou paparazzi com distorção de 24mm denunciam a IA; nenhum negativo conserta.
- **2 a 3 imperfeições, nunca mais.** · Muita sujeira/blur/ruído vira estilo, não foto real.

## Identidade e lote

- **Rosto vem só da referência de identidade.** · Referência de roupa/estilo nunca empresta rosto, olho, idade ou proporção.
- **Se a referência de cena tem pele danificada, não repita "no grain" mais forte.** · Mude a estratégia: referência limpa controla rosto e pele; a cena danificada controla só layout, pose e roupa.
- **Em lote, gire a pose (A–F) e declare os dois braços e as duas mãos.** · Escrever `hand on chest` faz o modelo repetir o gesto em todas as variantes.
- **Aprove o still ANTES de animar.** · Still reprovado não pode semear o vídeo pago. Um still limpo não garante frame em movimento limpo: inspecione o vídeo também.
- **Registre o arquivo aprovado e o papel de cada referência.** · Sem isso o lote seguinte reinventa a identidade.
- **Ordem antes de gastar crédito: projeto, identidade, conta e saldo, modelo, custo, 1 canário, só então o lote.** · Timeout não autoriza reenviar; só repita com prova de que o primeiro job falhou.

## Texto, produto e anúncio

- **Texto crítico: entre aspas, ≤12 palavras, 1 elemento por vez.** · Texto longo degrada em qualquer engine.
- **Texto que não pode errar (acento, nome de marca, preço): gere a imagem limpa e aplique no editor.** · 100% confiável; FLUX/Leonardo erram acento.
- **Produto flutua sem sombra de contato.** · Sempre `soft contact shadow` e a luz do produto igual à da cena.
- **Produto real: gere a cena com a mão em posição e insira o produto depois com referência.** · A engine inventa o rótulo de memória.
- **Claim médico no texto da arte derruba conta.** · OCR das plataformas lê o texto dentro da imagem. Use linguagem de experiência pessoal.
- **Antes/depois no mesmo frame, muita pele/barriga em destaque e marca de terceiro visível reprovam anúncio.** · São gatilhos automáticos de revisão em plataformas de anúncio.
- **A imagem tem que bater com a fala e com o público.** · Dor/dieta → pessoa compatível com a dor; resultado/desejo → pessoa do resultado. Ingrediente na tela = ingrediente da oferta.
- **Conferir o prompt literal na caixa antes de enviar quando a ferramenta tem modo direto.** · Erro de colagem ou prefixo repetido manda a imagem errada e queima crédito.

## Processo

- **Gere 4 opções, pegue a primeira boa, não a "quase".** · Iterar em cima de uma imagem ruim custa mais que gerar de novo.
- **Escreva a cena completa: quem, onde, emoção, luz, câmera/lente, proporção (9:16 pra vertical).** · Prompt curto delega a escolha ao modelo e volta com o padrão genérico.
- **Corrija a engine antes de corrigir o prompt.** · Se 2 rodadas de prompt não resolveram, a tarefa está na engine errada.
