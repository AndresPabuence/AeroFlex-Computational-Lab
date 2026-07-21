# AeroFlex Prototype Template Generator
# Generates three clean SVG cutting templates.
# Units are centimeters. Print each SVG at 100% scale.

PAGE_W = 42
PAGE_H = 29.7

WING_SPAN = 30
WING_CHORD = 8
WINGTIP_SECTION = 3

WING_X = 5
WING_Y = 7


def svg_header(title):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{PAGE_W}cm" height="{PAGE_H}cm" viewBox="0 0 {PAGE_W} {PAGE_H}">
<rect x="0" y="0" width="{PAGE_W}" height="{PAGE_H}" fill="white"/>
<text x="{PAGE_W / 2}" y="2" font-family="Arial" font-size="0.9" font-weight="bold" text-anchor="middle">{title}</text>
<text x="{PAGE_W / 2}" y="3" font-family="Arial" font-size="0.45" text-anchor="middle">Print at 100% scale. Verify the 5 cm scale box before cutting.</text>
'''


def svg_footer():
    return "</svg>"


def text(x, y, content, size=0.45, weight="normal", anchor="start"):
    return f'<text x="{x}" y="{y}" font-family="Arial" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="black">{content}</text>'


def line(x1, y1, x2, y2, width=0.08, dash=False):
    dash_code = 'stroke-dasharray="0.35,0.25"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="black" stroke-width="{width}" {dash_code}/>'


def rect(x, y, w, h, width=0.10):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="black" stroke-width="{width}"/>'


def path(d, width=0.10):
    return f'<path d="{d}" fill="none" stroke="black" stroke-width="{width}"/>'


def add_measurements(svg):
    # Main labels, kept away from the wing
    svg.append(text(WING_X + WING_SPAN / 2, WING_Y - 0.5, "30 cm wingspan", size=0.42, anchor="middle"))
    svg.append(text(WING_X + WING_SPAN + 0.8, WING_Y + WING_CHORD / 2, "8 cm chord", size=0.42))

    svg.append(text(5, 18.2, "Base dimensions:", size=0.48, weight="bold"))
    svg.append(text(5, 19.0, "- Wingspan: 30 cm", size=0.42))
    svg.append(text(5, 19.7, "- Wing chord: 8 cm", size=0.42))
    svg.append(text(5, 20.4, "- Wingtip section: 3 cm per side", size=0.42))


def add_legend_and_scale(svg):
    # Legend bottom-left
    svg.append(text(5, 23.0, "Legend", size=0.48, weight="bold"))
    svg.append(line(5, 24.0, 8, 24.0, width=0.12))
    svg.append(text(8.6, 24.15, "Cut line", size=0.42))

    svg.append(line(5, 25.2, 8, 25.2, width=0.08, dash=True))
    svg.append(text(8.6, 25.35, "Fold / guide line", size=0.42))

    # Scale box bottom-right
    svg.append(text(27, 23.0, "Scale Check", size=0.48, weight="bold"))
    svg.append(rect(27, 23.6, 5, 5, width=0.08))
    svg.append(text(29.5, 29.0, "5 cm x 5 cm", size=0.40, anchor="middle"))


def create_baseline():
    svg = [svg_header("AeroFlex Baseline Wing Template")]

    svg.append(text(5, 5.4, "Baseline Wing", size=0.60, weight="bold"))
    svg.append(text(5, 6.1, "Straight wing with no wingtip modification.", size=0.42))

    svg.append(rect(WING_X, WING_Y, WING_SPAN, WING_CHORD, width=0.12))

    add_measurements(svg)
    svg.append(text(5, 21.3, "Instruction: cut the rectangle as one straight wing.", size=0.42))

    add_legend_and_scale(svg)
    svg.append(svg_footer())

    with open("baseline_wing_template.svg", "w", encoding="utf-8") as file:
        file.write("\n".join(svg))


def create_simple_wingtip():
    svg = [svg_header("AeroFlex Simple Wingtip Template")]

    svg.append(text(5, 5.4, "Simple Wingtip", size=0.60, weight="bold"))
    svg.append(text(5, 6.1, "Straight wing with both tips folded upward.", size=0.42))

    svg.append(rect(WING_X, WING_Y, WING_SPAN, WING_CHORD, width=0.12))

    left_fold = WING_X + WINGTIP_SECTION
    right_fold = WING_X + WING_SPAN - WINGTIP_SECTION

    svg.append(line(left_fold, WING_Y, left_fold, WING_Y + WING_CHORD, width=0.08, dash=True))
    svg.append(line(right_fold, WING_Y, right_fold, WING_Y + WING_CHORD, width=0.08, dash=True))

    add_measurements(svg)
    svg.append(text(5, 21.3, "Instruction: fold both 3 cm tips upward along the dashed lines.", size=0.42))
    svg.append(text(5, 22.0, "Recommended bend angle: 30 to 45 degrees.", size=0.42))

    add_legend_and_scale(svg)
    svg.append(svg_footer())

    with open("simple_wingtip_template.svg", "w", encoding="utf-8") as file:
        file.write("\n".join(svg))


def create_curved_wingtip():
    svg = [svg_header("AeroFlex Curved Wingtip Template")]

    svg.append(text(5, 5.4, "Curved Wingtip", size=0.60, weight="bold"))
    svg.append(text(5, 6.1, "Straight center wing with smooth rounded tips.", size=0.42))

    center_left = WING_X + WINGTIP_SECTION
    center_right = WING_X + WING_SPAN - WINGTIP_SECTION
    right_edge = WING_X + WING_SPAN

    top = WING_Y
    bottom = WING_Y + WING_CHORD

    outline = (
        f"M {center_left} {top} "
        f"L {center_right} {top} "
        f"C {right_edge} {top}, {right_edge} {bottom}, {center_right} {bottom} "
        f"L {center_left} {bottom} "
        f"C {WING_X} {bottom}, {WING_X} {top}, {center_left} {top} "
        f"Z"
    )

    svg.append(path(outline, width=0.12))

    svg.append(line(center_left, top, center_left, bottom, width=0.08, dash=True))
    svg.append(line(center_right, top, center_right, bottom, width=0.08, dash=True))

    add_measurements(svg)
    svg.append(text(5, 21.3, "Instruction: cut along the outer curved line.", size=0.42))
    svg.append(text(5, 22.0, "Dashed lines are construction guides only.", size=0.42))

    add_legend_and_scale(svg)
    svg.append(svg_footer())

    with open("curved_wingtip_template.svg", "w", encoding="utf-8") as file:
        file.write("\n".join(svg))


if __name__ == "__main__":
    create_baseline()
    create_simple_wingtip()
    create_curved_wingtip()

    print("Generated clean prototype templates:")
    print("- baseline_wing_template.svg")
    print("- simple_wingtip_template.svg")
    print("- curved_wingtip_template.svg")