def encrypt(text, key):
    res = ""
    key = key.lower()
    ki = 0
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            shift = ord(key[ki % len(key)]) - ord('a')
            res += chr((ord(c) - base + shift) % 26 + base)
            ki += 1
        else:
            res += c
    return res

def decrypt(text, key):
    res = ""
    key = key.lower()
    ki = 0
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            shift = ord(key[ki % len(key)]) - ord('a')
            res += chr((ord(c) - base - shift) % 26 + base)
            ki += 1
        else:
            res += c
    return res

if __name__ == "__main__":
    msg = "Hello, World!"
    key = "KEY"
    enc = encrypt(msg, key)
    dec = decrypt(enc, key)
    print("Original  :", msg)
    print("Encrypted :", enc)
    print("Decrypted :", dec)