import hashlib

# Domain parameters (L = 512 bits, N = 160 bits): p, q prime, q | (p - 1), g = h^((p-1)/q) mod p
p = 0xa514bc94367067273b3512b7adf74b326ac42612866caa98a1882cd27e87d1ccb73da5da53153f4f2b6f4258129ed64e0931ce5763d1a04a6bc0e59102bfcb0b
q = 0xe5c61cac26f559ed8a7d1d70235b1b28d612ddbb
g = 0x90bdd5dc2213467acedc96a7f196f6298889891b1ddba5df5fade2922c912ef1e9a9516e3d1c90b128ac494715812cac06d47e77ba717e9bbc67ec1890fc1d08


def hash_message(msg):
    # SHA-1 gives a 160-bit digest, equal to the size of q
    return int.from_bytes(hashlib.sha1(msg).digest(), "big")


def generate_keys(name):
    x = int.from_bytes(name, "big") % (q - 1) + 1      # private key, 0 < x < q
    y = pow(g, x, p)                                    # public key
    return x, y


def sign(msg, x, k):
    r = pow(g, k, p) % q
    s = (pow(k, -1, q) * (hash_message(msg) + x * r)) % q
    return r, s


def verify(msg, r, s, y):
    if not (0 < r < q and 0 < s < q):
        return False
    w = pow(s, -1, q)
    u1 = (hash_message(msg) * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    return v == r


message = b"GITAMUNIVERSITYISDEEMEDTOBEUNIVERSITY"
given_key = b"LOHITHSRIKAR"

x, y = generate_keys(given_key)
# per-message secret k derived deterministically so the output is reproducible
k = int.from_bytes(hashlib.sha256(given_key + message).digest(), "big") % (q - 1) + 1

r, s = sign(message, x, k)

print("DSS (DSA) Digital Signature")
print("-----------------------------")
print("Message    :", message.decode())
print("Given Key  :", given_key.decode())
print("SHA-1 Hash :", format(hash_message(message), "040X"))
print("Private x  :", format(x, "X"))
print("Public y   :", format(y, "X"))
print("Secret k   :", format(k, "X"))
print("Signature r:", format(r, "040X"))
print("Signature s:", format(s, "040X"))
print("Verify     :", "VALID" if verify(message, r, s, y) else "INVALID")
print("Tampered   :", "VALID" if verify(message + b"X", r, s, y) else "INVALID", "(message altered)")