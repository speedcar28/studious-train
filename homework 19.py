'''
Write a Python program that counts the number of vowels in a string entered by the user
'''

vowel = 0
letter = input("enter letters")
for letters in letter:
    if 'a' in letter or 'e' in letter or 'i' in letter or 'o' in letter or 'u':
        vowel += 1
print(vowel)
