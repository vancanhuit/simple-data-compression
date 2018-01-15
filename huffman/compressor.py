from entity.node import Node
from queue import PriorityQueue
import collections
import os
from helpers import utility
import pickle


def compress(input_file, output_path):
    ''' Compress input_file, store it in output_path and then
    return output_file '''
    # Get file name and extension
    input_filename, input_fileext = os.path.splitext(
        os.path.basename(input_file))
    output_filename = input_filename + '.huffman'
    output_file = os.path.join(output_path, output_filename)

    with open(input_file, 'r') as f:
        data = f.read()

    # Get frequency table from data
    frequencies = collections.Counter(data)
    root = build_tree(frequencies)
    encoded_str = utility.get_encoded_str(root, data)
    padded_encoded_str = utility.pad_encoded_str(encoded_str)
    byte_data = utility.get_byte_array(padded_encoded_str)

    with open(output_file, 'wb') as out:
        # Serialize data to file
        pickle.dump((frequencies, byte_data), out)
    return output_file


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
