import random
def game():
    print('''       Welcome to the game 
      "ROCK-PAPER-SCISSORS" ''')
    print("")
    name = input("Please enter your name: ")
    computer_list = ['ROCK', 'PAPER', 'SCISSORS']
    score = ("y", "x", "z")
    while True:
        c_cho = random.choice(computer_list)
        print(f'''{name}, what is your choice? 
ROCK(1), PAPER(2), SCISSORS(3), or end game (q or quit)''')
        u_i = input("Input: ")
        if u_i == "1" and c_cho == "ROCK" or u_i == "2" and c_cho == "PAPER" or u_i == "3" and c_cho == "SCISSORS":
            print(f'''None is the winner of the game!
Computer has  {c_cho}''')
        elif u_i == "1"and c_cho == "PAPER" or u_i == "2" and c_cho == "SCISSORS" or u_i == "3" and c_cho == "ROCK":
            print(f'''Computer is the winner of the game!
Computer has {c_cho}''')
        elif u_i == "1" and c_cho == "SCISSORS" or u_i == "2" and c_cho == "ROCK" or u_i == "3" and c_cho == "PAPER":
            print(f'''{name} is the winner of the game!
Computer has {c_cho}''')
        elif u_i == "q" or u_i == "quit":
            print("Goodbye, thank you for playing!")
            break
        else:
            print('Wrong input! Please try again!')




game()
