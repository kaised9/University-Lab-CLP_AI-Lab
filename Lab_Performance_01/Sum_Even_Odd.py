numbers_set = [10, 11,12, 13, 14, 15, 20, 21,27, 38, 50]

sum_even = 0
sum_odd= 0

for i in numbers_set:
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print("Sum Of Even Numbers Are:", sum_even)
print("Sum Of Odd Numbers Are:", sum_odd)