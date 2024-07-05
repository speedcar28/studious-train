'Find the factorial of a number using while loop'
n = int(input("number"))
num = 1
while n >= 1:
    num = num * n
    n = n - 1
print(num)