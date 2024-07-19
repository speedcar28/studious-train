word = input("enter something")
word = word.lower()
vowel = 'aeiou'

count = 0

for letter in word:
    if letter in vowel:
        count += 1
print(f'{count} vowels')