def decompress(root, compressed_data):
    decompressed_data = []
    current = root
    for code in compressed_data:
        if code == "0":
            current = current.left
        else:
            current = current.right

        if current.is_leaf():
            char = current.char
            decompressed_data.append(char)
            current = root
    return ''.join(decompressed_data)
