distance = float(input("Enter journey distance in km: "))
fuel_price = float(input("Enter fuel price per litre: "))

# Vehicle mileage in km per litre
vehicle1_mileage = float(input("Enter Vehicle 1 mileage: "))
vehicle2_mileage = float(input("Enter Vehicle 2 mileage: "))

# Extra fuel kept as a reserve
reserve = float(input("Enter reserve fuel in litres: "))

fuel1 = distance / vehicle1_mileage + reserve
fuel2 = distance / vehicle2_mileage + reserve

cost1 = fuel1 * fuel_price
cost2 = fuel2 * fuel_price

print("Vehicle 1 journey cost:", cost1)
print("Vehicle 2 journey cost:", cost2)

if cost1 < cost2:
    print("Vehicle 1 is cheaper.")
else:
    print("Vehicle 2 is cheaper.")
