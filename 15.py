height = float(input("height in meters "))
weight = float(input("weight in kilogram "))
bmi = weight/(height*height)
if bmi < 18.5:
    print("you are underweight, bmi is", bmi)
elif 18.5 <= bmi < 24.9:
    print("you are Normal weight, bmi is", bmi)
elif 25 <= bmi < 29.9:
    print("you are Overweight, bmi is", bmi)
elif bmi >= 30:
    print("you are Obesity, bmi is", bmi)
