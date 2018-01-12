import pytest
from huffman import compressor
from queue import PriorityQueue
from huffman.node import Node
import collections
import os


class TestCompressor(object):
    ''' Test functions in compress module '''
    def test_create_queue_from_frequencies(self):
        frequencies = {'a': 1, 'b': 2}
        q = compressor.create_queue_from_frequencies(frequencies)
        assert not q.empty()
        assert q.qsize() == 2
        assert q.get()[1] == Node('a', 1)
        assert q.get()[1] == Node('b', 2)

    def test_get_codes(self):
        child1 = Node('a', 1)
        child2 = Node('b', 2)
        child3 = Node('', 3, child1, child2)
        child4 = Node('c', 4)
        root = Node('', 7, child3, child4)

        codes = compressor.get_codes(root)
        assert type(codes) is dict
        assert 'a' in codes.keys()
        assert 'b' in codes.keys()
        assert 'c' in codes.keys()
        assert codes['a'] == '00'
        assert codes['b'] == '01'
        assert codes['c'] == '1'

    def test_build_tree(self):
        frequencies = {'a': 1, 'b': 2}
        root = compressor.build_tree(frequencies)
        assert type(root) is Node
        assert root.freq == 3

    def test_get_encoded_str(self):
        data = 'aab'
        frequencies = collections.Counter(data)
        root = compressor.build_tree(frequencies)
        encoded_str = compressor.get_encoded_str(root, data)
        assert encoded_str == '110'

    def test_compress(self):
        input_file = os.path.join(
            os.getcwd(), 'data', 'uncompressed', 'demo.txt')
        output_path = os.path.join(
            os.getcwd(), 'data', 'compressed')
        output_file = compressor.compress(input_file, output_path)
        assert os.path.exists(output_file)
