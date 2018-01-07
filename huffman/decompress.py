def get_decoded_str(root, encoded_str):
    decoded_data = []
    current = root
    for code in encoded_str:
        if code == "0":
            current = current.left
        else:
            current = current.right

        if current.is_leaf():
            char = current.char
            decoded_data.append(char)
            current = root
    return ''.join(decoded_data)
