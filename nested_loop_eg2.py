# Initialising a variable
string_list = ["Coder", "Academy", "Champion"]
result = 0

for string in string_list:
    for letter in string:
        if letter in "aeiouAEIOU":
            result += 1

print("The total occurence of vowel in the list:", result)

