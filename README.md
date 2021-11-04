# Project 1_Python Classes_BlackJack

## Definition

In this project I have developed some code that would allow one ore more users to run the game of BlackJack, interacting with the computer and playing against it.
The code is mainly based on creating classes per each item that is needed to play this game:

### 1. class Deck

Create an object that will have attributes and methods.
- Attributes: cards, cards_value
- Methods: shuffle_deck (randomly shuffle cards), pop_card (take a card from the deck)

### 2. class Player

Create an object that will have attributes and methods.
- Attributes: name, hand value, list of decisions
- Methods: hand_card (increase hand value according to the value of the card taken from the deck)

### 3. class Rules

Create an object that will have attributes and methods.
- Attributes: none
- Methods: first_check_value (Before Croupier turn it will check if the hand value of the players is 0), final_check_value (# Compare hands values between players an Croupier)

### 4. class Game

Create an object (THE GAME) that will have attributes and methods.
- Attributes: list_players (objects from class Player), croupier (object from class Player named Croupier), rules (object from class Rules)
- Methods: welcome (welcome players), num_players (ask number of players and define all attributes), start_game (generate the game with the players, deck and rules) 


## Execution of the game

a) Execute file Final_project1_Blackjack.py in the Command Line

b) Execute notebook Final_project1_Blackjack_PlayGame.ipynb, where the .py file is imported and a new game is created in the notebook
