
from ...parts.outline import outline

def text(t):
    return {"type": "text", "text": t, "fontsize": 40, "fontfamily": "Arial", "stroke": False, "fill": "black", "text-anchor": "middle", "y": 100, "x": 100}

def ground(sid, bbox, icn, std2525, metadata=None, colors=None):
    # Port of src/lettersidc/sidc/ground.js (Subset)
    
    affiliation = metadata.get("affiliation", "Friend") if metadata else "Friend"
    icon_color = colors["iconColor"][affiliation] if colors else "black"
    
    # Initialize dictionary lists
    if "S-G-UCI---" not in sid: sid["S-G-UCI---"] = []
    if "S-G-UCA---" not in sid: sid["S-G-UCA---"] = []
    if "S-G-UCF---" not in sid: sid["S-G-UCF---"] = []
    
    # Define Icon Parts (ICN)
    # Infantry
    icn["GR.IC.FF.INFANTRY"] = {
        "type": "path",
        "d": "M 25,50 L 175,150 M 25,150 L 175,50",
        "fill": False,
        "stroke": icon_color,
        "strokewidth": 3
    }

    # Armor (Oval)
    icn["GR.IC.ARMOUR"] = {
        "type": "path",
        "d": "M125,80 C150,80 150,120 125,120 L75,120 C50,120 50,80 75,80 Z",
        "fill": False,
        "stroke": icon_color,
        "strokewidth": 3
    }
    
    # Field Artillery (Dot)
    icn["GR.IC.FIELD ARTILLERY"] = { "type": "circle", "cx": 100, "cy": 100, "r": 15, "fill": icon_color } 

    # Mapping SIDC to Icons
    sid["S-G-UCI---"] = [icn["GR.IC.FF.INFANTRY"]]
    sid["S-G-UCA---"] = [icn["GR.IC.ARMOUR"]]
    sid["S-G-UCF---"] = [icn["GR.IC.FIELD ARTILLERY"]]
    
    # Adding more sample mappings
    sid["S-G-------"] = []
    
    return sid
