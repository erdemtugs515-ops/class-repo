print("Calculate fuel consumption")
dist= input("Enter travel distance (Kilometers): ")
fuel= input("Enter fuel usage(Liters): ")
fuelusage=int(fuel)

Consumption = (fuelusage/dist)*100
Consumption = int(Consumption)

print(f"Fuel consumption is {Consumption} 1 per 100km")