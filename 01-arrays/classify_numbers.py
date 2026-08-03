numbers = [12, -5, 0, 34, -8, 0, 7, -1]
positive_count = 0
negative_count = 0
zero_count = 0

for num in numbers:
    if num > 0:
        positive_count = positive_count + 1
    elif num < 0:
        negative_count = negative_count + 1
    else:
        zero_count = zero_count + 1

print("Positives:", positive_count)
print("Negatives:", negative_count)
print("Zeros:", zero_count)