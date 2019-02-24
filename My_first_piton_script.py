'''
Most likely this will be file that contains all the objects or something like that

this document will contain functions for gameEngine, that are not game engine itselves

'''


def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()




def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")