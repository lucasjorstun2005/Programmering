import sys

class Game(object):
    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.turn = 0

    def greet_user(self, currplayer):
        print("Det är din tur " + currplayer.symbol)

    def play(self):
        flag = False

        while flag == False:
            currplayer = self.players[self.turn]

            self.board.print_board()

            self.greet_user(currplayer)

            move = Move(self.board, currplayer)
            player_move = move.ask_move()

            self.board.tiles[player_move] = currplayer.symbol

            winner = self.check_win(currplayer.symbol)

            if winner != False:
                self.game_over(winner)
                flag = True
            else:
                self.turn = 1 - self.turn
            
    def check_win(self, player_symbol):
        tiles = self.board.tiles

        for i in range(3):
            if tiles[i] == player_symbol and tiles[i+3] == player_symbol and tiles[i+6] == player_symbol:
                return player_symbol
            elif tiles[(i*3)] == player_symbol and tiles[(i*3) + 1] == player_symbol and tiles[(i*3) + 2] == player_symbol:
                return player_symbol

            if tiles[0] == player_symbol and tiles[4] == player_symbol and tiles[8] == player_symbol:
                return player_symbol
            elif tiles[2] == player_symbol and tiles[4] == player_symbol and tiles[6] == player_symbol:
                return player_symbol

        return False
    def game_over(self, player_symbol):
        self.board.print_board()
        print("Spelet är slut! Vinnaren är " + player_symbol + "!")

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
        self.tiles = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    
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
    def __init__(self, board, player):
        self.board = board
        self.player = player
    
    def ask_move(self):
        flag = False
        possible_moves = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

        while flag != True:
            move = input("Vänligen ange numret dit du vill flytta " + self.player.symbol + ": ")

            # Kolla efter om använder har angett ett nummer mellan 0-8, om så, konvertera det till int
            if move in possible_moves:
                move = int(move)
            # Annars, be användaren att ange ett nytt nummer
            else:
                print("Vänligen ange ett nummer mellan 0-8: ")
                return self.ask_move()
            
            if move == self.board.tiles[move]:
                print("Det har redan gjorts ett drag här, försök igen:")
                return self.ask_move()
            
            return move



player1 = HumanPlayer('X')
player2 = HumanPlayer('O')

my_board = Board()

my_game = Game(my_board, player1, player2)
my_game.play()
