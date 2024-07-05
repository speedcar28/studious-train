'''
Write a Python program that prints the multiplication table of a number entered by the user from 1 to 10
'''
num = int(input("number"))
for i in range(10+1):
    print(f'{num} x {i} = {num * i}')