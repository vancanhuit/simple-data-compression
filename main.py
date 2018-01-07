from huffman import compress

data = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
root = compress.compress(data)
codes = compress.get_codes(root)

for char, code in codes.items():
    print('{}: {}'.format(char, code))
