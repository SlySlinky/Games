#Blackjack code by Dallin (not working with graphics yet), including gameplay functions at the top

import random
from Button import Button
tick = 0
deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
random.shuffle(deck)
player_hand = [deck.pop(0), deck.pop(0)]
dealer_hand = [deck.pop(0), deck.pop(0)]
tickholder = 0
button1 = Button(440,250,750,700,"Roulette")
button2 = Button(440,250,115,435,"Blackjack")
button3 = Button(440,250,750,260,"Craps")
button4 = Button(380,350,1445,335,"Slots")
button5 = Button(100,100,50,50,"home")
hit = Button(200,200,500,500,"hit")
stand = Button(200,200,900,500,"stand")

game = "home"

def get_total(hand):
    total = 0
    num_aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            num_aces += 1
            total += 11
        else:
            total += int(card)
    while total > 21 and num_aces > 0:
        total -= 10
        num_aces -= 1
    return total

def print_game(player_hand, dealer_hand, player_total, dealer_total, is_player_turn):
    text("Player's hand: " + player_hand, 200,1000)
    text("Player's total: " + player_total, 400,1000)
    text("Dealer's hand: " +  dealer_hand[0] if is_player_turn else dealer_hand,600,1000 )
    if is_player_turn:
        print()
    else:
        text("Dealer's total:" + dealer_total, 100, 500)

def play_dealer_turn(deck, dealer_hand):
    dealer_total = get_total(dealer_hand)
    while dealer_total < 17:
        dealer_hand.append(deck.pop(0))
        dealer_total = get_total(dealer_hand)
    return dealer_hand, dealer_total

def setup():
    global mainScreen
    frameRate(60)
    size(1920,1080)
    mainScreen = loadImage("CasinoMenuTemplate.png")
    mainScreen.resize(1920,1080)
    image(mainScreen,0,0)

        
def draw():
    global tick,tickholder, mainScreen, button1, button2, button3, button4, button5, game, hit, stand, dealer_hand, dealer_total, player_hand, player_total
    tick = tick + 1
    print(frameRate)
    if tick == 1:
        mainScreen = loadImage("CasinoMenuTemplate.png")
        mainScreen.resize(1920,1080)
        button1 = Button(440,250,750,700,"Roulette")
        button2 = Button(440,250,115,435,"Blackjack")
        button3 = Button(440,250,750,260,"Craps")
        button4 = Button(380,350,1445,335,"Slots")   
        button5 = Button(100,100,50,50,"home")
        hit = Button(200,200,500,500,"hit")
        stand = Button(200,200,900,500,"stand")
        
    if game == "home":
        image(mainScreen,0,0)       
        button1.Display()
        button2.Display()
        button3.Display()
        button4.Display()
        
        game = button1.CheckClick(game, "nav")
        game = button2.CheckClick(game, "nav")
        game = button3.CheckClick(game, "nav")
        game = button4.CheckClick(game, "nav")
        tickholder = tick
    elif game == "Craps":
        background(0,100,50)
        button5.Display()
        game = button5.CheckClick(game, "nav")
    elif game == "Blackjack":
        choice = ""
        background(0,220,70)
        button5.Display()
        game = button5.CheckClick(game, "nav")
        if tick > tickholder + 60:
            print("test 0")
            hit.Display()
            stand.Display()
            choice = hit.CheckClick("hit","slct")
            print("test 1")
            if choice == "":
                choice = stand.CheckClick("stand","slct")
                print("test 2")
            if choice == "hit":
                print("you hit")
                tickholder = tick
            elif choice == "stand":
                print("you stand")
                tickholder = tick
            is_player_turn = True
            player_total = get_total(player_hand)
            dealer_total = get_total(dealer_hand)
            print_game(player_hand, dealer_hand, player_total, dealer_total, is_player_turn)
        
            if player_total == 21:
                text("Blackjack! You win!", 500,800)
            elif player_total > 21:
                print("Bust! You lose!", 500, 800)
            if is_player_turn:
                if choice == "hit":
                    player_hand.append(deck.pop(0))
                elif choice == "stand":
                    is_player_turn = False
            else:
                dealer_hand, dealer_total = play_dealer_turn(deck, dealer_hand)
                if dealer_total > 21:
                    print_game(player_hand, dealer_hand, player_total, dealer_total, is_player_turn)
                    text("Dealer bust! You win!", 800, 800)
                elif dealer_total >= player_total:
                    print_game(player_hand, dealer_hand, player_total, dealer_total, is_player_turn)
                    print("Dealer wins!", 800, 800)
        
            text("Thanks for playing!", 1000,1000)
        
            
        
    elif game == "Roulette":
        background(0,220,70)
        button5.Display()
        game = button5.CheckClick(game, "nav")
    else:
        background(235)
        button5.Display()
        game = button5.CheckClick(game, "nav")
