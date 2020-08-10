birth = input("Enter your birthday in format YYYY, MM and DD: ")
while len(birth) != 8:
    birth = input("Incorrect format. Try again: ")
#Digit of Life
dol = 0
for digit in birth:
    dol += int(digit)
while dol > 9:
    dol = int(str(dol)[0]) + int(str(dol)[1])
print("Digit of Life:", dol)
