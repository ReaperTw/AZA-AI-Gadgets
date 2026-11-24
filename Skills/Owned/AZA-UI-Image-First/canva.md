# Canva branch

For designs finished in Canva (posters, slides, social posts, covers). The image carries the visuals; every word stays an editable Canva text block. Replaces steps 2–5 of `SKILL.md`; the brief (step 1) still applies, with **Screen** set to the Canva canvas size in px (e.g. 1080×1350 post, 1920×1080 slide).

## 1. Text-free base image

Call `generate_image` for the canvas aspect ratio with a prompt that asks for **no text, letters, or logos** and names the empty zones the text will sit in ("calm empty area in the top third for a headline, clear band at the bottom for details"). When the tool has no size matching the canvas ratio, generate the nearest larger one and center-crop to the canvas px. Pick one of at most two variants and save it as `canva/<name>-base.png`.

Done when the image has no rendered text and every planned zone is visually quiet.

## 2. Text plan

Look at the base image and place each text block over a quiet area. Write `canva/<name>-text.md` as one table, coordinates and font size in canvas px, measured from the top-left (the values Canva's Position panel takes):

| id | text | x | y | w | font | size | weight | color | align |
|---|---|---|---|---|---|---|---|---|---|

Rules for the plan:

- Fonts available in Canva: Noto Sans TC / Noto Serif TC for Chinese, plus one Latin font at most.
- At most three type sizes; headline, body, and small print.
- Each text color has at least 4.5:1 contrast against the image area under it; take colors from the brief's palette.

Done when every word from the brief's **Content** line is in the table.

## 3. Editable layout PDF

Build `canva/<name>.html` at the exact canvas size: the base image as a full-bleed background, each table row as an absolutely positioned text element with its own font, size, and color. Print it to `canva/<name>.pdf` with headless Chrome (`--headless --print-to-pdf --no-pdf-header-footer`), with `@page { size: <W>px <H>px; margin: 0 }` and `html, body { margin: 0; overflow: hidden }` so the page is exactly one canvas. Render a PNG of the same page as `canva/<name>-preview.png` and check it against the plan.

Canva's PDF import turns each text element into its own editable text block over the image, so the user uploads one file and edits words in place.

## 4. Deliver

Hand over:

- `canva/<name>.pdf` — upload to Canva (Upload → the PDF → open as design).
- `canva/<name>-base.png` and `canva/<name>-text.md` — the manual route: set the PNG as background, add one text box per row, and type the row's x / y / w into Position.
- `canva/<name>-preview.png` — what it should look like.

Stop after delivery; the next round starts only when the user approves.
