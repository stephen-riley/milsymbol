from ..components import BBox


def str_width(string, font_size):
    if not string:
        return 0

    # Character widths relative to font size (approximate based on Arial)
    # This matches the JS implementation table
    char_widths = {
        " ": 9,
        "!": 10,
        '"': 15,
        "#": 17,
        "$": 17,
        "%": 27,
        "&": 22,
        "'": 8,
        "(": 10,
        ")": 10,
        "*": 12,
        "+": 18,
        ",": 9,
        "-": 10,
        ".": 9,
        "/": 9,
        "0": 17,
        "1": 17,
        "2": 17,
        "3": 17,
        "4": 17,
        "5": 17,
        "6": 17,
        "7": 17,
        "8": 17,
        "9": 17,
        ":": 10,
        ";": 10,
        "<": 18,
        "=": 18,
        ">": 18,
        "?": 19,
        "@": 30,
        "A": 22,
        "B": 22,
        "C": 22,
        "D": 22,
        "E": 21,
        "F": 19,
        "G": 24,
        "H": 22,
        "I": 9,
        "J": 17,
        "K": 22,
        "L": 19,
        "M": 25,
        "N": 22,
        "O": 24,
        "P": 21,
        "Q": 24,
        "R": 22,
        "S": 21,
        "T": 19,
        "U": 22,
        "V": 21,
        "W": 29,
        "X": 21,
        "Y": 21,
        "Z": 19,
        "[": 10,
        "]": 10,
        "^": 18,
        "_": 17,
        "`": 10,
        "a": 17,
        "b": 19,
        "c": 17,
        "d": 19,
        "e": 17,
        "f": 10,
        "g": 19,
        "h": 19,
        "i": 9,
        "j": 9,
        "k": 17,
        "l": 9,
        "m": 27,
        "n": 19,
        "o": 19,
        "p": 19,
        "q": 19,
        "r": 12,
        "s": 17,
        "t": 10,
        "u": 19,
        "v": 17,
        "w": 24,
        "x": 17,
        "y": 17,
        "z": 15,
        "{": 12,
        "|": 9,
        "}": 12,
        "~": 18,
    }

    width = 0
    for char in string:
        # Default to 28.5 (width of W approx) if unknown
        w = char_widths.get(char, 28.5)
        width += (font_size / 30) * w

    return width


def textfields(symbol):
    metadata = symbol.metadata
    options = symbol.options
    style = symbol.style
    colors = symbol.colors

    # If not enabled, return empty
    if not style.infoFields:
        return {"pre": [], "post": [], "bbox": BBox()}

    bbox = metadata.get("baseGeometry", {}).get("bbox", BBox())
    gbbox = BBox()  # Helper bbox calculating text bounds

    # Inherit existing bbox logic from JS?
    # In JS, gbbox starts empty but merged with labelOverride logic.
    # Here we simplify.

    draw_array = []

    affiliation = metadata.get("affiliation", "Friend")

    font_color = (
        style.infoColor
        if style.infoColor
        else getattr(colors["iconColor"], affiliation, "black")
    )
    # Simplify font color logic
    if isinstance(font_color, dict):
        font_color = font_color.get(affiliation, "black")

    font_family = style.fontfamily
    font_size = style.infoSize
    space_text_icon = 20

    # Mapping fields to positions (L1-L5, R1-R5) based on Standard/Dimension
    g_strings = {
        k: "" for k in ["L1", "L2", "L3", "L4", "L5", "R1", "R2", "R3", "R4", "R5"]
    }

    # Check if we have any text fields to print
    # ... (Skipping full check for brevity, will assume yes if fields exist)

    # Logic for Air (Letter based or Number based)
    is_air = metadata.get("baseDimension") == "Air"
    is_ground = metadata.get("baseDimension") == "Ground" or True  # Default fallback

    if is_air:
        g_strings["R1"] = options.uniqueDesignation
        g_strings["R2"] = options.iffSif
        g_strings["R3"] = options.type
        # ... others

    elif is_ground:
        g_strings["L1"] = options.dtg
        # L2 altitude/location
        l2_parts = []
        if options.altitudeDepth:
            l2_parts.append(options.altitudeDepth)
        if options.location:
            l2_parts.append(options.location)
        g_strings["L2"] = "/".join(l2_parts)

        g_strings["L4"] = options.uniqueDesignation
        g_strings["L5"] = options.speed

        g_strings["R2"] = options.staffComments
        g_strings["R4"] = options.higherFormation

        # R5 Eval rating etc.
        r5_parts = []
        if options.evaluationRating:
            r5_parts.append(options.evaluationRating)
        if options.combatEffectiveness:
            r5_parts.append(options.combatEffectiveness)
        if options.signatureEquipment:
            r5_parts.append(options.signatureEquipment)
        if options.hostile:
            r5_parts.append(options.hostile)
        if options.iffSif:
            r5_parts.append(options.iffSif)
        g_strings["R5"] = "/".join(r5_parts)

        # L3 Type/Platform
        l3_parts = []
        if options.type:
            l3_parts.append(options.type)
        if options.platformType:
            l3_parts.append(options.platformType)
        if options.equipmentTeardownTime:
            l3_parts.append(options.equipmentTeardownTime)
        g_strings["L3"] = "/".join(l3_parts)

        # R1
        if metadata.get("activity"):
            g_strings["R1"] = options.country
        else:
            g_strings["R1"] = options.reinforcedReduced

        # R3
        r3_parts = []
        if options.additionalInformation:
            r3_parts.append(options.additionalInformation)
        if options.commonIdentifier:
            r3_parts.append(options.commonIdentifier)
        g_strings["R3"] = "/".join(r3_parts)

    # Calculate positions
    # JS: gbbox.x1 = bbox.x1 - max(strWidth...)

    # Calculate max widths for layout
    left_width = 0
    right_width = 0

    for k in ["L1", "L2", "L3", "L4", "L5"]:
        w = str_width(g_strings[k], font_size)
        if w > 0:
            left_width = max(left_width, w + space_text_icon)

    for k in ["R1", "R2", "R3", "R4", "R5"]:
        w = str_width(g_strings[k], font_size)
        if w > 0:
            right_width = max(right_width, w + space_text_icon)

    # Update gbbox
    # bbox.x1 is usually around 50-100 depending on symbol? No, bbox is absolute coords?
    # BBox defaults: 100,100,100,100? No.
    # Symbol center is usually 100,100 in milsymbol internal coords.

    # We add text to draw_array

    # L1
    if g_strings["L1"]:
        draw_array.append(
            {
                "type": "text",
                "text": g_strings["L1"],
                "x": bbox.x1 - space_text_icon,
                "y": 100 - 1.5 * font_size,
                "text-anchor": "end",
                "fontsize": font_size,
                "fontfamily": font_family,
                "fill": font_color,
                "stroke": False,
            }
        )
    # L2
    if g_strings["L2"]:
        draw_array.append(
            {
                "type": "text",
                "text": g_strings["L2"],
                "x": bbox.x1 - space_text_icon,
                "y": 100 - 0.5 * font_size,
                "text-anchor": "end",
                "fontsize": font_size,
                "fontfamily": font_family,
                "fill": font_color,
                "stroke": False,
            }
        )
    # L3
    if g_strings["L3"]:
        draw_array.append(
            {
                "type": "text",
                "text": g_strings["L3"],
                "x": bbox.x1 - space_text_icon,
                "y": 100 + 0.5 * font_size,
                "text-anchor": "end",
                "fontsize": font_size,
                "fontfamily": font_family,
                "fill": font_color,
                "stroke": False,
            }
        )
    # L4 (Unique Designation)
    if g_strings["L4"]:
        draw_array.append(
            {
                "type": "text",
                "text": g_strings["L4"],
                "x": bbox.x1 - space_text_icon,
                "y": 100 + 1.5 * font_size,
                "text-anchor": "end",
                "fontsize": font_size,
                "fontfamily": font_family,
                "fill": font_color,
                "stroke": False,
            }
        )
    # L5
    if g_strings["L5"]:
        draw_array.append(
            {
                "type": "text",
                "text": g_strings["L5"],
                "x": bbox.x1 - space_text_icon,
                "y": 100 + 2.5 * font_size,
                "text-anchor": "end",
                "fontsize": font_size,
                "fontfamily": font_family,
                "fill": font_color,
                "stroke": False,
            }
        )

    # R1 (Reinforced/Reduced)
    if g_strings["R1"]:
        draw_array.append(
            {
                "type": "text",
                "text": g_strings["R1"],
                "x": bbox.x2 + space_text_icon,
                "y": 100 - 1.5 * font_size,
                "text-anchor": "start",
                "fontsize": font_size,
                "fontfamily": font_family,
                "fill": font_color,
                "stroke": False,
            }
        )
    # R2
    if g_strings["R2"]:
        draw_array.append(
            {
                "type": "text",
                "text": g_strings["R2"],
                "x": bbox.x2 + space_text_icon,
                "y": 100 - 0.5 * font_size,
                "text-anchor": "start",
                "fontsize": font_size,
                "fontfamily": font_family,
                "fill": font_color,
                "stroke": False,
            }
        )
    # R3
    if g_strings["R3"]:
        draw_array.append(
            {
                "type": "text",
                "text": g_strings["R3"],
                "x": bbox.x2 + space_text_icon,
                "y": 100 + 0.5 * font_size,
                "text-anchor": "start",
                "fontsize": font_size,
                "fontfamily": font_family,
                "fill": font_color,
                "stroke": False,
            }
        )
    # R4
    if g_strings["R4"]:
        draw_array.append(
            {
                "type": "text",
                "text": g_strings["R4"],
                "x": bbox.x2 + space_text_icon,
                "y": 100 + 1.5 * font_size,
                "text-anchor": "start",
                "fontsize": font_size,
                "fontfamily": font_family,
                "fill": font_color,
                "stroke": False,
            }
        )
    # R5
    if g_strings["R5"]:
        draw_array.append(
            {
                "type": "text",
                "text": g_strings["R5"],
                "x": bbox.x2 + space_text_icon,
                "y": 100 + 2.5 * font_size,
                "text-anchor": "start",
                "fontsize": font_size,
                "fontfamily": font_family,
                "fill": font_color,
                "stroke": False,
            }
        )

    # Quantity (Field C) - Top Center
    if options.quantity:
        draw_array.append(
            {
                "type": "text",
                "text": options.quantity,
                "x": 100,
                "y": bbox.y1 - 10,
                "text-anchor": "middle",
                "fontsize": font_size,
                "fontfamily": font_family,
                "fill": font_color,
                "stroke": False,
            }
        )

    # Headquarters Element (Field Q) - Bottom Center
    if options.headquartersElement:
        draw_array.append(
            {
                "type": "text",
                "text": options.headquartersElement,
                "x": 100,
                "y": bbox.y2 + 35,
                "text-anchor": "middle",
                "fontsize": 35,
                "fontfamily": font_family,
                "fontweight": "bold",
                "fill": font_color,
                "stroke": False,
            }
        )

    # Update gbbox
    # x1/x2
    if left_width > 0:
        gbbox.x1 = min(gbbox.x1, bbox.x1 - left_width)
    if right_width > 0:
        gbbox.x2 = max(gbbox.x2, bbox.x2 + right_width)

    # y1/y2
    # Check max vertical usage
    # We use y around 100.
    # Top can be 100 - 2.5 * font_size (if we added L1..L5 logic fully matching JS, but here we used 1.5 and 2.5)
    # L1: -1.5, L2: -0.5, L3: +0.5, L4: +1.5, L5: +2.5
    # The font size is the baseline? BBox needs to cover ascent/descent.
    # Simplified approximation:
    if g_strings["L1"] or g_strings["R1"]:
        # y is 100 - 1.5 * fs. Ascent is approx 1 fs. So top is 100 - 2.5 fs.
        gbbox.y1 = min(gbbox.y1, 100 - 2.5 * font_size)
    if g_strings["L2"] or g_strings["R2"]:
        # y is 100 - 0.5 * fs. Top is 100 - 1.5 fs.
        gbbox.y1 = min(gbbox.y1, 100 - 1.5 * font_size)

    if g_strings["L5"] or g_strings["R5"]:
        gbbox.y2 = max(gbbox.y2, 100 + 3 * font_size)
    elif g_strings["L4"] or g_strings["R4"]:
        gbbox.y2 = max(gbbox.y2, 100 + 2 * font_size)
    elif g_strings["L3"] or g_strings["R3"]:
        gbbox.y2 = max(gbbox.y2, 100 + 1 * font_size)

    # Quantity/HQ
    if options.quantity:
        gbbox.y1 = min(gbbox.y1, bbox.y1 - 10 - font_size)
    if options.headquartersElement:
        gbbox.y2 = max(gbbox.y2, bbox.y2 + 35 + 35)  # + fontsize

    # Return result
    # We return post instructions
    return {"pre": [], "post": draw_array, "bbox": gbbox}
