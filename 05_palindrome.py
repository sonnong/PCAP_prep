text = input("Enter a string: ")
if text == "":
    print("Empty string isn't a palindrome")
else:
    text = text.lower().replace(" ", "")
    try:
        while text[0] == text[-1]:
            text = text[1:-1]
        print("It's not a palindrome.")
    except:
        print("It's a palindrome.")
