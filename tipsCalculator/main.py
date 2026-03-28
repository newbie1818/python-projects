
def calculate_tip(bill_amount):

#bill_amount = input("How much is your bill. Enter the number: ")

    print ("Choose the tip amount: 10, 15, 20, 25, 30, or your own")

    choice = input("Enter your choice here: ")

    tip_percent = int(bill_amount)*int(choice)//100
    total_amount_payed = int(bill_amount) + tip_percent

    print(f"You have to pay total: {total_amount_payed}")

calculate_tip(input("How much is your bill. Enter the number: "))