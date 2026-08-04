def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i   # found it, return the position
    return -1          # not found

numbers = [45, 12, 78, 3, 90, 34]

print(linear_search(numbers, 78))   # should print 2
print(linear_search(numbers, 100))  # should print -1
