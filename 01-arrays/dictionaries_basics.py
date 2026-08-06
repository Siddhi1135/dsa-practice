prices = {"Bali": 499, "Paris": 899, "Tokyo": 799}

print(prices["Bali"])          # look up by key, not position
print(prices.get("Dubai"))     # safe lookup - returns None if missing, no error

prices["Dubai"] = 649          # add a new key-value pair
print(prices)

for place in prices:
    print(place, ":", prices[place])


