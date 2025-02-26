def add(first_input, second_input):
    return int(first_input + second_input + 0.5)

def main():
    first_input = float(input("Enter a float: "))
    second_input = float(input("Enter a float: "))
    result = add(first_input, second_input)
    print(result)

if __name__ == "__main__":
    main()

