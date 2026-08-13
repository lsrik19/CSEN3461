def mod_inverse(det, m=26):
    for i in range(1, m):
        if (det * i) % m == 1:
            return i
    raise ValueError("Determinant has no modular inverse. Bad key.")

def hill_cipher_2x2(text, key, encrypt=True):
    cleaned_text = "".join([c for c in text.upper() if c.isalpha()])
    
    if not cleaned_text:
        return "<No alphabetic characters to encrypt>"

    text_nums = [ord(c) - 65 for c in cleaned_text]


    if len(text_nums) % 2 != 0: 
        text_nums.append(23) 
    
    if not encrypt:
        det = (key[0][0] * key[1][1] - key[0][1] * key[1][0]) % 26
        inv = mod_inverse(det)
        key = [
            [(key[1][1] * inv) % 26, (-key[0][1] * inv) % 26],
            [(-key[1][0] * inv) % 26, (key[0][0] * inv) % 26]
        ]

    result = ""
    for i in range(0, len(text_nums), 2):
        x, y = text_nums[i], text_nums[i+1]
        result += chr(((key[0][0]*x + key[0][1]*y) % 26) + 65)
        result += chr(((key[1][0]*x + key[1][1]*y) % 26) + 65)
        
    return result

if __name__ == "__main__":
    key = [[3, 3], [2, 5]]
    
    test_cases = [
        "Lohith Srikar Bolisetti",
        "SITA$RAMA",
        "            ABC",
        "SEETHA",
        "SITA123$$",
        "GITAM UNIVERSITY",
        "2024064631"
    ]
    
    for tc in test_cases:
        encrypted = hill_cipher_2x2(tc, key, encrypt=True)
        decrypted = hill_cipher_2x2(encrypted, key, encrypt=False) if encrypted != "<No alphabetic characters to encrypt>" else encrypted
        
        print(f"Original Input : '{tc}'")
        print(f"Encrypted      : {encrypted}")
        print(f"Decrypted      : {decrypted}")
        print("-" * 40)