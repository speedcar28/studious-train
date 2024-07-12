'''def factorial(n):
    t = 1
    for i in range(1, n + 1):
        t = t * i
    print(t)


factorial(4)'''


def find_max(a, b, c):
    if a > b:
        if a > c:
            return a
        elif c > a:
            return c
    elif b > a:
        if b > c:
            return b
        elif c > b:
            return c
    else:
        print("all are same")


print(f'the biggest number is {find_max(25, 42, 17)} from the following')
