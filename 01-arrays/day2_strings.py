word = "wanderly"

print(word[0])        # first character
print(word[-1])       # last character
print(len(word))      # length of string
print(word.upper())   # uppercase
print(word[0:4])      # slicing: characters index 0 to 3



word = "wanderly"
vowels = "aeiou"
count = 0

for letter in word:
    if letter in vowels:
        count = count + 1

print("Vowel count:", count)