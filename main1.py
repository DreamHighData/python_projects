import random

random_num = random.randint(1,100)

game_count = 1

while True:
    try:
        my_numbber = int(input("Please enter a number between 1 and 100 : "))
        if my_numbber > random_num:
            print("Down")
        elif my_numbber < random_num:
            print("Up")
        elif my_numbber == random_num:
            print(f"Good Job! you try it at {game_count} times and you got it!")
            break

        game_count += 1
    except Exception as e:
        print("Error! Please enter the number!")
        print("Error : ", e)
