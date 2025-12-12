
from setuptools import setup, find_packages

setup(
    name="milsymbol",
    version="0.1.0",
    description="A Python library for MIL-STD-2525 and STANAG APP-6 military symbols, ported from milsymbol.js",
    author="Antigravity",
    packages=find_packages(),
    install_requires=[
        "cairosvg",
    ],
    extras_require={
        "png": ["cairosvg>=2.0.0"],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: GIS",
        "Programming Language :: Python :: 3",
    ],
)
