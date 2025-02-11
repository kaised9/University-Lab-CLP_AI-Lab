import matplotlib.pyplot as plt

regions_name = ["Dinajpur", "Khulna", "Sylhet", "Comilla", "Dhaka"]
sales_revenue = [350, 450, 180, 370, 700]

plt.figure(figsize=(8, 5))
plt.bar(regions_name, sales_revenue, color='green', edgecolor='black')

plt.xlabel("Regions")
plt.ylabel("Sales Revenue (in $1000s)")
plt.title("Sales Revenue Comparison Across Regions")

for i, revenue in enumerate(sales_revenue):
    plt.text(i, revenue + 5, f"${revenue}K", ha='center', fontsize=10)
    
plt.show()
