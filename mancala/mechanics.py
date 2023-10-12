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
        if (not 0) not in board[int(self.turn)]: # if the row is all zeros
            player_end = self.players[int(self.turn)].end
    
            if player_end == True or ((not 0) not in board[int( not self.turn)] ): # if the player has previously skipped a turn or nothing that ISN'T zero is in the other row, end the game
                self.win_check()
            
            player_end= True #changing the player's end condition
            self.turn = not self.turn
            return
    
        if(not self.turn): # fancy way of 'self.turn == False'
            board = self.reverseGrid(board) 

        player.distribute(hole, board) #board would be reversed for player 2

        if(not self.turn): # re-reverse grid
            board = self.reverseGrid(board) 
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

        onside = True #iterating on original row 
        num = board[0][hole] #board [0] refers to moving player's row
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
            
            
        self.bonus(board) 
        return board   

    def bonus(self, board) -> [[int]]: #check for extra oppurtunities to score
        for i in board[1]:
            if i == 2 or i == 3:
                self.score += i
                i = 0
