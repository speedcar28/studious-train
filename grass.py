from math import sqrt
from time import sleep

ex1a = 13
ex2a = 17
ex3a = 25
ex4a = 17
ex5a = 26
command = ''
inp1 = ''
inp2 = ''
while command != 'stop':
    print("Hi i'm Jythongrass I will teach you how to use pythagoras")
    print("By the end of the course you will learn basic pythagoras")
    print(" If you are ready type yes")
    command = input('> ')
    if command != 'yes':
        break
    command = ''
    print('Lets start with a magic')
    inp1 = int(input('Enter a number: '))
    inp2 = int(input('Enter another number: '))
    res = sqrt((inp1*inp1) + (inp2*inp2))
    print(res)
    print("How do you think this number appeared?")
    sleep(1)
    print("Pythagorean theorem, the well-known geometric theorem that the sum of the squares on the legs of a right "
          "triangle is equal to the square on the hypotenuse")
    print("(the side opposite the right angle)—or, in familiar "
          "algebraic notation, a, square + b, square = c, square.")

    print('In simple words you just find power of 2 in both the number '
          'then you add them and find the square root which gives the 3rd sides length')
    print("Type yes to continue")
    command = input('> ')
    if command != 'yes':
        break
    command = ''
    print("Here is an example:")
    sleep(1)
    print("In a triangle side A is 8 and side B is 6")
    sleep(2)
    print("So to find the 3rd side we use the pythagoras method.")
    sleep(3)
    print("Find the power of 2 in A(8) and in B(6) we get A as 64 and B as 36")
    sleep(3.5)
    print("When we add this number we get: 64 + 36 = 100")
    sleep(2)
    print("When we find square root of this we get 10")
    sleep(2)
    print("Were is an excercise")
    print('A = 12, B = 5, C = ?')
    sleep(0.5)
    while command != ex1a:
        command = int(input('ans: '))
    print('Correct')
    command = ''
    sleep(1)
    print('A = 15, B = 8, C = ?')
    while command != ex2a:
        command = int(input('ans: '))
    command = ''
    print('Correct')
    sleep(0.5)
    print('A = 7, B = 24,C = ? ')
    while command != ex3a:
        command = int(input('ans: '))
    command = ''
    print('Correct')
    sleep(0.5)
    print('A = 8, B = 15, C = ?')
    while command != ex4a:
        command = int(input('ans: '))
    command = ''
    sleep(0.5)
    print('Correct')
    print('A = 24, B = 10 C = ?')
    while command != ex5a:
        command = int(input('ans: '))
    command = ''
    print('Correct')
    sleep(3)
    print("Congratulations you learned the basics of pythagoras")
    sleep(5)
    break
