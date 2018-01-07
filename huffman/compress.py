from huffman.node import Node
from queue import PriorityQueue
import collections


def compress(root, data):
    codes = get_codes(root)
    compressed_data = []
    for d in data:
        compressed_data.append(codes[d])

    return ''.join(compressed_data)


def build_tree(frequencies):
    q = create_queue_from_frequencies(frequencies)
    while not (q.qsize() == 1):
        left = q.get()[1]
        right = q.get()[1]
        new_node = Node('', left.freq + right.freq, left, right)
        q.put((new_node.freq, new_node))

    root = q.get()[1]
    return root


def create_queue_from_frequencies(frequencies):
    q = PriorityQueue()
    for k, v in frequencies.items():
        n = Node(k, v)
        q.put((n.freq, n))
    return q


def get_codes(root):
    current = root
    codes = {}
    code = []

    _assign_codes(root, codes, code)
    return codes


def _assign_codes(current, codes, code):
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
