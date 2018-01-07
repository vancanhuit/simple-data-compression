from huffman import compress, decompress
import collections

data = 'aa bbb cccc'
frequencies = collections.Counter(data)
root = compress.build_tree(frequencies)
codes = compress.get_codes(root)
encoded_str = compress.get_encoded_str(root, data)
decoded_str = decompress.get_decoded_str(root, encoded_str)

print(codes)
print(encoded_str)
print(decoded_str)
