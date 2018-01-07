from huffman import compress
import collections

data = 'aab'
frequencies = collections.Counter(data)
root = compress.build_tree(frequencies)
encoded_data = compress.get_encoded_data(root, data)

print(encoded_data)
