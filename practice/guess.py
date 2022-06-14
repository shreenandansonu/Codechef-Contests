import random
max=input("Enter the maximum number you want to guess ")
r=random.randint(0,int(max))
print(r)
guess=input("Guess the number ")

i = 1
while int(r)!=int(guess):
  print("You guess is wrong. Good luck next time!")
  guess=input("Guess the number ")
  i += 1
  if int(r)==int(guess):
      print("your guessed number is CORRECT! It's your "+ str(i) + "th guess.")

