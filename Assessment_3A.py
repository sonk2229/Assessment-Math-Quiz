import random

# generates an integer between 0 and 10
# to simulate a question


def roll_random():
    roll_result = random.randint(1, 10)
    return roll_result


# rolls two random numbers and returns total

    # roll two random
    random_1 = roll_random()
    random_2 = roll_random()

    # Show the user the result
    print(f"{who}: {random_1} & {random_2}")
