
from .components import ColorMode

def get_color_mode(mode):
    # Default color modes defined in ms.js / colormodes.js
    # We might need to port them. For now, we define them here or import.
    # TODO: Implement full ColorModes map
    if mode == "Light":
        return ColorMode(
            civilian="rgb(128,0,128)",
            friend="rgb(128,224,255)",
            hostile="rgb(255,128,128)",
            neutral="rgb(170,255,170)",
            unknown="rgb(255,255,128)"
        )
    # Fallback or other modes
    return ColorMode(
        civilian="rgb(128,0,128)",
        friend="rgb(0,226,255)",
        hostile="rgb(255,48,49)",
        neutral="rgb(0,255,0)",
        unknown="rgb(255,255,0)"
    )

def get_colors(symbol):
    style = symbol.style
    metadata = symbol.metadata
    
    base_fill_color = style.colorMode if isinstance(style.colorMode, ColorMode) else get_color_mode(style.colorMode)
    base_frame_color = style.frameColor if isinstance(style.frameColor, ColorMode) else get_color_mode("FrameColor") # TODO: Define FrameColor
    base_icon_color = style.iconColor if isinstance(style.iconColor, ColorMode) else get_color_mode("IconColor") # TODO: Define IconColor
    
    # Defaults in case get_color_mode returns defaults for everything not found
    # In JS, ms.getColorMode creates a new instance.
    
    base_icon_fill_color = base_fill_color
    base_color_black = get_color_mode("Black")
    base_color_white = get_color_mode("White")
    base_color_off_white = get_color_mode("OffWhite")
    base_color_none = get_color_mode("None")

    # If it is a Civilian Symbol and civilian colors not are turned off
    # Note: In Python we need to access attributes carefully if they are dicts or objects.
    # Using .Civilian etc assuming ColorMode object.

    if style.civilianColor and metadata.get("civilian"):
        base_fill_color.Friend = base_fill_color.Neutral = base_fill_color.Unknown = base_fill_color.Civilian
        base_frame_color.Friend = base_frame_color.Neutral = base_frame_color.Unknown = base_frame_color.Civilian
        base_icon_color.Friend = base_icon_color.Neutral = base_icon_color.Unknown = base_icon_color.Civilian

    # Joker and Faker
    if metadata.get("joker") or metadata.get("faker"):
        base_fill_color.Friend = base_fill_color.Hostile
        base_frame_color.Friend = base_frame_color.Hostile
        base_icon_color.Friend = base_icon_color.Hostile

    # Mono color
    if style.monoColor:
        base_frame_color.Friend = base_frame_color.Neutral = base_frame_color.Hostile = base_frame_color.Unknown = base_frame_color.Civilian = style.monoColor
        base_color_black = base_frame_color
        base_color_white = base_fill_color = base_color_none

    colors = {
        "fillColor": base_fill_color,
        "frameColor": base_frame_color,
        "iconColor": base_icon_color,
        "iconFillColor": base_icon_fill_color,
        "none": base_color_none,
        "black": base_color_black,
        "white": base_color_white
    }

    # Turn off the frame
    if metadata.get("frame"):
        colors["frameColor"] = style.frameColor if isinstance(style.frameColor, ColorMode) else base_color_black
    else:
        colors["frameColor"] = base_color_none

    # Filled or not
    if metadata.get("fill"):
        colors["fillColor"] = base_color_none if (not metadata.get("frame") and not (not metadata.get("frame") and not style.icon)) else base_fill_color
        colors["iconColor"] = style.iconColor if isinstance(style.iconColor, ColorMode) else base_color_black
        colors["iconFillColor"] = base_fill_color if not metadata.get("frame") else base_color_off_white
        colors["white"] = base_color_off_white
    else:
        colors["fillColor"] = base_color_none
        colors["frameColor"] = base_color_none if not metadata.get("frame") else base_frame_color
        colors["iconColor"] = base_frame_color
        colors["iconFillColor"] = base_color_none
        
        if not metadata.get("frame") and not metadata.get("fill") and not style.icon:
             colors["frameColor"] = base_color_black
             colors["fillColor"] = base_color_black
             
    return colors
