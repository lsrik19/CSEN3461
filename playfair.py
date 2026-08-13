def rail_fence_encrypt(s: str, r: int) -> str:
    n = len(s)
    
    if r <= 1 or r >= n:
        return s

    result = []
    step = 2 * (r - 1)

    for i in range(r):
        for j in range(i, n, step):
            result.append(s[j])
            
            diag_index = j + step - 2 * i
            if i != 0 and i != r - 1 and diag_index < n:
                result.append(s[diag_index])

    return "".join(result)

if __name__ == "__main__":
    rails = 3
    
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
        encrypted = rail_fence_encrypt(tc, rails)
        
        print(f"Original : '{tc}'")
        print(f"Encrypted: '{encrypted}'")
        print("-" * 40)