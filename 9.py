'''mark = int(input("marks"))
if 100 >= mark >= 90:
    print("a", mark)
if mark <= 60 and 89 <= mark:
    print("b", mark)
if mark <= 20 and 59 <= mark:
    print("c", mark)
else:
    print("f", mark)

a = int(input("num1: "))
b = int(input("num2: "))
c = int(input("num3: "))
if a > b:
    if a>c:
        print(f'{a} is the largest')
    else:
        print(f'{c}is the gretest')
else:
    if b > a:
        if b > c:
            print(f'{b} is the largest')
        else:
            print(f'{c}is the gretest')'''
num = int(input("num: "))
if num > 0:
    print('positive')
    if num % 2 == 0:
        print('even')
    else:
        print('odd')
if num < 0:
    print('negative')
    if num % 2 == 0:
        print('even')
    else:
        print('odd')
if num == 0:
    print('0')
else:
    print('not a number')
