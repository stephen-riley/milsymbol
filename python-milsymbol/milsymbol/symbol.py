
from .options import SymbolOptions, SymbolStyle
from .components import BBox

class Symbol:
    def __init__(self, sidc=None, **kwargs):
        self.options = SymbolOptions()
        self.style = SymbolStyle()
        
        self.bbox = BBox()
        self.colors = {}
        self.metadata = {}
        self.octagon_anchor = {"x": 50, "y": 50}
        self.symbol_anchor = {"x": 50, "y": 50}
        self.valid_icon = True
        self.draw_instructions = []

        if sidc:
            self.options.sidc = sidc
            
        if kwargs:
            self.set_options(**kwargs)
        else:
            self.update()

    def set_options(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self.options, key):
                setattr(self.options, key, value)
            elif hasattr(self.style, key):
                setattr(self.style, key, value)
            elif key == "SIDC":  # Backward compatibility
                self.options.sidc = value
            else:
                # Store unknown options in options mostly to match flexible JS behavior
                # or maybe warn? JS just sets it on options if not in style.
                setattr(self.options, key, value)
        
        # Trigger updates (metadata, colors, etc.)
        self.update()
        return self

    def get_options(self, include_style=True):
        opts = self.options.__dict__.copy()
        if include_style:
            opts.update(self.style.__dict__)
        return opts
    
    def get_style(self):
        return self.style.__dict__.copy()


    def update(self):
        # Update metadata
        from .metadata import get_metadata
        self.metadata = get_metadata(self)
        
        # Update colors
        from .colors import get_colors
        self.colors = get_colors(self)
        
        # Reset bounding box
        self.bbox = BBox()
        
        # Build draw instructions
        self.draw_instructions = []
        
        from .parts.base import base_geometry
        from .parts.icon import icon
        from .parts.modifiers import modifiers
        
        # Pipeline parts
        parts = [base_geometry, icon, modifiers]
        
        for part in parts:
            res = part(self)
            if not res: continue
            
            if res.get("pre"):
                self.draw_instructions = res["pre"] + self.draw_instructions
            
            if res.get("post"):
                self.draw_instructions = self.draw_instructions + res["post"]
                

            if res.get("bbox"):
                self.bbox.merge(res["bbox"])

        # Text fields
        from .parts.textfields import textfields
        res = textfields(self)
        if res:
            self.draw_instructions = res.get("pre", []) + self.draw_instructions
            self.draw_instructions = self.draw_instructions + res.get("post", [])
                
        # Calculate sizes and anchors (Simplified)
        # Assuming padding and scale logic is needed
        # Porting minimal logic for initial rendering
        
        self.base_width = self.bbox.width + (self.style.strokeWidth * 2) + (self.style.outlineWidth * 2)
        self.base_height = self.bbox.height + (self.style.strokeWidth * 2) + (self.style.outlineWidth * 2)
        
        self.width = (self.base_width * self.style.size) / 100
        self.height = (self.base_height * self.style.size) / 100
        
        # Adjust bbox for viewbox (simplified, assuming viewbox matches bbox for now) 
        # In JS it calculates anchors.


    def as_svg(self):
        from .renderer import Renderer
        return Renderer(self).to_svg()
    
    def as_png(self):
        try:
            import cairosvg
            return cairosvg.svg2png(bytestring=self.as_svg().encode("utf-8"))
        except ImportError:
            raise ImportError("cairosvg is required for PNG output. Install it with `pip install cairosvg`.")

    def to_data_url(self):
        return "data:image/svg+xml;utf8," + self.as_svg()

