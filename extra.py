values = "23456789TJQKA"
suits = "cdhs"
nsuits = 4
def rank_card(value, suit):
    try:
        return values.index(value) * nsuits + suits.index(suit)
    except:
        return False
rank=rank_card('4','d')

def value(rank):
    return values[rank // nsuits]
print(value(rank))