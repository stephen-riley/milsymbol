
from milsymbol import Symbol

def test_subsurface_symbol():
    print("Generating Subsurface symbol...")
    # S-U-SNA--- : Subsurface Friend Nuclear Attack Submarine
    symbol = Symbol("SFUSSNA---", size=30)
    
    svg = symbol.as_svg()
    print("SVG Generated length:", len(svg))
    
    with open("test_subsurface_symbol.svg", "w") as f:
        f.write(svg)
        
    print("Saved to test_subsurface_symbol.svg")

if __name__ == "__main__":
    test_subsurface_symbol()
