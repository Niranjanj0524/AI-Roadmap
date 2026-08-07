text = "Hello World"
sentence = "Python is an amazing programming language"

#Print each character of a string.
for char in text:
    print(char, end=" ")
print("\n")

#length of string
print(len(text))
print("\n")

#reverse string
print(text[::-1])
print("\n")

#vowels count
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)
print(f"Vowel Count {vowel_count}")
print("\n")

#check palindrome
word = "madam"
isPalindrome = word == word[::-1]
print(isPalindrome)
print("\n")

#First 5 text
print(text[:6])
print("\n")

#toUpperCase and toLowerCase
str = "NiRaNjaN"
print(str.upper())
print(str.lower())
print("\n")

#Replace word in sentence
print(sentence.replace('Python','Java'))
print("\n")

