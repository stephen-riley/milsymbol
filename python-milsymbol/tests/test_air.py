
from milsymbol import Symbol

def test_air_symbol():
    print("Generating Air symbol...")

    # S-A-MF---- is the internal key format.
    # Valid SIDC: SFAPMF---- (S=Warfighting, F=Friend, A=Air, P=Present, MF----=Fixed Wing)
    symbol = Symbol("SFAPMF----", size=30)
    
    svg = symbol.as_svg()
    print("SVG Generated length:", len(svg))
    
    with open("test_air_symbol.svg", "w") as f:
        f.write(svg)
        
    print("Saved to test_air_symbol.svg")

if __name__ == "__main__":
    test_air_symbol()
