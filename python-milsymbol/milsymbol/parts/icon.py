
from ..components import BBox
from ..sidc.lettersidc import ground as ground_sidc

def icon(symbol, ms=None):
    # Port of src/symbolfunctions/icon.js
    draw_array1 = []
    draw_array2 = []
    gbbox = BBox(x1=50, x2=150, y1=50, y2=150)
    
    metadata = symbol.metadata
    style = symbol.style
    colors = symbol.colors
    options = symbol.options
    
    if style.icon:
        # TODO: Caching logic
        
        icon_parts = {} # Should be populated by getIconParts if we were loading all parts
        
        # In this simplified version, we define parts inside the specific SIDC module
        # or we pass a dict to be populated.
        


        # Letter based SIDCs
        if not metadata.get("numberSIDC"):
            icons = {}


            from ..sidc.lettersidc import ground as ground_sidc
            from ..sidc.lettersidc import air as air_sidc
            from ..sidc.lettersidc import sea as sea_sidc
            from ..sidc.lettersidc import subsurface as subsurface_sidc
            
            ground_sidc.ground(icons, None, icon_parts, metadata.get("STD2525"), metadata=metadata, colors=colors)
            air_sidc.air(icons, None, icon_parts, metadata.get("STD2525"), metadata=metadata, colors=colors)
            sea_sidc.sea(icons, None, icon_parts, metadata.get("STD2525"), metadata=metadata, colors=colors)
            subsurface_sidc.subsurface(icons, None, icon_parts, metadata.get("STD2525"), metadata=metadata, colors=colors)
            
            # Construct generic SIDC key
            # SIDC format for key: codingScheme(1) + affiliation(1) + battleDimension(1) + functionID(6)
            # Actually ground.js uses S-G-UCI--- format.
            # options.sidc[0] etc.
            
            sidc = options.sidc
            generic_sidc = sidc[0] + "-" + sidc[2] + "-" + sidc[4:10]
            
            # Fallback for affiliation specific shapes (like Amphibious)?
            # ground.js mapping keys are "S-G-UCI---"
            
            if generic_sidc in icons:
                draw_array2.extend(icons[generic_sidc])
            else:
                symbol.valid_icon = False
                
    # Outline logic
    # if (not (style.frame and metadata.get("fill")) or style.monoColor or metadata.get("controlMeasure")):
    #     if style.outlineWidth > 0:
            # draw_array1.append(outline(...))
            
    return {
        "pre": draw_array1,
        "post": draw_array2,
        "bbox": gbbox
    }
