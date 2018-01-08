from huffman import decompress, compress
import collections
import os


class TestDecompress(object):
    def test_get_decoded_str(self):
        data = 'aab'
        frequencies = collections.Counter(data)
        root = compress.build_tree(frequencies)
        encoded_str = compress.get_encoded_str(root, data)
        decoded_str = decompress.get_decoded_str(root, encoded_str)
        assert decoded_str == data
