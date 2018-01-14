from shannon import compressor
import os


class TestCompressor(object):
    def test_create_nodes_from_frequencies(self):
        frequencies = {'A': 3, 'C': 1, 'B': 1}
        nodes = compressor.create_nodes_from_frequencies(frequencies)
        assert nodes is not None
        assert len(nodes) == 3
        assert nodes[0].char == 'A'
        assert nodes[1].char == 'C'
        assert nodes[2].char == 'B'

    def test_split(self):
        frequencies = {'L': 2, 'H': 1, 'E': 1, 'O': 1}
        nodes = compressor.create_nodes_from_frequencies(frequencies)
        index = compressor.split(nodes)
        assert nodes[0].char == 'L'
        assert nodes[1].char == 'O'
        assert nodes[2].char == 'H'
        assert nodes[3].char == 'E'
        assert index == 1

    def test_build_tree(self):
        frequencies = {'L': 2, 'H': 1, 'E': 1, 'O': 1}
        nodes = compressor.create_nodes_from_frequencies(frequencies)
        root = compressor.build_tree(nodes)
        assert root.freq == 5
        assert root.left.char == 'L'

    def test_compress(self):
        input_file = os.path.join(os.getcwd(), 'data', 'test', 'demo-fano.txt')
        output_path = os.path.join(os.getcwd(), 'data', 'compressed')
        output_file = compressor.compress(input_file, output_path)
        assert os.path.exists(input_file)
        assert os.path.isfile(input_file)
