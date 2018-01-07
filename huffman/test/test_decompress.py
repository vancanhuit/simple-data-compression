from huffman import decompress, compress
import collections


class TestDecompress(object):
    def test_decompress(self):
        data = 'aab'
        frequencies = collections.Counter(data)
        root = compress.build_tree(frequencies)
        compressed_data = compress.compress(root, data)
        decompressed_data = decompress.decompress(root, compressed_data)
        assert decompressed_data == data
