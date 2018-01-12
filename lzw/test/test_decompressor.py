from lzw import compressor, decompressor


class TestDecompress(object):
    def test_decode(codes):
        data = 'ABABBABCABABBA'
        codes = compressor.encode(data)
        decoded_data = decompressor.decode(codes)
        assert decoded_data == data
