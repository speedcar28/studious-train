'''
You're printing all even numbers from 1 to 10
, except for the number 6.
Use a for loop with a continue statement to skip printing 6.
'''
for i in range(11):
    if i == 6:
        continue
    elif i % 2 == 0:
        print(i)