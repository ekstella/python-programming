try: 
    price = float(input("Enter price: "))
    vat = 0.24
    price_with_vat = price * (1 + vat)

    print(f"The price with VAT is {price_with_vat:.2f}")

except ValueError:
    print("Invalid price")