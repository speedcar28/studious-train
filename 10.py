'''a = float(input("number1 "))
b = float(input("number2 "))
op = input("operator")

if op == '+':
    print(a+b)
elif op == '-':
    print(a - b)
elif op =='*':
    print(a * b)
elif op =='/':
    print(a / b)

n = ["liana", "nithilan", 'kanish']
l = ["reverse name"]
for i in n:
    l.append(i[::-1])
print(l)'''

s = int(input("start of fireworks"))
e = int(input("end of fireworks"))
for i in range(s, e, 2):
    print('*' * i)
