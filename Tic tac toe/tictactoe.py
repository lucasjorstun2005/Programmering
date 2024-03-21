import sys

class Game(object):
    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.turn = 0

class Player(object):
    pass

class HumanPlayer(Player):
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self):
        move = 0
        while move == 0:
            print("Det är din tur " + self.symbol)
    
class ComputerPlayer(Player):
    '''Kan läggas till funktion för eventuell dator 
    men då måste den vara smart nog att den faktiskt är intressant att spela mot
    och inte bara gör slumpmässiga drag som inte har någon tanke bakom det. Med det menar jag att datorspelaren
    försöker blockera människospelaren från att vinna, samt att datorn själv försöker vinna'''
    pass

class Board(object):
    # En lista med rutor
    def __init__(self):
        self.tiles = range(9)
    
    # Organiserar rader så att det är tre rutor i varje rad
    def organize_board(self):
        board = [self.tiles[0], self.tiles[1], self.tiles[2]], [self.tiles[3], self.tiles[4], self.tiles[5]], [self.tiles[6], self.tiles[7], self.tiles[8]]

        return board
    
    def print_board(self):
        board = self.organize_board()

        # Printar ut raderna för brädet
        for row in board:
            sys.stdout.write('|')
            for tile in row:
                sys.stdout.write(str(tile) + '|')
            sys.stdout.write('\n')

class Move(object):
    pass

player1 = HumanPlayer('X')
player2 = HumanPlayer('O')

my_board = Board()
my_board.print_board()
