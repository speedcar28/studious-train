'''
Write a Python program that takes multiple inputs from the user until the user enters 'done'.
And then finally prints the values entered as list.
'''


total = []
num = 0
while True:
    num = input("num")
    if num == 'done':
        break
    else:
        total.append(num)
print(total)