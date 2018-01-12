from lzw import compressor
import os


class TestCompressor(object):
    def test_encode(self):
        data = 'ABABBABCABABBA'
        codes = compressor.encode(data)
        assert len(codes) == 9
