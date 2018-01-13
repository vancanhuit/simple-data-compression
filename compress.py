#!/usr/bin/env python3
import huffman.compressor
import lzw.compressor
import os
import argparse
import sys


'''
This script is used for executing compression
via command line interface
'''
# Command line parser
parser = argparse.ArgumentParser(description='Compress a file')
parser.add_argument('input_file', help='input file to be compressed')
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


uncompressed_size = os.stat(input_file).st_size
print('Uncompressed size: {} bytes'.format(uncompressed_size))

print('===== Using {} compression algorithm ======'.format(alg.upper()))
output_file = ''
if alg == 'huffman':
    output_file = huffman.compressor.compress(input_file, output_path)
elif alg == 'lzw':
    output_file = lzw.compressor.compress(input_file, output_path)

# Print some compression information
compressed_size = os.stat(output_file).st_size
print('Output file: {}'.format(output_file))
print('Compressed size: {} bytes'.format(compressed_size))
print('Compression ratio = {0} / {1} = {2:.3f}'.format(
    uncompressed_size, compressed_size,
    uncompressed_size / compressed_size))
sys.exit(0)
