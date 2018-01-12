from huffman import decompressor, compressor
import collections
import os


class TestDecompressor(object):
    ''' Test functions in decompress module '''
    def test_get_decoded_str(self):
        data = 'aab'
        frequencies = collections.Counter(data)
        root = compressor.build_tree(frequencies)
        encoded_str = compressor.get_encoded_str(root, data)
        decoded_str = decompressor.get_decoded_str(root, encoded_str)
        assert decoded_str == data
