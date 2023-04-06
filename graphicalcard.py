import stddraw
from picture import Picture
from card import Card

class GraphicalCard(Card):
    "A class for displaying graphical playing cards"
    
    _rank_to_name = {'ace':'A', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6',
                    '7':'7', '8':'8', '9':'9', '10':'T', 'jack':'J', 'queen':'Q', 'king':'K'}
    _suit_to_name  ={'spades':'S','hearts':'H','clubs':'C','diamonds':'D'}
    _image_dir = './cards/'
    
    __xloc = -1
    __yloc = -1
    
    image = None
    
    def __init__(self, rank, suit):
        # Initialize the superclass.  Let it use the default rank and suit dictionaries.
        super().__init__(rank, suit)
        # Load the card based on the rank and suit.
        file_name = self._image_dir + self._suit_to_name[suit] +         self._rank_to_name[str(rank)] + ".gif"
        self._image = Picture(file_name)
        
    def draw(self, x, y):
        """
        Draw the card on the screen at the given point.
        """
        self._xloc = x
        self._yloc = y
        stddraw.picture(self._image, x, y)
        
    def clone(self):
        return GraphicalCard(self.get_rank(), self.get_suit())