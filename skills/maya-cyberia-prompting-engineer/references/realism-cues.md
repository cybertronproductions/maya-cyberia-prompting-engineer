# Realism Cue Library

Use these as selective visual steering phrases. Choose a coherent lane and use two to six cues, not the entire library.

> **Higgsfield Soul 2.0 (no-negative engine):** do NOT use the `IMG_xxxx.HEIC/.CR2 metadata style` cues,
> `natural skin pores`, `visible skin pores and peach fuzz`, `fine sensor noise`, `no ...` clauses, or the
> "Failure Prevention" negative block below: they render as printed text or corrupt the skin. Use the prose
> equivalents and positive assertions (see `SKILL.md`, Soul 2.0 positive-only mode). On every other engine
> filename tokens are "risky": test one image first (`references/engines-2026.md`).

## Phone and UGC

- `IMG_2985.HEIC metadata style`
- `IMG_4827.HEIC, candid iPhone video still`
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
- `phone not visible, no interface, no screenshot frame`

Use this lane for testimonials, recipes, casual avatars, home scenes, influencer content, and believable social stills.

## RAW Photo and High-End Optics

- `IMG_9854.CR2 metadata style`
- `Canon EOS R5, RF 85mm f/1.2L at f/2`
- `Leica SL2-S, Summilux-M 35mm f/1.4 character`
- `Phase One IQ4 medium-format tonal detail`
- `true optical falloff`
- `natural microcontrast`
- `subtle chromatic aberration at high-contrast edges`
- `realistic highlight roll-off`
- `fine sensor noise in shadow regions`
- `unretouched RAW development`

Use only one camera system in a prompt. Match focal length to the framing: 24-35mm for environmental context, 50mm for natural perspective, 85-105mm for portrait compression, macro lenses for close product detail.

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

Do not request real Getty, magazine, studio, or news-agency watermarks. Do not use `warner bros .com`, movie titles, or archive labels as supposed secret syntax. Translate them into `studio publicity still aesthetic`, `archival production still`, or `big-budget film publicity photography`.

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

- `visible skin pores and peach fuzz`
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

Use imperfections that logically follow from the scene. Avoid adding grime, noise, or blur everywhere.

## Product and Material Realism

- `accurate glass refraction and liquid meniscus`
- `label curvature around cylindrical packaging`
- `realistic specular highlights`
- `micro-scratches on polished metal`
- `soft fingerprints on glossy plastic`
- `fabric weave visible at close range`
- `physically consistent cast shadows`
- `correct contact shadows beneath objects`
- `no duplicated packaging, no fused objects`

## Failure Prevention

Add a short negative block tailored to the scene:

```text
no beauty filter, no plastic skin, no CGI sheen, no duplicate person, no duplicated products, no extra fingers, no malformed hands, no warped face, no impossible reflection, no floating objects, no unreadable labels unless text is intentionally omitted, no captions, no watermark, no logo, no app interface, no phone frame, no collage, no split screen
```

## Principle

Filename tokens such as `IMG_2985.HEIC` and `IMG_9854.CR2` may nudge a model toward familiar camera aesthetics, but they are not verified secret switches and do not create real EXIF metadata. The reliable gains come from the full bundle: coherent capture lane, optics, lighting, texture, imperfection, composition, and constraints.
