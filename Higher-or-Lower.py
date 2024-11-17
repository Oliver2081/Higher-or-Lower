import random
import math
import inflect
from os import system, name

appVersion = '1.1'
turns = 0
inflect = inflect.engine()
replay = True

def clear():
	if name == 'nt':
		system('cls')
	else:
		system('clear')
		
while replay == True:
	replay = False
	clear()
	
	print(f"Higher or Lower: v{appVersion}\n")
	
	print("How Many Turns Do You Want To Play? (Min: 5, Max: 51)")
	turnsAnswered = False
	
	while turnsAnswered == False:
		try:
			turns = int(input(": "))
		except ValueError:
			turnsAnswered = False
			
		if (turns >= 5 and turns <= 51):
			turnsAnswered = True
		else:
			turnsAnswered = False

	def createDeck():
		ranks = ['Ace', '2','3','4','5','6','7','8','9','10','Jack','Queen','King']
		suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
		deck = [None] * 52

		for i in range(52):
			if 0 <= i < 13:
				pos = i
				deck[i] = ranks[pos] + " Of " + suits[0]

			if 13 <= i < 26:
				pos = i - 13
				deck[i] = ranks[pos] + " Of " + suits[1]

			if 26 <= i < 39:
				pos = i - 26
				deck[i] = ranks[pos] + " Of " + suits[2]

			if 39 <= i < 52:
				pos = i - 39
				deck[i] = ranks[pos] + " Of " + suits[3]

		random.shuffle(deck)

		return deck

	def cardToValue(card):
		valueMap = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
		if card[0] in valueMap:
			cardValue = valueMap[card[0]]
		else:
			cardValue = card[0]
		return cardValue

	deck = createDeck()

	for i in range(turns):
		print(f"Your {inflect.ordinal(i + 1)} Card is The {deck[i]}")

		guessed = False

		while (guessed == False):
			guess = input("H/L: ").upper()
			try:
				letterPos = guess.index('H')
				guessed = True
			except ValueError:
				try:
					letterPos = guess.index('L')
					guessed = True
				except ValueError:
					guessed = False


		print(f"You Guessed: {guess[letterPos]}")

		currentCard = deck[i]
		nextCard = deck[i + 1]

		currentCardVal = int(cardToValue(currentCard))
		nextCardVal = int(cardToValue(nextCard))

		if (nextCardVal > currentCardVal and guess[letterPos] == 'H'):
			correct = True
		elif (nextCardVal < currentCardVal and guess[letterPos] == 'L'):
			correct = True
		else:
			correct = False

		if correct == True:
			print(f"Correct\n")
		if correct == False:
			print(f"Incorrect\n")
			break

	print(f"You Scored: {i}/{turns} Correctly")

	answered = False

	while (answered == False):
		playAgain = input("Play Again? (Y/N): ").upper()
		try:
			playAgain.index('Y')
			answered = True
			replay = True
		except ValueError:
			try:
				playAgain.index('N')
				answered = True
				replay = False
			except ValueError:
				answered = False
