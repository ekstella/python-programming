def compute_earnings(hourly_wage, hours_worked):
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * hourly_wage * 1.5
        regular_pay = 40 * hourly_wage
        total_earnings = regular_pay + overtime_pay
    else:
        total_earnings = hours_worked * hourly_wage
    return total_earnings

def main():
    hourly_wage = float(input("Enter wage: "))
    hours_worked = int(input("Enter hours: "))
    earnings = compute_earnings(hourly_wage, hours_worked)
    print(f"The earnings are {earnings:.2f}")

main()
