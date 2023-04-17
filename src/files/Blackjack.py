class Blackjack:
    deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    player_hand = [deck.pop(0), deck.pop(0)]
    dealer_hand = [deck.pop(0), deck.pop(0)]
    player_total = 0
    dealer_total = 0
    total = 0
    ok = 0

    
    def __init__(self, ok):
        self.ok = ok
        
        
    def get_total(self, hand):
        self.total = 0
        num_aces = 0
        for card in hand:
            if card in ['J', 'Q', 'K']:
                self.total += 10
            elif card == 'A':
                num_aces +=1
                self.total += 11
            else:
                self.total += int(card)
        while self.total > 21 and num_aces > 0:
            self.total -= 10
            num_aces -= 1
        return self.total
    def print_game(self, player_total, dealer_total, is_player_turn):
        self.player_total = player_total
        self.dealer_total = dealer_total
        print()
        textSize(50)
        fill(0)
        text(str(self.player_hand), 500, 200)
        text("Player's total:"+ str(player_total), 500, 500)
        text("Dealer's hand:" + self.dealer_hand[0] if is_player_turn else self.dealer_hand, 500, 700)
        if is_player_turn:
            print()
        else:
            text("Dealer's total:" + str(dealer_total), 500, 1000)
        print()
