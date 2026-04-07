import random
def random_number():
    while True:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        mult = num1 * num2
        print(f" Here is an exemple for you: {num1} * {num2} =  ?")


        for count in range(3):
            result = input("Type in your answer:>")

            if result.isdigit() == False:
                print("Enter a number")
                continue


            elif (int(result) == mult):
                print("Correct")
                break

            elif count == 2:
                print(f"It was the last attempt. The correct answer is {mult}")
                print("Make one more attempt")


        count = count+1


random_number()





