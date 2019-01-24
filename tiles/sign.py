"""
A sign is a tile that pops up some text when interacted with
"""
import tiles.tile
import byte_reader

class Sign(tiles.tile.Tile):
    def __init__(self, texture):
        self.texture = texture
    
    def init_meta(self):
        return ['Empty sign', 'Author']
    
    def meta_from_bytes(self, bytes: bytearray, index: [int]):
        message = byte_reader.read_str(bytes,index)
        author  = byte_reader.read_str(bytes,index)
        return [message, author]
    
    def bytes_from_meta(self, meta):
        return (byte_reader.write_str(meta[0]) 
                + byte_reader.write_str(meta[1])
                )