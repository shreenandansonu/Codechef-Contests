import random as rm
from typing import Match
t=int(input("How many times do you want to play "))
score=0
signs=['STONE','PAPER','SCISSORS']
for _ in range(t):
    c_n=rm.choice(signs)
    u_n=input("Enter your Sign ").upper
    if (u_n in signs) and (c_n==u_n):
        print("Match Draw \n")
        print(score)
    elif (u_n in signs) and (u_n=="STONE") and (c_n=="SCISSORS"):
        print("You won!")
        score+=10
        print(score)
    elif (u_n in signs) and (u_n=="SCISSORS") and (c_n=="STONE"):
        print("You lost!")
        score-=10
        print(score)
    elif (u_n in signs) and (u_n=="PAPER") and (c_n=="STONE"):
        print("You won!")
        score+=10
        print(score)
    elif (u_n in signs) and (u_n=="STONE") and (c_n=="PAPER"):
        print("You lost!")
        score-=10
        print(score)
    elif (u_n in signs) and (u_n=="SCISSORS") and (c_n=="PAPER"):
        print("You won!")
        score+=10
        print(score)
    elif (u_n in signs) and (u_n=="PAPER") and (c_n=="SCISSORS"):
        print("You lost!")
        score-=10
        print(score)
if score>+0:
    print("You Won the match!")
else :
    print("You Lost the match!")