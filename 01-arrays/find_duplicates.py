def find_duplicates(numbers):
    seen = {}
    duplicates = []
    for number in numbers:
        if number in seen:
            duplicates.append(number)
        else:
            seen[number] = True
    return duplicates

numbers = [4,7,2,4,9,7,1]
print(find_duplicates(numbers))  # should print [4,7]
