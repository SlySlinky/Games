class Blackjack:
    deck = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH','AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD','AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC','AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS']
    player_hand = [deck.pop(int(random(0,len(deck)))),deck.pop(int(random(0,len(deck))))]
    dealer_hand = [deck.pop(int(random(0,len(deck)))), deck.pop(int(random(0,len(deck))))] #int(random(1,len(deck)+1))
    player_total = 0
    dealer_total = 0
    total = 0
    ok = 0

    
    def __init__(self, ok):
        self.ok = ok
        
    def reset(self):
        self.deck = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH','AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD','AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC','AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS']
        self.player_hand = [self.deck.pop(int(random(0,len(self.deck)))),self.deck.pop(int(random(0,len(self.deck))))]
        self.dealer_hand = [self.deck.pop(int(random(0,len(self.deck))))] #int(random(1,len(deck)+1))
        self.player_total = 0
        self.dealer_total = 0
        self.total = 0
            
    def get_total(self, hand):
        self.total = 0
        num_aces = 0
        for card in hand:
            if '10' in card:
                cardvalue = '10'
            else:
                cardvalue = card[0]
            if cardvalue in ['J', 'Q', 'K']:
                self.total += 10
            elif cardvalue == 'A':
                num_aces +=1
                self.total += 11
            else:                
                self.total += int(cardvalue)
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
        text("Player's total:"+ str(player_total), 1500, 100)
        if is_player_turn:
            print()
        else:
            text("Dealer's total:" + str(dealer_total), 500, 1000)
        print()
