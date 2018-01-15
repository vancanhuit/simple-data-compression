# Simple data compressing

## Tools

- Install [Python 3.5+](https://www.python.org/)
- (Optional) Install `pytest` for running unit tests. Unit tests are placed in `test` folders.

    ```sh
    $ [sudo] pip install pytest
    ```

## Usage

To compress a file and store it in a path, run `compress.py` script. To show help, enter `./compress.py -h` command:

```sh
$ ./compress -h
usage: compress.py [-h] [--alg {huffman,fano,lzw}] input_file output_path

Compress a file

positional arguments:
  input_file            input file to be compressed
  output_path           output path for storing decompressed output file

optional arguments:
  -h, --help            show this help message and exit
  --alg {huffman,fano,lzw}
                        choose an algorithm, default is huffman
```

When run this script, you must choose one of three algorithms (`huffman`, `fano`, `lzw`), pass an `input file` to be compressed and an `output path` for storing decompressed file.
Huffman algorithm will be default when run this script. To run with another algorithm, use option `--alg` to specify an algorithm you want. For example:

```sh
$ ./compress.py ~/Desktop/5-1300msg2.txt ~/Desktop
Uncompressed size: 10033 bytes
===== Using HUFFMAN compression algorithm ======
Output file: /home/vancanhuit/Desktop/5-1300msg2.huffman
Compressed size: 6065 bytes
Compression ratio = 10033 / 6065 = 1.654
$ ./compress.py --alg=lzw ~/Desktop/6-160msg3.txt ~/Desktop
Uncompressed size: 4994 bytes
===== Using LZW compression algorithm ======
Output file: /home/vancanhuit/Desktop/6-160msg3.lzw
Compressed size: 3944 bytes
Compression ratio = 4994 / 3944 = 1.266
```

To decompress, run `./decompress.py`. Options are similar above:

```sh
$ ./decompress.py -h
usage: decompress.py [-h] [--alg {huffman,fano,lzw}] input_file output_path

Decompress a file

positional arguments:
  input_file            input file to be decompressed
  output_path           output path for storing uncompressed output file

optional arguments:
  -h, --help            show this help message and exit
  --alg {huffman,fano,lzw}
                        choose an algorithm, default is huffman
```

For example:

```sh
$ ./decompress.py --alg=lzw  ~/Desktop/6-160msg3.lzw ~/Desktop
Compressed size: 3944 bytes
====== Using LZW decompression algorithm =======
Output file: /home/vancanhuit/Desktop/6-160msg3.txt
Uncompressed size: 4994 bytes
$ ./decompress.py ~/Desktop/5-1300msg2.huffman ~/Desktop
Compressed size: 6065 bytes
====== Using HUFFMAN decompression algorithm =======
Output file: /home/vancanhuit/Desktop/5-1300msg2.txt
Uncompressed size: 10033 bytes
```

## Test data
Text files is taken from [Ling Spam dataset](http://csmining.org/index.php/ling-spam-datasets.html). This text dataset is divided into 10 parts, located in `data/test` folder.
