import pytest
from transfer_money import transfer_money, get_users

def test_transfer_money_success():
    assert transfer_money(125, 555, 666000) == "Transfer successful"

def test_transfer_money_invalid_user():
     with pytest.raises(ValueError, match="User does not exist"):
        transfer_money(101,123,333789)

def test_transfer_money_negative_amount():
    with pytest.raises(ValueError, match = "Invalid amount"):
        transfer_money(125, -1,666000)

def test_transfer_money_zero_amount():
    with pytest.raises(ValueError, match = "Invalid amount"):
        transfer_money(125,0,666000)

def test_transfer_positive_amount():
    assert transfer_money(125,1,666000) == "Transfer successful"

def test_transfer_money_invalid_card():
    with pytest.raises(ValueError, match="Card number is required"):
        transfer_money(125,555,"")
