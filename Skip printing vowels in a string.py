string = input("Enter a string: ")
vowels = "aeiouAEIOU"
for char in string:
    if char in vowels:
        continue
    print(char, end="")