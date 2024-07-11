""" def greet():
   print("hello")

 greet()"""

'''name = input("name: ")
 def greet(name):
   print("hello", name)

 greet(name)'''

'''from random import randint


def calc(num_1, num_2=randint(1, 100)):
    c = num_1 + num_2
    print(f'result: {c}')


num_1 = int(input("num 1: "))

calc(num_1)'''


'Write a program to create a user-defined function to print whether user-given input is even or odd.'


num = int(input("num: "))


def num_check():
    if num % 2 == 0:
        print("number is even")
    elif num % 2 != 0:
        print("number is odd")


num_check()
