class Board():
    def __init__(self) -> None:
        self.board = [[0,0,0,0,0,0],[0,0,0,0,0,0]]
        self.turn = True
        self.players = [Player, Player]

    def getPlayers(self) -> None:
        self.players[0] = Player(input("Player 1 Name:"))
        self.players[1] = Player(input("Player 2 Name:"))

    def reverseGrid(self, board : [[int]]) -> [[int]]:
        pholder = board[0]
        board[0] = board[1]
        board[1] = pholder
        board[0].reverse()
        board[1].reverse()
        return board
    
    def move(self, hole: int) -> None:
        board = self.board
        player = self.players[int(self.turn)] #int(bool) is either 0 or 1
        if(not self.turn): # fancy way of 'self.turn == False'
            board = self.reverseGrid(board) 
        player.distribute(hole, board) #board would be reversed for player 2

        if(not self.turn): # re-reverse grid
            board = self.reverseGrid(board) 
        return

    
    
    def win_check(self) -> None:
        pass

class Player():
    def __init__(self, name) -> None:
        #represents whole grid
        self.name = name
        self.score = 0
        self.end = False

    def getGrid(self) -> [int]:
        return self.grid

    def distribute(self, hole, board) -> [[int]]:
        onside = True #on original
        num = board[0][hole] 
        board[0][hole] = 0
        i = num
        while(num > 0):
            if i == len(self.grid): # adds score, iterate on otherside
                if onside == True: #checks if it's going into own goal
                    self.score+=1
                    num-=1
                onside=not onside #swap side
                i = 0
            board[int(onside)][i] +=1
            num-=1
            i+=1
            
            
        self.bonus() #check for extra points        

    def bonus(self) -> None:
        pass
