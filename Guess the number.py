# import random
#
#
# def guess(x):  # define a function
# 	random_number = random.randint (1, x)  # randint allow us to return integers N
# 	guess = 0
# 	while guess != random_number:
# 		guess = int(input (f'Guess a number between 1 and {x}: '))
# 		if guess < random_number:
# 			print("Sorry, guess again. Too low ")
# 		elif guess > random_number:
# 			print("Sorry, guess again, Too High")
#
# 	print(f'You have guessed the number  {random_number}')

#
# guess (10)
import random


def computer_guess(x):
	low = 1
	high = x
	feedback = ' '
	while feedback != 'c':
		if low != high:   # this because randint sometimes will throw an error if high = low
			guess = random.randint (low, high)
		else:
			guess = low # could also be equal to high because high is equal to low
		feedback = input (f'Is {guess} too high (H), too low (L), or correct (C) ??').lower ()
		if feedback == 'h':
			high = guess - 1
		elif feedback == "l":
			low = guess + 1

	print (f" The computer guessed the number {guess}, correctly")


computer_guess (10)