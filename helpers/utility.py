def pad_encoded_str(encoded_str):
    extra_zero = 8 - len(encoded_str) % 8
    padded_encoded_str = '0' * extra_zero + encoded_str
    extra_zero_info = '{0:08b}'.format(extra_zero)
    padded_encoded_str = extra_zero_info + padded_encoded_str
    return padded_encoded_str


def remove_padding(padded_encoded_str):
    extra_zero_info = padded_encoded_str[:8]
    extra_zero = int(extra_zero_info, 2)
    padded_encoded_str = padded_encoded_str[8:]
    encoded_str = padded_encoded_str[extra_zero:]
    return encoded_str


def get_byte_array(padded_encoded_str):
    b = bytearray()
    length = len(padded_encoded_str)
    for i in range(0, length, 8):
        byte = padded_encoded_str[i:i + 8]
        b.append(int(byte, 2))
    return b


def write_byte_array_to_file(byte_array, file):
    with open(file, 'wb') as f:
        f.write(byte_array)


def read_bytes_from_file(file):
    b = bytes()
    with open(file, 'rb') as f:
        b = f.read()
    return b


def convert_bytes_to_bit_str(byte_array):
    bin_format = '{0:08b}'
    bit_data = []
    for b in byte_array:
        data = bin_format.format(b)
        bit_data.append(data)
    return ''.join(bit_data)
