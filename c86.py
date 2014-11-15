values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
suits = ['H','D,','S','C']

class Hand():
    def __init__(self, ID, cards):
        cards = cards.split()
        self.ID = ID
        self.value = []
        self.suit = []
        for card in cards:
            self.value.append(card[0])
            self.suit.append(card[1])
        zipped = zip(self.value, self.suit)
        zipped = sorted(zipped, key=lambda x:values.index(x[0]), reverse=True)
        self.value, self.suit = zip(*zipped)
        
    def __repr__(self):
        p = self.ID + ','
        for i in range(len(self.value)):
            p+= self.value[i] + self.suit[i] + ' '
        return p[:-1]

    def __len__(self):
        return len(self.value)

def winner(n):
    if n == 1:
        return 'left'
    elif n == 2:
        return 'right'
    else:
        return 'none'

def highcard(left,right):
    for i in range(5):
        if values.index(left.value[0]) > values.index(right.value[0]):
            return 'left'
        elif values.index(left.value[0]) < values.index(right.value[0]):
            return'right'
    else:
        return 'none'

def f(test='6D 7H AH 7S QC 6H 2D TD JD AS'):
    test = test.rstrip()
    left = Hand(1, test[:len(test)//2].rstrip())
    right = Hand(2, test[len(test)//2:].lstrip())
    game = [left,right]
    result = 0
    #Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    for hand in game:
        suit = hand.suit[0]
        for i in range(5):
            if hand.value[i] != values[-i-1] or hand.suit[i] != suit:
                break
        else:
            result+= hand.ID
    if result:
        return winner(result)
    #Straight Flush: All cards are consecutive values of same suit.
    for hand in game:
        suit = hand.suit[0]
        value = values.index(hand.value[0])
        if value > 3:
            for i in range(5):
                if hand.value[i] != values[value-i] or hand.suit[i] != suit:
                    break
            else:
                result+= hand.ID
    if result == 3:
        return highcard(left,right)
    if result:
        return winner(result)
    #Four of a Kind: Four cards of the same value.
    for hand in game:
        if sum(hand.value[i] == hand.value[1] for i in range(5)) == 4:
            result+= hand.ID
    if result == 3:
        highleft = values.index(left.value[1])
        highright= values.index(right.value[1])
        if highleft > highright:
            return 'left'
        elif highleft < highright:
            return 'right'
        else:
            return 'none'
    if result:
        return winner(result)
    #Full House: Three of a kind and a pair.
    for hand in game:
        l = sum(hand.value[i] == hand.value[1] for i in range(3))
        r = sum(hand.value[i] == hand.value[3] for i in range(2,5))
        if l + r == 5:
            result+= hand.ID
    if result == 3:
        highleft = values.index(left.value[2])
        highright= values.index(right.value[2])
        if highleft > highright:
            return 'left'
        elif highleft < highright:
            return 'right'
        else:
            return 'none'
    if result:
        return winner(result)    
    #Flush: All cards of the same suit.
    for hand in game:
        suit = left.suit[0]
        for i in range(5):
            if left.suit[i] != suit:
                break
        else:
            result+= hand.ID
    if result == 3:
        return highcard(left,right)
        #in reality there could be flush and any non-straight following...
    if result:
        return winner(result)
    #Straight: All cards are consecutive values.
    for hand in game:
        value = values.index(hand.value[0])
        if value > 3:
            for i in range(5):
                if hand.value[i] != values[value-i]:
                    break
            else:
                result+= hand.ID
    if result == 3:
        return highcard(left,right)
    if result:
        return winner(result)
    #Three of a Kind: Three cards of the same value.
    for hand in game:
        for j in range(3):
            if sum(hand.value[i] == hand.value[j] for i in range(5)) == 3:
                result+= hand.ID
                break
    if result == 3:
        highleft = values.index(left.value[2])
        highright= values.index(right.value[2])
        if highleft > highright:
            return 'left'
        elif highleft < highright:
            return 'right'
        else:
            return 'none'
    if result:
        return winner(result)
    #Two Pairs: Two different pairs.
    for hand in game:
        if sum(left.value[j] == left.value[j+1] for j in range(4)) == 2:
            result+= hand.ID
    if result == 3:#need to deal with tiebreaker on the two pair!!!!****
        highleft = values.index(left.value[0])
        highright= values.index(right.value[0])
        if highleft > highright:
            return 'left'
        elif highleft < highright:
            return 'right'
        else:
            return 'none'
    if result:
        return winner(result)
    #One Pair: Two cards of the same value.
    for hand in game:
        for i in range(4):
            if left.value[i] == left.value[i+1]:
                result+= hand.ID
                break
    if result == 3:#need to deal with tiebreaker on the pair!!!!****
        highleft = values.index(left.value[0])
        highright= values.index(right.value[0])
        if highleft > highright:
            return 'left'
        elif highleft < highright:
            return 'right'
        else:
            return 'none'
    if result:
        return winner(result)
    #High Card: Highest value card.
    return highcard(left,right)
