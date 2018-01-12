import os


def encode(data):
    # Initialize dictionary
    dic = {}
    for c in range(0, 256):
        dic[chr(c)] = c
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
