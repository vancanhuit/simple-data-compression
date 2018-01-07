from huffman import compress, decompress
import collections

data = 'aa bbb cccc'
frequencies = collections.Counter(data)
root = compress.build_tree(frequencies)
codes = compress.get_codes(root)
compressed_data = compress.compress(root, data)
decompressed_data = decompress.decompress(root, compressed_data)

print(codes)
print(compressed_data)
print(decompressed_data)
