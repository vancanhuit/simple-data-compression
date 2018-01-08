from helpers import utility
import os


class TestUtility(object):
    def test_pad_encoded_str(self):
        encoded_str = '110'
        padded_encoded_str = utility.pad_encoded_str(encoded_str)
        assert padded_encoded_str == '0000010100000110'

    def test_remove_padding(self):
        padded_encoded_str = '0000010100000110'
        encoded_str = utility.remove_padding(padded_encoded_str)
        assert encoded_str == '110'

    def test_get_byte_array(self):
        padded_encoded_str = '0000010100000110'
        b = utility.get_byte_array(padded_encoded_str)
        assert len(b) == 2
        assert b[0] == 5
        assert b[1] == 6

    def test_write_byte_array_to_file(self):
        b = bytes(b'\x05\x06')
        file = os.path.join(os.getcwd(), 'data', 'output.huffman')
        utility.write_byte_array_to_file(b, file)
        assert os.path.exists(file)

    def test_read_bytes_from_file(self):
        file = os.path.join(os.getcwd(), 'data', 'output.huffman')
        b = utility.read_bytes_from_file(file)
        assert type(b) is bytes
        assert len(b) == 2

    def test_convert_bytes_to_bit_str(self):
        b = bytes(b'\x05\x06')
        bit_str = utility.convert_bytes_to_bit_str(b)
        assert bit_str == '0000010100000110'
