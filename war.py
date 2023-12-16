import random
class Card():
    def __init__(self, value, strength, colour=''):
        self.value = value
        self.colour = colour
        self.strength = strength

    def __str__(self):
        if self.colour:
            return f"{self.value} of {self.colour}"
        else:
            return f"{self.value}"
    
class Hand():
    colours = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    values = [
            {"name":'Ace',
            "strength": 14 },
            {"name":'King',
            "strength": 13 },
            {"name":'Queen',
            "strength": 12 },
            {"name":'Jack',
            "strength": 11 },
            {"name":'10',
            "strength": 10 },
            {"name":'9',
            "strength": 9 },
            {"name":'8',
            "strength": 8 },
            {"name":'7',
            "strength": 7 },
            {"name":'6',
            "strength": 6 },
            {"name":'5',
            "strength": 5 },
            {"name":'4',
            "strength": 4 },
            {"name":'3',
            "strength": 3 },
            {"name":'2',
            "strength": 2 },
        ]
    joker = {"name":'Joker',
            "strength": 15 }

    def __init__(self, cards=[]):
        self.cards = cards

    def full_deck(self):
        self.cards = [Card(value['name'], value['strength'], colour) for value in self.values for colour in self.colours]
        for _ in range(2):
            self.cards.append(Card(self.joker["name"], self.joker["strength"]))
        return self

    def shuffle_cards(self):
        random.shuffle(self.cards)
        return self
    
    def divide_deck(self):
        half_length = len(self.cards) // 2
        first_half = self.cards[:half_length]
        second_half = self.cards[half_length:]
        return first_half, second_half
    
    def __add__(self, other):
        for card in other.cards:
            self.cards.append(card)
        return self
    
    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return self
        else:
            raise ValueError("The card your trying to removeis not in the deck")
        
    def add_card(self, card):
        self.cards.append(card)
        return self

def main():
    deck = Hand().full_deck().shuffle_cards()
    player1, player2 = deck.divide_deck()
    player1 = Hand(player1)
    player2 = Hand(player2)
    
    while player1.cards and player2.cards:
        player1_card = player1.cards.pop(0)
        player2_card = player2.cards.pop(0)
        print(f"Player 1 plays: {player1_card}")
        print(f"Player 2 plays: {player2_card}")
        if player1_card.strength > player2_card.strength:
            print("Player 1 wins the round!")
            player1.cards.extend([player1_card, player2_card])
        elif player1_card.strength < player2_card.strength:
            print("Player 2 wins the round!")
            player2.cards.extend([player1_card, player2_card])
        else:
            while player1_card.strength == player2_card.strength:
                print("War!")
                if player1.cards and player2.cards:
                    temp_pile = [player1.cards.pop(0), player2.cards.pop(0)]
                    player1_card = player1.cards.pop(0)
                    if player1_card.strength > player2_card.strength:
                        print("Player 1 wins the round!")
                        player1.cards.extend([player1_card, player2_card])
                        player1.cards.extend(temp_pile)
                        break
                    elif player1_card.strength < player2_card.strength:
                        print("Player 2 wins the round!")
                        player2.cards.extend([player1_card, player2_card])
                        player2.cards.extend(temp_pile)
                        break
                else:
                    break
        
    if player1.cards:
        print("Player 1 wins the game!")
    elif player2.cards:
        print("Player 2 wins the game!")
    else:
        print("It's a tie!")
        



if __name__ == "__main__":
    main()