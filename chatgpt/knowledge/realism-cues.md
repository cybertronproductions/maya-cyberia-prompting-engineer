# Realism Cue Library

Selective visual steering phrases. Choose ONE coherent capture lane and use two to six cues, never the whole library.

Engine notes (doctrine.md wins on conflicts):
- Cues that are negations ("no interface", "no phone frame", "no captions") and any filename/metadata token (`IMG_2985.HEIC`, `IMG_9854.CR2`) are for negative-capable engines only. On Higgsfield Soul 2.0 and other no-negative engines they render as printed text or the very thing they name. Use the plain-words equivalents.
- Pore and fine-hair cues are for subjects under ~40. On 45+ subjects use soft diffused light and a clean even skin description instead (see doctrine.md, Skin Lock).

## Phone and UGC

- `IMG_2985.HEIC metadata style` (negative-capable engines only)
- `IMG_4827.HEIC, candid iPhone video still` (negative-capable engines only; on Soul 2.0 say `single photograph`)
- `ordinary wide phone lens`
- `slight front-camera or back-camera perspective distortion`
- `subtle focus inconsistency`
- `realistic smartphone compression`
- `uneven automatic exposure`
- `mixed automatic white balance`
- `Smart HDR restraint`
- `gentle motion softness`
- `handheld framing with imperfect symmetry`
- `unedited domestic footage`
- `phone not visible, no interface, no screenshot frame` (negative-capable engines only)

Use this lane for testimonials, recipes, casual avatars, home scenes, influencer content and believable social stills.

## RAW Photo and High-End Optics

- `IMG_9854.CR2 metadata style` (negative-capable engines only)
- `Canon EOS R5, RF 85mm f/1.2L at f/2`
- `Leica SL2-S, Summilux-M 35mm f/1.4 character`
- `Phase One IQ4 medium-format tonal detail`
- `true optical falloff`
- `natural microcontrast`
- `subtle chromatic aberration at high-contrast edges`
- `realistic highlight roll-off`
- `fine sensor noise in shadow regions` (optional; clean surfaces are the default)
- `unretouched RAW development`

Use only one camera system per prompt. Match focal length to framing: 24-35mm for environmental context, 50mm for natural perspective, 85-105mm for portrait compression, macro lenses for close product detail.

## Editorial and Paparazzi

- `candid paparazzi outtake`
- `editorial outtake between posed frames`
- `press-photo aesthetic`
- `contact sheet scan aesthetic`
- `behind-the-scenes publicity still`
- `on-camera flash with hard falloff`
- `slightly missed framing`
- `subject caught mid-expression`
- `ambient crowd occlusion`
- `wire-service documentary composition`

Do not request real news-agency, magazine or studio watermarks. Do not use studio domains, movie titles or archive labels as supposed secret syntax. Translate them into `studio publicity still aesthetic`, `archival production still` or `big-budget film publicity photography`.

## Cinema Still

- `archival production still aesthetic`
- `big-budget narrative film frame`
- `practical lights visible in the scene`
- `motivated key light`
- `subtle halation around highlights`
- `controlled film grain`
- `cinema-lens edge softness`
- `production-designed environment`
- `naturalistic blocking`
- `frame captured between lines of dialogue`

Use cinema cues only when the user wants a produced film image. Do not mix them into ordinary phone footage.

## Physical Imperfections

- `visible skin pores and peach fuzz` (under ~40 only)
- `subtle facial asymmetry`
- `tiny flyaway hairs`
- `fabric fibers and seam tension`
- `fingerprints and faint smudges on glass`
- `minor wrinkles in clothing`
- `irregular window shadows`
- `mixed indoor and daylight color temperature`
- `small exposure clipping in bright windows`
- `realistic mirror geometry and parallax`
- `lived-in background without staged clutter`

Use imperfections that follow logically from the scene. Never add grime, noise or blur everywhere. Two or three is the limit.

## Product and Material Realism

- `accurate glass refraction and liquid meniscus`
- `label curvature around cylindrical packaging`
- `realistic specular highlights`
- `micro-scratches on polished metal`
- `soft fingerprints on glossy plastic`
- `fabric weave visible at close range`
- `physically consistent cast shadows`
- `correct contact shadows beneath objects`
- `no duplicated packaging, no fused objects` (negative-capable engines; on Soul 2.0 write `one single product, clean simple composition`)

## Failure Prevention

Negative-capable engines (Nano Banana 2.1, GPT Image, Seedream): add a short negative block tailored to the scene:

```text
no beauty filter, no plastic skin, no CGI sheen, no duplicate person, no duplicated products, no extra fingers, no malformed hands, no warped face, no impossible reflection, no floating objects, no unreadable labels unless text is intentionally omitted, no captions, no watermark, no logo, no app interface, no phone frame, no collage, no split screen
```

No-negative engines (Higgsfield Soul 2.0): never use the block above. Fold the same intent into positive assertions:

```text
One single adult, exactly two hands with five fingers each, one single product with a clean readable label area, clean simple composition, soft even light, single photograph
```

## Principle

Filename tokens such as `IMG_2985.HEIC` and `IMG_9854.CR2` may nudge a model toward familiar camera aesthetics, but they are not verified secret switches and they do not create real EXIF metadata. The reliable gains come from the full bundle: a coherent capture lane, optics, lighting, texture, imperfection, composition and constraints.
