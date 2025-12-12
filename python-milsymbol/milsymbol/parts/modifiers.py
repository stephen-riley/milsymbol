
from ..components import BBox

def modifiers(symbol):
    # Port of src/symbolfunctions/modifier.js
    draw_array1 = []
    draw_array2 = []
    
    metadata = symbol.metadata
    style = symbol.style
    colors = symbol.colors
    
    bbox = symbol.bbox # Should use base geometry bbox really, but symbol.bbox is accumulated
    # In JS: var bbox = new ms.BBox(this.metadata.baseGeometry.bbox);
    if metadata.get("baseGeometry") and metadata["baseGeometry"].get("bbox"):
        bbox = BBox(metadata["baseGeometry"]["bbox"])
    
    # Resolve color used for modifiers (Frame Color or Icon Color)
    # JS: var color = this.style.frameColor ? ... : ...
    # In Python colors dict has frameColor/iconColor resolved
    color = colors.get("frameColor")
    if not color or color == "none":
        color = colors.get("iconColor")
        
    # Handle affiliation specific lookup if it's a dict (ColorMode)
    if hasattr(color, "get"): # Dictionary-like
         color = color.get(metadata["affiliation"])
    elif hasattr(color, "__dict__"): # Object w attributes
         color = getattr(color, metadata["affiliation"], "black")
         
    if not color: color = "black"

    gbbox = BBox()

    # Echelon
    if metadata.get("echelon"):
        installation_padding = 15 if metadata.get("installation") else 0
        y1 = bbox.y1
        
        echelons = {
            "Team/Crew": [
                {"type": "circle", "cx": 100, "cy": y1 - 20, "r": 15, "fill": False},
                {"type": "path", "d": f"M80,{y1 - 10}L120,{y1 - 30}"}
            ],
            "Squad": [
                {"type": "circle", "fill": color, "cx": 100, "cy": y1 - 20, "r": 7.5, "stroke": False} # Filled dot
            ],
            "Section": [
                {"type": "circle", "fill": color, "cx": 115, "cy": y1 - 20, "r": 7.5, "stroke": False},
                {"type": "circle", "fill": color, "cx": 85, "cy": y1 - 20, "r": 7.5, "stroke": False}
            ],
            "Platoon/detachment": [
                {"type": "circle", "fill": color, "cx": 100, "cy": y1 - 20, "r": 7.5, "stroke": False},
                {"type": "circle", "fill": color, "cx": 70, "cy": y1 - 20, "r": 7.5, "stroke": False},
                {"type": "circle", "fill": color, "cx": 130, "cy": y1 - 20, "r": 7.5, "stroke": False}
            ],
            "Company/battery/troop": [
                {"type": "path", "d": f"M100,{y1 - 10}L100,{y1 - 35}"}
            ],
            "Battalion/squadron": [
                {"type": "path", "d": f"M90,{y1 - 10}L90,{y1 - 35}"},
                {"type": "path", "d": f"M110,{y1 - 10}L110,{y1 - 35}"}
            ],
            "Regiment/group": [
                {"type": "path", "d": f"M100,{y1 - 10}L100,{y1 - 35}"},
                {"type": "path", "d": f"M120,{y1 - 10}L120,{y1 - 35}"},
                {"type": "path", "d": f"M80,{y1 - 10}L80,{y1 - 35}"}
            ],
            "Brigade": [
                {"type": "path", "d": f"M87.5,{y1 - 10} l25,-25 m0,25 l-25,-25"}
            ],
            "Division": [
                {"type": "path", "d": f"M70,{y1 - 10} l25,-25 m0,25 l-25,-25   M105,{y1 - 10} l25,-25 m0,25 l-25,-25"}
            ],
            "Corps/MEF": [
                 {"type": "path", "d": f"M52.5,{y1 - 10} l25,-25 m0,25 l-25,-25    M87.5,{y1 - 10} l25,-25 m0,25 l-25,-25    M122.5,{y1 - 10} l25,-25 m0,25 l-25,-25"}
            ],
            "Army": [
                {"type": "path", "d": f"M35,{y1 - 10} l25,-25 m0,25 l-25,-25   M70,{y1 - 10} l25,-25 m0,25 l-25,-25   M105,{y1 - 10} l25,-25 m0,25 l-25,-25    M140,{y1 - 10} l25,-25 m0,25 l-25,-25"}
            ],
            "Army Group/front": [
                 {"type": "path", "d": f"M17.5,{y1 - 10} l25,-25 m0,25 l-25,-25    M52.5,{y1 - 10} l25,-25 m0,25 l-25,-25    M87.5,{y1 - 10} l25,-25 m0,25 l-25,-25    M122.5,{y1 - 10} l25,-25 m0,25 l-25,-25       M157.5,{y1 - 10} l25,-25 m0,25 l-25,-25"}
            ],
            "Region/Theater": [
                {"type": "path", "d": f"M0,{y1 - 10} l25,-25 m0,25 l-25,-25   M35,{y1 - 10} l25,-25 m0,25 l-25,-25   M70,{y1 - 10} l25,-25 m0,25 l-25,-25   M105,{y1 - 10} l25,-25 m0,25 l-25,-25    M140,{y1 - 10} l25,-25 m0,25 l-25,-25     M175,{y1 - 10} l25,-25 m0,25 l-25,-25"}
            ],
            "Command": [
                 {"type": "path", "d": f"M70,{y1 - 22.5} l25,0 m-12.5,12.5 l0,-25   M105,{y1 - 22.5} l25,0 m-12.5,12.5 l0,-25"}
            ]
        }
        
        geom_list = echelons.get(metadata["echelon"])
        if geom_list:
             # Apply translation and colors
             processed_geoms = []
             for part in geom_list:
                 part_copy = part.copy() # Clone
                 if "fill" not in part_copy: part_copy["fill"] = False
                 if "stroke" not in part_copy: part_copy["stroke"] = color
                 if "strokewidth" not in part_copy: part_copy["strokewidth"] = style.strokeWidth
                 processed_geoms.append(part_copy)
             
             draw_array2.append({
                 "type": "translate",
                 "x": 0,
                 "y": -installation_padding,
                 "draw": processed_geoms
             })
             
             
             # BBox updates
             echelon_bboxes = {
                "Team/Crew": {"y1": y1 - 40 - installation_padding},
                "Squad": {"y1": y1 - 20 - 7.5 - installation_padding},
                "Section": {"y1": y1 - 20 - 7.5 - installation_padding},
                "Platoon/detachment": {"y1": y1 - 20 - 7.5 - installation_padding},
                "Company/battery/troop": {"y1": y1 - 40 - installation_padding},
                "Battalion/squadron": {"y1": y1 - 40 - installation_padding},
                "Regiment/group": {"y1": y1 - 40 - installation_padding},
                "Brigade": {"y1": y1 - 15 - 25 - installation_padding},
                "Division": {"y1": y1 - 15 - 25 - installation_padding, "x1": 70, "x2": 130},
                "Corps/MEF": {"y1": y1 - 15 - 25 - installation_padding, "x1": 52.5, "x2": 147.5},
                "Army": {"y1": y1 - 15 - 25 - installation_padding, "x1": 35, "x2": 165},
                "Army Group/front": {"y1": y1 - 15 - 25 - installation_padding, "x1": 17.5, "x2": 182.5},
                "Region/Theater": {"y1": y1 - 15 - 25 - installation_padding, "x1": 0, "x2": 200},
                "Command": {"y1": y1 - 15 - 25 - installation_padding, "x1": 70, "x2": 130}
             }
             
             bbox_update = echelon_bboxes.get(metadata["echelon"])
             if bbox_update:
                 gbbox.merge(BBox(bbox_update))

    return {
        "pre": draw_array1,
        "post": draw_array2,
        "bbox": gbbox
    }
