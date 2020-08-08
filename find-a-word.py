word = input("Word: ")
chars = input("Characters: ")
word = word.lower()
chars = chars.lower()
answer = "YES"
for char in word:
    if char not in chars:
        answer = "NO"
        break
print(answer)

        
