# def build_message(name):
#     return f"Hello, {name}"

# def main():
#     message = build_message(input("What is Your Name? "))
#     print(message)

# if __name__ == "__main__":
#     main()


# =====================================


def summarize_amounts(amounts):
    count = 0
    total = 0

    for amount in amounts:
        count = count + 1
        total = total + amount

    return {
        "count": count,
        "total": total,
    }


def print_summary(summary):
    print(f"Records processed: {summary['count']}")
    print(f"Total Amount: {summary['total']:.2f}")


def main():
    transaction_amounts = [19.99, 45.00, 100.50]
    summary = summarize_amounts(transaction_amounts)
    print_summary(summary)


if __name__ == "__main__":
    main()
