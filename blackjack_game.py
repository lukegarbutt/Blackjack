# main file             S C H D
import random

def main(): # this function will call our individual modules probably on a loop to play blackjack
	deck = initialise_deck() # list of 52 card objects, all unique suit and value
	deck.shuffle() # deck method that will shuffle the cards
	for i in deck:
		print(i.value, i.suit)

# create deck class

class deck():
	def __init__(self):
		self.deck = add_cards()

	def shuffle(self):
		self.deck = random.shuffle(self.deck)

	def add_cards(self):
		deck = []
		for i in range(1, 53):
			deck.append(card(i))
		return(deck)


# create card class

# create game rules and conditions

# create player class

# create dealer class

if __name__ == '__main__':
	main()