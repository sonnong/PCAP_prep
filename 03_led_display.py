#define patterns of each number for all 5 rows
one = ["#", "#", "#", "#", "#"]
two = ["###", "  #", "###", "#  ", "###"]
three = ["###", "  #", "###", "  #", "###"]
four = ["# #", "# #", "###", "  #", "  #"]
five = ["###", "#  ", "###", "  #", "###"]
six = ["###", "#  ", "###", "# #", "###"]
seven = ["###", "  #", "  #", "  #", "  #"]
eight = ["###", "# #", "###", "# #", "###"]
nine = ["###", "# #", "###", "  #", "###"]
zero = ["###", "# #", "# #", "# #", "###"]

digits = [zero, one, two, three, four, five, six, seven, eight, nine]

#read user's input and display the numbers
number = input("Enter a non-negative integer: ")
for row in range(5):
    for n in number:
        print(digits[int(n)][row], end = " ")
    print()
