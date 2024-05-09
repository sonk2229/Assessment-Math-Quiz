import random

# generates an integer between 0 and 10
# to simulate a question


def random_num():
    random_result = random.randint(1, 10)
    return random_result


# generates two random numbers and gives both of them

def two_random_num(who):

#rolls  two random numbers
roll_1 = random_num()
roll_2 = random_num()
