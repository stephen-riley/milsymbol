import math
from ..components import BBox


def direction(symbol):
    draw_array1 = []
    draw_array2 = []

    metadata = symbol.metadata
    options = symbol.options
    style = symbol.style
    colors = symbol.colors

    # Get base bbox
    bbox = symbol.bbox
    if metadata.get("baseGeometry", {}).get("bbox"):
        bbox = BBox(metadata["baseGeometry"]["bbox"])

    gbbox = BBox()

    # Resolve color
    # JS: this.colors.iconColor[this.metadata.affiliation] || this.colors.iconColor["Friend"]
    acolor = getattr(colors.get("iconColor"), metadata.get("affiliation"), None)
    if not acolor:
        acolor = getattr(colors.get("iconColor"), "Friend", "black")

    if isinstance(
        acolor, dict
    ):  # Should have been resolved by getattr if it was a ColorMode object...
        acolor = acolor.get(metadata.get("affiliation", "Friend"), "black")

    color = acolor

    if style.infoFields and options.direction:
        # Movement indicator
        if options.speedLeader == 0:
            arrow_length = 95

            # The arrow path itself, centered at 100,100 and pointing up?
            # JS: M100,100 l0,-(len-20) ...
            # Then rotated by direction.

            arrow_draw = [
                {
                    "type": "path",
                    "fill": color,
                    "stroke": color,
                    "strokewidth": style.strokeWidth,
                    "d": f"M100,100 l0,-{arrow_length - 20} -5,3 5,-15 5,15 -5,-3",
                }
            ]

            arrow_grp = {
                "type": "rotate",
                "degree": options.direction,
                "x": 100,
                "y": 100,
                "draw": arrow_draw,
            }

            # BBox calculation
            # JS logic converts degrees to radians
            rad = (float(options.direction) / 360) * math.pi * 2

            # Note: JS y axis is down.
            # y1 min (top)
            gbbox.y1 = min(100 - math.cos(rad) * arrow_length, 100)
            gbbox.y2 = max(100 - math.cos(rad) * arrow_length, 100)
            gbbox.x1 = min(100 + math.sin(rad) * arrow_length, 100)
            gbbox.x2 = max(100 + math.sin(rad) * arrow_length, 100)

            # Placement logic
            is_ground = metadata.get("baseDimension") == "Ground" or not metadata.get(
                "baseDimension"
            )
            is_hq = metadata.get("headquarters")

            final_arrow = []

            if is_ground and not is_hq:
                # Translate to bottom of symbol
                final_arrow = [
                    {"type": "translate", "x": 0, "y": bbox.y2, "draw": [arrow_grp]},
                    {
                        "type": "path",
                        "fill": color,
                        "stroke": color,
                        "strokewidth": style.strokeWidth,
                        "d": f"M 100,{bbox.y2} l0,100",  # Vertical line connecting symbol to arrow center(100,100->relative 100,100+y2)
                    },
                ]
                # In JS: arrow is translated by y: bbox.y2.
                # The arrow group is at 100,100.
                # So the center of rotation becomes 100, 100+bbox.y2.
                # And the line is M 100,bbox.y2 l0,100.
                # Wait, "l0,100" means line down 100 units.
                # So it connects (100, bbox.y2) to (100, bbox.y2 + 100).
                # The arrow rotation center is at (100, 100) inside the translated group?
                # Yes. Translate(0, bbox.y2) moves (100,100) to (100, 100+bbox.y2).
                # So the arrow starts appearing at the end of the line.

                # BBox update for the vertical line and translation
                gbbox.y1 += bbox.y2
                gbbox.y2 += bbox.y2
                # x stays centered? No, x offset by translation (0).

                # And the straight line
                gbbox.y2 = max(gbbox.y2, bbox.y2 + 100)

            elif is_hq:
                # Logic for HQ
                # x: bbox.x1 - 100
                # y: bbox.y2 - (100 - hqStaffLength)
                hq_len = style.hqStaffLength or 100  # Default if undefined
                dy = bbox.y2 - (100 - hq_len)
                dx = bbox.x1 - 100

                final_arrow = [
                    {"type": "translate", "x": dx, "y": dy, "draw": [arrow_grp]}
                ]
                gbbox.x1 += dx
                gbbox.x2 += dx
                gbbox.y1 += dy
                gbbox.y2 += dy

            else:
                # Default fallback if neither ground nor HQ?
                # JS `if (baseDim == Ground ...)` block implies others might skip translation?
                # Actually JS only adds to drawArray2 inside that block.
                # Wait, if NOT ground, it behaves differently?
                # The JS code structure:
                # if (Ground or "") { ... calculate arrow ... }
                # drawArray2.push(arrow)
                # If NOT ground, arrow is... undefined?
                # Ah, `arrow` is defined inside the block. If not ground, `arrow` remains `undefined`?
                # No, `var arrow;` at top.
                # `arrow = [...]` assignment is inside the block.
                # So for Air/Sea, `arrow` might be the initial definition?
                # Initial definition: `arrow = [{ type: "rotate"... }]`
                # So if not Ground, it just adds the rotated arrow at 100,100?
                # JS line 42: `arrow = [...]` (The rotated arrow list).
                # JS line 68: `if (Ground...)`.
                # If false, it falls through to line 100 `gbbox.y2 += ...` and `drawArray2.push(arrow)`.
                # So yes, for non-ground, it draws at 100,100.
                final_arrow = [arrow_grp]

            # Add bbox line width padding
            gbbox.y2 += float(style.strokeWidth)

            draw_array2.extend(final_arrow)

        else:
            # Speed Leader unimplemented for now (not requested)
            pass

    return {"pre": draw_array1, "post": draw_array2, "bbox": gbbox}
