---
name: AZA-UI-Image-First
description: Image-first visual workflow — generate the design with the generate_image tool first, then build to match it. Use when a task creates or restyles a page, screen, layout, or visual component, or makes a Canva design (poster, slide, social post) whose text must stay editable.
license: MIT
metadata:
  author: Azazel
  version: "1.0.0"
---

# AZA-UI-Image-First

The image is the design; the code is its implementation. The mockup comes first, every run, before any UI code is written.

When the result is finished in Canva, do step 1 here, then follow [canva.md](canva.md) for the rest.

## 1. Brief

Read the project's existing styles first (CSS variables, theme files, component library, fonts). Then write a brief of five lines:

- **Screen**: which page or component, and its viewport (desktop 1440×900 or mobile 390×844).
- **Content**: the real labels, headings, and data the screen shows, in the UI's language.
- **Direction**: one leading word for the look (editorial, calm, dense, playful…) plus the palette.
- **Constraints**: existing tokens and components the design must reuse.
- **States**: which state this image shows (default, empty, loading, error).

Done when all five lines are filled from the ticket or the codebase.

## 2. Mockup

Call `generate_image` with the brief as the prompt: one screen per image, real labels, flat UI screenshot style, the stated viewport. Generate at most two variants and pick one.

Copy the chosen image into the project at `design/mockups/<screen>.png`.

If `generate_image` is unavailable or fails, report the tool error as the run's result and stop. The image step is the guarantee this skill exists for.

If the ticket says "concept only", deliver the image path and stop here.

## 3. Spec

Read the image and write `design/mockups/<screen>.md`:

- Layout: grid, column widths, section order.
- Colors: hex values, each mapped to an existing token where one is close.
- Type: font families, sizes, weights per level.
- Spacing and radius scale.
- Components: every visible element, each marked reuse-existing or new.

Done when every visible element in the image appears in the component list.

## 4. Build

Implement against the spec, reusing the project's tokens and components. Treat the image as the target for layout, hierarchy, and color; keep real behaviour and accessibility from the codebase.

## 5. Compare

Screenshot the result at the brief's viewport using a headless browser (background only). Place it beside the mockup in one image at `design/mockups/<screen>-compare.png` and list the differences.

Fix the differences in layout, hierarchy, and color, for at most two rounds. Then deliver:

- the mockup path, the comparison image path,
- the remaining differences, each with the reason it stays.

Stop after delivery; the next round starts only when the user approves.
