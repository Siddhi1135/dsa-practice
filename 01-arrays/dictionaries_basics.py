prices = {"Bali": 499, "Paris": 899, "Tokyo": 799}

print(prices["Bali"])          # look up by key, not position
print(prices.get("Dubai"))     # safe lookup - returns None if missing, no error

prices["Dubai"] = 649          # add a new key-value pair
print(prices)

for place in prices:
    print(place, ":", prices[place])


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
