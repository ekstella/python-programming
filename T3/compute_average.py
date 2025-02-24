count = 0
total = 0.0

number = float(input("Enter first number: "))

while number != 0:
    total += number
    count += 1
    number = float(input("Enter next number: "))

if count == 0:
    print("Nothing to be calculated")
else:
    average = total / count
    print(f"The average is {average:.2f}")