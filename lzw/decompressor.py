import os


def decompress(input_file, output_path):
    input_filename, input_fileext = os.path.splitext(
        os.path.basename(input_file))
    output_filename = input_filename + '.txt'
    output_file = os.path.join(output_path, output_filename)

    with open(input_file, 'rb') as f:
        data = f.read()

    step = 2
    length = len(data)
    codes = []
    for i in range(0, length, step):
        b = int.from_bytes(data[i:i + step], byteorder='big', signed=False)
        codes.append(b)

    encoded_str = decode(codes)
    with open(output_file, 'w') as out:
        out.write(encoded_str)

    return output_file


def decode(codes):
    # Initialize dictionary
    dic = {c: chr(c) for c in range(0, 256)}
    max_code = 255

    s = None
    entries = []
    for k in codes:
        entry = dic.get(k, None)
        if entry is None:
            entry = s + s[0]

        entries.append(entry)
        if s is not None:
            max_code += 1
            dic[max_code] = s + entry[0]
        s = entry
    return ''.join(entries)
