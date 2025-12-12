
from .common import text, textm1, textm2

def define_subsurface_icons(icon_parts, metadata, colors, std2525):
    frame = metadata.get("frame")
    affiliation = metadata.get("affiliation", "Friend")
    
    icon_color = colors["iconColor"][affiliation]
    icon_fill_color = colors["iconFillColor"][affiliation]
    white = colors["white"][affiliation]
    black = colors["black"][affiliation]
    
    icn = {}

    icn["SU.IC.MILITARY"] = text("MIL")
    icn["SU.IC.CIVILIAN"] = text("CIV")
    # ...
    
    icn["SU.IC.SUBMARINE"] = {
        "type": "path",
        "d": "m 75,85 50,0 15,15 -15,15 -50,0 -15,-15 z"
    }

    icn["SU.IC.SUBMARINE CONVENTIONAL PROPULSION"] = {
        "type": "path",
        "d": "m 75,110 -10,-10 10,-10 20,0 0,-10 10,0 0,10 20,0 10,10 -10,10 z"
    }

    icn["SU.IC.SUBMARINE NUCLEAR PROPULSION"] = {
        "type": "path",
        "d": "m 75,110 -10,-10 10,-10 0,-10 50,0 0,10 10,10 -10,10 z"
    }
    
    icn["SU.IC.SUBMARINE, SURFACED"] = [
        {"type": "path", "d": "m 75,80 50,0 15,15 -15,15 -50,0 -15,-15 z"},
        {"type": "path", "fill": False, "d": "m 65,120 10,-10 10,10 10,-10 10,10 10,-10 10,10 10,-10"}
    ]
    
    icn["SU.IC.SUBMARINE, SNORKELING"] = [
        {"type": "path", "d": "m 75,120 -10,-10 10,-10 20,0 0,-20 10,0 0,20 20,0 10,10 -10,10 z"},
        {"type": "path", "fill": False, "d": "m 65,95 10,-10 10,10 10,-10 10,10 10,-10 10,10 10,-10"}
    ]

    # Modifiers
    icn["SU.IC.SUBMARINE ATTACK (SSN)"] = {
        "type": "text", "fill": white, "stroke": False, "x": 100, "y": 110, "fontsize": 30, "text": "A"
    }
    icn["SU.IC.SUBMARINE BALLISTIC MISSILE (SSBN)"] = {
        "type": "text", "fill": white, "stroke": False, "x": 100, "y": 110, "fontsize": 30, "text": "B"
    }
    icn["SU.IC.SUBMARINE GUIDED MISSILE (SSGN)"] = {
        "type": "text", "fill": white, "stroke": False, "x": 100, "y": 110, "fontsize": 30, "text": "G"
    }
    
    # Mines (Simplified)
    icn["SU.IC.SEA MINE"] = {
        "type": "path",
        "fill": colors["iconColor"]["Hostile"] if (std2525 and affiliation != "Friend") else icon_fill_color, # Logic simplified
        "stroke": black if (std2525 and affiliation != "Friend") else icon_color,
        "d": "M 115.9,73 126.5,62.4 137.1,73 126.5,83.6 m -53,0 L 62.9,73 73.5,62.4 84.1,73 m 8.4,-3 0,-15 15,0 0,15 m 22.5,30 c 0,16.6 -13.4,30 -30,30 -16.6,0 -30,-13.4 -30,-30 0,-16.6 13.4,-30 30,-30 C 116.6,70 130,83.4 130,100 z"
    }
    
    icn["SU.IC.TORPEDO"] = {
        "type": "path",
        "d": "m 65,105 -5,-5 5,-5 60,0 c 0,0 5,5 5,5 l 5,-5 0,10 -5,-5 -5,5 z"
    }
    
    # Populate
    for key, value in icn.items():
        if key not in icon_parts:
            icon_parts[key] = value
