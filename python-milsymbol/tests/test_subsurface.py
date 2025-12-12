
import os
from milsymbol import Symbol

def test_subsurface_symbol():
    print("Generating Subsurface symbol...")
    # S-U-SNA--- : Subsurface Friend Nuclear Attack Submarine
    symbol = Symbol("SFUSSNA---")
    
    svg = symbol.as_svg()
    print("SVG Generated length:", len(svg))
    
    output_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, "test_subsurface_symbol.svg"), "w") as f:
        f.write(svg)
        
    print(f"Saved to {output_dir}/test_subsurface_symbol.svg")

if __name__ == "__main__":
    test_subsurface_symbol()
