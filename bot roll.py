import random
trigger=str(input('welcome! please type start: '))
if trigger== 'start':
      menue=input("""
      ///welcome to Death roll///
        these are your  options:
        type 'start' to start the game 
        type 'help' to display the rules
        type 'quit' to fuck off XD
      """)
      if menue == 'start':
            ask= int(input('what is your bet? '))
            bet= ask
            sum= 0
            sum= bet * 10
            reward= sum * 2
            bot_roll= random.randint(1,sum)
            print(f'bot roll is: {bot_roll}')
            if bot_roll == 1:
             reward = bet *2
             print(f"player wins new balance is {reward}")
            while True:
             player_help = input('type roll to roll ')
             player_roll= random.randint(1,bot_roll)
             print(f'your roll is: {player_roll}') 
             if player_roll== 1:
              print(f'your roll was 1 sorry you lost: {bet} and bot won: {reward}')
              input('press any key to exit: ')
              break
              

             bot_roll=random.randint(1,player_roll)
             print(f'bot roll is: {bot_roll}')
             if bot_roll==1:
              print(f'bot rolled 1 and lost you win {reward}!!!')
              input('press any key to exit: ')
              break
      if menue == 'help':
            explanation=input("""
            the game is simple you place a bet, your bet is then multiplied by 10 after that you and the bot
            will roll a random number between 1 and the multiplied number
            each roll the numbers go down the first to rach the number 1 
            losses the the bet money! 

            understood?
            type 'yes' if you got it!
            type 'no' if you an idiot and you didnt get it!    
            
            """)
            if explanation== 'yes':
             ask= int(input('what is your bet? '))
             bet= ask
             sum= 0
             sum= bet * 10
             reward= sum * 2
             bot_roll= random.randint(1,sum)
             print(f'bot roll is: {bot_roll}')
             if bot_roll == 1:
              reward = bet *2
              print(f"player wins new balance is {reward}")
             while True:
              player_help = input('type roll to roll ')
              player_roll= random.randint(1,bot_roll)
              print(f'your roll is: {player_roll}') 
              if player_roll== 1:
               print(f'your roll was 1 sorry you lost: {bet} and bot won: {reward}')
               input('press any key to exit: ')
               break

              bot_roll=random.randint(1,player_roll)
              print(f'bot roll is: {bot_roll}')
              if bot_roll==1:
               print(f'bot rolled 1 and lost you win {reward}!!!')
               input('press any key to exit: ')
               break
            if explanation== 'no':
                  print("""please visit this link for more info about your state:
                  
                  https://contact.krembo.org.il/

                  """)
      if menue== 'quit':
            print('fuck you nigga1!')
            quit