class Queue:
    def __init__(self):
        self.__queue=[]
        self.index=-1
    def check_empty(self):
        if self.index==-1:
            return True
        return False
    def enqueue(self,card):
        self.index+=1
        self.__queue.append(card)
    def dequeue(self):
        self.index -= 1
        return self.__queue.pop(0)
    def print_queue(self):
        print(self.__queue)


values = "23456789TJQKA"
suits = "cdhs"
nsuits = 4

def rank_card(value, suit):
    try:
        return values.index(value) * nsuits + suits.index(suit)
    except:
        return False

def value(rank):
    return rank // nsuits

def initialize_decks():
    deck1=Queue()
    deck2=Queue()
    decks=[deck1,deck2]
    for deck in decks:
        input_deck=input().split()
        for card in input_deck:
            deck.enqueue(rank_card(card[0],card[1]))

    war(decks[0],decks[1])
def war(deck1,deck2):
    steps=0
    war_cards=Queue()
    while(not deck1.check_empty() and not deck2.check_empty() and steps<100000):
        steps+=1
        card1=deck1.dequeue()
        card2=deck2.dequeue()
        war_cards.enqueue(card1)
        war_cards.enqueue(card2)
        if value(card1)>value(card2):
            clear_queue(war_cards,deck1)
        elif value(card2)>value(card1):
            clear_queue(war_cards,deck2)
    if deck2.check_empty() and not deck1.check_empty():
        print("a wins in", steps,"steps")
    elif deck1.check_empty() and not deck2.check_empty():
        print("b wins in",steps,"steps")
    elif deck1.check_empty() and deck2.check_empty():
        print("Match has been tied in ",steps," steps")
    else:
        print("maximum limit reached")
def clear_queue(queue1,queue2):
    while not queue1.check_empty():
        queue2.enqueue(queue1.dequeue())

initialize_decks()