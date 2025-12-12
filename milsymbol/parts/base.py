
from .outline import outline

def base_geometry(symbol, ms=None):
    # Port of src/symbolfunctions/basegeometry.js
    draw_array1 = []
    draw_array2 = []
    
    metadata = symbol.metadata
    style = symbol.style
    colors = symbol.colors
    
    frame_color = getattr(colors["frameColor"], metadata["affiliation"], None)
    if frame_color is None:
        frame_color = getattr(colors["frameColor"], "Civilian") # Fallback
    
    # If unframed but with icon, then just return.
    base_geom = metadata.get("baseGeometry", {})
    if (not metadata.get("frame") and style.icon) or not base_geom.get("g") or not base_geom.get("g").get("type"):
        return {
            "pre": draw_array1,
            "post": draw_array2,
            "bbox": base_geom.get("bbox")
        }

    # Clone the base geometry
    geom = base_geom["g"].copy()
    
    fill_color = style.fillColor or getattr(colors["fillColor"], metadata["affiliation"], "")
    
    geom["fill"] = fill_color
    geom["fillopacity"] = style.fillOpacity
    geom["stroke"] = frame_color
    geom["strokewidth"] = style.strokeWidth if style.size >= 10 else 10
    
    # Outline
    if style.frame and style.outlineWidth > 0:
        geom_outline = None
        if geom["type"] == "path" and metadata.get("fill") and not style.monoColor:
            geom_outline = geom.copy()
            geom_outline["d"] += " Z" # Making sure the path is closed
            geom_outline["strokewidth"] = style.strokeWidth if style.size >= 10 else 10
            geom_outline.pop("fill", None)
        else:
            geom_outline = geom
            
        outline_color = style.outlineColor[metadata["affiliation"]] if isinstance(style.outlineColor, dict) else style.outlineColor
        
        draw_array1.append(outline(
            geom_outline,
            style.outlineWidth,
            style.strokeWidth,
            outline_color
        ))

    # Add a dashed outline to the frame if we are using monocolor and the status is not present.
    if (style.monoColor or not style.fill) and metadata.get("notpresent"):
        geom["strokedasharray"] = metadata["notpresent"]
        
    draw_array2.append(geom)

    # Space Modifiers (Skipped implementation for brevity, can implement later if needed)
    # Action Modifiers (Skipped implementation for brevity)
    
    return {
        "pre": draw_array1,
        "post": draw_array2,
        "bbox": base_geom.get("bbox")
    }
