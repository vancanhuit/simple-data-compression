from lzw import compressor
import os


class TestCompressor(object):
    def test_encode(self):
        data = 'ABABBABCABABBA'
        codes = compressor.encode(data)
        assert len(codes) == 9

    def test_compress(self):
        input_file = os.path.join(
            os.getcwd(), 'data', 'demo-lzw.txt')
        output_path = os.path.join(os.getcwd(), 'data', 'compressed')
        output_file = compressor.compress(input_file, output_path)
        assert os.path.exists(output_file)
        assert os.path.isfile(output_file)
