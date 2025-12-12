
import os
from milsymbol import Symbol

def test_air_symbol():
    print("Generating Air symbol...")

    # S-A-MF---- is the internal key format.
    # Valid SIDC: SFAPMF---- (S=Warfighting, F=Friend, A=Air, P=Present, MF----=Fixed Wing)
    symbol = Symbol("SFAPMF----")
    
    svg = symbol.as_svg()
    print("SVG Generated length:", len(svg))
    
    output_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, "test_air_symbol.svg"), "w") as f:
        f.write(svg)
        
    print(f"Saved to {output_dir}/test_air_symbol.svg")

if __name__ == "__main__":
    test_air_symbol()
