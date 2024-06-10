# checks for an integer more than 0 (allows <enter>)

def int_check(question):

    while True:

        error = "Please enter an integer that is a number ."

        to_check = input(question)

        # Check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

        # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main Routine Starts here

# Intialise game variables
mode = "regular"
Questions_played = 0


print("Math Quiz")
print()

# Instructions
# Check that users have entered a valid
# option based on a list


def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an itme in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


def instruction():
    print('''

    **** Instructions ****

To begin, choose the number of Questions you would like to do
and what type of difficulty the Quiz in on for the Questions there are easy, normal
and then hard. 


Then choose how many Questions you'd like to do <enter> 
for infinite mode.

Your goal is to try to get all the Question's correct.

Press <xxx> to end game at anytime 

Good Luck!
    ''')


# Main routine
print()
print("Math Quiz")
print()

# loop for testing purposes

# ask user if they want to see the instructions and display
# them if requested
want_instructions = string_checker("Do you want to read the instruction?")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("program continues")

# Ask user for numbers of rounds / infinite mode
num_Questions = int_check("How many Questions would you like to do? Push <enter> for infinite mode: ")

if num_Questions == "infinite":
    mode = "infinite"
    num_Questions = 5

# Game loop starts  here
while Questions_played < num_Questions:

    # Question heading (based on mode)
    if mode == "infinite":
        Questions_heading = f"\n Question {Questions_played + 1} (Infinite Mode) "
    else:
        Questions_heading = f"\n Question {Questions_played + 1} of {num_Questions} "

    print(Questions_heading)
    print()

    import random

    # generates an integer between 0 and 10
    # to simulate a question


    def gen_number():
        gen_result = random.randint(1, 10)
        return gen_result


    # rolls two random numbers and returns total

    # roll two random
    random_1 = gen_number()
    random_2 = gen_number()

    # Then + the ramdom_1 & random_2 then give random_1 + random_2 after user gives response
    print(f" {random_1} + {random_2} ")

    # get user choice
    user_choice = int_check("")

    print(f" {random_1} + {random_2} = {random_1 + random_2} ")

    # If user choice os the exit code, break the loop
    if user_choice == "xxx":
        break

    if user_choice == random_1 + random_2:
        print("you got this correct")
     
        if user_choice > random_1 + random_2:
            print("you got this incorrect ")

    Questions_played += 1

    # if users are in infinite mode, increase number of Questions
    if mode == "infinite":
        num_Questions += 1


# Quiz loop ends here

# Quiz History / Statistics area
