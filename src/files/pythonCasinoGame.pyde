#John Sundberg and Dallin Morgan

from Button import Button
from Craps import Craps
from Blackjack import Blackjack
tick = 0

button1 = Button(440,250,750,700,"Roulette")
button2 = Button(440,250,115,435,"Blackjack")
button3 = Button(440,250,750,260,"Craps")
button4 = Button(380,350,1445,335,"Slots")
button5 = Button(100,100,50,50,"home")
crepe = Craps(100)
failure = Blackjack(10)
hit = Button(200,200,500,500,"hit")
stand = Button(200,200,900,500,"stand")
roll = Button(200,200,900,500,"roll")
tickholder = 0
game = "home"
sect = ""

def setup():
    fullScreen()
    global mainScreen
    frameRate(60)
    size(1920,1080)
    mainScreen = loadImage("CasinoMenuTemplate.png")
    mainScreen.resize(1920,1080)

    image(mainScreen,0,0)

        
def draw():
    global failure, tick, crepe, mainScreen, crapsboard, roll, sect, button1, button2, button3, button4, button5, game, hit, stand, tickholder
    tick = tick + 1
    print(frameRate)
    if tick == 1:
        crapsboard = loadImage("Craps.png")
        crapsboard.resize(width+5,height)
        mainScreen = loadImage("CasinoMenuTemplate.png")
        mainScreen.resize(1920,1080)
        button1 = Button(440,250,750,700,"Roulette")
        button2 = Button(440,250,115,435,"Blackjack")
        button3 = Button(440,250,750,260,"Craps")
        button4 = Button(380,350,1445,335,"Slots")   
        button5 = Button(100,100,50,50,"home")
        hit = Button(300,200,width/2-400,height/2,"hit")
        stand = Button(300,200,width/2+100,height/2,"stand")
        roll = Button(300,200,width/2-150,height/2,"roll")
        sect = "home"
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
        sect = "start"
    elif game == "Craps":
        background(0,100,50)

        image(crapsboard,0,0)
        button5.Display()
        game = button5.CheckClick(game, "nav")
        if sect == "start":
            roll.Display()
            choice = roll.CheckClick("roll","slct")
            if choice == "roll":
                sect = "roll"
                tickholder = tick
        
        elif sect == "roll":
            roll1 = int(random(1,7))
            roll2 = int(random(1,7))
            print(roll1,roll2)
            if tick < 60 + tickholder:
                
                crepe.rolldice(roll1,roll2)
            else:
                crepe.rolldice(crepe.theroll1,crepe.theroll2)
            
    elif game == "Blackjack":
        background(0,220,70)
        is_player_turn = True
        player_total = failure.get_total(failure.player_hand)
        dealer_total = failure.get_total(failure.dealer_hand)
        failure.print_game(player_total,dealer_total,is_player_turn)
        button5.Display()
        game = button5.CheckClick(game, "nav")
        if tick > tickholder + 60: 
            hit.Display()
            stand.Display()
            choice = hit.CheckClick("hit","slct")
            if choice == "":
                choice = stand.CheckClick("stand","slct")
            if choice == "hit":
                print("you hit")
                tickholder = tick
            elif choice == "stand":
                print("you stand")
                tickholder = tick
                
        
    elif game == "Roulette":
        background(0,220,70)
        button5.Display()
        game = button5.CheckClick(game, "nav")
    else:
        background(235)
        button5.Display()
        game = button5.CheckClick(game, "nav")
