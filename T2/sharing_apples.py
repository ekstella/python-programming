apples = int(input("How many apples? "))
children = int(input("How many children? "))

apples_per_children = apples // children
leftover_apples = apples % children


print("")
print(f"Each child will get {apples_per_children:.0f} apples.")
print(f"There will be {leftover_apples:.0f} leftover apples.")