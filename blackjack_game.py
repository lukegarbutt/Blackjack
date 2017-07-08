# main file             S C H D
import random

def main(): # this function will call our individual modules probably on a loop to play blackjack
	deck1 = deck() # list of 52 card objects, all unique suit and value
	deck1.shuffle() # deck method that will shuffle the cards
	for i in range(52):
		card = deck1.draw_card()
		print(card.suit, card.value)

# create deck class

class deck():
	def __init__(self):
		self.add_cards()

	def shuffle(self):
		random.shuffle(self.list_of_cards)

	def add_cards(self):
		self.list_of_cards = []
		for i in range(52):
			self.list_of_cards.append(card(i))

	def draw_card(self):
		card = self.list_of_cards.pop(0)
		self.list_of_cards.append(card)
		return(card)

# create card class

class card():
	def __init__(self, id):
		self.init_val(id)
		self.init_suit(id)

	def init_suit(self, id):
		suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
		id = id%4
		self.suit = suits[id]

	def init_val(self, id):
		values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
		id = id%13
		self.value = values[id]

# create game rules and conditions

# create player class

# create dealer class


if __name__ == '__main__':
	main()