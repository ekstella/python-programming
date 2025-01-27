females = int(input("Enter the number of female students: "))
males = int(input("Enter the number of male students: "))

total = females + males;

if total == 0:
    print("")
    print("Female: 0.0 %")
    print("Male: 0.0 %")
else:
    female_percentage = (females / total) * 100
    male_percentage = (males / total) * 100
    print("")
    print(f"Female: {female_percentage:.1f} %")
    print(f"Male: {male_percentage:.1f} %")
