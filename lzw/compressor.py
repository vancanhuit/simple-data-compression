import os


''' This module implement LZW compression algorithm '''


def compress(input_file, output_path):
    input_filename, input_fileext = os.path.splitext(
        os.path.basename(input_file))
    output_filename = input_filename + '.lzw'
    output_file = os.path.join(output_path, output_filename)

    with open(input_file, 'r') as f:
        data = f.read()

    codes = encode(data)

    # write codes into file with 2-bytes for each code
    with open(output_file, 'wb') as out:
        for c in codes:
            out.write((c).to_bytes(2, byteorder='big'))

    return output_file


def encode(data):
    # Initialize dictionary
    dic = {chr(c): c for c in range(0, 256)}
    chars = dic.keys()
    max_code = 255

    index = 0
    s = data[index]
    length = len(data)
    codes = []
    while index < length - 1:
        c = data[index + 1]
        if s + c in chars:
            s = s + c
            index += 1
        else:
            codes.append(dic[s])
            max_code += 1
            dic[s + c] = max_code
            s = c
            index += 1
    codes.append(dic[s])
    return codes
