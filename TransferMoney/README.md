# Transfer Money function 
 A money transfer module simulating a money transfer function with input validation. 

### What it does

1. Validates user id against a list of existing users
2. Validates transfer amount (must be greater than 0)
3. Validates card number (must not be empty or None)
4. Returns a success message if all the checks pass 

## Project Structure
 
```
TransferMoney/
├── transfer_money.py       # Business logic
└── test_transfer_money.py  # pytest test suite
```
## How to run tests
 
```bash
pytest TransferMoney/test_transfer_money.py
```

 ## Test Coverage
| Test | Description |
|------|-------------|
| `test_transfer_money_success` | Valid input returns success message |
| `test_transfer_money_invalid_user` | Non-existent user raises ValueError |
| `test_transfer_money_negative_amount` | Negative amount raises ValueError |
| `test_transfer_money_zero_amount` | Zero amount raises ValueError |
| `test_transfer_positive_amount` | Amount of 1 passes validation |
| `test_transfer_money_invalid_card` | Empty card number raises ValueError |