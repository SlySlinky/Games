class Button:
    l = 0.0
    w = 0.0
    x = 0.0
    y = 0.0
    typeholder = ""
    button = loadImage("Blackjack.png")
    rollover = loadImage("Rollover.png")
    
    def __init__(self, l, w, x, y, type):
        self.l = l
        self.w = w
        self.x = x
        self.y = y
        self.rollover = loadImage("Rollover.png")
        if type == "Blackjack":
            self.button = loadImage("Blackjack.png")
        elif type == "Roulette":
            self.button = loadImage("Roulette.png")
        elif type == "Craps":
            self.button = loadImage("Craps.png")
        elif type == "Playagain":
            self.button = loadImage("ButtonUp.png")
            self.rollover = loadImage("ButtonUp.png")

        elif type == "home":
            self.button = loadImage("Home.png")
        elif type == 'Help':
            self.button = loadImage("Question.png")
            self.rollover = loadImage("CircleRollover.png")
        
        elif type == "hit":
            self.button = loadImage("Hit.png")
        elif type == "stand":
            self.button = loadImage("Stand.png")
        elif type == "roll":
            self.button = loadImage("Roll.png")
        elif type == "spin":
            self.button = loadImage("HandleUp.png")
            self.rollover = loadImage("HandleUp.png")
        elif type == "Slots":
            self.button = loadImage("SlotMachine.png")
            self.rollover = loadImage("MachineRollover.png")
        self.typeholder = type

    def Display(self):
        self.button.resize(self.l,self.w)
        image(self.button,self.x,self.y)
        if self.l+self.x > mouseX and mouseX > self.x and self.w+self.y > mouseY and mouseY > self.y:
            self.rollover.resize(self.l,self.w)  
            image(self.rollover, self.x, self.y)
    def CheckClick(self, screen, btype):

        if self.l+self.x > mouseX and mouseX > self.x and self.w+self.y > mouseY and mouseY > self.y and mousePressed:
            if btype == "nav":
                return self.typeholder
            elif btype == "slct":
                return screen
        else:
            if btype == "nav":
                return screen
            elif btype == "slct":
                return ""
