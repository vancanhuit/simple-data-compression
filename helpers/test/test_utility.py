from helpers import utility
from entity.node import Node
import os
import collections


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

    def test_convert_bytes_to_bit_str(self):
        b = bytes(b'\x05\x06')
        bit_str = utility.convert_bytes_to_bit_str(b)
        assert bit_str == '0000010100000110'

    def test_get_codes(self):
        child1 = Node('a', 1)
        child2 = Node('b', 2)
        child3 = Node('', 3, child1, child2)
        child4 = Node('c', 4)
        root = Node('', 7, child3, child4)

        codes = utility.get_codes(root)
        assert type(codes) is dict
        assert 'a' in codes.keys()
        assert 'b' in codes.keys()
        assert 'c' in codes.keys()
        assert codes['a'] == '00'
        assert codes['b'] == '01'
        assert codes['c'] == '1'

    def test_get_encoded_str(self):
        data = 'ABB'
        n1 = Node('A', 1)
        n2 = Node('B', 2)
        root = Node('', 3, n2, n1)
        encoded_str = utility.get_encoded_str(root, data)
        assert encoded_str == '100'

    def test_get_decoded_str(self):
        data = 'aab'
        n1 = Node('a', 2)
        n2 = Node('b', 1)
        root = Node('', 3, n2, n1)
        encoded_str = utility.get_encoded_str(root, data)
        decoded_str = utility.get_decoded_str(root, encoded_str)
        assert decoded_str == data
