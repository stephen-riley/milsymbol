
from ...parts.sea import define_sea_icons

def sea(sid, bbox, icon_parts, std2525, metadata=None, colors=None):
    # Port of src/lettersidc/sidc/sea.js
    
    # Define icons first
    define_sea_icons(icon_parts, metadata, colors, std2525)
    
    icn = icon_parts
    
    sid["S-S-------"] = []
    sid["S-S-C-----"] = [icn["SE.IC.COMBATANT"]]
    sid["S-S-CL----"] = [icn["SE.IC.SURFACE COMBATANT, LINE"]]
    sid["S-S-CLCV--"] = [icn["SE.IC.CARRIER"]]
    sid["S-S-CLCC--"] = [icn["SE.IC.CRUISER"]]
    sid["S-S-CLDD--"] = [icn["SE.IC.DESTROYER"]]
    sid["S-S-CLFF--"] = [icn["SE.IC.FRIGATE"]]
    sid["S-S-CM----"] = [icn["SE.IC.MINE WARFARE VESSEL"]]
