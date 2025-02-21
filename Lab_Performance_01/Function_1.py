def largest_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

num_1 = float(input("Enter The First Number: "))
num_2 = float(input("Enter The Second Number: "))

large_num = largest_number(num_1, num_2)
print("The Largest Number is: ",large_num)