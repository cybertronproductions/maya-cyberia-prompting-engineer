# Maya Cyberia Prompting Engineer — by Z9

**A regra que muda tudo: não peça beleza, descreva imperfeição.**

Engenharia de prompt de imagem hiper-realista, open source. Tudo que a gente aprendeu
gerando milhares de imagens pra anúncio, UGC, avatar e packshot, empacotado pra rodar
em 3 lugares:

| Onde | Como usar |
|---|---|
| **ChatGPT** (GPT Store) | 👉 **[Abrir a Maya Cyberia no ChatGPT](GPT_LINK)** — de graça, é só clicar |
| **Claude Code** | plugin (instala em 2 comandos, abaixo) |
| **Codex / outro agente** | copia a pasta `skills/maya-cyberia-prompting-engineer` |

Engines cobertas: **Nano Banana**, **GPT Image 2**, **Higgsfield Soul 2.0**, **FLUX.2**,
**Seedream**, Leonardo, Freepik. Detalhe de cada uma (versão,
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

### Seu próprio GPT

Quer montar o seu? Tudo que vai no GPT Builder está em [`chatgpt/`](chatgpt/):
`instructions.md` (cola em Instructions), `knowledge/` (sobe como Knowledge) e
`gpt-config.md` (nome, descrição, conversation starters, foto).

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
Higgsfield Soul 2.0, FLUX.2 and Seedream. MIT licensed.

Feito por **Cyborg Z9** · MIT
