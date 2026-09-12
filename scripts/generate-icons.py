#!/usr/bin/env python3
"""Rasterize the OutOf0 symbol into the icon files the site serves.

Source of truth is `brand/logos/symbol-reverse.svg` (ink background, white ring,
signal-green arrow). The geometry below is that SVG transcribed into PIL draw
calls — keep the two in sync if the symbol ever changes.

Requires Pillow (`python3 -m pip install pillow`). Not a project dependency;
this is a one-off asset build, run by hand when the symbol changes:

    python3 scripts/generate-icons.py

Outputs:
    public/favicon.ico          16 / 32 / 48 px, opaque ink
    public/apple-touch-icon.png 180 px, opaque ink
"""
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw

REPO = Path(__file__).resolve().parent.parent

INK = (11, 13, 15, 255)          # #0B0D0F
WHITE = (255, 255, 255, 255)
SIGNAL = (57, 255, 20, 255)      # #39FF14

# Symbol geometry, in the SVG's 64x64 coordinate space.
# PIL draws an outline *inward* from the bbox, while SVG centres the stroke on the
# path — so the ellipse bbox is grown by STROKE/2 to land on the same outer edge.
ELLIPSE = (13 - 7, 9 - 7, 45 + 7, 55 + 7)
STROKE = 14
NOTCH = [(41, 32), (56, 22), (56, 42)]
ARROW = [(43.5, 32), (54, 25.5), (54, 38.5)]

# Mark bounds including the stroke.
MARK = (6.0, 2.0, 56.0, 62.0)
SUPERSAMPLE = 4


def render(size: int, pad_ratio: float = 0.1) -> Image.Image:
    """Draw the mark on an opaque ink square of `size` px."""
    s = size * SUPERSAMPLE
    pad = s * pad_ratio
    scale = (s - 2 * pad) / (MARK[3] - MARK[1])
    ox = (s - (MARK[2] - MARK[0]) * scale) / 2 - MARK[0] * scale
    oy = pad - MARK[1] * scale

    def pt(p):
        return (ox + p[0] * scale, oy + p[1] * scale)

    img = Image.new("RGBA", (s, s), INK)
    d = ImageDraw.Draw(img)
    d.ellipse([pt((ELLIPSE[0], ELLIPSE[1])), pt((ELLIPSE[2], ELLIPSE[3]))],
              outline=WHITE, width=round(STROKE * scale))
    d.polygon([pt(p) for p in NOTCH], fill=INK)
    d.polygon([pt(p) for p in ARROW], fill=SIGNAL)

    return img.resize((size, size), Image.LANCZOS)


def main() -> None:
    (REPO / "public" / "apple-touch-icon.png").parent.mkdir(parents=True, exist_ok=True)

    ico = render(256)
    ico.save(REPO / "public" / "favicon.ico",
             sizes=[(16, 16), (32, 32), (48, 48)])
    render(180).convert("RGB").save(REPO / "public" / "apple-touch-icon.png")

    for name in ("favicon.ico", "apple-touch-icon.png"):
        p = REPO / "public" / name
        print(f"wrote {p.relative_to(REPO)}  {p.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
