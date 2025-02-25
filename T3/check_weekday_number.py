try:
    weekday_input = int(input("Enter a weekday number: "))
    if 1 <= weekday_input <= 7:
        print("OK")
    else:
        print("Please enter an integer between 1 and 7")
except ValueError:
    print("Please enter an integer between 1 and 7")