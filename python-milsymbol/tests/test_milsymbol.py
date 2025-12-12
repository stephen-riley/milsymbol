
import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

from milsymbol import Symbol

def test_svg_generation():
    print("Generating symbol...")
    # SFG-UCI--- : Ground Friend Unit Combat Infantry
    symbol = Symbol("SFG-UCI---", size=30)
    
    svg = symbol.as_svg()
    print("SVG Generated:")
    print(svg)
    
    with open("test_symbol.svg", "w") as f:
        f.write(svg)
        

    print("Saved to test_symbol.svg")
    
    try:
        print("Generating PNG...")
        png_data = symbol.as_png()
        with open("test_symbol.png", "wb") as f:
            f.write(png_data)
        print("Saved to test_symbol.png")
    except ImportError as e:
        print(f"Skipping PNG generation: {e}")
    except Exception as e:
        print(f"PNG generation failed: {e}")

if __name__ == "__main__":
    test_svg_generation()
