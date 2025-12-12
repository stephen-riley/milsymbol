
from .components import BBox

def get_metadata(symbol):
    # This mirrors src/ms/symbol/getmetadata.js
    style = symbol.style
    options = symbol.options
    
    metadata = {
        "activity": False,
        "affiliation": "undefined",
        "baseAffilation": "",
        "baseDimension": "",
        "baseGeometry": {"g": "", "bbox": BBox()},
        "civilian": False,
        "condition": "",
        "context": "",
        "dimension": "undefined",
        "dimensionUnknown": False,
        "echelon": "",
        "faker": False,
        "fenintDummy": False,
        "fill": style.fill,
        "frame": style.frame,
        "functionid": "",
        "headquarters": False,
        "installation": False,
        "joker": False,
        "mobility": "",
        "notpresent": "",
        "numberSIDC": False, # Is the SIDC number based
        "space": False,
        "STD2525": True, # Default to True, need logic to check standard
        "taskForce": False,
        "unit": False
    }

    mapping = {
        "context": ["Reality", "Exercise", "Simulation"],
        "status": ["Present", "Planned", "FullyCapable", "Damaged", "Destroyed", "FullToCapacity"],
        "echelonMobility": {
            "11": "Team/Crew",
            "12": "Squad",
            "13": "Section",
            "14": "Platoon/detachment",
            "15": "Company/battery/troop",
            "16": "Battalion/squadron",
            "17": "Regiment/group",
            "18": "Brigade",
            "21": "Division",
            "22": "Corps/MEF",
            "23": "Army",
            "24": "Army Group/front",
            "25": "Region/Theater",
            "26": "Command",
            "31": "Wheeled limited cross country",
            "32": "Wheeled cross country",
            "33": "Tracked",
            "34": "Wheeled and tracked combination",
            "35": "Towed",
            "36": "Rail",
            "37": "Pack animals",
            "41": "Over snow (prime mover)",
            "42": "Sled",
            "51": "Barge",
            "52": "Amphibious",
            "61": "Short towed array",
            "62": "Long towed Array",
            "71": "Leader Individual",
            "72": "Deputy Individual"
        },
        "affiliation": ["Hostile", "Friend", "Neutral", "Unknown"],
        "dimension": ["Air", "Ground", "Sea", "Subsurface"]
    }
    
    metadata["context"] = mapping["context"][0]
    
    if style.standard:
        metadata["STD2525"] = False if style.standard == "APP6" else True

    if style.monoColor:
        metadata["fill"] = False
        
    options.sidc = str(options.sidc).replace("*", "-").replace(" ", "")
    
    metadata["numberSIDC"] = options.sidc.isdigit()
    
    if metadata["numberSIDC"]:
        # TODO: Implement number SIDC metadata extraction
        # metadata = get_metadata_number(symbol, metadata, mapping)
        pass

    else:
        from .sidc.letter import get_metadata_letter
        metadata = get_metadata_letter(symbol, metadata, mapping)
        

    # Validation and baseGeometry logic...
    from .symbol_geometries import symbol_geometries
    
    key = metadata.get("dimension") + metadata.get("affiliation")
    if key in symbol_geometries:
        metadata["baseGeometry"] = symbol_geometries[key]
    else:
        # Fallback or initialization
        metadata["baseGeometry"] = {"g": {"type": "path", "d": ""}, "bbox": BBox()}

    if not style.frame and not style.icon:
        metadata["baseGeometry"] = symbol_geometries["PositionMarker"]

        
    return metadata
