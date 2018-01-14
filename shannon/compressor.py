from entity.node import Node
from operator import attrgetter
from helpers import utility
import os
import collections
import pickle


def compress(input_file, output_path):
    input_filename, input_fileext = os.path.splitext(
        os.path.basename(input_file))
    output_filename = input_filename + '.fano'
    output_file = os.path.join(output_path, output_filename)

    with open(input_file, 'r') as f:
        data = f.read()

    frequencies = collections.Counter(data)
    nodes = create_nodes_from_frequencies(frequencies)
    root = build_tree(nodes)
    codes = utility.get_codes(root)
    encoded_str = utility.get_encoded_str(root, data)
    padded_encoded_str = utility.pad_encoded_str(encoded_str)
    byte_array = utility.get_byte_array(padded_encoded_str)

    with open(output_file, 'wb') as out:
        pickle.dump((frequencies, byte_array), out)

    return output_file


def build_tree(nodes):
    length = len(nodes)
    if length == 1:
        return nodes[0]

    index = split(nodes)
    left = build_tree(nodes[0:index])
    right = build_tree(nodes[index:])
    return Node('', left.freq + right.freq, left, right)


def create_nodes_from_frequencies(frequencies):
    nodes = []
    for k, v in frequencies.items():
        nodes.append(Node(k, v))
    # Sort by frequencies, then by alphabet
    nodes.sort(key=attrgetter('freq', 'char'), reverse=True)
    return nodes


def split(nodes):
    length = len(nodes)
    total = sum([n.freq for n in nodes])
    second_half_total = 0
    index = length

    while (index >= 0) and (second_half_total < (total - second_half_total)):
        index -= 1
        second_half_total += nodes[index].freq

    diff1 = second_half_total - (total - second_half_total)
    diff2 = abs(diff1 - 2 * nodes[index].freq)
    if diff2 < diff1:
        index += 1
    return index
