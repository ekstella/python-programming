gigs = int(input("Number of gigs: "))
gigs_with_strings = int(input("Gigs to be played with the same set of strings: "))
strings_cost = float(input("Price of a set of guitar strings: "))

sets_needed = -(-gigs // gigs_with_strings)

total_cost = sets_needed * strings_cost

print(f"The guitarist needs {sets_needed} new sets of guitar strings")
print(f"The total cost is {total_cost:.2f} euros")