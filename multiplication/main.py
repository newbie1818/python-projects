import random
import sys
def random_number():
    while True:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        mult = num1 * num2
        print(f" Here is an exemple for you: {num1} * {num2} =  ?")

        count = 0
        while count <= 2:

            result = input("Type in your answer:>").casefold()
            if result == "exit":
                sys.exit()

            try:
                if (int(result) == mult):
                    print("Correct")
                    break

                elif count == 2:
                    print(f"It was the last attempt. The correct answer is {mult}")

                else:
                    print("Make one more attempt")
                count = count + 1

            except ValueError:
                print("Enter a valid number")

random_number()





