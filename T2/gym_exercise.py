gym_visits = int(input("Enter the number of days of gym visits per year: "))
day_pass = float(input("Enter price for a day pass: "))
membership_fee = float(input("Enter yearly membership fee: "))

yearly_visits_price = gym_visits * day_pass


if yearly_visits_price > membership_fee:
    subtract = yearly_visits_price - membership_fee
    print("")
    print(f"Paying the yearly membership fee is {subtract:.2f} euros cheaper" )
if yearly_visits_price < membership_fee:
    subtract = membership_fee - yearly_visits_price
    print("")
    print(f"Buying day passes is {subtract:.2f} euros cheaper")
if yearly_visits_price == membership_fee:
    print("")
    print(f"There is no price difference")