text = input("Enter a text: ")
shift = int(input("Enter a shift value (1..25): "))
while shift not in range(26):
    shift = input("Invalid shift value. Try again: ")
cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
    else:
        code = ord(char) + shift
        if char.isupper()and code > ord("Z"):
                code = ord("A") + code - ord("Z") - 1
        if char.islower() and code > ord("z"):
                code = ord("a") + code - ord("z") - 1
        cipher += chr(code)
print("Cipher:", cipher)
