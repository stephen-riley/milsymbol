
from ...parts.subsurface import define_subsurface_icons

def subsurface(sid, bbox, icon_parts, std2525, metadata=None, colors=None):
    # Port of src/lettersidc/sidc/subsurface.js
    
    define_subsurface_icons(icon_parts, metadata, colors, std2525)
    icn = icon_parts
    
    sid["S-U-------"] = []
    sid["S-U-S-----"] = [icn["SU.IC.SUBMARINE"]]
    sid["S-U-SF----"] = [icn["SU.IC.SUBMARINE, SURFACED"]]
    sid["S-U-SK----"] = [icn["SU.IC.SUBMARINE, SNORKELING"]]
    
    sid["S-U-SN----"] = [icn["SU.IC.SUBMARINE NUCLEAR PROPULSION"]]
    sid["S-U-SNA---"] = [icn["SU.IC.SUBMARINE NUCLEAR PROPULSION"], icn["SU.IC.SUBMARINE ATTACK (SSN)"]]
    sid["S-U-SNB---"] = [icn["SU.IC.SUBMARINE NUCLEAR PROPULSION"], icn["SU.IC.SUBMARINE BALLISTIC MISSILE (SSBN)"]]
    sid["S-U-SNG---"] = [icn["SU.IC.SUBMARINE NUCLEAR PROPULSION"], icn["SU.IC.SUBMARINE GUIDED MISSILE (SSGN)"]]
    
    sid["S-U-SC----"] = [icn["SU.IC.SUBMARINE CONVENTIONAL PROPULSION"]]
    
    sid["S-U-WM----"] = [icn["SU.IC.SEA MINE"]]
    sid["S-U-WT----"] = [icn["SU.IC.TORPEDO"]]
