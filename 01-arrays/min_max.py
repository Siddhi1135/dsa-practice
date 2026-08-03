numbers=[45,12,78,3,90,34]
smallest=numbers[0]
largest=numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print("Smallest:", smallest)
print("Largest:", largest)