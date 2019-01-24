import byte_reader
import tiles.floor
import tiles.sign
N_SIZE_BYTES = 1
N_TILE_ID_BYTES = 1

class Room:
    def __init__(self, 
                 width: int, 
                 height: int, 
                 tiles: [], 
                 tile_types: []
                 ):
        self.width = width
        self.height = height
        self.tiles = tiles
        self.tile_types = tile_types
    
    def to_bytes(self):
        byte_array = bytearray([])
        byte_array += byte_reader.write_int(N_SIZE_BYTES, self.width)
        byte_array += byte_reader.write_int(N_SIZE_BYTES, self.height)
        for tile in self.tiles:
            byte_array += byte_reader.write_int(
                            N_TILE_ID_BYTES,
                            tile[0]
                            )
        for tile in self.tiles:
            tile_type = self.tile_types[tile[0]]
            byte_array += tile_type.bytes_from_meta(tile[1])
        return byte_array

    @staticmethod
    def from_bytes(
            bytes: bytearray, 
            index: [int], 
            tile_types: []
            ):
        width  = byte_reader.read_int(N_SIZE_BYTES,bytes,index)
        height = byte_reader.read_int(N_SIZE_BYTES,bytes,index)
        tile_ids = []
        for _ in range(width*height):
            tile_ids.append(
                byte_reader.read_int(N_TILE_ID_BYTES,bytes,index)
            )
        tiles = []
        for tile_id in tile_ids:
            tiles.append([
                tile_id,
                tile_types[tile_id].meta_from_bytes(bytes,index)
                ])
        return Room(width, height, tiles, tile_types)

    @staticmethod
    def create_filled(
            width: int,
            height: int,
            fill_id: int,
            fill_meta: [],
            tile_types
            ):
        tiles = []
        for _ in range(width*height):
            tiles.append([fill_id, fill_meta])
        return Room(width,height,tiles,tile_types)

tiletypes = [
    tiles.floor.Floor(1),
    tiles.sign.Sign(1)
]
print(
    Room.create_filled(
        5,5,1,
        ["hi","Justin Beiber"],
        tiletypes
        ).to_bytes(),
    )