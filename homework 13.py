'''
Write a program that repeatedly asks the user to enter a number until they enter a negative number.
 Print the sum of all entered numbers (excluding the negative number)
'''
total = 0
num = 0
while True:
    num = int(input("num"))
    if 0 > num:
        break
    else:
        total = total + num
print(total)
