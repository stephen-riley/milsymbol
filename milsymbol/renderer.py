
import xml.etree.ElementTree as ET

class Renderer:
    def __init__(self, symbol):
        self.symbol = symbol

    def to_svg(self):
        # Create SVG root
        width = self.symbol.width
        height = self.symbol.height
        viewbox = f"{self.symbol.bbox.x1} {self.symbol.bbox.y1} {self.symbol.bbox.width} {self.symbol.bbox.height}"
        
        svg = ET.Element("svg", {
            "version": "1.1",
            "baseProfile": "tiny",
            "width": str(width),
            "height": str(height),
            "viewBox": viewbox,
            "preserveAspectRatio": "xMidYMid meet",
            "xmlns": "http://www.w3.org/2000/svg"
        })
        
        # Add draw instructions
        for instruction in self.symbol.draw_instructions:
            self._process_instruction(instruction, svg)
            
        return ET.tostring(svg, encoding="unicode")

    def _process_instruction(self, instruction, parent):
        if isinstance(instruction, list):
            for item in instruction:
                self._process_instruction(item, parent)
            return

        itype = instruction.get("type")
        
        if itype == "path":
            attrib = {
                "d": instruction.get("d"),
                "fill": self._get_color(instruction.get("fill"), "none"),
                "stroke": self._get_color(instruction.get("stroke"), "none"),
                "stroke-width": str(instruction.get("strokewidth", 0))
            }
            if instruction.get("fillopacity"):
                attrib["fill-opacity"] = str(instruction.get("fillopacity"))
            if instruction.get("strokedasharray"):
                attrib["stroke-dasharray"] = str(instruction.get("strokedasharray"))
            if instruction.get("linecap"):
                attrib["stroke-linecap"] = instruction.get("linecap")
                
            ET.SubElement(parent, "path", attrib)
            
        elif itype == "circle":
            attrib = {
                "cx": str(instruction.get("cx")),
                "cy": str(instruction.get("cy")),
                "r": str(instruction.get("r")),
                "fill": self._get_color(instruction.get("fill"), "none"),
                "stroke": self._get_color(instruction.get("stroke"), "none"),
                "stroke-width": str(instruction.get("strokewidth", 0))
            }
            ET.SubElement(parent, "circle", attrib)
            
        elif itype == "text":
            attrib = {
                "x": str(instruction.get("x")),
                "y": str(instruction.get("y")),
                "font-family": instruction.get("fontfamily", "Arial"),
                "font-size": str(instruction.get("fontsize")),
                "fill": self._get_color(instruction.get("fill"), "black"),
                "text-anchor": instruction.get("text-anchor", "start")
            }
            if instruction.get("stroke"):
                attrib["stroke"] = self._get_color(instruction.get("stroke"))
                
            text_elem = ET.SubElement(parent, "text", attrib)
            text_elem.text = instruction.get("text")
            
        elif itype == "translate":
            # Group with transform
            g = ET.SubElement(parent, "g", {
                "transform": f"translate({instruction.get('x', 0)},{instruction.get('y', 0)})"
            })
            for sub in instruction.get("draw", []):
                self._process_instruction(sub, g)
                
        elif itype == "scale":
            g = ET.SubElement(parent, "g", {
                "transform": f"scale({instruction.get('factor', 1)})"
            })
            for sub in instruction.get("draw", []):
                self._process_instruction(sub, g)

    def _get_color(self, color, default=None):
        if color is None: return default
        if color is False: return "none"
        if isinstance(color, dict): return "none" # Should not happen if resolved correctly
        return str(color)
