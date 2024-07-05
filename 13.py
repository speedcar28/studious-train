'''s = int(input('start number'))
e = int(input('end number'))
for i in range(s, e):
    if i % 5 == 0:
        continue
    elif i == 50:
        break
    else:
        print(i*i)'''
l = []
while True:
    name = input("name's")
    if name == '':
        break
    l.append(name)
c = 0
for i in l:
    c += 1
print('number of students', i)
print('students', l)