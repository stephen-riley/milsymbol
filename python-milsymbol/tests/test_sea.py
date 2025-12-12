
from milsymbol import Symbol

def test_sea_symbol():
    print("Generating Sea symbol...")
    # S-S-CLCV-- : Sea Surface Friend Carrier
    symbol = Symbol("SFSPCLCV--", size=30)
    
    svg = symbol.as_svg()
    print("SVG Generated length:", len(svg))
    
    with open("test_sea_symbol.svg", "w") as f:
        f.write(svg)
        
    print("Saved to test_sea_symbol.svg")

if __name__ == "__main__":
    test_sea_symbol()
