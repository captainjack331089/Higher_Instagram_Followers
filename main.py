import random
from art import logo, vs
from replit import clear
from game_data import data


def check_answer(followera, followerb, choice):
    status = 0
    if followera > followerb and choice == "a":
        status = 1
    elif followera < followerb and choice == "a":
        status = 0
    elif followera > followerb and choice != "a":
        status = 0
    elif followera < followerb and choice == "b":
        status = 1
    return status


def game():
    status = 1
    score = 0
    print(logo)
    while status:
        l = len(data)
        pool = random.sample(range(0, l - 1), 2)

        A = data[pool[0]]
        A_name = A['name']
        A_follower_count = A['follower_count']
        A_description = A['description']
        A_country = A['country']

        B = data[pool[1]]
        B_name = B['name']
        B_follower_count = B['follower_count']
        B_description = B['description']
        B_country = B['country']

        print(f'Compare A: {A_name}, a {A_description}, from {A_country}.')
        print(vs)
        print(f'Compare B: {B_name}, a {B_description}, from {B_country}.')

        choice = input("Who has more followers? Type 'A' or 'B':").lower()
        clear()
        print(logo)
        result = check_answer(A_follower_count, B_follower_count, choice)
        if not result:
            print(f"Sorry, that's wrong. Final score: {score}.")
            # game should be done
            status = 0
        else:
            score += 1
            print(f"You're right! Current score: {score}.")


game()

# data.remove(data[pool[0]])
# data.remove(data[pool[1]])
