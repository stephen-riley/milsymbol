
import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

from milsymbol import Symbol

def test_svg_generation():
    print("Generating symbol...")
    # SFG-UCI----D : Ground Friend Unit Combat Infantry Platoon
    symbol = Symbol("SFG-UCI----K")
    
    svg = symbol.as_svg()
    print("SVG Generated:")
    print(svg)
    
    output_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, "test_symbol.svg"), "w") as f:
        f.write(svg)
        

    print(f"Saved to {output_dir}/test_symbol.svg")
    
    try:
        print("Generating PNG...")
        png_data = symbol.as_png()
        with open(os.path.join(output_dir, "test_symbol.png"), "wb") as f:
            f.write(png_data)
        print(f"Saved to {output_dir}/test_symbol.png")
    except ImportError as e:
        print(f"Skipping PNG generation: {e}")
    except Exception as e:
        print(f"PNG generation failed: {e}")

if __name__ == "__main__":
    test_svg_generation()
