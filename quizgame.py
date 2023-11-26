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
    print("Sorry, that was wrong! The answer is #.")

answer = input("What is used to print to the console? ")
if answer.lower() == 'print':
    print('Correct!')
    score += 1
else:
    print("Sorry, that was wrong! The answer is print.")

answer = input("What data type is used for numbers? ")
if answer.lower() == "int":
    print('Correct!')
    score += 1
else: 
    print("Sorry, that was wrong! The answer is int.")

answer = input("What data type is used for numbers with decimals? ")
if answer.lower() == "float":
    print('Correct!')
    score += 1
else: 
    print("Sorry, that was wrong! The answer is float.")

answer = input("Python is an interpreted, high-level, general-purpose programming language. True or False? ")
if answer.lower() == "true":
    print('Correct!')
    score += 1
else: 
    print("Sorry, that was wrong! The answer is true.")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")