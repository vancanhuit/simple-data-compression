import pickle
import os
from huffman import compressor
from helpers import utility

''' This module contains function for implementing Huffman decoding '''


def decompress(input_file, output_path):
    input_filename, input_fileext = os.path.splitext(
        os.path.basename(input_file))
    output_filename = input_filename + '.txt'
    output_file = os.path.join(output_path, output_filename)

    with open(input_file, 'rb') as f:
        data = pickle.load(f)

    frequencies, byte_array = data
    root = compressor.build_tree(frequencies)
    bit_str = utility.convert_bytes_to_bit_str(byte_array)
    encoded_str = utility.remove_padding(bit_str)
    decoded_str = get_decoded_str(root, encoded_str)

    with open(output_file, 'w') as out:
        out.write(decoded_str)
    return output_file


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
            if type(char) is int:
                char = chr(char)
            decoded_data.append(char)
            current = root
    return ''.join(decoded_data)
