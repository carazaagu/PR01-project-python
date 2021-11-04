import random
import time

# Create a class that will define the attributes and methods of the deck

class Deck():
    def __init__(self):
        # Define the deck
        spade = "♠"
        heart = "♥"
        diamond = "♦"
        club = "♣"
        suits = [spade, heart, diamond, club]
        numbers = [i for i in range(2,11)] + ['J', 'Q', 'K', 'A']
        value = {}
        self.cards = [(suit,number) for suit, number in zip(suits*len(numbers),numbers*len(suits))]

        #Define the value of each card
        for i in self.cards:
            if type(i[1]) == int:
                value[i] = i[1]
            elif (type(i[1])==str) & (i[1]!='A'):
                value[i] = 10
            else:
                value[i] = [1,11]
        self.cards_value = value

    
    def shuffle_deck(self):
        # Shuffle the cards of the deck
        random.shuffle(self.cards)
    
    
    def pop_card(self):
        # Pop a card from the deck
        # If there is no card left, a new deck is created
        if len(self.cards) == 0:
            self.cards = [(suit,number) for suit, number in zip(suits*len(numbers),numbers*len(suits))]
            random.shuffle(self.cards)
            return self.cards.pop()
        else:
            return self.cards.pop()


# Create a class that will define the attributes and methods of the players

class Player():
    def __init__(self, name):
        # Define name, hand value, choices and status (playing or not)
        self.name = name
        self.hand_value = 0
        self.decision_move = ['hit', 'stand']
        self.decision_play = ['yes','no']
            

    def stop (self, answer):
        # Player decides whether to keep playing or not
        if answer == 'No':
            self.playing = False
    

    def hand_card (self, value):
        # Hand of the player increases its value, allowing to chose value of an Ace
        if type(value) == int:
            self.hand_value += value
        elif (type(value) != int) & (self.name=='Croupier'):
            if self.hand_value + 11 > 21:
                self.hand_value += 1
            else:
                self.hand_value += 11
        else:
            print(f"{self.name}, would you like the A's having a value of 1 or 11?")
            ace_value=int(input(f"{self.name}, would you like the A's having a value of 1 or 11?"))
            while ace_value not in [1,11]:
                ace_value=int(input(f"{self.name}, would you like the A's having a value of 1 or 11?"))
            self.hand_value += ace_value


class Rules():

    def first_check_value (self, list_players, croupier):
        # Before Croupier turn it will check if the hand value of the players is 0
        values = [player.hand_value == 0 for player in list_players]
        if all(values) == True:
            return 'Repeat the game'
        else:
            return 'Keep playing'
        
    
    def final_check_value (self, list_players, croupier):
        # Compare hands davlues between players an Croupier
        for player in list_players:
            if player.hand_value > croupier.hand_value:
                print(f'{player.name} hand value is {player.hand_value} and {croupier.name} hand value is {croupier.hand_value}. {player.name} wins!\n')
                time.sleep(1.5)
            elif player.hand_value == croupier.hand_value:
                print(f'{player.name} hand value is {player.hand_value} and {croupier.name} hand value is {croupier.hand_value}. There is a draw!\n')
                time.sleep(1.5)
            else:
                print(f'{player.name} hand value is {player.hand_value} and {croupier.name} hand value is {croupier.hand_value}. {croupier.name} wins!\n')
                time.sleep(1.5)
        print("Let's play another game!\n")
        time.sleep(1.5)


class Game():

    def __init__(self):
        pass

    def welcome(self):
        # Welcome
        print("""Welcome to the Digital Casino. Tonight we will be playing the game of Black Jack. 
I will be playing on behalf of the Digital Casino against you. I take for granted that you are
familiar with the rules of the game. Please take a sit, enjoy the game and good luck.\n""")
        
        # Call method num_players
        time.sleep(1.5)
        self.num_players()

    def num_players(self):
        # Define a list of players that will be playing: number of players, each one as an object of the class Player, and included in a list
        self.list_players = []
        print('The maximum number of players that can play at the same time is 5.\nHow many players will play in the next game?\n')
        num_players = int(input('How many players will play in the next game?'))
        while num_players > 5:
            print('This is too many people. As I said, the maximum number of players that can plat at the same time is 5.\n\nHow many players will play in the next game?\n')
            num_players = int(input('How many players will play in the next game?'))
        if num_players == 0:
            print('Thank you for coming. Digital Casino wishes you a lovely day')
        else:
            for i in range(num_players):
                obj = Player(name=f'Player{i}')
                self.list_players.append(obj)
            print(f'''Therefore, in this hand there will be playing {len(self.list_players)} players against the Croupier\n''')

            # Define Croupier: object from the class Player, names Croupier
            self.croupier = Player(name='Croupier')
            
            # Define checking rules: object from the class Rules
            self.rules = Rules()

            # Create the deck and shuffle it: object of the class Dech and method shuffle
            self.deck = Deck()
            self.deck.shuffle_deck()

            # Call method start_game
            time.sleep(1.5)
            self.start_game()


    def start_game(self):
        # Dealing the 1st cards: pop a card from the deck and add its value to player's or croupier's hand. Value shown to the table
        for i in range(len(self.list_players)):
            time.sleep(1.5)
            card = self.deck.pop_card()
            self.list_players[i].hand_card(self.deck.cards_value[card])
            print(f'{self.list_players[i].name} first card: {card}. The value of the hand is {self.list_players[i].hand_value}')
        time.sleep(1.5)
        card_c1 = self.deck.pop_card()
        self.croupier.hand_card(self.deck.cards_value[card_c1])
        print(f'\n{self.croupier.name} first card: {card_c1}. The value of the hand is {self.croupier.hand_value}\n')

        # Dealing the 2nd cards: pop a card from the deck and add its value to player's or croupier's hand. Value shown to the table with the exception of the Croupier
        for i in range(len(self.list_players)):
            time.sleep(1.5)
            card2 = self.deck.pop_card()
            self.list_players[i].hand_card(self.deck.cards_value[card2])
            print(f'{self.list_players[i].name} second card: {card2}. The value of the hand is {self.list_players[i].hand_value}')
        time.sleep(1.5)
        card_c2 = self.deck.pop_card()
        self.croupier.hand_card(self.deck.cards_value[card_c2])
        print(f'\n{self.croupier.name} second card is not turned. The value of the hand is Unknown\n')
        time.sleep(1.5)

        # Each player keeps playing until they Stand or they overpass a hand value of 21
        for i in range(len(self.list_players)):
            while self.list_players[i].hand_value < 21:
                print(f'{self.list_players[i].name}, your hand value is {self.list_players[i].hand_value}. Would you like to Hit or Stand?')
                decision = input(f'{self.list_players[i].name}, your hand value is {self.list_players[i].hand_value}. Would you like to Hit or Stand?').lower()
                while decision not in self.list_players[i].decision_move:
                    decision = input(f'{self.list_players[i].name}, your hand value is {self.list_players[i].hand_value}. Would you like to Hit or Stand?').lower()
                if decision == 'stand':
                    break
                else:
                    card3 =  self.deck.pop_card()
                    self.list_players[i].hand_card(self.deck.cards_value[card3])
                    print(f'{self.list_players[i].name} new card: {card3}')
            time.sleep(1.5)
            if self.list_players[i].hand_value == 21:
                print(f'{self.list_players[i].name}, your hand value is 21. Your turn is finished\n')
            elif self.list_players[i].hand_value < 21:
                print(f'{self.list_players[i].name}, your turn is finished\n')
            else:
                self.list_players[i].hand_value = 0
                print(f'{self.list_players[i].name}, your hand value is over 21. Your turn is finished\n')
                time.sleep(1.5)

        # Croupier plays: first check if the value of the other players' hands are all 0 or not. If 0, start the game again
        time.sleep(1.5)
        first_check = self.rules.first_check_value(self.list_players, self.croupier)
        if first_check == 'Repeat the game':
            print("All players hand value is 0. Croupier has won and the game is over.\nLet's play another game!\n")
            time.sleep(1.5)
            self.num_players()
        else:
            pass
        print(f'Second card of Croupier is turned: {card_c2}. Croupier hand is {self.croupier.hand_value}')
        while self.croupier.hand_value < 17:
            card_c3 = self.deck.pop_card()
            self.croupier.hand_card(self.deck.cards_value[card_c3])
            time.sleep(1.5)
            print(f'Croupier hits another card: {card_c3}. The value of Croupier hand is {self.croupier.hand_value}')
        
        time.sleep(1.5)
        if self.croupier.hand_value <= 21:
                print('Croupier turn is finished\n')
        else:
            self.croupier.hand_value = 0
            print('Croupier hand value is over 21. Croupier turn is finished\n')
        
        # Check results
        self.rules.final_check_value(self.list_players, self.croupier)

        # Start the game again
        self.num_players()

# Execute game
def main():
	Game().welcome()
if __name__=="__main__":
	main()