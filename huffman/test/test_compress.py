import pytest
from huffman import compress
from queue import PriorityQueue
from huffman.node import Node
import collections


class TestCompress(object):
    def test_create_queue_from_frequencies(self):
        frequencies = {'a': 1, 'b': 2}
        q = compress.create_queue_from_frequencies(frequencies)
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

        codes = compress.get_codes(root)
        assert type(codes) is dict
        assert 'a' in codes.keys()
        assert 'b' in codes.keys()
        assert 'c' in codes.keys()
        assert codes['a'] == '00'
        assert codes['b'] == '01'
        assert codes['c'] == '1'

    def test_build_tree(self):
        frequencies = {'a': 1, 'b': 2}
        root = compress.build_tree(frequencies)
        assert type(root) is Node
        assert root.freq == 3

    def test_get_encoded_str(self):
        data = 'aab'
        frequencies = collections.Counter(data)
        root = compress.build_tree(frequencies)
        encoded_str = compress.get_encoded_str(root, data)
        assert encoded_str == '110'
