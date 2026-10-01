def ksa(key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def prga(S, length):
    i = j = 0
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        yield S[(S[i] + S[j]) % 256]


def rc4(data, key):
    S = ksa(key)
    return bytes(b ^ k for b, k in zip(data, prga(S, len(data))))


plaintext = b"GITAMUNIVERSITYISDEEMEDTOBEUNIVERSITY"
key = b"LOHITHSRIKAR"

ciphertext = rc4(plaintext, key)
print("RC4 Encryption")
print("-----------------------------")
print("Plain Text :", plaintext.decode())
print("Key        :", key.decode())
print("Cipher Text:", ciphertext.hex().upper())
