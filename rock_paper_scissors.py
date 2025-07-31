import random
from colorama import Fore, Style, init
import time
#initialize colorama
init(autoreset=True)

print("Welcome to the Rock, Paper or Scissors game!")
print("Press 'q' to quit the game.")
wins = 0
losses = 0
ties = 0
choices={"r":"Rock", "p":"Paper", "s":"Scissors"}

while True:
 ran=random.choice(["Rock", "Paper", "Scissors"])
 a=input("Rock, Paper or Scissors? (r/p/s): ").lower()
 
 if a == "q":
   print(Fore.LIGHTMAGENTA_EX + f"Final scores: Wins-{wins} | Losses-{losses} | Ties-{ties}")
   print("Thanks for playing!")
   break
 
 if a not in choices:
    print(Fore.RED + "Invalid input.")
    continue
 
 user_choice=choices[a]
 
 if user_choice == ran:
    print(Fore.YELLOW + "It's a Tie")
    ties+=1
    print(Fore.LIGHTBLUE_EX + f"Scores: Wins-{wins} | Losses-{losses} | Ties-{ties}")
    continue
 
 print(f"You chose {user_choice}")
 print(f"Computer chose {ran}")

 if (user_choice == "Rock" and ran == "Scissors") or \
    (user_choice == "Scissors" and ran == "Paper") or \
    (user_choice == "Paper" and ran == "Rock"):
   print(Fore.GREEN + "You won!")
   wins+=1
 else:
   print(Fore.RED + "You lost!")
   losses+=1
 print(Fore.LIGHTBLUE_EX + f"Scores: Wins-{wins} | Losses-{losses} | Ties-{ties}")
 time.sleep(2)




                                                                                                    