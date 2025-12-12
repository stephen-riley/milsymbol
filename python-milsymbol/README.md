
# Milsymbol for Python

A Python library for generating military symbols according to MIL-STD-2525 and STANAG APP-6 standards. Ported from the [milsymbol.js](https://github.com/spatialillusions/milsymbol) library.

## Installation

```bash
pip install .
```

For PNG support (requires `cairosvg`):

```bash
pip install ".[png]"
```

## Usage

```python
from milsymbol import Symbol

# Generate a symbol
symbol = Symbol("SFG-UCI---", size=30)

# Get SVG string
svg = symbol.as_svg()

# Save to file
with open("symbol.svg", "w") as f:
    f.write(svg)
```

## Features

- **Domains**: Air, Sea, Subsurface, and partial Ground support.
- **Modifiers**: Standard text modifiers (Unique Designation, Staff Comments, etc.).
- **Output**: SVG and PNG (optional).

## License

MIT License (See LICENSE file).
