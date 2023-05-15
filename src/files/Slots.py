class Slots:
    
    bet = 0
    

    theroll1 = 0
    theroll2 = 0
    theroll3 = 0
    above1 = 0
    above2 = 0
    above3 = 0
    below1 = 0
    below2 = 0
    below3 = 0

        
    def __init__(self, bet):
        self.bet = bet
        
    def spinknobs(self, roll1, roll2, roll3):
        top = 440
        middle = 590
        bottom = 740
        pot = loadImage("JackPot.png")
        pot.resize(150,150)     
        self.theroll1 = roll1
        self.theroll2 = roll2
        self.theroll3 = roll3
        if roll1 > 5:
            self.above1 = roll1 - 6
            self.below1 = roll1 - 5
        elif roll1 < 5:
            self.above1 = roll1 + 5
            self.below1 = roll1 + 6
        else:
            self.above1 = roll1 + 5
            self.below1 = roll1 - 5

        if roll2 > 5:
            self.above2 = roll2 - 6
            self.below2 = roll2 - 5
        elif roll2 < 5:
            self.above2 = roll2 + 5
            self.below2 = roll2 + 6
        else:
            self.above2 = roll2 + 5
            self.below2 = roll2 - 5    
                    
        if roll3 > 5:
            self.above3 = roll3 - 6
            self.below3 = roll3 - 5
        elif roll3 < 5:
            self.above3 = roll3 + 5
            self.below3 = roll3 + 6
        else:
            self.above3 = roll3 + 5
            self.below3 = roll3 - 5      
        textSize(200)
        if roll1 == 10:
       
            image(pot,615,middle - 130)

        else:
            text(str(roll1),645,middle)
        if roll2 == 10:
       
            image(pot,795,middle - 130)

        else:
            text(str(roll2),825,middle)
        if roll3 == 10:
       
            image(pot,975,middle - 130)

        else:
            text(str(roll3),1005,middle)
        if self.above1 == 10:
       
            image(pot,615,top - 130)

        else:
            text(str(self.above1),645,top)
        if self.below1 == 10:
       
            image(pot,615,bottom - 130)

        else:
            text(str(self.below1),645,bottom)
            
        if self.above2 == 10:
       
            image(pot,795,top - 130)

        else:
            text(str(self.above2),825,top)
        if self.below2 == 10:
       
            image(pot,795,bottom - 130)

        else:
            text(str(self.below2),825,bottom)
        
        if self.above3 == 10:
       
            image(pot,975,top - 130)

        else:
            text(str(self.above3),1005,top)
        if self.below3 == 10:
       
            image(pot,975,bottom - 130)

        else:
            text(str(self.below3),1005,bottom)
                
    def payme(self, a1, a2, a3, b1, b2, b3, c1, c2, c3):
        if a2 == b2 and b2 == c2:
            if a2 == 10:
                return 2000
            elif a2 == 0:
                return 1000
            else:
                return 100 * a2
        elif (a1 == b2 and b2 == c3) or (a3 == b2 and b2 == c1):
            if a2 == 10:
                return 1500
            elif a2 == 0:
                return 750
            else:
                return 75 * b2         
        else:
             return 0   
