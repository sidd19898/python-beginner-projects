# Number guessing game
# computer select number from 1 and 100 as a target number 
# computer asks user for his guess 
# if the guess is higher than target number it should print too high or two low
# congratulation you have guessed correct number

import random

a = random.randint(1,100)

while True:

 b = int(input("guess the number between 1 to 100 : "))
 
 if (a == b):
    print("congratulation you have guessed correct number")
    break
 
 elif(b < a):
    print("too low guess higher")
 elif(b > a):
    print("too high guess lower")    
