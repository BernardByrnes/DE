def calculate_tip(bill_amount, tip_percentage):
    tip_rate = tip_percentage / 100
    return bill_amount * tip_rate


def calculate_amount(tip_amount, bill_amount):
    return tip_amount + bill_amount


def amount_per_person(total_amount, num_of_people):
    return total_amount / num_of_people


def main():
    bill_text = input("What is your bill?")
    tip_text = input("What Is The Tip Percentage?")
    customers = input("How many people are splitting the bill?")

    bill_amount = float(bill_text)
    tip_percentage = float(tip_text)
    num_of_people = int(customers)

    tip_amount = calculate_tip(bill_amount, tip_percentage)
    total_amount = calculate_amount(tip_amount, bill_amount)
    per_person = amount_per_person(total_amount, num_of_people)

    print("")
    print("Tip CalCulator Result")
    print("---------------------")
    print(f"Bill: ${bill_amount}")
    print(f"Tip: ${tip_amount}")
    print(f"Total: ${total_amount}")
    print(f"People: ${num_of_people}")
    print(f"Per Person: ${per_person}")


if __name__ == "__main__":
    main()
