word=input("Enter your word:")
print("old word:",word)
new_word=word[::-1]
print("New word:",new_word)

if(word==new_word):
    print("The word is palindrome")
else:
    print("The word is not palindrome")