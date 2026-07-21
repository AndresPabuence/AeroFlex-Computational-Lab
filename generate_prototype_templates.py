# Generates a simple SVG cutting template for the three AeroFlex prototypes.
# Units are in centimeters. Print at 100% scale if using as a physical template.

svg_width = 36
svg_height = 36

wing_span = 30
wing_chord = 8
wingtip_width = 3

start_x = 3
baseline_y = 3
simple_y = 14
curved_y = 25


def rect(x, y, w, h, stroke="black", fill="none", dash=False):
    dash_style = 'stroke-dasharray="0.3,0.2"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" stroke="{stroke}" fill="{fill}" stroke-width="0.05" {dash_style}/>'


def line(x1, y1, x2, y2, stroke="black", dash=False):
    dash_style = 'stroke-dasharray="0.3,0.2"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="0.04" {dash_style}/>'


def text(x, y, content, size=0.45):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-family="Arial">{content}</text>'


svg = []

svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}cm" height="{svg_height}cm" viewBox="0 0 {svg_width} {svg_height}">')

svg.append(text(3, 1.5, "AeroFlex Prototype Cutting Templates", 0.7))
svg.append(text(3, 2.2, "Use the same base dimensions for all prototypes. Main variable: wingtip shape.", 0.4))

# =========================
# Baseline Wing
# =========================
svg.append(text(start_x, baseline_y - 0.5, "1. Baseline Wing - straight wing, no wingtip modification", 0.45))
svg.append(rect(start_x, baseline_y, wing_span, wing_chord))

svg.append(text(start_x, baseline_y + wing_chord + 0.6, "30 cm wingspan", 0.35))
svg.append(text(start_x + wing_span + 0.3, baseline_y + 4, "8 cm chord", 0.35))

# =========================
# Simple Wingtip
# =========================
svg.append(text(start_x, simple_y - 0.5, "2. Simple Wingtip - fold both tips upward 30 to 45 degrees", 0.45))
svg.append(rect(start_x, simple_y, wing_span, wing_chord))

# Fold lines
svg.append(line(start_x + wingtip_width, simple_y, start_x + wingtip_width, simple_y + wing_chord, dash=True))
svg.append(line(start_x + wing_span - wingtip_width, simple_y, start_x + wing_span - wingtip_width, simple_y + wing_chord, dash=True))

svg.append(text(start_x + 0.3, simple_y + wing_chord + 0.6, "Fold line: 3 cm from each wingtip", 0.35))
svg.append(text(start_x + 11, simple_y + wing_chord + 0.6, "Bend upward: 30 to 45 degrees", 0.35))

# =========================
# Curved Wingtip
# =========================
svg.append(text(start_x, curved_y - 0.5, "3. Curved Wingtip - use smooth curved ends", 0.45))

# Main center wing
center_x = start_x + wingtip_width
center_w = wing_span - 2 * wingtip_width
svg.append(rect(center_x, curved_y, center_w, wing_chord))

# Curved left wingtip path
left_path = (
    f'M {center_x} {curved_y} '
    f'C {start_x + 1.2} {curved_y + 0.5}, {start_x} {curved_y + 2.0}, {start_x} {curved_y + 4.0} '
    f'C {start_x} {curved_y + 6.0}, {start_x + 1.2} {curved_y + 7.5}, {center_x} {curved_y + wing_chord}'
)

# Curved right wingtip path
right_start = start_x + wing_span - wingtip_width
right_end = start_x + wing_span
right_path = (
    f'M {right_start} {curved_y} '
    f'C {right_end - 1.2} {curved_y + 0.5}, {right_end} {curved_y + 2.0}, {right_end} {curved_y + 4.0} '
    f'C {right_end} {curved_y + 6.0}, {right_end - 1.2} {curved_y + 7.5}, {right_start} {curved_y + wing_chord}'
)

svg.append(f'<path d="{left_path}" stroke="black" fill="none" stroke-width="0.05"/>')
svg.append(f'<path d="{right_path}" stroke="black" fill="none" stroke-width="0.05"/>')

# Guide lines
svg.append(line(center_x, curved_y, center_x, curved_y + wing_chord, dash=True))
svg.append(line(right_start, curved_y, right_start, curved_y + wing_chord, dash=True))

svg.append(text(start_x, curved_y + wing_chord + 0.6, "Curved ends should be cut smoothly and kept symmetric.", 0.35))

# Notes
svg.append(text(3, 35, "Note: Verify printed scale with a ruler before cutting physical materials.", 0.4))

svg.append("</svg>")

with open("prototype_cutting_templates.svg", "w") as file:
    file.write("\n".join(svg))

print("Prototype cutting template generated: prototype_cutting_templates.svg")