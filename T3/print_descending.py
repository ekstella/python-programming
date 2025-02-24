integer = int(input("Enter an integer: "))

if integer < 1:
    print("Nothing to be printed")
else:
    total = 0
    for i in range(integer, 0, -1):
        print(i, end=" ")
        total += 1
    print(f"\nThe sum is {total}")
