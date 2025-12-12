

from ..components import BBox


def get_metadata_letter(symbol, metadata, mapping):
    # Port of src/lettersidc/metadata.js
    options = symbol.options
    style = symbol.style
    
    sidc = options.sidc.upper()
    
    codingscheme = sidc[0] if len(sidc) > 0 else "-"
    affiliation = sidc[1] if len(sidc) > 1 else "-"
    battledimension = sidc[2] if len(sidc) > 2 else "-"
    status = sidc[3] if len(sidc) > 3 else "-"
    
    functionid = sidc[4:10] if len(sidc) >= 10 else "------"
    metadata["functionid"] = functionid
    
    symbolmodifier11 = sidc[10] if len(sidc) > 10 else "-"
    symbolmodifier12 = sidc[11] if len(sidc) > 11 else "-"
    
    if affiliation in ["H", "S", "J", "K"]:
        metadata["affiliation"] = mapping["affiliation"][0] # Hostile
    elif affiliation in ["F", "A", "D", "M"]:
        metadata["affiliation"] = mapping["affiliation"][1] # Friend
    elif affiliation in ["N", "L"]:
        metadata["affiliation"] = mapping["affiliation"][2] # Neutral
    elif affiliation in ["P", "U", "G", "W", "O"]:
        metadata["affiliation"] = mapping["affiliation"][3] # Unknown

    if battledimension in ["P", "A"]:
        metadata["dimension"] = mapping["dimension"][0] # Air
    elif battledimension in ["G", "Z", "F", "X"]:
        metadata["dimension"] = mapping["dimension"][1] # Ground
    elif battledimension in ["S"]:
        metadata["dimension"] = mapping["dimension"][2] # Sea
    elif battledimension in ["U"]:
        metadata["dimension"] = mapping["dimension"][3] # Subsurface

    # Dimension is in Space
    if battledimension == "P" and codingscheme != "O":
        metadata["space"] = True
        
    # Activities
    if codingscheme == "O" and battledimension in ["V", "O", "R"]:
        metadata["activity"] = True
        
    # Control Measure
    if codingscheme == "G":
        metadata["controlMeasure"] = True
        
    # Installation
    if symbolmodifier11 == "H":
        metadata["installation"] = True
        
    # Status
    # Needed: dashArrays are not yet implemented in Python side fully, passing string placeholder
    if style.frame and status == "A":
        metadata["notpresent"] = "anticipated" # Placeholder for dash array
        
    if style.frame and affiliation in ["P", "A", "S", "G", "M"]:
        metadata["notpresent"] = "pending" # Placeholder
        
    if status == "C": metadata["condition"] = mapping["status"][2]
    if status == "D": metadata["condition"] = mapping["status"][3]
    if status == "X": metadata["condition"] = mapping["status"][4]
    if status == "F": metadata["condition"] = mapping["status"][5]
    
    # Validation exercise
    if affiliation in ["G", "W", "D", "L", "M", "J", "K"]:
        metadata["context"] = mapping["context"][1]
        
    # Tactical symbols
    if codingscheme == "O":
        metadata["dimension"] = mapping["dimension"][1]
    if codingscheme == "E":
        metadata["dimension"] = mapping["dimension"][1]

    metadata["baseDimension"] = metadata["dimension"]
    metadata["baseAffilation"] = metadata["affiliation"]

    if affiliation == "J": metadata["joker"] = True
    if affiliation == "K": metadata["faker"] = True
    
    if metadata["joker"] or metadata["faker"]:
        metadata["affiliation"] = mapping["affiliation"][1] # Make it look like Friend

    # Headquarters/TaskForce/FeintDummy
    if symbolmodifier11 in ["F", "G", "C", "D"] or (symbolmodifier11 == "H" and symbolmodifier12 == "B"):
        metadata["feintDummy"] = True
        
    if symbolmodifier11 in ["A", "B", "C", "D"]:
        metadata["headquarters"] = True
        
    # More logic can be added here...
    
    return metadata
