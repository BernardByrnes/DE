def calculate_tip(bill_amount, tip_percentage):
    tip_rate = tip_percentage / 100
    return bill_amount * tip_rate


def calculate_total(bill_amount, tip_amount):
    return bill_amount + tip_amount


def main():
    bill_text = input("Enter Bill Amount: ")
    tip_text = input("Enter Tip Percentage: ")

    bill_amount = float(bill_text)
    tip_percentage = float(tip_text)

    tip_amount = calculate_tip(bill_amount, tip_percentage)
    total_amount = calculate_total(bill_amount, tip_amount)

    print("")
    print("Tip Calculator Result")
    print("----------------------")
    print(f"Bill: ${bill_amount:.2f}")
    print(f"Tip: ${tip_amount:.2f}")
    print(f"Total: ${total_amount:.2f}")


if __name__ == "__main__":
    main()
