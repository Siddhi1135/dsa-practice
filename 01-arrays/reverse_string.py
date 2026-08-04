# Reverse string
word = "wanderly"
reversed_word = ""

for letter in word:
    reversed_word = letter + reversed_word

print("Reversed:", reversed_word)


# Palindrome check
word = "level"
reversed_word = ""

for letter in word:
    reversed_word = letter + reversed_word

if word == reversed_word:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")