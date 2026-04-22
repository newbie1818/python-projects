import pytest
def get_users():
    return[125,555,666000]

def transfer_money(user_id, amount, card_number):
    if user_id not in get_users():
        raise ValueError("User does not exist")

    elif amount <= 0:
        raise ValueError("Invalid amount")

    elif card_number is None or card_number == "":
        raise ValueError("Card number is required")

    else:
        return "Transfer successful"