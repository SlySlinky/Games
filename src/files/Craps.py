
class Craps:

    bet = 0
    theroll1 = 0
    theroll2 = 0
    #sides = [one,two,three,four,five,six]
    def __init__(self, bet):
        self.bet = bet
        
    def rolldice(self, roll1, roll2):
        one = loadImage("Die1.png")
        two = loadImage("Die2.png")
        three = loadImage("Die3.png")
        four = loadImage("Die4.png")
        five = loadImage("Die5.png")
        six = loadImage("Die6.png")
        one.resize(100,100)
        two.resize(100,100)
        three.resize(100,100)
        four.resize(100,100)
        five.resize(100,100)
        six.resize(100,100)
        if roll1 == 1:
            image(one,width/2-150,height/2)
        elif roll1 == 2:
            image(two,width/2-150,height/2)     
        elif roll1 == 3:
            image(three,width/2-150,height/2)     
        elif roll1 == 4:
            image(four,width/2-150,height/2)        
        elif roll1 == 5:
            image(five,width/2-150,height/2)     
        elif roll1 == 6:
            image(six,width/2-150,height/2)       
        if roll2 == 1:
            image(one,width/2+50,height/2)
        elif roll2 == 2:
            image(two,width/2+50,height/2)          
        elif roll2 == 3:
            image(three,width/2+50,height/2)       
        elif roll2 == 4:
            image(four,width/2+50,height/2)    
        elif roll2 == 5:
            image(five,width/2+50,height/2)            
        elif roll2 == 6:
            image(six,width/2+50,height/2) 
        self.theroll1 = roll1
        self.theroll2 = roll2
