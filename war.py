import random
class Card():
    def __init__(self, value, colour):
        self.value = value
        self.colour = colour

    def __str__(self):
        return f"{self.value} of {self.colour}"
class CardDeck():
    colours = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    values = ['Joker', 'Ace', 'King', 'Queen','Jack', '10', '9', '8', '7', '6', '5','4','3','2']

    def __init__(self):
        self.deck = [f"{Card(value, colour)}" for value in self.values for colour in self.colours]

    def shuffle_cards(self):
        random.shuffle(self.deck)
        return self
    
    def divide_deck(self):
        half_length = len(self.deck) // 2
        first_half = self.deck[:half_length]
        second_half = self.deck[half_length:]
        return first_half, second_half
    
    def __str__(self):
        return ', '.join(map(str, self.deck))

def main():
    deck = CardDeck().shuffle_cards()
    first_half, second_half = deck.divide_deck()
    print(first_half[0])
    print(second_half[0])
    

if __name__ == "__main__":
    main()