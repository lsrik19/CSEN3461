def encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    rail, step = 0, 1
    for c in text:
        fence[rail].append(c)
        if rail == 0:
            step = 1
        elif rail == rails - 1:
            step = -1
        rail += step
    return "".join("".join(row) for row in fence)

def decrypt(cipher, rails):
    pattern = []
    rail, step = 0, 1
    for _ in range(len(cipher)):
        pattern.append(rail)
        if rail == 0:
            step = 1
        elif rail == rails - 1:
            step = -1
        rail += step

    res = [""] * len(cipher)
    idx = 0
    for r in range(rails):
        for i in range(len(cipher)):
            if pattern[i] == r:
                res[i] = cipher[idx]
                idx += 1
    return "".join(res)

if __name__ == "__main__":
    msg = "DEFENDTHEEASTWALL"
    rails = 3
    enc = encrypt(msg, rails)
    dec = decrypt(enc, rails)
    print("Original  :", msg)
    print("Encrypted :", enc)
    print("Decrypted :", dec)
