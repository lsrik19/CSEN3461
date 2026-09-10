def encrypt(text, shift):
    res = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            res += chr((ord(c) - base + shift) % 26 + base)
        else:
            res += c
    return res

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    msg = "Hello, World!"
    shift = 3
    enc = encrypt(msg, shift)
    dec = decrypt(enc, shift)
    print("Original  :", msg)
    print("Encrypted :", enc)
    print("Decrypted :", dec)
