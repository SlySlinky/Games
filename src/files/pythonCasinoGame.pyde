#John Sundberg and Dallin Morgan

from Button import Button
from Craps import Craps
from Blackjack import Blackjack
from CardHolder import CardHolder
from Slots import Slots
tick = 0
playagain = Button(440,250,750,700,"Playagain")
button1 = Button(440,250,750,700,"Roulette")
button2 = Button(440,250,115,435,"Blackjack")
button3 = Button(440,250,750,260,"Craps")
button4 = Button(380,350,1445,335,"Slots")
button5 = Button(100,100,50,50,"home")
help = Button(100,100,1750,100, "Help")
spin = Button(200,200,500,500,"spin")
crepe = Craps(100)
slug = Slots(100)
handel = loadImage("HandleDown.png")
failure = Blackjack(10)
hit = Button(200,200,500,500,"hit")
stand = Button(200,200,900,500,"stand")
roll = Button(200,200,900,500,"roll")
thisthing = CardHolder()
tickholder = 0
balance = 1000
game = "home"
sect = ""
buttondown = loadImage("ButtonDown.png")
slots = loadImage("SlotMachine.png")
bgslots = loadImage("BGSlots.png")
bgbj = loadImage("BlackjackBackground.png")
bgrou = loadImage("Roulette.png")
money = loadImage("Money.png")
thecurrentmoneytick = 0
def setup():
    #fullScreen()
    global mainScreen
    frameRate(60)
    size(1920,1080)
    mainScreen = loadImage("CasinoMenuTemplate.png")
    mainScreen.resize(1920,1080)

    image(mainScreen,0,0)

        
def draw():
    global money, slug, spin, buttondown, bgbj, bgrou, playagain, help, handel, balance, thecurrentmoneytick, failure, tick, crepe, mainScreen, crapsboard, roll, sect, button1, button2, button3, button4, button5, game, hit, stand, tickholder, slots, bgslots
    tick = tick + 1
    print(frameRate)
    if tick == 1:
        slug = Slots(100)
        balance = 1000
        handel = loadImage("HandleDown.png")
        handel.resize(80,320)

        crapsboard = loadImage("Craps.png")
        crapsboard.resize(width+5,height)
        mainScreen = loadImage("CasinoMenuTemplate.png")
        slots = loadImage("SlotMachineBlank.png")
        bgslots = loadImage("BGSlots.png")
        money = loadImage("Money.png")
        bgbj = loadImage("BlackjackBackground.png")
        bgrou = loadImage("Roulette.png")
        buttondown = loadImage("ButtonDown.png")
        money.resize(130,45)
        buttondown.resize(180, 180)
        bgslots.resize(1920,1080)
        bgbj.resize(1920,1080)
        bgrou.resize(1920,1080)
        mainScreen.resize(1920,1080)
        button1 = Button(440,250,750,700,"Roulette")
        button2 = Button(440,250,115,435,"Blackjack")
        button3 = Button(440,250,750,260,"Craps")
        button4 = Button(380,350,1445,335,"Slots")   
        button5 = Button(100,100,60,70,"home")
        playagain = Button(220,275,100,400,"Playagain")
        help = Button(100,100,1750,100, "Help")
        spin = Button(80,320,436,360,"spin")
        hit = Button(300,200,width/2-550,height/2+250,"hit")
        stand = Button(300,200,width/2+385,height/2+250,"stand")
        roll = Button(300,200,width/2-150,height/2,"roll")
        sect = "home"
    if game == "home":
        image(mainScreen,0,0)      

        fill(164,117,73)
        textSize(50)
        rect(60,200,280,65)
        fill(255)
        text(": "+str(balance),210,247)
        image(money,70,210)
        fill(0)
        button1.Display()
        button2.Display()
        button3.Display()
        button4.Display()
        help.Display()
        failure.reset()
        game = button1.CheckClick(game, "nav")
        game = button2.CheckClick(game, "nav")
        game = button3.CheckClick(game, "nav")
        game = button4.CheckClick(game, "nav")
        game = help.CheckClick(game, "nav")
        tickholder = tick
        sect = "start"
        if game == "Blackjack":
            if balance < 50:
                game = "home"
            else:
                balance = balance - 50
                
    elif game == "Help":
        background(102,0,204)

        fill(215)
        rect(60,70,100,100)
        button5.Display()
        fill(255)
        textSize(30)
        text("General Rules:", 200, 200)
        textSize(20)
        text("All games charge you upon starting the game. Blackjack costs $50 to play, and, if you win, you get anywhere between $25 and $100 in addition to getting back the $50 you paid.\nSlots costs $10, and if you win you get anywhere between 100 and 2000.\nIf you leave the game and then go back it will charge you again and reset the game.  ",200,250)
        textSize(30)
        text("Blackjack Rules:",200,395)
        textSize(20)
        text("Blackjack is usually played at a table of 2-7 players and uses one to eight 52-card decks. All number cards (2-10) score the value indicated on them.\n The face cards (Jack, Queen, King) score 10 points and Ace can either be treated as 1 or 11.\n all players are dealt two cards face-up in front of their respective betting positions. The dealer receives two cards, one face-up and another face-down.\n Starting to the left of the dealer, each player is given a chance to draw more cards. The players can either hit or stand. If the player calls out Hit, they are given an extra card.\n They can then either call out HIT again, or STAND if they do not wish to draw any more cards. \nThe player can HIT as many times as they wish, but have to aim not to bust (exceed a total of 21).\nIf the player busts, they immediately lose\nAfter each player has played and either stood or busted, the dealer takes their turn. They can, again, either HIT or STAND. \nIf the dealer's hand exceeds 21, all players who didn't bust win immediately. Those who did bust lose to the dealer.\nIf the dealer reaches a valid hand the cards are totalled and each player\'s hand is compared to the dealer\'s. If the player scored higher than the dealer they win.\nA perfect hand combines an ace with a 10, Jack, Queen or King and is known as a Blackjack.", 200,450)
        game = button5.CheckClick(game, "nav")
        fill(0)
        
    elif game == "Craps":
        background(0,100,50)
        image(crapsboard,0,0)
        fill(164,117,73)
        textSize(50)
        rect(60,200,280,65)
        fill(255)
        text(": "+str(balance),210,247)
        image(money,70,210)
        fill(0)
        fill(215)
        rect(60,70,100,100)

        button5.Display()
        game = button5.CheckClick(game, "nav")
        if sect == "start":
                fill(215)
                rect(width/2-150,height/2,299,198)
                roll.Display()
                choice = roll.CheckClick("roll","slct")
                if choice == "roll":
                    sect = "roll"
                    tickholder = tick
            
        elif sect == "roll":
            roll1 = int(random(1,7))
            roll2 = int(random(1,7))
            print(roll1,roll2)
            if tick < 30 + tickholder:
                
                crepe.rolldice(roll1,roll2)
            else:
                crepe.rolldice(crepe.theroll1,crepe.theroll2)
            
    elif game == "Blackjack":
        background(0,115,124)
        image(bgbj,0,0)
        fill(215,175)
        rect(1400,60,515,300)
        fill(164,117,73)
        textSize(50)
        rect(60,200,280,65)
        fill(255)
        text(": "+str(balance),210,247)
        image(money,70,210)
        fill(0)
        is_player_turn = True
        player_total = failure.get_total(failure.player_hand)
        dealer_total = failure.get_total(failure.dealer_hand)
        failure.print_game(player_total,dealer_total,is_player_turn)
        displayTheCards() 
        fill(215)
        rect(60,70,100,100)
        button5.Display()
        game = button5.CheckClick(game, "nav")
        
        if tick > tickholder + 30 and sect != "claimmoney" and sect != "dealerturn":
            fill(215)
            rect(width/2-550,height/2+250,299,198)
            rect(width/2+385,height/2+250,299,198)
            hit.Display()
            stand.Display()

            choice = hit.CheckClick("hit","slct")

            if choice == "":
                choice = stand.CheckClick("stand","slct")
            if choice == "hit":
                print("you hit")
                tickholder = tick
                failure.player_hand.append(failure.deck.pop(int(random(1,len(failure.deck)))))
            elif choice == "stand":
                print("you stand")
                tickholder = tick
                dealer_total = failure.get_total(failure.dealer_hand)
                sect = "dealerturn"
        if player_total > 20 and sect != "claimmoney":
            sect = "dealerturn"
            dealer_total = failure.get_total(failure.dealer_hand)
        if sect == "dealerturn":
            while dealer_total < 17:
                failure.dealer_hand.append(failure.deck.pop(int(random(1,len(failure.deck)))))
                dealer_total = failure.get_total(failure.dealer_hand)
            # text("Dealer's hand: " + str(dealer_hand), 100,100)
            fill(0)
            text("Dealer's total:" + str(dealer_total),1500,150)

            if dealer_total > 21 and player_total <= 21:
                text("Dealer bust! Player wins!", 1400,250)
                balance = balance + 100 + 5*int(random(5,20))
                sect = "claimmoney"
            elif dealer_total <= 21 and dealer_total > player_total:
                text("Dealer wins!!", 1500,250)
            elif player_total <= 21 and player_total > dealer_total:
                text("Player wins!!", 1500,250)
                balance = balance + 100 + 5*int(random(5,20))
                if player_total == 21:
                    textSize(30)
                    text("BLACKJACK!", width/2, height/2)
            elif player_total > 21 and dealer_total <= 21:
                text("Player bust! Dealer wins!!", 1400,250)
                text("You fool!", 250,900)
            elif dealer_total == 21:
                text("Dealer gets Blackjack!!", 1425,300)
                if dealer_total > player_total  or dealer_total > 21 and player_total > 21:
                    text("Dealer wins!!", 1500,250)
                elif dealer_total == player_total:
                    text("It's a tie!!", 1500,250)
                    textSize(270)
                    text("BLACKJACK!", width/2-600, height/2+100)
                    textSize(50)
                    balance = balance + 50
            elif dealer_total == player_total:
                text("It's a tie!!", 1500,250)
                balance = balance + 50
            sect = "claimmoney"
    
    
        if sect == "claimmoney":
            playagain.Display()
            choice = playagain.CheckClick("Playagain","slct")
            if choice == "Playagain":
                sect = "pushbutton"
                tickholder = tick
                balance = balance - 50
                failure.reset()
            fill(0)
            text("Dealer's total:" + str(dealer_total),1500,150)
            if dealer_total > 21 and player_total <= 21:
                text("Dealer bust! Player wins!", 1400,250)
            elif dealer_total < 21 and dealer_total > player_total or dealer_total > 21 and player_total > 21:
                text("Dealer wins!!", 1500,250)
            elif player_total <= 21 and player_total > dealer_total:
                if player_total == 21:
                    textSize(270)
                    text("BLACKJACK!", width/2-600, height/2+100)
                    textSize(50)
                text("Player wins!!", 1500,250)
            elif player_total > 21 and dealer_total <= 21:
                text("Player bust! Dealer wins!!", 1400,250)
                text("You fool!", 250,900)
            elif dealer_total == 21:
                text("Dealer gets Blackjack!!", 1425,300)
                if dealer_total > player_total or dealer_total > 21 and player_total > 21:
                    text("Dealer wins!!", 1500,250)
                elif dealer_total == player_total:
                    text("It's a tie!!", 1500,250)
                    textSize(270)
                    text("BLACKJACK!", width/2-600, height/2+100)
                    textSize(50)           
            elif dealer_total == player_total:
                text("It's a tie!!", 1500,250)
        elif sect == "pushbutton":
            if tick > tickholder + 4:
                sect = "start"
            else:
                image(buttondown, 123,450)
                
                
    elif game == "Roulette":
        background(0,220,70)
        image(bgrou,0,0)
        fill(164,117,73)
        textSize(50)
        rect(60,200,280,65)
        fill(255)
        text(": "+str(balance),210,247)
        image(money,70,210)
        fill(215)
        rect(60,70,100,100)
        button5.Display()
        game = button5.CheckClick(game, "nav")
        fill(0)
    else:
        background(235)
        image(bgslots,0,0)
        fill(164,117,73)
        textSize(50)
        rect(60,200,280,65)
        fill(255)
        text(": "+str(balance),210,247)
        image(money,70,210)
        fill(0)

        slots.resize(1100,1050)
        image(slots,width/2-550,0)

        if sect == "start":
            spin.Display()
            choice = spin.CheckClick("spin","slct")
            slug.spinknobs(slug.theroll1, slug.theroll2, slug.theroll3)
            if choice == "spin" and balance >= 10:
                sect = "roll"
                tickholder = tick
                balance = balance - 10
        
        elif sect == "roll":
            
            roll1 = int(random(0,11))
            roll2 = int(random(0,11))
            roll3 = int(random(0,11))
            image(handel,436,472)
            if tick < 100 + tickholder:
                slug.spinknobs(roll1, roll2, roll3)
            elif tick < 200 + tickholder:
                slug.spinknobs(slug.theroll1, roll2, roll3)
            elif tick < 300 + tickholder:
                slug.spinknobs(slug.theroll1, slug.theroll2, roll3)
                
            else:
                slug.spinknobs(slug.theroll1, slug.theroll2, slug.theroll3)
                sect = "start"
                balance = balance + slug.payme(slug.above1, slug.theroll1, slug.below1,slug.above2, slug.theroll2, slug.below2,slug.above3, slug.theroll3, slug.below3)
        # fill(255)
        # rect(500,500,1000,500)
        # fill(0)
        fill(215)
        rect(60,70,100,100)
        button5.Display()
        game = button5.CheckClick(game, "nav")
    if balance > 9995:
        balance = 9995
        
        
def displayTheCards():
    global thisthing, failure
    x = width/2-len(failure.player_hand)*50
    for i in failure.player_hand:
        thisthing.displayCard(i,x, 630)
        x = x + 100
    x = width/2-len(failure.dealer_hand)*50
    if len(failure.dealer_hand) == 1:
        x = x - 50
    for i in failure.dealer_hand:
        thisthing.displayCard(i,x, 100)
        x = x + 100
    if len(failure.dealer_hand) == 1:
        thisthing.displayCard('CardBack',x,100)
        
    
