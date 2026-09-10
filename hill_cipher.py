def encrypt(text, key):
    text = "".join(c for c in text.upper() if c.isalpha())
    if len(text) % 2 != 0:
        text += "X"
    res = ""
    for i in range(0, len(text), 2):
        x = ord(text[i]) - 65
        y = ord(text[i + 1]) - 65
        res += chr((key[0][0] * x + key[0][1] * y) % 26 + 65)
        res += chr((key[1][0] * x + key[1][1] * y) % 26 + 65)
    return res

def decrypt(text, key):
    det = (key[0][0] * key[1][1] - key[0][1] * key[1][0]) % 26
    inv_det = pow(det, -1, 26)
    inv_key = [
        [(key[1][1] * inv_det) % 26, (-key[0][1] * inv_det) % 26],
        [(-key[1][0] * inv_det) % 26, (key[0][0] * inv_det) % 26]
    ]
    return encrypt(text, inv_key)

if __name__ == "__main__":
    key = [[3, 3], [2, 5]]
    msg = "HELP"
    enc = encrypt(msg, key)
    dec = decrypt(enc, key)
    print("Original  :", msg)
    print("Encrypted :", enc)
    print("Decrypted :", dec)
