import random

comp_number = random.randint(1,100)

your_number = 0
count = 0

while comp_number != your_number:
    your_number = int(input("Enter your number:"))
    count = count + 1
    if comp_number > your_number:
        print("Your number is too small!")
    elif comp_number < your_number:
        print("Your number is too big!")
    elif comp_number == your_number:
        print("Bingo!")
        print(f"You've used {count} attempts")
        break





