import random

random_side = random.randint(0, 1)
if random_side == 1:
    print('Heads')
else:
    print("Tails")

names_sting = input('give names separated by commas')
names = names_sting.split(", ")
length = len(names)
rd = random.randint(0, length - 1)
print(names[rd])


# easier method rd = random.choice(names)


def treasure_map():
    row1 = ["⬜️", "️⬜️", "️⬜️"]
    row2 = ["⬜️", "⬜️", "️⬜️"]
    row3 = ["⬜️️", "⬜️️", "⬜️️"]
    treasure_map1 = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")

    position = input("Where do you want to put the treasure? ")

    horizontal = int(position[0])
    vertical = int(position[1])

    treasure_map1[vertical - 1][horizontal - 1] = "X"

    print(f"{row1}\n{row2}\n{row3}")


treasure_map()


def rock_paper_scissors():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    list = [rock, paper, scissors]
    print(f'{rock}\n{paper}\n{scissors}')
    user = int(input("What will you pick? 0 for Rock, 1 for Paper, 2 for Scissors\n"))
    if user >= 3:
        print('Invalid number')
    else:
        print('Your choice is')
        print(list[user])

    computer = random.randint(0, 2)
    print("Computer choose")
    print(list[computer])

    if user >= 3 or user < 0:
        print("You typed an invalid number, you lose!")
    elif user == 0 and computer == 2:
        print("You win!")
    elif computer == 0 and user == 2:
        print("You lose")
    elif computer > user:
        print("You lose")
    elif user > computer:
        print("You win!")
    elif computer == user:
        print("It's a draw")


rock_paper_scissors()
