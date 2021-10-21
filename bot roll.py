import random, os
from time import *
clear = lambda: os.system('cls')
clear()

WELCOME_TEXT = """///welcome to Death roll///
        these are your  options:
        type 'start' to start the game 
        type 'help' to display the rules
        type 'quit' to fuck off XD\n\n\t"""

EXPLAIN_TEXT = """
            the game is simple you place a bet, your bet is then multiplied by 10 after that you and the bot
            will roll a random number between 1 and the multiplied number
            each roll the numbers go down the first to rach the number 1 
            losses the the bet money! 

            understood?
            type 'yes' if you got it!
            type 'no' if you an idiot and you didnt get it!   \n 
            
            """

AUTISM_TEXT = """please visit this link for more info about your state:
                  
                  https://contact.krembo.org.il/

                  """

HOW_GAY_IS_YOUR_MOM = 69
GOODBYE_TEXT = "YOUR MOM IS SUPER GAY BYE!\n" * HOW_GAY_IS_YOUR_MOM
NOT_A_NUMBER_TEXT = "ARE YOU GAY STUPID DUMB OR DUMB NIGGA WE SAID NUMBER NOT YOUR MOMS STUPID NICKNAME!!!!!!!!"

def menu_start():
    try:
        bet = int(input('what is your bet? '))
    except:
        print(NOT_A_NUMBER_TEXT)
        menu_start()

    sum = bet * 10
    reward = sum * 2
    bot_roll = random.randint(1,sum)
    print(f'bot roll is: {bot_roll}')
    if bot_roll == 1:
        reward = bet *2
        print(f"player wins new balance is {reward}")
    while True:
        player_help = input('type roll to roll ')
        player_roll= random.randint(1,bot_roll)
        print(f'your roll is: {player_roll}') 
        if player_roll == 1:
            print(f'your roll was 1 sorry you lost: {bet} and bot won: {reward}')
            input('press any key to exit: ')
            break
        
        bot_roll=random.randint(1,player_roll)
        print(f'bot roll is: {bot_roll}')
        if bot_roll == 1:
            print(f'bot rolled 1 and lost you win {reward}!!!')
            input('press any key to exit: ')
            break

def menu_help():
    explanation = input(EXPLAIN_TEXT)
    menu_start() if explanation == "yes" else print(AUTISM_TEXT)


def menu_quit():
    print(GOODBYE_TEXT)

def menu(option):
    match option:
        case "start":
            menu_start()
        case "help":
            menu_help()
        case "quit":
            menu_quit()
        case _:
            menu(input(WELCOME_TEXT))

def main():
    option = input(WELCOME_TEXT)
    menu(option)

main()
