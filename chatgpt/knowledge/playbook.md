# PLAYBOOK - deep reference

Maya Cyberia Prompting Engineer, by Z9. Load only the section the task needs.

Reading rules:
- If this file disagrees with doctrine.md, doctrine.md wins (it is newer).
- For per-engine specifics, engines-2026.md wins.
- Every final image prompt is written in English, whatever language the user speaks.
- Filename tokens (IMG_2985.HEIC etc.) and "visible pores" in the templates below are for engines that accept them. On Higgsfield Soul 2.0 and any no-negative engine, delete them and follow the Positive-Only Mode in doctrine.md.

---

## 1. Focal length vs. face geometry

Focal length sets the GEOMETRY of the face. Get it wrong and the image looks fake, and no negative prompt can fix it.

| Focal | Distance | Face | Use for |
|-------|----------|------|---------|
| 24-28mm | arm's length | slight stretch, the "selfie face" | selfie, UGC, vlog |
| 35mm | 1-1.5 m | nearly neutral, context visible | street, lifestyle |
| 50mm | 2 m | neutral, human eye | casual portrait |
| 85mm | 3-4 m | compressed, flattering, blurred background | editorial, beauty |
| 135mm+ | far away | strong compression | paparazzi, distant candid |

A selfie with an 85mm face is fake. Paparazzi with 24mm distortion is fake.

## 2. Light recipes (source + direction + quality + temperature)

```
single window light from camera left, overcast, soft wraparound shadows
bare ceiling bulb directly above, hard shadows under eyes, warm tungsten
phone screen glow from below, dark room, cold blue cast on face
golden hour sun low behind subject, rim light on hair, flare bottom-left
on-camera flash, hard frontal light, background falls to black, slight red-eye
windshield daylight from the front, overcast, soft even light   <- the most believable one for UGC
```

Never use `cinematic lighting`, `perfect lighting`, `dramatic lighting`: they are beauty requests in disguise.
Subjects 45+: hard light (bare bulb, bare lamp) exposes veins and texture. Use `soft even front light` / `soft diffused falloff`.

## 3. Skin, texture and operator imperfection

Skin (pick 2-4, subjects under ~40 only): `visible pores on nose and cheeks, slight oiliness on the T-zone, faint dark circles, baby hairs at the hairline, lip lines`
Subjects 45+: do NOT use pore or texture words. They render as veins, leather and premature aging. Use soft diffused light and the Skin Lock from doctrine.md.

Operator (pick 2-3, never more): `slightly tilted framing, subject off-center, mild motion blur on the moving hand, focus missed to the shoulder, cropped at the forehead`

Materials: `fingerprints on the glass, lint on the sweater, scuffed table edge, condensation drops on the bottle`

Grain and sensor noise are optional and must be requested on purpose. Default is a clean natural surface.

## 4. Camera hack library

Filename tokens nudge the model toward a familiar camera aesthetic. They are NOT real EXIF metadata and NOT guaranteed switches. Pro tip: token + a plain-words description of the effect gives the dataset look plus fine control. Use ONE camera system per prompt.

Not for Higgsfield Soul 2.0 or any engine that prints text on the image: there, use only the plain-words description (e.g. "ordinary wide phone lens, mild perspective distortion").

**RAW / camera:** `IMG_4021.CR2` / `.CR3` (Canon) - `DSC_0231.NEF` (Nikon) - `DSC00412.ARW` (Sony) - `DSCF3302.RAF` (Fuji) - `L1004532.DNG` (Leica)

**Phone:** `IMG_2985.HEIC` (iPhone) - `+ flash on` - `night mode photo, handheld` - `0.5x selfie, front ultrawide` - `PIC_20260731_142233.jpg` (Android) - `Screenshot_20260731-214233.png`

**Devices:** `GOPR0142.JPG` (GoPro) - `DJI_0412.JPG` (drone) - `dashcam footage still, timestamp` - `security camera still, high angle, IR grain` - `laptop webcam frame, low resolution, backlit` - `trail camera photo, IR flash`

**Analog film:** `shot on Kodak Portra 400` (warm skin, the favorite) - `CineStill 800T` (night, red halation on neons) - `Kodak Gold 200` (90s vacation) - `Fuji Superia 400` (snapshot) - `disposable camera photo, flash` - `expired film, light leaks` - `instant film photo, white border` (polaroid)

**Cinema / press:** `stills archive` - `film still, 35mm anamorphic, subtle halation` - `press photograph, wire service crop` - `contact sheet scan`

**Social-object images:** `screenshot of an Instagram story, 23:47` - `FaceTime call screenshot` - `Zoom meeting screenshot` - `frame from a vlog, YouTube compression` - `photobooth strip` - `scanned yearbook photo, 1998` - `magazine scan, halftone dots`

Do not request real agency, magazine or studio watermarks. Translate them into neutral aesthetics: `press-photo aesthetic`, `studio publicity still aesthetic`, `archival production still`.

## 5. Text inside the image

- Always put text in quotes: `the label reads "VITAFLOW"`
- Max ~12 words per element; one element at a time when possible.
- Typography like a designer: `bold condensed sans-serif, white on red`
- Critical text -> GPT Image 2. Even better: generate the clean image and add the text in an editor (100% reliable).
- Accents (a with ogonek, o with double acute, c-cedilla, sharp s): GPT Image 2 is fine; FLUX/Leonardo get them wrong, so add text in an editor.
- On Soul 2.0 do not ask for text at all (see doctrine.md); add it afterwards.

## 6. Packshot: product that does not float

- [ ] `soft contact shadow grounding the bottle` (without it the product floats)
- [ ] `subtle reflection on the glossy surface` (if the surface is glossy)
- [ ] `bottle the size of her palm, fingers wrapping naturally` (scale)
- [ ] `label facing camera, slight curve distortion on the text`
- [ ] product light = scene light (same side)

**Inserting a real product (2 steps):**
1) Generate the scene with the hand in position (`hand raised, fingers curled as if holding a bottle`).
2) Insert the product with an edit engine (Nano Banana 2 Pro / GPT Image 2 edit) plus a reference photo: `Place the attached bottle in her hand. Match the window light, add contact shadow, keep face and pose unchanged.`
Never let the engine invent the label from memory.

## 7. Templates (swap the {variables})

**UGC car (the workhorse):**
```
{age}yo {ethnicity} woman, {hair}, sitting in her parked car, seatbelt
still on, talking to the front camera at arm's length, mid-sentence,
one hand gesturing, 26mm selfie distortion, windshield light from the
front, visible pores, slight under-eye shadows, slightly tilted
framing, IMG_2985.HEIC, 9:16
```
Soul 2.0 version: drop `IMG_2985.HEIC`, `visible pores`, `talking`, `mid-sentence`. Use `soft closed-mouth smile, eyes on the lens`, one explicit arm/hand pose, and close with `One single adult woman, exactly two hands with five fingers each, clean simple composition`.

**Authority editorial:**
```
editorial portrait of a {age}yo {profession}, {wardrobe}, seated at a
desk, looking off-camera mid-conversation, Canon EOS R5, 85mm f/1.4,
window light from camera left, natural skin texture, IMG_7203.CR2, 4:5
```

**Paparazzi:**
```
candid paparazzi outtake, {age}yo model leaving a cafe holding {prop},
caught mid-step looking away, 135mm long-lens compression, harsh midday
sun, slight motion blur on the far leg, press photograph framing,
IMG_8842.CR2, wire service crop, 3:2
```

**Story with text (GPT Image 2):**
```
screenshot of an Instagram story, 9:16: casual mirror photo of a {age}yo
woman in gym clothes, bathroom lighting from above, unedited. Story text
overlay in Instagram's default white font reads "{claim, max 8 words}",
time stamp "07:42" top right, recompressed screenshot quality
```

**Talking head (will become video):**
```
{age}yo woman in a white coat, clean modern clinic hallway, arms
relaxed, caught mid-explanation looking just off-camera, 50mm, waist-up,
ceiling panel light mixed with window daylight, visible skin texture,
9:16, first frame of a video
```
`first frame of a video` = neutral pose, relaxed mouth, ready to animate. On Soul 2.0 write `single photograph` instead (the phrase "video still" renders artifacts).

**Night lifestyle:**
```
{age}yo woman, oversized hoodie, sitting cross-legged on a hotel bed
scrolling her phone, warm tungsten lamp from the right, room falling
dark, slight grain in the shadows, lint on the hoodie, off-center
framing, PIC_20260731_214233.jpg, 9:16
```

## 8. Ad compliance (what gets accounts banned in health and supplement ads)

1. **Medical claim in the image.** Platform OCR reads the text INSIDE the creative. Overlays must use personal-experience language ("how I feel at 7am"), never a clinical promise ("burns fat", "cures X").
2. **Celebrity or real-authority face** without consent. Automatic detection plus competitor reports take accounts down. Use your own consistent avatar.
3. **Explicit body before/after.** A pair of compared silhouettes is an automatic flag. What passes: same person, same framing, change of context and energy (tired on the couch -> active in the kitchen).
4. Do not impersonate real brands or use real logos/watermarks.
