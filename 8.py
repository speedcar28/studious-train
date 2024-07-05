"""one = [1, 2, 3, 4, 5, 'r',"list"]
two = [1, 2, 3, 4, 5, 'r',"list"]
print(one == two)
print(one != two)
print(one is two)
print(one is not two)
print('r' in one)
print('r' not in one)

name = "bear"
name2 = "dog"
name3 = "cat"
animal = input("your name: ")
if name == animal or name2 == animal or name3 == animal:
    print("its you")
else: print("its not you")"""

num = int(input("number: "))
if num % 2 != 0:
    print(num, "odd")
else:
    print(num, "even")