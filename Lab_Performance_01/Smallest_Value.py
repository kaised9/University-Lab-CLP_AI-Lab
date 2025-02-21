numbers_set = [10, 11,12, 13, 14, 15, 20, 21,27, 38, 50]
smallest_number = numbers_set[0]
for i in numbers_set:
    if i < smallest_number:
        smallest_number = i 

print("Smallest Number is:",smallest_number)