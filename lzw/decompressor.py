def decode(codes):
    # Initialize dictionary
    dic = {c: chr(c) for c in range(0, 256)}
    max_code = 255

    s = None
    entries = []
    for k in codes:
        entry = dic[k]
        entries.append(entry)
        if s is not None:
            max_code += 1
            dic[max_code] = s + entry[0]
        s = entry
    return ''.join(entries)
