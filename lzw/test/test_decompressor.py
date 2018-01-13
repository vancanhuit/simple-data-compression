from lzw import compressor, decompressor
import os


class TestDecompress(object):
    def test_decode(self):
        data = 'ABABBABCABABBA'
        codes = compressor.encode(data)
        decoded_data = decompressor.decode(codes)
        assert decoded_data == data

    def test_decompress(self):
        input_file = os.path.join(
            os.getcwd(), 'data', 'compressed', 'demo-lzw.lzw')
        output_path = os.path.join(os.getcwd(), 'data', 'uncompressed')
        output_file = decompressor.decompress(input_file, output_path)
        assert os.path.exists(output_file)
        assert os.path.isfile(output_file)
