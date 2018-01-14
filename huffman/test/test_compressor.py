import pytest
from huffman import compressor
from queue import PriorityQueue
from entity.node import Node
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

    def test_build_tree(self):
        frequencies = {'a': 1, 'b': 2}
        root = compressor.build_tree(frequencies)
        assert type(root) is Node
        assert root.freq == 3

    def test_compress(self):
        input_file = os.path.join(
            os.getcwd(), 'data', 'test', 'demo.txt')
        output_path = os.path.join(
            os.getcwd(), 'data', 'compressed')
        output_file = compressor.compress(input_file, output_path)
        assert os.path.exists(output_file)
        assert os.path.isfile(output_file)
