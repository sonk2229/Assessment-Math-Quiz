# checks for an integer more than 0 (allows <enter>)
def int_check(question):

    while True:

        error = "Please enter an integer that is 1 or more."

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

    # get user choice
    user_choice = input("Answer: ")

    # If user choice os the exit code, break the loop
    if user_choice == "xxx":
        break

    Questions_played += 1

    # if users are in infinite mode, increase number of Questions
    if mode == "infinite":
        num_Questions += 1


# Game loop ends here

# Game History / Statistics area
