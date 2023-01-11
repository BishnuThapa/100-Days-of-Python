age = int(input("what is your current age?"))
total_age = int(90)
years_remaining = total_age-age
days_remaining = years_remaining*365
weeks_remaining = years_remaining*52
months_remaining = years_remaining*12

print(
    f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
