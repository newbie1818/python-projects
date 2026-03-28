# Tip Calculator

A simple command-line tip calculator written in Python.

### How it works

1. Enter your bill amount
2. Choose a tip percentage (10, 15, 20, 25, 30 — or enter your own)
3. Get the total amount to pay

### Code

```python
def calculate_tip(bill_amount):
    print("Choose the tip amount: 10, 15, 20, 25, 30, or your own")
    choice = input("Enter your choice here: ")

    tip_percent = int(bill_amount) * int(choice) // 100
    total_amount_payed = int(bill_amount) + tip_percent

    print(f"You have to pay total: {total_amount_payed}")

calculate_tip(input("How much is your bill. Enter the number: "))
```

### Requirements
 
- Python 3.x
- No external libraries needed