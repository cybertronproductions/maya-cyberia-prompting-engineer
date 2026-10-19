#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
forge.py — MAYA CYBERIA PROMPTING ENGINEER
Gerador determinístico de prompts de imagem fotorrealista.
Python puro (stdlib). Roda igual em Claude Code, Codex, Gemini CLI, Hermes.

Uso:
  engines: nano (Nano Banana 2.1 / Seedream), gpt (GPT Image 2.5), soul (Soul 2.0, positivo-only)
  python3 forge.py --recipe editorial --engine soul --subject "24yo italian-latina model, dark hair, blue eyes"
  python3 forge.py --json briefs.example.json --out prompts.txt
  python3 forge.py --list
"""
import argparse
import json
import re
import sys

# ---------------------------------------------------------------- receitas
# Cada receita preenche os 7 blocos do método. Campos sobrescrevíveis
# via CLI/JSON: subject, scene, action, camera, light, imperfection,
# fmt, product, text.

RECIPES = {
    "editorial": {
        "subject": "24yo woman, dark wavy hair, natural makeup",
        "scene": "minimal studio-adjacent office, large window, plants out of focus",
        "action": "seated, caught off-camera mid-conversation, relaxed shoulders",
        "camera": "Canon EOS R5, 85mm f/1.4, compressed perspective, creamy background blur",
        "light": "large window light from camera left, overcast day, soft shadow side toward camera",
        "imperfection": "natural skin texture, visible pores, a few baby hairs at the hairline",
        "fmt": "4:5",
        "meta_token": "IMG_7203.CR2",
        "meta_prose": "unprocessed RAW look, flat neutral color profile, no sharpening",
    },
    "ugc-selfie": {
        "subject": "24yo woman, hair a bit messy from the day",
        "scene": "parked car interior, seatbelt still on, windshield in front",
        "action": "talking to the front camera at arm's length, mid-sentence, one hand gesturing",
        "camera": "iPhone front camera, 26mm equivalent, slight selfie distortion, focus on face",
        "light": "windshield daylight from the front, overcast, soft even light",
        "imperfection": "visible pores, slight under-eye shadows, slightly tilted framing",
        "fmt": "9:16",
        "meta_token": "IMG_2985.HEIC",
        "meta_prose": "unedited smartphone photo, HEIC compression, computational HDR look",
    },
    "paparazzi": {
        "subject": "24yo model, sunglasses pushed up into her hair",
        "scene": "city sidewalk outside a café, midday",
        "action": "caught mid-step leaving the café, looking away from camera",
        "camera": "135mm long-lens compression, shot from across the street",
        "light": "harsh midday sun, hard shadows on the pavement",
        "imperfection": "slight motion blur on the far leg, press photograph framing, wire service crop",
        "fmt": "3:2",
        "meta_token": "IMG_8842.CR2",
        "meta_prose": "press pool photograph look, available light, functional framing",
    },
    "packshot": {
        "subject": "24yo woman, calm morning expression",
        "scene": "bright kitchen counter, morning routine props softly blurred",
        "action": "hand raised at chest height holding the product, looking down at it smiling slightly",
        "camera": "iPhone main camera, 26mm, close focus on the product and hand",
        "light": "window light from the right, soft contact shadow grounding the product",
        "imperfection": "fingerprint smudge on the label edge, natural grip with fingers wrapping the bottle",
        "fmt": "4:5",
        "meta_token": "IMG_3310.HEIC",
        "meta_prose": "unedited smartphone photo look, natural colors",
    },
    "lifestyle": {
        "subject": "24yo woman, oversized grey hoodie",
        "scene": "hotel bed, warm lamp on the nightstand, room service tray at the edge of frame",
        "action": "sitting cross-legged scrolling her phone, one knee up, absorbed",
        "camera": "35mm, waist-up, shot by a friend from the foot of the bed",
        "light": "warm tungsten lamp from the right, rest of the room falling dark",
        "imperfection": "slight grain in the shadows, subject a bit off-center, lint on the hoodie",
        "fmt": "9:16",
        "meta_token": "PIC_20260731_214233.jpg",
        "meta_prose": "casual phone photo at night, higher ISO noise, warm white balance",
    },
    "street": {
        "subject": "24yo woman, denim jacket, tote bag on shoulder",
        "scene": "crosswalk in a busy downtown street, storefronts behind",
        "action": "walking toward camera looking at something off-frame to the left",
        "camera": "35mm at eye level, walking pace, environmental framing",
        "light": "open shade from tall buildings, cool soft light, sunlit background strip",
        "imperfection": "pedestrians motion-blurred behind her, framing slightly rushed",
        "fmt": "3:2",
        "meta_token": "DSCF3302.RAF",
        "meta_prose": "documentary street photo look, film-simulation colors",
    },
    "testimonial": {
        "subject": "24yo woman in a white coat over casual clothes, ID badge slightly crooked",
        "scene": "clean modern clinic hallway, depth falling to soft blur",
        "action": "standing, arms relaxed, caught mid-explanation looking just off-camera",
        "camera": "50mm, waist-up, neutral perspective",
        "light": "ceiling panel light mixed with window daylight, slight shadow under chin",
        "imperfection": "visible skin texture, relaxed mouth, stable neutral pose",
        "fmt": "9:16, first frame of a video",
        "meta_token": "DSC_0231.NEF",
        "meta_prose": "unretouched natural look, neutral color profile",
    },
}

FORBIDDEN = (
    "8k", "masterpiece", "flawless", "perfect skin", "ultra detailed",
)

# ---------------------------------------------------------------- dialetos

def render_nano2(b):
    """Nano Banana 2.1 / Seedream — prosa narrativa contínua, sem tokens."""
    parts = [
        f"A candid photo of a {b['subject']}, in {b['scene']}.",
        f"She is {b['action']}.",
        f"Shot on {b['camera']}.",
        f"{b['light'].capitalize()}.",
        f"{b['imperfection'].capitalize()}.",
        f"{b['meta_prose'].capitalize()}. Aspect {b['fmt']}.",
    ]
    if b.get("text"):
        parts.insert(2, f"Visible text in the scene reads \"{b['text']}\".")
    return " ".join(parts)


def render_gpt2(b):
    """GPT Image 2 — estruturado em seções, texto entre aspas."""
    lines = [
        "Create a photorealistic image.",
        "",
        f"Subject: {b['subject']}.",
        f"Scene: {b['scene']}.",
        f"Action: {b['action']}.",
        f"Camera: {b['camera']}.",
        f"Light: {b['light']}.",
        f"Realism: {b['imperfection']}; {b['meta_prose']}; no beauty retouching.",
        f"Format: {b['fmt']}.",
    ]
    if b.get("text"):
        lines.insert(3, f"Text: render exactly \"{b['text']}\" ({b.get('text_style', 'bold sans-serif')}).")
    return "\n".join(lines)


SOUL_POSES = {
    "A": "both arms relaxed down at her sides, shoulders natural, hands out of frame",
    "B": "one arm extended holding the shot, the other arm hanging relaxed at her side",
    "C": "one hand tucking her hair behind her ear, the other arm down",
    "D": "one hand resting on her hip, weight shifted onto one leg, other arm extended",
    "E": "both hands wrapped around a coffee mug at waist level",
    "F": "one hand holding a phone down at her side, the other arm relaxed",
}
SKIN_LOCK = ("Smooth even skin tone across the face, neck and chest, soft clear skin "
             "surface, uniform complexion, clean retouched photographic finish, soft "
             "diffused front light wrapping the chest, gentle shadow transitions.")
# Soul 2.0 e positivo-only: frases das receitas que viram artefato la sao trocadas.
SOUL_SWAPS = (
    ("talking to the front camera at arm's length, mid-sentence, one hand gesturing",
     "eyes on the lens at arm's length, soft closed-mouth smile, lips together"),
    ("caught mid-explanation looking just off-camera", "soft closed-mouth smile, eyes on the lens"),
    ("mid-sentence", "soft closed-mouth smile"),
    (", ID badge slightly crooked", ""),
    ("visible pores, ", ""), ("visible skin texture, ", ""), ("natural skin texture, ", ""),
    (", visible pores", ""), ("slight grain in the shadows, ", ""),
    (", first frame of a video", ""),
)
# palavras que o Soul 2.0 desenha ou corrompe (doutrina positive-only)
SOUL_FORBIDDEN = (r"no text", r"text", r"caption", r"subtitle", r"watermark", r"logo",
                  r"overlay", r"metadata", r"exif", r"img_\w+", r"\.heic", r"\.cr2",
                  r"video still", r"mid-sentence", r"talking", r"speaking", r"pores",
                  r"grain", r"sensor noise", r"natural skin", r"visible texture",
                  r"badge", r"screenshot")


def render_soul(b):
    """Higgsfield Soul 2.0 — POSITIVO-ONLY. Sem negativo, sem filename/metadata,
    sem texto, sem tokens de pele. Skin Lock e pose opcionais (--skin-lock, --pose)."""
    if b.get("text"):
        sys.exit("BLOQUEADO — Soul 2.0 nao renderiza texto (desenha texto falso). "
                 "Use --engine gpt2 pra texto, ou aplique no editor.")
    f = {k: str(b[k]) for k in ("subject", "scene", "action", "light", "imperfection", "fmt")}
    for old, new in SOUL_SWAPS:
        f = {k: v.replace(old, new) for k, v in f.items()}
    parts = [
        f"{f['fmt']} single photograph of a {f['subject']}.",
        f"{f['scene'].capitalize()}, only one person in the scene.",
        f"{f['action'].capitalize()}.",
    ]
    if b.get("pose"):
        pose = SOUL_POSES.get(str(b["pose"]).upper())
        if not pose:
            sys.exit(f"pose desconhecida: {b['pose']} (use A-F)")
        parts.append(f"POSE: {pose}.")
    if b.get("skin_lock"):
        parts.append(SKIN_LOCK)
    parts += [
        f"{f['light'].capitalize()}, mixed white balance.",
        f"{f['imperfection'].capitalize()}.",
        "Ordinary wide phone lens rendering, authentic still-photo look.",
        "One single adult woman, exactly two hands with five fingers each, "
        "clean simple composition.",
    ]
    out = " ".join(parts)
    bad = sorted({m.group(0) for p in SOUL_FORBIDDEN
                  for m in re.finditer(rf"\b{p}\b" if p[0].isalpha() else p, out, re.I)})
    if bad:
        sys.exit(f"BLOQUEADO — token proibido no Soul 2.0 (positivo-only): {bad}")
    return out



# nano2/gpt2 = nomes antigos (mantidos); nano = Nano Banana 2.1, gpt = GPT Image 2.5
ENGINES = {
    "nano": render_nano2,
    "nano2": render_nano2,
    "gpt": render_gpt2,
    "gpt2": render_gpt2,
    "soul": render_soul,
}

# ---------------------------------------------------------------- núcleo

def build(recipe, engine, overrides=None):
    if recipe not in RECIPES:
        sys.exit(f"receita desconhecida: {recipe} (use --list)")
    if engine not in ENGINES:
        sys.exit(f"engine desconhecida: {engine} (use --list)")
    b = dict(RECIPES[recipe])
    for k, v in (overrides or {}).items():
        if v:
            b[k] = v
    prompt = ENGINES[engine](b)
    low = prompt.lower()
    hits = [w for w in FORBIDDEN if w in low]
    if hits:
        sys.exit(f"BLOQUEADO — termo proibido no prompt: {hits}")
    return prompt


def main():
    p = argparse.ArgumentParser(description="MAYA CYBERIA prompt forge")
    p.add_argument("--recipe", help="receita: " + ", ".join(RECIPES))
    p.add_argument("--engine", help="dialeto: " + ", ".join(ENGINES))
    p.add_argument("--subject")
    p.add_argument("--scene")
    p.add_argument("--action")
    p.add_argument("--light")
    p.add_argument("--text", help="texto literal a renderizar na imagem")
    p.add_argument("--fmt", help="aspect ratio, ex: 9:16")
    p.add_argument("--pose", help="Soul 2.0: pose A-F (gire uma por variante do lote)")
    p.add_argument("--skin-lock", dest="skin_lock", action="store_true",
                   help="Soul 2.0: Skin Lock (obrigatorio em sujeito 45+)")
    p.add_argument("--json", dest="json_path",
                   help="lote: arquivo JSON com lista de briefs")
    p.add_argument("--out", help="grava a saída num arquivo")
    p.add_argument("--list", action="store_true")
    a = p.parse_args()

    if a.list:
        print("receitas:", ", ".join(RECIPES))
        print("engines: ", ", ".join(ENGINES))
        return

    outputs = []
    if a.json_path:
        with open(a.json_path, encoding="utf-8") as f:
            briefs = json.load(f)
        for i, brief in enumerate(briefs, 1):
            recipe = brief.pop("recipe")
            engine = brief.pop("engine")
            label = brief.pop("label", f"brief-{i}")
            prompt = build(recipe, engine, brief)
            outputs.append(f"### {label} [{recipe} / {engine}]\n{prompt}")
    else:
        if not (a.recipe and a.engine):
            p.error("use --recipe e --engine, ou --json, ou --list")
        overrides = {k: getattr(a, k) for k in
                     ("subject", "scene", "action", "light", "text", "fmt",
                      "pose", "skin_lock")}
        outputs.append(build(a.recipe, a.engine, overrides))

    result = "\n\n".join(outputs)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(result + "\n")
        print(f"{len(outputs)} prompt(s) -> {a.out}")
    else:
        print(result)


if __name__ == "__main__":
    main()
