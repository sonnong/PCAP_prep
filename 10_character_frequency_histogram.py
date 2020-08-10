from os import strerror

filename = input("Enter source file name: ")
try:
    source = open(filename, 'rt')
except Exception as e:
    print("Cannot open source file:", strerror(e.errno))
    exit(e.errno)
    
#Initialize and update the character frequency dictionary
char_freq = {}

for line in source:
    for char in line:
        if char.isalpha():
            if char.isupper():
                char = char.lower()
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

sorted_char = sorted(char_freq, key = lambda char: char_freq[char], reverse = True)

try:
    hist = open("test.hist.txt", "wt")
    for char in sorted_char:
        hist.write(char + " -> " + str(char_freq[char]) + "\n")
    hist.close()
    print("Histogram created.")
except Exception as e:
    print("Cannot create histogram file:", strerror(e.errno))
    exit(e.errno)
