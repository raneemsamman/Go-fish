from random import randint
from random import shuffle
#import numpy as np
    # COMMENT OUT: i wanted to use it to utilize the unique method it has but will do that in the next version


# class Computer(Player) has more details over how my bot would work but i believe
# it would be able to utilize the count method to its benefit by maximizing the requests
# it makes for the highest value cards while also utilizing the memory list of previously requested cards

class Card:
    """ A card class representing a card, its value and points

    Attributes
    ===========
        value : str
            the card value (example: "2", "3", "A")
        points : int
            the corresponding points value of each cards

    Methods
    ==========
    __init__() : str ,str
            the card object constructor
    __str__ : self
           returns information about the card ( card number and its points value
    __eq__ :  self ,card
            retruns true if compared card object has the same attribute num
    """
    def __init__(self, value, points):
        self.value = value
        self.points = points

    def __str__(self) -> str:
        """ tostring for a card object """
        return f"{self.value}"
    def __eq__(self,other) -> bool:
        """
        makes diffrenet instacses of card equal if they are the same card number

        Parameters
        ============
        other : Card
                to be able to compare card given with the card instance
        """
        if not isinstance(other,Card): return False
        return self.value == (other.value)
class Deck:
    """
    a Deck class to create a full playing deck of cards of 52 cards total

    Methods
    ========
    __init__() :
        the deck object constructor function
    draw_card() : -> str
        a function to draw and remove a card from the deck
    """

    points_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":
              9,"10":10, "J":11, "Q":12, "K":13, "A":14}
    def __init__(self):
        self.cards = [Card(key,self.points_dict[key]) for key in self.points_dict] * 4
        # https://www.geeksforgeeks.org/shuffle-a-deck-of-card-with-oops-in-python/
        shuffle(self.cards)

    def draw_card(self) -> str:
        """draws a single card and removes it from deck"""

        if len(self.cards) > 0:
            card = self.cards[randint(0, len(self.cards)-1)]
            self.cards.remove(card)
            return card
        else:
            print("Deck is out of cards")
            return None
class DealerJudge:
    """
    A class for dealing cards to players hands and controlling score-related functions

    Attributes
    ===========
        PlayerType : str
            User vs Computer
        deck : int (taken from what Deck generates)
            the full deck of cards in hand
    Methods
    ===========
    deal_cards():
        deals cards for the players' (user and comp) hands
    displayCards():
        Display the contents of the player's hands
    go_fish():
        draws one card from the deck to the hand when go_fish is True
    scores():
        generates the scores of players' hands

    """
    def __init__(self, PlayerType:str, deck):
        self.PlayerType = PlayerType
        self.deck = deck
        self.cards = []
        self.count = len(self.cards)
        self.score = 0
        self.memory = []

    def deal_cards(self):
        """deals cards for the hand"""
        for i in range(7):
            self.cards.append(self.deck.draw_card())
        self.cards.sort(key=lambda card: card.value)
    def __str__(self):
        self.cards.sort(key=lambda card: card.value)
        return (str([i.value for i in self.cards]))

    def go_fish(self) -> str:
        """Prints go fish and draws a card"""

        print("Go fish!")

        card = self.deck.draw_card()

        self.cards.append(card)
        self.cards.sort(key=lambda card: card.value)

        if self.PlayerType == "comp":
            computer = Computer()

        if self.PlayerType == "user":
            for resp in ask_user():

                print("Now adding " + card.value + " to your hand.")
                self.memory.append(resp)
                print(self.memory)

        else:
            print("The computer has drawn a card.")

        return card

    def displayHands(self):
        """Displays the contents of the players hands"""

        print("The computer has ", len(gameTest.comp.cards), " cards.")
        print("Your cards are: ")
        # change this print up using tuples
        card_counts = []
        for card in self.cards:
            card_counts.append((self.cards.count(card), card.value))
        card_counts.sort(reverse = True)
        for pair in set(card_counts):
            print(pair[1], ":", pair[0])

    def Scores(self):
        """ Deals with calculating score and deciding the result when the game is over"""
        for card in self.cards:
            self.score += (card.points)
        return self.score

        comp_score = self.comp.Scores()
        user_score = self.user.Scores()
        print(f"your score is {user_score}, the computer has scored {comp_score}")

        if user_score > comp_score:
            print("You win! Well done!")
        elif user_score < comp_score:
            print("You lost. Better luck next time!")
        else:
            print("You tied! Good match!")

class Player:
    """ A class for handling players' actions such as their hands and cards

    Attributes
    ===========
        hand : list
            an empty list to hold each object's cards

    Methods
    ==========
        make_hand():
            creates the hand of the player by adding random cards to the hand obj

        give_cards():
            transfers cards from one hand to the other

        add_card():
            adds the card drawn to the hand object of the player

        list_cards():
            sorts the hands of the player and returns it as a list

    """

    def __init__(self, name):
        self.name = name
        self.hand = []

    def make_hand(self, deck:Deck):

        # create hand
        for i in range(7):
            self.hand.append(deck.draw_card())
        self.hand.sort()

        #print(self.hand) # COMMENT OUT: this is for testing

    def give_cards(self, taker, card:str):
        """

        Parameters
        ---------------
            taker       Player
        """

        print("Transfering card " + card)

        while(card in self.hand):
            self.hand.remove(card)
            taker.add_card(card)

    def add_card(self, card:str):

        self.hand.append(card)
        self.hand.sort()

    def list_cards(self) -> list:

        self.hand.sort()
        return self.hand

class Computer(Player):
    """
    a class for the CPU to become better at playing the game and use strategy

    Attributes
    ===========
        memory: list
            saved the input of the user

    Methods
    ==========
        def __init__()
        def moves_memory():
            saves the cards requested by the user in a list
        def make value():
            defines the strategy and game moves of the computer


    """
    def __init__(self, memory):
        # memory list for player's requests
        self.memory = []

        points_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,
                            "10":10, "J":11, "Q":12, "K":13, "A":14}

    def moves_memory():
        """
        a function to save the cards requested by the user in a list
        """
        for card_asked in ask_user():
            if card_asked not in self.comp:
                #adding users requests to the memory list
                self.memory.append(card_asked)
                print(self.memory)
            else:
                pass
        return memory

    def make_value(memory):
        """
        a function defining the strategy and game moves of the computer.
            It takes in memory as a paramter
        """
        #this code here runs so that whenever it is the computer's trun to play
        # it would try to utilize one of the below conditionals to its favour

        if self.PlayerType == "comp":

            if len(self.comp.hand) < 10:
                if self.comp.count(self.cards) == 3:
                    ask_comp()
                elif self.comp.count(self.cards) == 2:
                    ask_comp()
                elif self.comp.count(self.cards) == 1:
                    for self.cards in self.memory:
                       ask_comp()
            if len(self.comp.hand) > 10:
                 if self.cards in self.memory:
                    ask_comp()
            else:
                while self.user.go_fish() == False:
                    if ['A', 'K', 'Q', 'J'] in self.comp.hand:
                        ask_comp()

class GoFishGamePlay:
    """
    Runs the Go Fish game from its instructions to ending

    Attributes
    ===========
    deck : Deck
    user : DealerJudge
    comp : DealerJudge

    """
    memory = [] #a class attribute to be used to save user moves

    def __init__(self):
        self.deck = Deck()
        self.user = DealerJudge("User Hand",self.deck)
        self.comp = DealerJudge("comp Hand",self.deck)

    def playGame(self):
        """ a function that holds the actions of the players and the flow of game rules"""
        self.user.deal_cards()
        self.comp.deal_cards()
        while(not self.is_game_over()):
            self.ask_user()
            if self.is_game_over():
                break
            input("Press enter to continue")
            self.ask_comp()
            input("Press enter to continue")
            self.user.displayHands()

        print("The game is over!")
        comp_score = self.comp.Scores()
        user_score = self.user.Scores()
        print(f"your score is {user_score}, the computer has scored {comp_score}")

        if user_score > comp_score:
            print("\nYou win! Well done!")
        elif user_score < comp_score:
            print("You lost. Better luck next time!")
        else:
            print("You tied! Good match!")

        if self.play_again():
            self.deck = Deck()
            self.user = DealerJudge("user",self.deck)
            self.comp = DealerJudge("comp",self.deck)
            self.playGame()
        else:
            print("GGs. The Game is Over!")
            #self.play_again() == False

    def ask_comp(self):
        """Computer requests a card from the user """

        potential_cards = []
        for card in self.comp.cards:
            counting = self.comp.cards.count(card)
            if counting != 4:
                potential_cards.append(card.value)

        if (len(potential_cards) > 0):
            index = randint(0, len(potential_cards) - 1)
            resp = potential_cards[index]
        else:
            # the computer has only books!
            resp = self.comp.cards[randint(0, len(self.comp.cards) - 1)]

        print("The computer is requesting", resp)
        input("Press enter to continue.")

        if str(resp) in str(self.user):
            print("You have this card")
            self.give_cards(self.user, self.comp, Card(resp,self.deck.points_dict[resp]))
        else:
            print("You do not have this card")
            self.comp.go_fish()

    def ask_user(self):
        """Asks the user to request a card"""

        invalid = True
        validCards = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']

        while(invalid):

            print("What card would you like? ")

            resp = input("Enter one of your cards: " + str(self.user) + ": ")
            resp = resp.upper() #addition to check lower cases as well

            if resp in validCards:
                if resp in str(self.user):
                    invalid = False
                else:
                    invalid = True
                    print("Invalid response")
            else:
                invalid = True
                print("Invalid response")

        if resp in str(self.comp):
            print("Computer has card")
            self.give_cards(self.comp, self.user, Card(resp,self.deck.points_dict[resp]))
        else:
            print("Computer does not have card")
            self.user.go_fish()

    def give_cards(self, giver, taker, card):
        """Passes cards from one hand to another"""

        print("Transfering card " + str(card.value))

        while(card in giver.cards):
            giver.cards.remove(card)
            taker.cards.append(card)
        taker.cards.sort(key=lambda card: card.value)

    def Scores(self):
        """ Deals with calculating score and deciding the result when the game is over"""
        for card in self.cards:
            self.score += (card.points)
        return self.score

        comp_score = self.comp.Scores()
        user_score = self.user.Scores()
        print(f"your score is {user_score}, the computer has scored {comp_score}")

        if user_score > comp_score:
            print("You win! Well done!")
        elif user_score < comp_score:
            print("You lost. Better luck next time!")
        else:
            print("You tied! Good match!")

    def play_again(self) -> bool:
        """prompts user if they wish to play again"""

        while(True):

            resp = input("Would you like to play again? (Y/N): ")
            resp = resp.upper()

            if resp == "Y":

                return True

            if resp == "N":
                return False

            print("Invalid input")

    def is_game_over(self):
        """Determines if game is over"""
        # check that deck is empty ?
        if len(self.deck.cards) > 0:
            return False

        for card in self.comp.cards:
            counting = self.comp.cards.count(card)
            if counting != 4:
                return False

        for card in self.user.cards:
            counting = self.user.cards.count(card)
            if counting != 4:
                return False

        return True

    # https://www.youtube.com/watch?v=JeznW_7DlB0&t=454s
    @staticmethod
    def welcome_message():
        """Statement welcoming user and explaining game"""
        print( f"***** Welcome to the game 'Go Fish' *****\n ========================================\n\nYour goal is to collect as many 4-of-a-kind, or 'books', as you can. \nBooks are scored based on the card value with Aces being the highest and '2' being the lowest. \nNow let's play! Good luck!\n\n========================================\nPress enter to continue\n")

if __name__ == "__main__":
    """ The main method to run the game """
    gameTest = GoFishGamePlay()
    gameTest.welcome_message()
    gameTest.playGame()
