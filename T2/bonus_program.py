selling_price = float(input("Enter the car's selling price: "))

if selling_price < 50000:
    bonus = max(200, selling_price * 0.01)
else:
    bonus = max(200, selling_price * 0.015)

print(f"The bonus is {bonus:.2f} euros.")