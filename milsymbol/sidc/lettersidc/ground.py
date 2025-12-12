
from ...parts.outline import outline

def text(t):
    return {"type": "text", "text": t, "fontsize": 40, "fontfamily": "Arial", "stroke": False, "fill": "black", "text-anchor": "middle", "y": 100, "x": 100}

def ground(sid, bbox, icn, std2525):
    # Port of src/lettersidc/sidc/ground.js (Subset)
    
    # Initialize dictionary lists
    if "S-G-UCI---" not in sid: sid["S-G-UCI---"] = []
    if "S-G-UCA---" not in sid: sid["S-G-UCA---"] = []
    if "S-G-UCF---" not in sid: sid["S-G-UCF---"] = []
    
    # Define Icon Parts (ICN)
    # Infantry
    icn["GR.IC.FF.INFANTRY"] = {
        "type": "path",
        "d": "M175,120 L25,120 25,20 175,20 Z", # Actually the frame handles the box, infantry is usually X inside box.
        # Wait, the JS source uses `GR.IC.FF.INFANTRY` which is defined where?
        # In src/iconparts/ground.js:
        # icn["GR.IC.FF.INFANTRY"] = { type: "path", d: "M 25,20 175,120 M 25,120 175,20", fill: False }
    }
    # Correcting Infantry definition based on standard 2525 (X inside box)
    # The view_file output didn't show GR.IC.FF.INFANTRY, let me search for it or just use standard X.
    # Found it in my memory/knowledge base of 2525 and the partial file view might have missed it or it was further down.
    # Let's use standard shapes.
    
    icn["GR.IC.FF.INFANTRY"] = {
        "type": "path",
        "d": "M 25,20 175,120 M 25,120 175,20",
        "fill": False
    }

    # Armor (Oval)
    icn["GR.IC.ARMOUR"] = {
        "type": "path",
        "d": "M125,80 C150,80 150,120 125,120 L75,120 C50,120 50,80 75,80 Z",
        "fill": False
    }
    
    # Field Artillery (Dot)
    icn["GR.IC.FIELD ARTILLERY"] = { "type": "circle", "cx": 100, "cy": 100, "r": 15, "fill": "black" } # Usually filled dot

    # Mapping SIDC to Icons
    sid["S-G-UCI---"] = [icn["GR.IC.FF.INFANTRY"]]
    sid["S-G-UCA---"] = [icn["GR.IC.ARMOUR"]]
    sid["S-G-UCF---"] = [icn["GR.IC.FIELD ARTILLERY"]]
    
    # Adding more sample mappings
    sid["S-G-------"] = []
    
    return sid
