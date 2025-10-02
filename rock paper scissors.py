# computer choses from rock paper scissors
# ask for users choice rock paper or scissors
# print what user choses with emoji
# print what computer choses with emoji
"""
1 if user-rock and comp-paper
  print you lose
2 if user-paper and comp-rock
  print you win
3 if user-rock and comp-sci
  print you win
4 if user-sci and comp-rock
  print you lose
5 if user-paper and comp-sci
  print you lose
6 if user-sci and comp-paper
  print you win
"""

import random


a = ["✊","✌️","✋"]

while True:
 comp = random.choice(a)
 user = input("r/p/s :")
 print("you chose:",user)
 print("computer chose:",comp)
 if (user == "r" and comp == "✊"):
    print("its tie")
 elif (user == "p" and comp == "✋"):
    print("its tie")
 elif (user == "s" and comp == "✌️"):
    print("its tie")
 elif (user == "r" and comp == "✋"):
    print("you lose")
 elif (user == "p" and comp == "✊"):
    print("you win")
 elif (user == "r" and comp == "✌️"):
    print("you win")
 elif (user == "s" and comp == "✊"):
    print("you lose")
 elif (user == "p" and comp == "✌️"):
    print("you lose")
 elif (user == "s" and comp == "✋"):
    print("you win")

 ask = input("continue(y/n):")
 if(ask == "n"):
    break


