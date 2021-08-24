"""
 light.py by Thomas on 8/23/2021
"""
from color import Color

class Light:
    """Light is a point light of a color"""

    def __init__(self, position, color=Color.from_hex("#FFFFFF")):
        self.position = position
        self.color = color
