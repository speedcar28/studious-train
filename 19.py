num1 = int(input("number 1: "))
op = input("operation: ")
num2 = int(input("number 2: "))
if op == '+' or op == 'add' or op == 'sum' or op == 'addition':
    print(f'sum = {num1 + num2}')
elif op == '-' or op == 'difference' or op == 'subtraction' or op == 'sub':
    print(f'difference = {num1 - num2}')
elif op == 'x' or op == '*' or op == 'multiply' or op == 'multiplication' or op == 'product' or op == 'mult' or 'multi':
    print(f'product = {num1 * num2}')
elif op == '÷' or op == '/' or op == 'divide' or op == 'division' or op == 'quotient' or op == 'div' or op == 'divi':
    print(f'quotient = {num1 / num2} remainder = {num1 % num2}')
