print("Welcome to my Python Basics quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play <3")
score = 0

answer = input("What symbol is used to comment out a line? ")
if answer.lower() == "#":
    print('Correct!')
    score += 1
else: 
    print("Sorry, that was wrong!")

print("You got " + str(score) + " questions correct!")
print("You got " + str(score / 4) + "%.")