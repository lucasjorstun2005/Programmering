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
    och inte bara gör slumpmässiga drag som inte har någon tanke bakom det'''
    pass



player1 = HumanPlayer('X')
player2 = HumanPlayer('O')