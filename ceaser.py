name = input("Enter your name: ")
n = int(input("Enter the shift value: "))

result = ""

for c in name:
    shifted = (ord(c) - ord('a') + n) % 26
    result += chr(shifted + ord('a'))

print(result)