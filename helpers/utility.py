def pad_encoded_str(encoded_str):
    ''' Return encoded string with padding zero
    for storing in file in bytes '''
    extra_zero = 8 - len(encoded_str) % 8
    padded_encoded_str = '0' * extra_zero + encoded_str
    extra_zero_info = '{0:08b}'.format(extra_zero)
    padded_encoded_str = extra_zero_info + padded_encoded_str
    return padded_encoded_str


def remove_padding(padded_encoded_str):
    ''' Return encoded string with padding zero removed '''
    extra_zero_info = padded_encoded_str[:8]
    extra_zero = int(extra_zero_info, 2)
    padded_encoded_str = padded_encoded_str[8:]
    encoded_str = padded_encoded_str[extra_zero:]
    return encoded_str


def get_encoded_str(root, data):
    ''' Return encoded string of original data '''
    codes = get_codes(root)
    compressed_data = []
    for d in data:
        compressed_data.append(codes[d])
    return ''.join(compressed_data)


def get_decoded_str(root, encoded_str):
    ''' Decode encoded string '''
    decoded_data = []
    current = root
    for code in encoded_str:
        if code == "0":
            current = current.left
        else:
            current = current.right

        if current.is_leaf():
            char = current.char
            decoded_data.append(char)
            current = root
    return ''.join(decoded_data)


def get_codes(root):
    ''' Return codes for each element in original data '''
    current = root
    codes = {}
    code = []

    _assign_codes(root, codes, code)
    return codes


def _assign_codes(current, codes, code):
    ''' Recursively get codes helper '''
    if current.is_leaf():
        key = current.char
        codes[key] = ''.join(code)
        return

    if current.left:
        code.append('0')
        _assign_codes(current.left, codes, code)
        code.pop()

    if current.right:
        code.append('1')
        _assign_codes(current.right, codes, code)
        code.pop()


def get_byte_array(padded_encoded_str):
    ''' Convert padded encoded string into bytes
    for storing to file in bytes '''
    b = bytearray()
    length = len(padded_encoded_str)
    for i in range(0, length, 8):
        byte = padded_encoded_str[i:i + 8]
        b.append(int(byte, 2))
    return b


def convert_bytes_to_bit_str(byte_array):
    ''' Convert bytes to bit string for decoding '''
    bin_format = '{0:08b}'
    bit_data = []
    for b in byte_array:
        data = bin_format.format(b)
        bit_data.append(data)
    return ''.join(bit_data)
