import collections

Card = collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]


# List Comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for size in sizes for color in colors]

# Generator Expression

for tshirts in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirts)

# match / case

metro_areas = [
    ('','','',('','',)),
    ('','','',('','',)),
    ('','','',('','',)),
    ('','','',('','',)),
    ('','','',('','',))
]

def match_case():
    print(f'{"":15} | {'latitud':>9} | {'longitude':>9}')
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')