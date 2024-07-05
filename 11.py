'''num = 0
nu = int(input("end number"))
for i in range(0, nu+1):
    num += i
    print("each num added up", num)
num = 1
nu = int(input("end number"))
for i in range(1, nu + 1):
    num *= i
print("num factorial", num)'''
i = 1
count = 0
num = int(input("num"))
while i <= num:
    count += i
    i += 1
print(count)