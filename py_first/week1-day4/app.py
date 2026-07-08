transaction_amounts = [19.99, 45.00, 100.50]

records_processed = 0
total_amount = 0

for amount in transaction_amounts:
    records_processed = records_processed + 1
    total_amount = total_amount + amount

summary = {
    "records_processed": records_processed,
    "total_amount": total_amount,
}

print(f"Records Processed:  {summary['records_processed']}")
print(f"Total Amount:  {summary['total_amount']}")
