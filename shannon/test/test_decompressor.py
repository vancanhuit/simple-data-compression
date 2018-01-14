from shannon import decompressor
import os


class TestDecompressor(object):
    def test_decompress(self):
        input_file = os.path.join(
            os.getcwd(), 'data', 'compressed', 'demo-fano.fano')
        output_path = os.path.join(os.getcwd(), 'data', 'uncompressed')
        output_file = decompressor.decompress(input_file, output_path)
        assert os.path.exists(output_file)
        assert os.path.isfile(output_file)
