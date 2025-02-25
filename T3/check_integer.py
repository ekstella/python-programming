user_input = input("Enter an integer: ")

try:
    number = int(user_input)
    print("OK")
    
except ValueError:
    print(f"'{user_input}' is not an integer")
