name = input("Enter Name : ")
print(name)
print("Reverse String : ",name[::-1])
print("Count char in String : ",len(name))
print("Upper Case : ",name.upper())
print("Lower Case : ",name.lower())
print("Title Case  : ",name.title())

palindrome = name[::-1]
isPalindrome = name == palindrome
print("Is Palindrome : ",isPalindrome)

vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in name if char in vowels)
print(f"Vowel Count {vowel_count}")
print("\n")

print("First char : " , name[0])
print("First char : " , name[-1])