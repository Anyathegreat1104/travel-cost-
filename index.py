distance = int(input("Enter distance in kilometres: "))
mileage = int(input("Enter vehicle mileage: "))
price = int(input("Enter petrol price per litre: "))

petrol = distance / mileage
cost = petrol * price

print("Petrol required =", petrol)
print("Total fuel cost =", cost)