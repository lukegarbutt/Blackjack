# main file             S C H D
import random

def main(): # this function will call our individual modules probably on a loop to play blackjack
	deck_of_cards = deck() # list of 52 card objects, all unique suit and value
	deck_of_cards.shuffle() # deck method that will shuffle the cards
	number_of_players = 3
	list_of_players, dealer = initialise_game(number_of_players, deck_of_cards)
	print("Dealer has cards {} of {} and {} of {}.".format(dealer.cards[0].value, dealer.cards[0].suit, dealer.cards[1].value, dealer.cards[1].suit))
	for i in list_of_players:
		print("{} has cards {} of {} and {} of {}.".format(i.name, i.cards[0].value, i.cards[0].suit, i.cards[1].value, i.cards[1].suit))

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

class player():
	def __init__(self, name):
		self.cards = []
		self.name = name

	def player_hit(self, deck):
		self.cards.append(deck.draw_card())

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
		self.name = "Dealer"

	def dealer_hit(self, deck):
		self.cards.append(deck.draw_card())

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

def initialise_game(number_of_players, deck):
	list_of_players = []
	for i in range(number_of_players):
		player_str = "Player_" + str(i+1)
		list_of_players.append(player(player_str))
	dealer_obj = dealer()
	for i in list_of_players: # deal each player 1 card
		i.player_hit(deck)
	dealer_obj.dealer_hit(deck) # deal dealer 1 card
	for i in list_of_players: # repeat above two lines
		i.player_hit(deck)
	dealer_obj.dealer_hit(deck)
	return(list_of_players, dealer_obj)

if __name__ == '__main__':
	main()