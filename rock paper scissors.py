# Name
# Rock paper scissors
# added a comment
# Variables
import random

pScore = 0
cScore = 0
ties = 0
computerChoices = ["r","p","s"]

# Welcome message
# Print the message
print("Welcome to Rock Paper Scissors")
# Prompt for players name
pName = input("What is your name? ")

# Game loop
# Final Score
def printScore():
	# Write message
	print("The score is: ")
	# Write player score
	print(pName + ": " + str(pScore))
	# Write computer score
	print("Computer: " + str(cScore))
	# Write how many ties
	print("Ties: " + str(ties))

# Game loop
# make a forever loop
while True: 
	# print current score
	printScore()
	# prompt for a choice (r (rock), p (paper), s(scissors), q(quit))
	pChoice = input("Enter r (rock), p (paper), s(scissors), q(to quit): ")
	# compare for players entering q
	if pChoice == "q":
		break
	# get computers choice (random)
	cChoice = random.choice(computerChoices)
	
	# compare for players entering r
	if pChoice == "r":
		print(pName + " picked rock")
		#If computer is r
		if cChoice == "r":
			print("Computer picked rock")
			print("Its a tie")
			ties = ties + 1
		#If computer is p 
		elif cChoice == "p": 
			print("Computer picked paper")
			print("Paper covers rock")
			cScore = cScore + 1 
		#If computer is s
		else:
			print("Computer pciked scissors")
			print("rock breaks scissors")
			pScore = pScore + 1
	# compare for players entering p
	elif pChoice == "p":
		print(pName + " picked paper")
		#If computer is r
		if cChoice == "r":
			print("Computer picked rock")
			print("Paper covers rock")
			pScore = pScore + 1
		#If computer is p 
		elif cChoice == "p": 
			print("Computer picked paper")
			print("Its a tie")
			ties = ties + 1 
		#If computer is s
		else:
			print("Computer picked scissors")
			print("Scissors cuts paper")
			cScore = cScore + 1

		pass
	# compare for players entering s
	elif pChoice == "s":
		print(pName + " picked scissors")
		#If computer is r
		if cChoice == "r":
			print("Computer picked rock")
			print("Rock smashes scissors")
			cScore = cScore + 1
		#If computer is p 
		elif cChoice == "p": 
			print("Computer picked paper")
			print("Paper is cut by scissors")
			pScore = pScore + 1 
		#If computer is s
		else:
			print("Computer pciked scissors")
			print("Its a tie")
			ties = ties + 1
		pass
	# compare for players entering q

	