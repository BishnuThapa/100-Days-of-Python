# Tip Calculator

print("Welcome to the tip calculator.")
bill = float(input("What was the toal bill ? $ "))
tip = int(input("What percentage tip would you like to give? 10, 12 of 15? "))
people = int(input("How many people to split the bill ? "))
tip_as_percent = tip/100
total_tip_amount = bill*tip_as_percent
total_bill_amount = bill + total_tip_amount
bill_per_person = total_bill_amount/people
final_amount = round(bill_per_person, 2)  # 2 is decimal places
print(f"Each person sould pay { final_amount} ")
