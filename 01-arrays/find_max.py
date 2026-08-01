numbers=[23,67,12,89,45]
biggest=numbers[0] #starting by assuming the first number as the biggest
for num in numbers:
    if num>biggest:
        biggest=num  #update only if we find something bigger
print("Biggest number:",biggest)

