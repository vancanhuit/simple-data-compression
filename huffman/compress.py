from huffman.node import Node
from queue import PriorityQueue
import collections
import os
from helpers import utility

''' This module contains functions for implmenting Huffman encoding '''


def compress(input_file, output_path):
    ''' Compress input_file, store it in output_path and then
    return output_file '''
    # Get file name and extension
    input_filename, input_fileext = os.path.splitext(
        os.path.basename(input_file))
    output_filename = input_filename + '.huffman'
    output_file = os.path.join(output_path, output_filename)

    with open(input_file, 'rb') as f:
        data = [b for b in f.read()]

    # Get frequency table from data
    frequencies = collections.Counter(data)
    root = build_tree(frequencies)
    codes = get_codes(root)
    encoded_str = get_encoded_str(root, data)
    padded_encoded_str = utility.pad_encoded_str(encoded_str)
    byte_data = utility.get_byte_array(padded_encoded_str)
    utility.write_byte_array_to_file(byte_data, output_file)
    return output_file


def get_encoded_str(root, data):
    ''' Return encoded string of original data '''
    codes = get_codes(root)
    compressed_data = []
    for d in data:
        compressed_data.append(codes[d])
    return ''.join(compressed_data)


def build_tree(frequencies):
    ''' Build Huffman tree and return its root '''
    q = create_queue_from_frequencies(frequencies)
    while q.qsize() > 1:
        left = q.get()[1]
        right = q.get()[1]
        new_node = Node('', left.freq + right.freq, left, right)
        q.put((new_node.freq, new_node))

    root = q.get()[1]
    return root


def create_queue_from_frequencies(frequencies):
    ''' Create priority queue from frequency table '''
    q = PriorityQueue()
    for k, v in frequencies.items():
        n = Node(k, v)
        q.put((n.freq, n))
    return q


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
