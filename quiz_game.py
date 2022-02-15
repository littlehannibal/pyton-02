#exercise quiz game

print("Welcome to my user computer quiz")

play = input("Do you wanna play? ")
print(play)
#in this case print the output

if play.lower() != "yes":
    quit()

print("Ok, Let's play!")

score = 0

answer = input("What did Galileo Galilei discover in 1610? ")
if answer.lower() == "Four satellites of Jupiter":
    print("Exact, next question!")
    score +=1
else:
    print('Incorrect!')
    score -=0.25

answer = input("Where in June 1633 did Galileo Galilei abjure his errors? ")
if answer.lower() == "Church of Santa Maria Sopra Minerva":
    print("Exact, next question!")
    score += 1
else:
    print('Incorrect!')
    score -= 0.25

answer = input(" When was Isaac Newton born? ")
if answer.lower() == "25 December 1642":
    print("Exact!")
    score += 1
else:
    print('Incorrect!')
    score -= 0.25

answer = input(" What is Isaac Newton’s third law of motion? ")
if answer.lower() == "To every action there is an equal and opposite reaction":
    print("Exact!")
    score += 1
else:
    print('Incorrect!')
    score -= 0.25

print("you got " + str(score) + " this is the total score!")
#for making %
print(str((score/4) * 100) + "%")

