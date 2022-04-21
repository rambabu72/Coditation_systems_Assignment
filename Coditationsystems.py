class Coditation:

    def __init__(self):
        self.numberOfColumns = 7
        self.numberOfLines = 6
        self.board = [ [ '  ' for _ in range( self.numberOfColumns)] for _ in range(self.numberOfLines) ]

    def displayBoard(self):
        """display the board like table format or box format """
        for i, line in enumerate(self.board):
            # Printing the line separators
            print("_" * self.numberOfColumns * 4)
            # Printing the line
            print(*line, sep=' |')
            # Printing numbers
        print('   '.join(str(x) for x in range(self.numberOfColumns)))

    def isAvailable(self, line, column):
        """this is check the column is available or not"""
        
        if line[column] == '  ':
            return True
        return False

    def player_choice(self,nextplayer):
        """ Select the column where do you want to put your piece"""
        
        choice = int(input(f"{nextplayer} Please select an empty space between 0 and 6 : "))
        while self.board[0][choice] != '  ':
            choice = int(input("This column is full. Please choose between 0 and 6 : "))
        return choice

    def player_input(self):
        """ Select Colour by player which colour do you want"""
        
        player1 = input("player Do you want Red or Yellow (r or y) : ")
        while True:
            if player1.upper() == 'R':
                player2='Y'
                print("You've choosen " + player1 + ". Player 2 will be " + player2)
                # print("The First Table Move Option is given to Player : ")
                return player1.upper(),player2
                
            elif player1.upper() == 'Y':
                player2='R'
                print("You've choosen " + player1 + ". Player 2 will be " + player2)
                # print("The First Table Move Option is given to Player : ")
                return player1.upper(),player2
            else:
                player1 = input("Please pick a marker 'R' or 'Y' : ")

    def checkLines(self, marker, board=None):
        if board is None:
            board=self.board
        # Checkin lines
        for line in board:
            for i in range(0,len(line)):
                if i < len(line) - 3:
                    if line[i] == line[i+1] == line[i+2] == line[i+3] == " " + marker:
                        return True

    def checkDiags(self, marker):
        diagBoard = []
        for i, line in enumerate(self.board):
            for idx, item in enumerate(line):
                # Find of there is some marker
                if item == ' ' + marker:
                    diagBoard.append(int(str(i)+str(idx)))

        for item in diagBoard:
            if int(item) + 11 in diagBoard and int(item) + 22 in diagBoard and int(item) + 33 in diagBoard:
                return True

        for item in reversed(diagBoard):
            if int(item) - 9 in diagBoard and int(item) - 18 in diagBoard and int(item) - 27 in diagBoard:
                return True

    def generateReversedBoard(self):
        """this command is used to reverse the board"""
        reversedBoard = []
        for line in self.board:
            for index, item in enumerate(line):
                try:
                    reversedBoard[index].append(item)
                except:
                    reversedBoard.append([])
                    reversedBoard[index].append(item)
        return reversedBoard

    def play(self, playercolumn, marker):
        for item in reversed(self.board):
            if self.isAvailable(item, playercolumn):
                item[playercolumn] = " " + marker
                return True
        return False

c = Coditation()

# First while lopp init
game = True
while game:
    # Choose your marker
    players = c.player_input()
    # Display the board
    c.displayBoard()
    # Second while loop init
    win = False
    i = 1
    while not win:
        # Start Playing
        if i % 2 == 0:
            currentPlayer = "Player1"
            nextplayer = "Player2"
            marker = players[1]
        else:
            currentPlayer = "Player2"
            nextplayer = "Player1"
            marker = players[0]
        # Player to choose where to put the mark
        position = c.player_choice(nextplayer)
        if not c.play(position, marker):
            print(f"Column {position} full")

        # Generate the reversed board
        reversedBoard = c.generateReversedBoard()
        # Check if won
        if c.checkLines(marker) or c.checkLines(marker, reversedBoard) or c.checkDiags(marker):
            # update the win to exit the second while loop
            win = True
            c.displayBoard()
            print(f"Game won by {nextplayer}")
            # Ask for replay. 
            # If no, change the first loop game = True to False
            # If yes, reset our class with fresh new datas
            replay = input("Do you want to play again (Y/N) ? ")
            if replay.lower() == 'n':
                game = False
                print("Game ended !")
            else:
                c = Coditation()
            break
        c.displayBoard()
        i += 1