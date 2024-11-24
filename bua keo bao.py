from random import randint

print("Nhap Bua, Keo, Bao:")
player = input()
computer = randint(0,2)

print("---")
print("You choose: " + player)
print("computer choose: " + player)
print("---")

if player == computer:
	print("Draw")
else:
	if computer == 0:
		computer = "Bua"
	if computer == 1:
		computer = "Bao"
	if computer == 2:
		computer = "Keo"

	elif player == "Keo":
		if computer == "Bua":
			print("Lose")
		else:
			print("Win")

	elif player == "Bua":
		if computer == "Keo":
			print("Win")
		else:
			print("lose")

	elif player == "Bao":
		if computer == "Keo":
			print("Lose")
		else:
			print("win")

	else:
		print("Nhap Sai!")