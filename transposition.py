def single_encrypt(text, key):
    cols = len(key)
    pad = (cols - len(text) % cols) % cols
    text += "X" * pad
    rows = len(text) // cols
    order = sorted(range(cols), key=lambda k: key[k])
    return "".join(text[r * cols + c] for c in order for r in range(rows))

def single_decrypt(cipher, key):
    cols = len(key)
    rows = len(cipher) // cols
    order = sorted(range(cols), key=lambda k: key[k])
    grid = [[""] * cols for _ in range(rows)]
    idx = 0
    for c in order:
        for r in range(rows):
            grid[r][c] = cipher[idx]
            idx += 1
    return "".join("".join(row) for row in grid)

def encrypt(text, key1, key2):
    return single_encrypt(single_encrypt(text, key1), key2)

def decrypt(cipher, key1, key2):
    return single_decrypt(single_decrypt(cipher, key2), key1)

if __name__ == "__main__":
    msg = "ATTACKATDAWN"
    k1 = "KEY"
    k2 = "LOCK"
    enc = encrypt(msg, k1, k2)
    dec = decrypt(enc, k1, k2)
    print("Original  :", msg)
    print("Encrypted :", enc)
    print("Decrypted :", dec)
