# main file             S C H D
import random

def main(): # this function will call our individual modules probably on a loop to play blackjack
	deck1 = deck() # list of 52 card objects, all unique suit and value
	deck1.shuffle() # deck method that will shuffle the cards
	number_of_players = 1
	initialise_game(number_of_players)

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

	def card_score(self):
		try:
			return(int(card.value))
		except:
			if card.value == 'Jack' or card.value == 'Queen' or card.value == 'King':
				return(10)
			elif card.value == 'Ace':
				return('Ace')

# create game rules and conditions

# create player class

# create hand class
class hand():
	def __init__(self, person):
		self.person = person
		self.cards = []

	def draw_to_hand(self, deck):
		self.cards.append(deck.draw_card())


# create dealer class

class dealer():
	def __init__(self):
		self.cards = []

	def initialise_hand(self):
		self.dealers_hand = hand("Dealer")

	def dealer_twist(self, deck):
		self.dealers_hand.draw_to_hand(deck)

	def dealer_turn(self, dealers_hand):
		while(True):
			score = 0
			ace_count = 0
			for card in dealers_hand:
				card_score = card.card_score()
				if card_score == 'Ace':
					ace_count += 1
				else:
					score += card_score
			break

def initialise_game(number_of_players):
	for i in range(number_of_players):
		pass # initialise the players hands similar to the dealers one
	# deal each player 1 card
	# deal dealer 1 card
	# repeat above two lines

if __name__ == '__main__':
	main()