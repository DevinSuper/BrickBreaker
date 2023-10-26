class Board():
    def __init__(self) -> None:
        self.board = [[4,4,4,4,4,4],[4,4,4,4,4,4]]
        self.turn = True
        self.players = [Player, Player]

    def getPlayers(self) -> None:
        self.players[0] = Player(input("Player 1 Name:"))
        self.players[1] = Player(input("Player 2 Name:"))

    def reverseGrid(self, board : [[int]], hole ) -> ([[int]], int): 
        pholder = board[0]
        board[0] = board[1]
        board[1] = pholder
        board[0].reverse()
        board[1].reverse()
        newhole = 5-hole
        return board, newhole
    
    def move(self, hole: int) -> None:
        board = self.board
        player = self.players[int(self.turn)] #int(bool) is either 0 or 1
        if board[int(self.turn)] == [0,0,0,0,0,0]: # if the row is all zeros
            player_end = self.players[int(self.turn)].end
    
            if player_end == True or (board[int(not self.turn)] == [0,0,0,0,0,0] ): # if the player has previously skipped a turn or the other row has all zeros, try to end the game
                self.win_check()
            
            player_end= True #changing the player's end condition
            self.turn = not self.turn
            return
    
        if(not self.turn): # fancy way of 'self.turn == False'
            board, hole = self.reverseGrid(board, hole) 

        player.distribute(hole, board) #board would be reversed for player 2

        if(not self.turn): # re-reverse grid
            board,hole = self.reverseGrid(board,hole) 
        self.turn = not self.turn

    
    
    def win_check(self) -> str:
        if self.players[0].score > self.players[1].score:
            return self.players[0].name+" wins"
        elif self.players[0].score == self.players[1].score:
            return "Tie"
        else:
            return self.players[1].name+" wins"


class Player():
    def __init__(self, name) -> None:
        #represents whole grid
        self.name = name
        self.score = 0
        self.end = False

    def distribute(self, hole, board) -> [[int]]:
        self.end = False # if the player had been skipped previously, this resets the count of being skipped twice

        onside = False #iterating on original row 
        num = board[0][hole] #board [0] refers to moving player's row
        board[0][hole] = 0
        i = hole-1
        while(num > 0):
            if i == -1: # adds score, iterate on otherside
                if onside == False: #checks if it's going into own goal
                    self.score+=1
                    num-=1
                onside=not onside #swap side
                i = 5
                if num == 0:
                    break
            board[int(onside)][i] +=1
            num-=1
            i-=1
            
            
            
        self.bonus(board) 
        return board   

    def bonus(self, board) -> [[int]]: #check for extra oppurtunities to score
        for i in board[1]:
            if i == 2 or i == 3:
                self.score += i
                i = 0
