
import copy

def outline(geom, outline_width, stroke_width, color):
    # Port of src/ms/outline.js
    def process(g, o_width, s_width, c):
        if isinstance(g, list):
            return [process(item, o_width, s_width, c) for item in g]
        
        clone = copy.deepcopy(g)
        
        # Remove fill and fillopacity
        clone.pop("fill", None)
        clone.pop("fillopacity", None)
        
        if clone.get("type") in ["translate", "rotate", "scale"]:
            clone["draw"] = [process(d, o_width, s_width, c) for d in clone.get("draw", [])]
        else:
            current_stroke = clone.get("strokewidth")
            if current_stroke is None:
                current_stroke = s_width
            
            # If stroke is not False (it might be 0, so check for False)
            if clone.get("stroke") is not False:
                clone["strokewidth"] = float(current_stroke) + 2 * o_width
            else:
                clone["strokewidth"] = 2 * o_width
            
            clone["stroke"] = c
            clone["fill"] = False
            clone["linecap"] = "round"
            
        return clone

    return process(geom, outline_width, stroke_width, color)
