#!/usr/bin/env python3
import lzw.decompressor
import shannon.decompressor
import huffman.decompressor
import os
import argparse
import sys


'''
This script is used for executing decompression
via command line interface
'''
# Command line parser
parser = argparse.ArgumentParser(
    description='Decompress a file')
parser.add_argument('input_file', help='input file to be decompressed')
parser.add_argument(
    'output_path', help='output path for storing decompressed output file')
parser.add_argument(
    '--alg',
    help='choose an algorithm, default is huffman',
    choices=['huffman', 'fano', 'lzw'], default='huffman')
args = parser.parse_args()

# Main script
input_file = args.input_file
output_path = args.output_path
alg = args.alg

if not os.path.isfile(input_file):
    print("ERROR: {} isn't a file or doesn't exist".format(input_file))
    sys.exit(1)

if not os.path.isdir(output_path):
    print("ERROR: {} isn't a path or doesn't exist.".format(output_path))
    sys.exit(1)


compressed_size = os.stat(input_file).st_size
print('Compressed size: {} bytes'.format(compressed_size))

print('====== Using {} decompression algorithm ======='.format(alg.upper()))
output_file = ''

if alg == 'lzw':
    output_file = lzw.decompressor.decompress(input_file, output_path)
elif alg == 'huffman':
    output_file = huffman.decompressor.decompress(input_file, output_path)
else:
    output_file = shannon.decompressor.decompress(input_file, output_path)

uncomprssed_size = os.stat(output_file).st_size
print('Output file: {}'.format(output_file))
print('Uncompressed size: {} bytes'.format(uncomprssed_size))
sys.exit(0)
