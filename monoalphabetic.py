alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypt(text, key):
    res = ""
    for c in text:
        if c.lower() in alpha:
            sub = key[alpha.index(c.lower())]
            res += sub.upper() if c.isupper() else sub.lower()
        else:
            res += c
    return res

def decrypt(text, key):
    res = ""
    for c in text:
        if c.lower() in key.lower():
            sub = alpha[key.lower().index(c.lower())]
            res += sub.upper() if c.isupper() else sub.lower()
        else:
            res += c
    return res

if __name__ == "__main__":
    key = "qwertyuiopasdfghjklzxcvbnm"
    msg = "Hello, World!"
    enc = encrypt(msg, key)
    dec = decrypt(enc, key)
    print("Original  :", msg)
    print("Encrypted :", enc)
    print("Decrypted :", dec)
