
from .common import text, textm1, textm2

def define_air_icons(icon_parts, metadata, colors, std2525):
    frame = metadata.get("frame")
    affiliation = metadata.get("affiliation", "Friend")
    
    icon_color = colors["iconColor"][affiliation]
    icon_fill_color = colors["iconFillColor"][affiliation]
    black = colors["black"][affiliation]
    
    icn = {}

    icn["AR.I.MILITARY"] = text("MIL")
    icn["AR.I.CIVILIAN"] = text("CIV")
    # ... Simplified for brevity, porting main ones ...
    

    icn["AR.I.MILITARY FIXED WING"] = {
        "type": "path",
        "d": "M100,100 L130,88 c15,0 15,24 0,24 L100,100 70,112 c-15,0 -15,-24 0,-24 Z",
        "fill": icon_color,
        "stroke": False
    }

    icn["AR.I.MILITARY ROTARY WING"] = {
        "type": "path",
        "d": "M60,85 l40,15 40,-15 0,30 -40,-15 -40,15 z",
        "fill": icon_color,
        "stroke": False
    }
    
    icn["AR.I.FIGHTER"] = text("F")
    
    # Modifiers
    icn["AIR.M1.ATTACK"] = textm1("A")
    icn["AIR.M1.BOMBER"] = textm1("B")
    icn["AIR.M1.CARGO"] = textm1("C")
    icn["AIR.M1.FIGHTER"] = textm1("F")
    icn["AIR.M1.INTERCEPTOR"] = textm1("I")
    icn["AIR.M1.TANKER"] = textm1("K")
    icn["AIR.M1.UTILITY"] = textm1("U")
    
    # Populate icon_parts
    for key, value in icn.items():
        if key not in icon_parts:
            icon_parts[key] = value

