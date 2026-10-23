# Maya Cyberia Prompting Engineer — by Z9

**A regra que muda tudo: não peça beleza, descreva imperfeição.**

Engenharia de prompt de imagem hiper-realista, open source. Tudo que a gente aprendeu
gerando milhares de imagens pra anúncio, UGC, avatar e packshot, empacotado pra rodar
em 3 lugares:

## ⚡ Instala em 10 segundos: solta no seu agente

Copia a frase abaixo e cola no seu agente (Claude Code, Codex, Cursor, Gemini CLI, qualquer um que use skills):

```
Instala a skill Maya Cyberia Prompting Engineer pra mim: baixa https://github.com/cybertronproductions/maya-cyberia-prompting-engineer/releases/latest/download/maya-cyberia-1.0.0.zip, descompacta e copia a pasta skills/maya-cyberia-prompting-engineer inteira pra pasta de skills do agente que você é (Claude Code: ~/.claude/skills/ · Codex: ~/.codex/skills/ · outro: a pasta de skills dele). Depois lê o SKILL.md e me confirma que a Maya Cyberia tá instalada.
```

Pronto. Depois é só pedir: *"maya cyberia, prompt de selfie UGC de uma mulher de 30 anos na cozinha"*.

Engines cobertas: **Nano Banana**, **GPT Image 2**, **Higgsfield Soul 2.0** e
**Seedream**. Detalhe de cada uma (versão,
dialeto, se aceita negative prompt, se o hack de metadados funciona) em
[`references/engines-2026.md`](skills/maya-cyberia-prompting-engineer/references/engines-2026.md).

---

## O método em 30 segundos

Todo prompt tem 7 blocos:

1. **Sujeito** — idade + etnia + 2 traços
2. **Cena** — com desgaste e época (`90s tile, magnets on the fridge`)
3. **Ação candid** — nunca "posing" (`caught mid-laugh, eyes off-camera`)
4. **Câmera** — focal coerente (selfie 24–28mm · editorial 85mm · paparazzi 135mm)
5. **Luz** — fonte + direção + qualidade (`window light from the left, overcast`)
6. **Imperfeição** — 2 a 3, nunca mais (`visible pores, slight motion blur`)
7. **Formato** — aspect ratio + hack de câmera (`9:16, IMG_2985.HEIC`)

Os blocos 5 e 6 carregam 70% do realismo. `8k, masterpiece, flawless, perfect skin` = cara de IA na hora.

### O hack dos metadados

Escrever o nome de arquivo que a câmera real gera (`IMG_2985.HEIC` do iPhone, `IMG_9854.CR2`
da Canon, `DSC00412.ARW` da Sony, `DSCF3302.RAF` da Fuji) puxa o modelo pra estética daquela
câmera. Aprendi com o canal **Metrimule** lá atrás e refinei testando.

⚠️ **Não funciona em toda engine.** No Higgsfield Soul 2.0 o nome do arquivo aparece *escrito*
na imagem. Lá o caminho é o modo positivo (sem negative prompt, sem "no ..."). Tabela completa
em `engines-2026.md`.

---

## Instalar

### Claude.ai (upload de skill)

[Baixar maya-cyberia-skill.zip](https://cybertronproductions.github.io/maya-cyberia-prompting-engineer/maya-cyberia-skill.zip).
Envie esse ZIP, sem descompactar, em **Personalizar → Skills → Adicionar**
(em algumas versões: **Configurações → Capacidades → Skills**) e ative a skill.
O ZIP contém a pasta da skill diretamente na raiz. A disponibilidade depende da sua conta e das permissões do workspace.

### ChatGPT (Projeto)

[Baixar o pacote para Projeto do ChatGPT](https://cybertronproductions.github.io/maya-cyberia-prompting-engineer/maya-cyberia-chatgpt-projeto.zip) e descompactar.
Crie um projeto chamado **Maya Cyberia**, cole `instructions.md` nas instruções do projeto
e adicione os quatro arquivos de `knowledge/`. Converse com a Maya dentro desse projeto.
O pacote inclui `LEIA-ME.txt` com o passo a passo. Um chat comum aberto por link não instala a Cyberia.

### Claude Code (plugin)

```
/plugin marketplace add cybertronproductions/maya-cyberia-prompting-engineer
/plugin install maya-cyberia@maya-cyberia
```

Depois é só pedir: *"maya cyberia, prompt de selfie UGC de uma mulher de 30 anos na cozinha"*.

### Codex

```bash
git clone https://github.com/cybertronproductions/maya-cyberia-prompting-engineer
cp -r maya-cyberia-prompting-engineer/skills/maya-cyberia-prompting-engineer ~/.codex/skills/
```

### CLI de lote (opcional)

```bash
python skills/maya-cyberia-prompting-engineer/scripts/forge.py --list
python skills/maya-cyberia-prompting-engineer/scripts/forge.py --recipe ugc-selfie --engine nano
python skills/maya-cyberia-prompting-engineer/scripts/forge.py --json skills/maya-cyberia-prompting-engineer/scripts/briefs.example.json --out prompts.txt
```

---

## O que tem aqui

```
skills/maya-cyberia-prompting-engineer/
  SKILL.md                    o método (o agente lê isso primeiro)
  PLAYBOOK.md                 focal x rosto, receitas de luz, hacks, templates de anúncio
  references/engines-2026.md  cada engine hoje: versão, dialeto, o que funciona
  references/realism-cues.md  biblioteca de pistas de realismo
  references/lessons.md       lições que custaram crédito pra aprender
  references/realismo-iphone-paparazzi.md   selfie, UGC, candid, câmera escondida
  references/avatar-influencer.md           persona recorrente, character sheet, avatar falante
  references/packshot-produto.md            produto na mão/mesa, escala em %, rótulo
  references/criativo-dtc.md                anúncio, cena de prova, capa, compliance
  references/erros-e-correcoes.md           sintoma → causa → correção, tudo testado
  references/exemplos-aprovados.md          14 prompts literais com status
  scripts/forge.py            gera prompt pronto (receita x engine)
chatgpt/                      pacote do GPT (instructions + knowledge + config)
```

## Regras fixas

- Prompt final sempre em inglês (a conversa pode ser em português)
- Só adultos. Nunca pessoa real identificável sem autorização
- Criativo de anúncio: zero promessa médica escrita na imagem (o OCR das plataformas lê tudo)

## Contribuir

Achou um token que funciona, ou uma engine que mudou? Abre uma issue ou PR com
**prompt + engine + imagem antes/depois**. Sem prova, não entra.

---

**English:** open-source hyper-realistic image prompt engineering skill for ChatGPT, Claude Code
and Codex. Core rule: *don't ask for beauty, describe imperfection.* 7-block method, camera
filename hacks (with per-engine caveats), engine dialects for Nano Banana, GPT Image 2,
Higgsfield Soul 2.0 and Seedream. MIT licensed.

Feito por **Cyborg Z9** · MIT

## Conferir os downloads

Os pacotes e seus hashes SHA-256 ficam na [release mais recente](https://github.com/cybertronproductions/maya-cyberia-prompting-engineer/releases/latest).
O arquivo `maya-cyberia-1.0.0.zip` nesse endereço é mantido como alias compatível para os links de instalação já divulgados; a versão real está no `plugin.json` dentro dele.
Para reconstruir os pacotes a partir deste repositório: `python scripts/package_release.py`.
O script usa apenas Python padrão, preserva o corpo da skill e os prompts e verifica o conteúdo de cada ZIP.
