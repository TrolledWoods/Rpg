def read_int(n_bytes, bytes: bytearray, index: [int]):
    index[0] += n_bytes
    return int.from_bytes(
        bytes[index[0]-n_bytes:index[0]],
        byteorder='big', signed=False
    )

def write_int(n_bytes: int, value: int):
    reverse_byte_vals = []
    for _ in range(n_bytes):
        reverse_byte_vals.append(value & 255)
        value = value >> 8
    if value > 0:
        raise Exception("Value does not fit within "
                        + str(n_bytes)
                        + " bytes")
    return bytearray(reverse_byte_vals[::-1])

def write_str(text: str):
    """
    text cannot be longer than 255 characters
    """
    return bytearray([len(text)]) + text.encode()

def read_str(bytes: bytearray, index: [int]):
    length = read_int(1, bytes, index)
    text_bytes = bytes[index[0]:index[0]+length]
    index[0] += length
    return text_bytes.decode()