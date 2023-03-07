def is_palindrome(input_str):
    input_str = input_str.lower().replace(' ', '')
    return input_str == input_str[::-1]


word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")
