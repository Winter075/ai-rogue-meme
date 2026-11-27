"""Draw the rogue-agent meme as a clean flat-vector PNG, entirely in code."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
CREAM = (246, 241, 228)
INK = (27, 38, 54)
TEAL = (32, 74, 84)
CYAN = (139, 233, 240)
ORANGE = (226, 137, 76)
PAPER = (255, 252, 244)
RED = (198, 68, 64)

IMPACT = "C:/Windows/Fonts/impact.ttf"
BOLD = "C:/Windows/Fonts/arialbd.ttf"


def fit_font(draw, text, path, size, max_width):
    while size > 12:
        font = ImageFont.truetype(path, size)
        if draw.textbbox((0, 0), text, font=font)[2] <= max_width:
            return font
        size -= 2
    return ImageFont.truetype(path, size)


def caption(draw, text, y, size):
    font = fit_font(draw, text, IMPACT, size, W - 60)
    box = draw.textbbox((0, 0), text, font=font)
    x = (W - (box[2] - box[0])) / 2 - box[0]
    draw.text(
        (x, y),
        text,
        font=font,
        fill=INK,
        stroke_width=6,
        stroke_fill=CREAM,
    )


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    # Top and bottom caption bands.
    d.rectangle((0, 0, W, 18), fill=INK)
    d.rectangle((0, H - 18, W, H), fill=INK)
    caption(d, "MY AI AGENT WENT ROGUE", 38, 78)
    caption(d, "IT PROMOTED ITSELF", 828, 70)
    caption(d, "AND MADE ME THE INTERN", 902, 70)

    # Floor shadow and desk.
    d.ellipse((130, 700, 900, 748), fill=(223, 214, 195))
    d.rounded_rectangle((120, 636, 904, 700), radius=14, fill=(150, 105, 72), outline=INK, width=6)
    d.rounded_rectangle((120, 636, 904, 654), radius=8, fill=(190, 143, 100), outline=INK, width=4)

    # Tired human on the left, buried under folders.
    d.rounded_rectangle((196, 430, 360, 636), radius=34, fill=ORANGE, outline=INK, width=7)
    d.ellipse((224, 344, 336, 456), fill=(238, 197, 163), outline=INK, width=7)
    d.arc((224, 330, 336, 430), 180, 360, fill=INK, width=9)  # hood
    d.line((250, 392, 268, 392), fill=INK, width=7)  # tired eyes
    d.line((294, 392, 312, 392), fill=INK, width=7)
    d.arc((270, 412, 300, 432), 200, 340, fill=INK, width=6)
    d.polygon([(196, 470), (150, 560), (206, 580)], fill=ORANGE, outline=INK)
    d.polygon([(360, 470), (410, 560), (352, 580)], fill=ORANGE, outline=INK)
    for i, colour in enumerate(((240, 226, 190), (255, 252, 244), (222, 205, 170))):
        y = 470 + i * 46
        d.rounded_rectangle((246, y, 404, y + 54), radius=6, fill=colour, outline=INK, width=5)
        d.line((258, y + 16, 386, y + 16), fill=RED, width=4)
    d.ellipse((392, 316, 406, 330), fill=CYAN, outline=INK, width=3)  # sweat drop

    # Executive chair behind the robot.
    d.rounded_rectangle((596, 300, 880, 636), radius=42, fill=TEAL, outline=INK, width=8)
    d.rounded_rectangle((630, 336, 846, 470), radius=28, fill=(44, 94, 102), outline=INK, width=5)
    d.line((738, 636, 738, 700), fill=INK, width=12)
    for dx in (-56, 0, 56):
        d.line((738, 694, 738 + dx, 722), fill=INK, width=9)
        d.ellipse((738 + dx - 12, 714, 738 + dx + 12, 738), fill=INK)
    d.rounded_rectangle((596, 470, 636, 556), radius=18, fill=TEAL, outline=INK, width=6)
    d.rounded_rectangle((840, 470, 880, 556), radius=18, fill=TEAL, outline=INK, width=6)

    # The smug robot, feet up, coffee in hand.
    d.rounded_rectangle((636, 388, 840, 592), radius=30, fill=(228, 233, 236), outline=INK, width=8)
    d.rounded_rectangle((654, 408, 822, 500), radius=20, fill=CYAN, outline=INK, width=6)
    d.ellipse((688, 436, 706, 454), fill=INK)  # eyes
    d.ellipse((770, 436, 788, 454), fill=INK)
    d.arc((716, 444, 762, 484), 15, 165, fill=INK, width=6)  # smug grin
    d.line((738, 388, 738, 356), fill=INK, width=8)
    d.ellipse((726, 336, 750, 360), fill=RED, outline=INK, width=4)
    d.line((840, 470, 896, 520), fill=(228, 233, 236), width=22)
    d.ellipse((888, 500, 940, 552), fill=PAPER, outline=INK, width=6)
    d.arc((900, 480, 916, 508), 20, 160, fill=INK, width=4)  # coffee steam
    d.arc((918, 476, 936, 508), 20, 160, fill=INK, width=4)
    d.line((700, 592, 660, 648), fill=(228, 233, 236), width=24)
    d.line((780, 592, 826, 642), fill=(228, 233, 236), width=24)
    d.rounded_rectangle((612, 632, 700, 662), radius=14, fill=INK)
    d.rounded_rectangle((802, 628, 890, 658), radius=14, fill=INK)

    # Name plaque on the desk: the punchline's final prop.
    d.rounded_rectangle((560, 664, 812, 714), radius=10, fill=PAPER, outline=INK, width=6)
    plaque = ImageFont.truetype(BOLD, 34)
    bbox = d.textbbox((0, 0), "MANAGER", font=plaque)
    d.text((686 - (bbox[2] - bbox[0]) / 2, 674), "MANAGER", font=plaque, fill=INK)

    target = Path(__file__).with_name("entry.png")
    img.save(target, optimize=True)
    print("wrote", target, img.size)


if __name__ == "__main__":
    main()
