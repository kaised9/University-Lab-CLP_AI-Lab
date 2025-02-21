def sum(*n):
    total_sum = 0
    for i in n:
        total_sum += i
    return total_sum

result_sum = sum(101, 120, 140, 200, 260)
print("The Sum Of This Numbers is:", result_sum)