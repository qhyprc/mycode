#! /usr/bin/python3
import random

def game():

  game_dic = {}
  while True:
    name = input("Enter participants name or exit: ").lower()
    if (name == "exit" and not game_dic):
        print("Nice try, but no one likes it :-( ")
        break
    elif (name == "exit"): 
        max_value = max(game_dic.values())
        current_winner = [k for k, v in game_dic.items() if v == max_value]
        winner = ""
        for name in current_winner:
          winner += str(name) +", "
        print("Congrets! {} win the game with hightest dice {}".format(winner, max_value))
        break
    elif (name == "cheat"):
        name = input("Who is this smartest guy? ").lower()
        while True:
          try:
            game_dic[name] = int(input("What number you want? "))
            break
          except Exception as resp:
            print(resp)
            print("Dude, read the error above! put a MAX number here to cheat!!!")


    elif (len(name)==0):
        print("At least one char for your NAME please!")
        continue        
    else:
      game_dic[name] = random.randint(1,6)
      print("Hi {}, your dice is {}".format(name, game_dic[name]))
      continue

  while True:
    answer = input("Wanna try again? Y/N: ").lower()
    if (answer == "y"):
      game()
    elif (answer == "n"):
      return
    else:
      print("Plesae type Y/N only.")
      continue


print("""

RANDOM DICE

Game Rules:
1. you can enter a participants name to start/continue the game
2. enter 'exit' to end the game and show game result
  
  READY? GO!

  """)  

game()

