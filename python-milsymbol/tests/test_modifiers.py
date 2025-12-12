
from milsymbol import Symbol

def test_modifiers():
    print("Generating Symbol with Modifiers...")
    # S-G-U-C----- : Ground Unit Combat
    symbol = Symbol("SGFUC---------", 
                    uniqueDesignation="Alpha Company", 
                    higherFormation="1st Battalion",
                    speed="30 kph",
                    reinforcedReduced="+",
                    staffComments="Moving East",
                    size=30)
    
    svg = symbol.as_svg()
    print("SVG Generated length:", len(svg))
    
    if "Alpha Company" in svg:
        print("Found Unique Designation in SVG")
    else:
        print("Unique Designation NOT found in SVG")
        
    with open("test_modifiers.svg", "w") as f:
        f.write(svg)
        
    print("Saved to test_modifiers.svg")

if __name__ == "__main__":
    test_modifiers()
