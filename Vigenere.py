def vigenere_cipher(text: str, key: str, encrypt: bool = True) -> str:
    key = "".join([c for c in key.upper() if c.isalpha()])
    if not key:
        raise ValueError("Key must contain at least one letter.")

    result = []
    key_index = 0
    
    for char in text:
        if char.isalpha():
            text_val = ord(char.upper()) - 65
            key_val = ord(key[key_index % len(key)]) - 65
            
            if encrypt:
                new_val = (text_val + key_val) % 26
            else:
                new_val = (text_val - key_val) % 26

            new_char = chr(new_val + 65)
            if char.islower():
                new_char = new_char.lower()
                
            result.append(new_char)
            
            key_index += 1
        else:
            result.append(char)
            
    return "".join(result)

if __name__ == "__main__":
    keyword = "SECURE"
    
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
        encrypted = vigenere_cipher(tc, keyword, encrypt=True)
        decrypted = vigenere_cipher(encrypted, keyword, encrypt=False)
        
        print(f"Original : '{tc}'")
        print(f"Encrypted: '{encrypted}'")
        print(f"Decrypted: '{decrypted}'")
        print("-" * 40)