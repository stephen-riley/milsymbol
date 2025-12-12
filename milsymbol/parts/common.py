

def text(str_val):
    size = 42
    y = 115
    if len(str_val) == 1:
        size = 45
        y = 115
    if len(str_val) == 3:
        size = 35
        y = 110
    if len(str_val) >= 4:
        size = 32
        y = 110
        
    return {
        "type": "text",
        "text": str_val,
        "fontsize": size,
        "fontfamily": "Arial",
        "stroke": False,
        "fill": "black",
        "text-anchor": "middle",
        "y": y,
        "x": 100
    }

def textm1(str_val):
    size = 30
    if len(str_val) == 3:
        size = 25
    if len(str_val) >= 4:
        size = 22
        
    return {
        "type": "text",
        "text": str_val,
        "fontsize": size,
        "fontfamily": "Arial",
        "stroke": False,
        "fill": "black",
        "text-anchor": "middle",
        "y": 77,
        "x": 100
    }

def textm2(str_val):
    size = 30
    y = 145
    if len(str_val) == 3:
        size = 25
        y = 140
    if len(str_val) >= 4:
        size = 20
        y = 135
        
    return {
        "type": "text",
        "text": str_val,
        "fontsize": size,
        "fontfamily": "Arial",
        "stroke": False,
        "fill": "black",
        "text-anchor": "middle",
        "y": y,
        "x": 100
    }
