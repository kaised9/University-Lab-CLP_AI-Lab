import matplotlib.pyplot as plt

all_days = ["Saturday", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
temperatures_value = [21, 24, 25, 20, 18, 16, 19]

plt.figure(figsize=(8, 5))
plt.plot(all_days, temperatures_value, marker='o', linestyle='-', color='b', linewidth=2, markersize=6)

plt.xlabel("Days Of The Week")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Variations Over a Week")
plt.grid(True) 

plt.show()
