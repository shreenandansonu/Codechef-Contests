print("WELCOME TO MY QUIZ!")
playing=input("Do you want ot play? ")

if playing.lower() != "yes":
   quit()
print("Alright! let's PLAY :)")
score=0

answer=input("What is the largest connective tissue? ")
if answer=="Integumentary system":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT")
    score -= 0.25    

answer=input("What is the largest human cell? ")
if answer=="Neuron":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT") 
    score -= 0.25

answer=input("What is the largest bone in human body? ")
if answer=="Feamur":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT") 
    score -= 0.25

answer=input("What is the smallest bone in human body? ")
if answer=="Ear bone":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT")  
    score -= 0.25   

print("Your Score is " + str(score) + " and your percentage is " +str(100*score/4)+"%")
