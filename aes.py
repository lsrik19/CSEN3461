def gmul(a, b):
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        hi = a & 0x80
        a = (a << 1) & 0xFF
        if hi:
            a ^= 0x1B
        b >>= 1
    return p


def make_sbox():
    sbox = []
    for x in range(256):
        inv = 0
        if x:
            for y in range(1, 256):
                if gmul(x, y) == 1:
                    inv = y
                    break
        s = inv
        for i in range(1, 5):
            s ^= ((inv << i) | (inv >> (8 - i))) & 0xFF
        sbox.append(s ^ 0x63)
    return sbox


SBOX = make_sbox()
RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]


def expand_key(key):
    w = [list(key[i:i + 4]) for i in range(0, 16, 4)]
    for i in range(4, 44):
        t = w[i - 1][:]
        if i % 4 == 0:
            t = t[1:] + t[:1]
            t = [SBOX[b] for b in t]
            t[0] ^= RCON[i // 4 - 1]
        w.append([a ^ b for a, b in zip(w[i - 4], t)])
    return [sum(w[4 * r:4 * r + 4], []) for r in range(11)]


def add_round_key(s, k):
    return [a ^ b for a, b in zip(s, k)]


def sub_bytes(s):
    return [SBOX[b] for b in s]


def shift_rows(s):
    # state is column-major: s[row + 4*col]
    return [s[(r + 4 * ((c + r) % 4))] for c in range(4) for r in range(4)]


def mix_columns(s):
    out = []
    for c in range(4):
        a = s[4 * c:4 * c + 4]
        out += [gmul(a[0], 2) ^ gmul(a[1], 3) ^ a[2] ^ a[3],
                a[0] ^ gmul(a[1], 2) ^ gmul(a[2], 3) ^ a[3],
                a[0] ^ a[1] ^ gmul(a[2], 2) ^ gmul(a[3], 3),
                gmul(a[0], 3) ^ a[1] ^ a[2] ^ gmul(a[3], 2)]
    return out


def encrypt_block(block, round_keys):
    s = add_round_key(list(block), round_keys[0])
    for r in range(1, 10):
        s = add_round_key(mix_columns(shift_rows(sub_bytes(s))), round_keys[r])
    s = add_round_key(shift_rows(sub_bytes(s)), round_keys[10])
    return bytes(s)


def pad(data):
    p = 16 - (len(data) % 16)
    return data + bytes([p]) * p


def encrypt(plaintext, key):
    round_keys = expand_key(key)
    data = pad(plaintext)
    return b"".join(encrypt_block(data[i:i + 16], round_keys)
                    for i in range(0, len(data), 16))


plaintext = b"GITAMUNIVERSITYISDEEMEDTOBEUNIVERSITY"
given_key = "LOHITHSRIKAR"
aes_key = given_key.encode("ascii").ljust(16, b"\x00")  # zero-pad to 128 bits

ciphertext = encrypt(plaintext, aes_key)
print("AES-128 Encryption (ECB, PKCS#7 padding)")
print("-----------------------------")
print("Plain Text :", plaintext.decode())
print("Given Key  :", given_key)
print("AES Key    :", aes_key.hex().upper(), "(zero-padded to 16 bytes)")
print("Cipher Text:", ciphertext.hex().upper())
