class CardHolder:
    cardID = loadImage("CardBack.png")
    def displayCard(self,card,x,y):
        global cardID
        cardID = loadImage(card+".png")
        cardID.resize(240, 370)
        image(cardID,x,y)
