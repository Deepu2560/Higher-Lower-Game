import random
from data import questions
from art import logo

current = random.choice(questions)
score = 0


def gamestart(choicenQues):
    print(f"Your score = {score}")
    print(
        f'\n"{current["name"]}" \n       Has \n"{current["number"]}" average monthly searches'
    )

    ans = input(
        f'\n"{choicenQues["name"]}" \n       Has \n"Higher" or "Lower" searches than {current["name"]} ? '
    )

    if str.lower(
            ans) == "higher" and choicenQues["number"] >= current["number"]:
        return True
    elif str.lower(
            ans) == "lower" and choicenQues["number"] <= current["number"]:
        return True
    else:
        print(
            f'\nCorrect Answer:\n"{choicenQues["name"]}" \n       Has \n"{choicenQues["number"]}" average monthly searches\n'
        )
        return False


end_game = False

while not end_game:
    print(logo)
    choice = random.choice(questions)

    if gamestart(choicenQues=choice):
        current = choice
        print(
            f'\n"{current["name"]}" \n       Has \n"{current["number"]}" average monthly searches'
        )
        score += 1
    else:
        print("You lose this game. Try again")
        print("Your total score:", score)
        end_game = True
