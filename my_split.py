def mysplit(strng):
    split_list = []
    for letter in strng:
        if letter == " " or letter == "\n":
            index = strng.find(letter)
            word = strng[:index]
            if word != '':
                split_list.append(word)
            strng = strng[(index + 1):]
    if strng != '':
        split_list.append(strng)
    return split_list

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
