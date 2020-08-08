text1 = input("Enter first text: ")
text2 = input("Enter second text: ")
if text1 == "" or text2 == "":
    print("The texts are not anagrams.")
else:
    text1 = text1.lower().replace(" ", "")
    text2 = text2.lower().replace(" ", "")
    text1_list = sorted(list(text1))
    text2_list = sorted(list(text2))

    if text1_list == text2_list:
        print("The texts are anagrams.")
    else:
        print("The texts are not anagrams.")
