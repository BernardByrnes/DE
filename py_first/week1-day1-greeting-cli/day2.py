# number_text = input("Enter Number")
# number = float(number_text)

# print(number)

bill_amount = 50.00
tip_percentage = 20

tip_rate = tip_percentage / 100
tip_amount = tip_rate * bill_amount
total_amount = tip_amount + bill_amount

print(f"Bill: ${bill_amount:.2f}")
print(f"Tip: ${tip_amount:.2f}")
print(f"Total: ${total_amount:.2f}")
