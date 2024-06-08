numbers = [3, 41, 12, 0, 24, 15]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("The largest number is", largest)