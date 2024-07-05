"""Write a Python program that takes an integer input from the user and determines if the number is positive
 and a multiple of 5 and 7. If the number is positive, it should further check if it is a multiple of 5 and 7
and print the appropriate message."""
inp = int(input("number: "))
if inp % 2 == 0:
    print("the number is even")
    if inp % 5 == 0 & inp % 7 == 0:
        print(" and divisible by 5 and 7")
    else:
        print(" the number is not divisible by 5 and 7")

else:
    print("the number is not even or divisible by 5 and 7")
