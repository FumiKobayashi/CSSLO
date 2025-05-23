"""
CSSLO - A library for quantum error correction codes
"""

from .distance import distGenetic, indepLZ, minWeight, minWeightLZ, minWeightZ2, zimDist

__version__ = "0.1.0"

__all__ = [
    "distGenetic",
    "indepLZ",
    "minWeight",
    "minWeightLZ",
    "minWeightZ2",
    "zimDist",
]
