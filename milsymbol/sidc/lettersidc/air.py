
from ...parts.air import define_air_icons

def air(sid, bbox, icon_parts, std2525, metadata=None, colors=None):
    # Port of src/lettersidc/sidc/air.js
    
    # Define icons first
    define_air_icons(icon_parts, metadata, colors, std2525)
    
    icn = icon_parts
    
    # AIR ===========================================================================
    sid["S-A-------"] = []
    sid["S-A-M-----"] = [icn["AR.I.MILITARY"]]
    sid["S-A-MF----"] = [icn["AR.I.MILITARY FIXED WING"]]
    
    sid["S-A-MFF---"] = [icn["AR.I.FIGHTER"]] # Just text 'F'
    # Wait, in JS it maps to AR.I.FIGHTER which is text("F").
    # But usually fixed wing also has the frame/geometry..
    # In milsymbol JS, getIcons returns an array of parts.
    # The frame is handled separately by base geometry.
    # So "S-A-MFF---" -> [icn["AR.I.FIGHTER"]] which puts 'F' in the center.
    # The base geometry (AirFriend) provides the "shape" (screen/tub things).
    
    sid["S-A-MFA---"] = [icn.get("AR.I.ATTACK/STRIKE", {"type": "text", "text": "A"})] # Fallback
    
    # Rotatory Wing
    sid["S-A-MH----"] = [icn["AR.I.MILITARY ROTARY WING"]]
    
    # Add more mappings as needed
