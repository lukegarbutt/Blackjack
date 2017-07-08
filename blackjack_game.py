# main file             S C H D
import random
import time

def main(): # this function will call our individual modules probably on a loop to play blackjack
	deck_of_cards = deck() # list of 52 card objects, all unique suit and value
	deck_of_cards.shuffle() # deck method that will shuffle the cards
	number_of_players = 3
	list_of_players, dealer = initialise_game(number_of_players, deck_of_cards)
	print("Dealer has cards {} of {} and {} of {}.".format(dealer.cards[0].value, dealer.cards[0].suit, dealer.cards[1].value, dealer.cards[1].suit))
	for i in list_of_players:
		print("{} has cards {} of {} and {} of {}.".format(i.name, i.cards[0].value, i.cards[0].suit, i.cards[1].value, i.cards[1].suit))
	dealer.dealer_turn(deck_of_cards)

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
			return(int(self.value))
		except:
			if self.value == 'Jack' or self.value == 'Queen' or self.value == 'King':
				return(10)
			elif self.value == 'Ace':
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

# create dealer class

class dealer():
	def __init__(self):
		self.cards = []
		self.name = "Dealer"

	def dealer_hit(self, deck):
		self.cards.append(deck.draw_card())

	def dealer_turn(self, deck):
		dealer_bust = False
		while(True):
			time.sleep(0.1)
			if dealer_bust:
				break
			score = 0
			ace_count = 0
			for card in self.cards:
				card_score = card.card_score()
				if card_score == 'Ace':
					ace_count += 1
					score += 11
				else:
					score += card_score
			if score > 22:
				while(score > 21):
					if ace_count == 0:
						print('Dealer bust at {}'.format(score))
						dealer_bust = True
						break
					else:
						ace_count -= 1
						score -= 10
			if score < 17:
				self.dealer_hit(deck)
				print('Dealer drew the {} of {}'.format(self.cards[-1].value, self.cards[-1].suit))
			else:
				print('Dealer stands on {} with cards --to be filled in later--'.format(score))
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
	for i in range(10):
		main()
		print()