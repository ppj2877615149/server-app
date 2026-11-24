#!/usr/bin/env python3
"""Draw the "Server" app icon: a solid navy background with a server rack.

The icon is a flat, geometric server rack (stacked horizontal server blades
with status LEDs) -- no phone shape anywhere. It is generated at 1024x1024
and written to the Xcode asset catalog's single-size app icon slot
(AppIcon-512@2x.png); Xcode derives every smaller size from it at build time.

Run from the repository root (or pass an output path):
    python3 scripts/make_icons.py [output.png]
"""
import os
import sys

from PIL import Image, ImageDraw

SIZE = 1024
BG = (22, 35, 63)          # deep navy, solid background
RACK = (36, 52, 79)         # slate blue-grey cabinet
RACK_EDGE = (61, 84, 120)   # cabinet border
BLADE = (51, 70, 95)        # server blade
BLADE_EDGE = (74, 99, 133)  # blade border
VENT = (30, 43, 66)         # vent slots / drive line
LED_GREEN = (74, 222, 128)
LED_AMBER = (251, 191, 36)


def draw_icon(size=SIZE):
    img = Image.new("RGB", (size, size), BG)
    d = ImageDraw.Draw(img)
    s = size / 1024.0  # scale factor so the drawing works at any size

    # Rack cabinet, centred.
    x0, y0, x1, y1 = 262 * s, 180 * s, 762 * s, 844 * s
    d.rounded_rectangle([x0, y0, x1, y1], radius=36 * s, fill=RACK,
                        outline=RACK_EDGE, width=max(2, int(4 * s)))

    # Four horizontal server blades inside the cabinet.
    blade_h = 120 * s
    gap = 24 * s
    bx0, bx1 = 292 * s, 732 * s
    by = 236 * s
    for _ in range(4):
        d.rounded_rectangle([bx0, by, bx1, by + blade_h], radius=16 * s,
                            fill=BLADE, outline=BLADE_EDGE,
                            width=max(1, int(2 * s)))
        cy = by + blade_h / 2
        # Status LEDs on the left of each blade.
        r = 10 * s
        d.ellipse([322 * s - r, cy - r, 322 * s + r, cy + r], fill=LED_GREEN)
        d.ellipse([352 * s - r, cy - r, 352 * s + r, cy + r], fill=LED_AMBER)
        # Drive-bay line across the middle of the blade.
        d.rounded_rectangle([392 * s, cy - 3 * s, 592 * s, cy + 3 * s],
                            radius=3 * s, fill=VENT)
        # Vent slots on the right of each blade.
        for i in range(3):
            vy = cy - 18 * s + i * 18 * s
            d.rounded_rectangle([622 * s, vy - 3 * s, 702 * s, vy + 3 * s],
                                radius=3 * s, fill=VENT)
        by += blade_h + gap
    return img


def draw_splash(size=2732):
    """A plain solid-navy launch image (no logo, no phone)."""
    return Image.new("RGB", (size, size), BG)


def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    icon_out = os.path.join(
        repo_root, "ios", "App", "App", "Assets.xcassets",
        "AppIcon.appiconset", "AppIcon-512@2x.png")
    os.makedirs(os.path.dirname(icon_out), exist_ok=True)
    draw_icon().save(icon_out, "PNG")
    print("wrote", icon_out)
    splash_dir = os.path.join(
        repo_root, "ios", "App", "App", "Assets.xcassets",
        "Splash.imageset")
    os.makedirs(splash_dir, exist_ok=True)
    splash = draw_splash()
    for name in ("splash-2732x2732.png", "splash-2732x2732-1.png",
                 "splash-2732x2732-2.png"):
        out = os.path.join(splash_dir, name)
        splash.save(out, "PNG")
        print("wrote", out)


if __name__ == "__main__":
    main()
