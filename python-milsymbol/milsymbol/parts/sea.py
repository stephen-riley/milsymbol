
from .common import text, textm1, textm2

def define_sea_icons(icon_parts, metadata, colors, std2525):
    frame = metadata.get("frame")
    affiliation = metadata.get("affiliation", "Friend")
    
    icon_color = colors["iconColor"][affiliation]
    icon_fill_color = colors["iconFillColor"][affiliation]
    white = colors["white"][affiliation]
    black = colors["black"][affiliation]
    
    icn = {}

    icn["SE.IC.MILITARY"] = text("MIL")
    icn["SE.IC.MANUAL TRACK"] = text("MAN")
    icn["SE.IC.COMBATANT"] = [
        {
            "type": "path",
            "d": "m 86.9,110 c -3.6,2 -7.2,3.9 -10.8,5.9 2.1,2.9 6.7,3.9 10,2.1 2.6,-0.9 4.7,-3.8 3.1,-6.1 -0.8,-0.6 -1.5,-1.3 -2.3,-1.9 z m 26.3,0.1 c 3.6,2 7.2,3.9 10.8,5.9 -2.1,2.9 -6.7,3.9 -10,2.1 -2.6,-0.9 -4.7,-3.8 -3.1,-6.1 0.8,-0.6 1.5,-1.3 2.3,-1.9 z",
            "fill": icon_color,
            "stroke": False
        },
        {
            "type": "path",
            "d": "m 112.9,110 c -5.6,-4 -11.3,-7.9 -16.1,-12.5 -4.2,-4.5 -7,-9.8 -9.2,-15.1 -0.8,4.4 -0.9,9.3 2.4,13.2 3.6,4.5 8.6,8.1 13.5,11.8 2.3,1.7 4.7,3.3 7.1,4.8 0.8,-0.7 1.5,-1.5 2.3,-2.2 m -25.7,0 c 5.6,-4 11.3,-7.9 16.1,-12.5 4.2,-4.5 7,-9.8 9.2,-15.1 0.8,4.4 0.9,9.3 -2.4,13.2 -3.6,4.5 -8.6,8.1 -13.5,11.8 -2.3,1.7 -4.7,3.3 -7.1,4.8 -0.8,-0.7 -1.5,-1.5 -2.3,-2.2",
            "fill": white,
            "stroke": black,
            "strokewidth": 2
        }
    ]
    
    icn["SE.IC.SURFACE COMBATANT, LINE"] = {
        "type": "path",
        "stroke": False,
        "fill": icon_color,
        "d": "m 100,120 -25,-17 15,2 0,-10 5,0 0,-5 -15,0 0,-5 15,0 0,-5 10,0 0,5 15,0 0,5 -15,0 0,5 5,0 0,10 15,-2 z"
    }
    
    icn["SE.IC.CARRIER"] = {
        "type": "path",
        "fill": icon_color,
        "stroke": False,
        "d": "m 80,100 20,20 20,-20 -20,0 0,-20 -20,0 z"
    }
    
    icn["SE.IC.CRUISER"] = text("CC")
    icn["SE.IC.DESTROYER"] = text("DD")
    icn["SE.IC.FRIGATE"] = text("FF")
    
    icn["SE.IC.MINE WARFARE VESSEL"] = {
        "type": "path",
        "fill": icon_color,
        "stroke": False,
        "d": "m 98.3,81 0,4.1 c -2.4,0.3 -4.6,1.4 -6.4,2.9 l -3.5,-3.5 -2.4,2.4 3.6,3.6 c -0.9,1.3 -1.5,4.9 -1.8,6.5 l -10.8,0 0,3 3,0 20,20 20,-20 3,0 0,-3 -10,0 c -1,-1.7 -2,-5.3 -3,-6.7 l 4,-3.7 -2,-2.4 -4,3.6 c -2,-1.4 -4,-2.4 -6,-2.7 l 0,-4.1 z"
    }
    
    # Populate icon_parts
    for key, value in icn.items():
        if key not in icon_parts:
            icon_parts[key] = value
