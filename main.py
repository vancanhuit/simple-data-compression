from huffman import compress, decompress
import collections
import os

input_file = '/home/vancanhuit/Desktop/demo.txt'
output_path = '/home/vancanhuit/Desktop'

output_file = compress.compress(input_file, output_path)

uncompressed_data_size = os.stat(input_file).st_size
compressed_data_size = os.stat(output_file).st_size
print('Uncompressed size data: {} bytes'.format(uncompressed_data_size))
print('Compressed size data: {} bytes'.format(compressed_data_size))
print('Compression ratio: {0} / {1} = {2:.3f}'.format(
    uncompressed_data_size, compressed_data_size,
    uncompressed_data_size / compressed_data_size))
