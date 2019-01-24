"""
A group for all the normal floor tiles. These all only really
have a texture, and never collide when moving onto them.
They also have no meta data
"""
import tiles.tile

class Floor(tiles.tile.Tile):
    def __init__(self, texture):
        self.texture = texture