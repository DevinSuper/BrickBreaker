import pygame
import random 
import time
from pygame import mixer

pygame.init() 
mixer.init()
# Dimensions of the screen 
WIDTH, HEIGHT = 700, 600 

# Color variables
BLACK = (0, 0, 0) 
LIGHT_BLUE = (173, 216, 230)
PURPLE = (128,0,128)
WHITE = (255, 255, 255) 
GREEN = (0, 255, 0) 
RED = (255, 0, 0) 
YELLOW = (255, 255, 0)
BLUE = (0,0,255)

font = pygame.font.Font('freesansbold.ttf', 15) 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Brick Breaker") 
# to control the frame rate 
clock = pygame.time.Clock() 
FPS = 45

# Striker class (Playform)
class Striker: 
	def __init__(self, posx, posy, width, height, speed, color): 
		self.posx, self.posy = posx, posy 
		self.width, self.height = width, height 
		self.speed = speed 
		self.color = color 

		# The rect variable is used to handle the placement 
		# and the collisions of the object 
		self.strikerRect = pygame.Rect( 
			self.posx, self.posy, self.width, self.height) 
		self.striker = pygame.draw.rect(screen, 
							self.color, self.strikerRect) 

	# Used to render the object on the screen 
	def display(self): 
		self.striker = pygame.draw.rect(screen, 
							self.color, self.strikerRect) 

	# Used to update the state of the object 
	def update(self, xFac): 
		self.posx += self.speed*xFac 

		# Restricting the striker to be in between the 
		# left and right edges of the screen 
		if self.posx <= 0: 
			self.posx = 0
		elif self.posx+self.width >= WIDTH: 
			self.posx = WIDTH-self.width 

		self.strikerRect = pygame.Rect( 
			self.posx, self.posy, self.width, self.height) 

	# Returns the rect of the object 
	def getRect(self): 
		return self.strikerRect 


# Block Class (Bricks)
class Block: 
	def __init__(self, posx, posy, width, height, color): 
		self.posx, self.posy = posx, posy 
		self.width, self.height = width, height 
		self.color = color 
		self.damage = 100

		# The white blocks have the health of 200. So, 
		# the ball must hit it twice to break 
		if color == PURPLE:
			self.health = 300
		elif color == WHITE: 
			self.health = 200
		else: # if the color is green
			self.health = 100

		# The rect variable is used to handle the placement 
		# and the collisions of the object 
		self.blockRect = pygame.Rect( 
			self.posx, self.posy, self.width, self.height) 
		self.block = pygame.draw.rect(screen, self.color, 
									self.blockRect) 
	def gety(self):
		return self.posy
	
	def getx(self):
		return self.posx
	# Used to render the object on the screen if and only 
	# if its health is greater than 0 
	def display(self): 
		if self.health > 0: 
			self.brick = pygame.draw.rect(screen, 
								self.color, self.blockRect) 

	# Used to decrease the health of the block 
	def hit(self): 
		self.health -= self.damage 

	# Used to get the rect of the object 
	def getRect(self): 
		return self.blockRect 

	# Used to get the health of the object 
	def getHealth(self): #should return a number
		return self.health 

	def changeColor( self , newColor ):
		self.color = newColor


# Ball Class 
class Ball: 
	def __init__(self, posx, posy, radius, speed, color): 
		self.posx, self.posy = posx, posy 
		self.radius = radius 
		self.speed = speed 
		self.color = color 
		self.xFac, self.yFac = 1, 1

		self.ball = pygame.draw.circle( 
			screen, self.color, (self.posx, 
								self.posy), self.radius) 


	# Used to display the object on the screen 
	def display(self): 
		self.ball = pygame.draw.circle( 
			screen, self.color, (self.posx, 
								self.posy), self.radius) 
	def getballx(self):
		return self.posx

	def getbally(self):
		return self.posy
	# Used to update the state of the object 
	def update(self): 
		self.posx += self.xFac*self.speed 
		self.posy += self.yFac*self.speed 

		# Reflecting the ball if it touches 
		# either of the vertical edges 
		if self.posx <= 0 or self.posx >= WIDTH: 
			self.xFac *= -1

		# Reflection from the top most edge of the screen 
		if self.posy <= 0: 
			self.yFac *= -1

		# If the ball touches the bottom most edge of 
		# the screen, True value is returned 
		if self.posy >= HEIGHT: 
			return True

		return False

	# Resets the position of the ball 
	def reset(self): 
		self.posx = 0
		self.posy = HEIGHT 
		self.xFac, self.yFac = 1, -1

	# Used to change the direction along Y axis 
	def hit(self): 
		self.yFac *= -1

	# Returns the rect of the ball. In this case, 
	# it is the ball itself 
	def getRect(self): 
		return self.ball




# Function used to check collisions between any two entities 
def collisionChecker(rect, ball): 
	if pygame.Rect.colliderect(rect, ball): 
		return True
	return False


# Function used to populate the blocks 
def populateBlocks(blockWidth, blockHeight, horizontalGap, verticalGap): 
	listOfBlocks = [] 
	for i in range(0, WIDTH, blockWidth+horizontalGap): 
		for j in range(0, HEIGHT//2, blockHeight+verticalGap): 
			listOfBlocks.append( 
				Block(i, j, blockWidth, blockHeight, 
					random.choice([WHITE, GREEN, PURPLE]))) 
	return listOfBlocks 
	
	

# Once all the lives are over, this function waits until exit or space bar is pressed and does the corresponding action 
def gameOver(): 
	font2 = pygame.font.Font('freesansbold.ttf', 50) 
	gameOver = True
	screen.fill((0,0,0))
	pygame.draw.rect(screen, BLACK , pygame.Rect(30, 30, 60, 60))
	text = font2.render("Press Space to Restart!", True, (255,255,255))
	text_rect = text.get_rect()
	text_rect.center = (350,300)
	screen.blit(text, text_rect)
	pygame.display.update() #Updates The Screen 
	global FPS
	FPS = 45 #Reset the fps 
	print('reset')
	while gameOver:
		# Event handling 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				return False
			if event.type == pygame.KEYDOWN: 
				if event.key == pygame.K_SPACE: 
					return True
	


# Game Manager 
def main(): 
	running = True
	lives = 3
	score = 0
	counter = 0
	mult = 1
	
	scoreText = font.render("score", True, WHITE) 
	scoreTextRect = scoreText.get_rect() 
	scoreTextRect.center = (40, HEIGHT-10) 
	
	livesText = font.render("Lives", True, WHITE) 
	livesTextRect = livesText.get_rect() 
	livesTextRect.center = (120, HEIGHT-10) 

	imgpath = r"C:\Users\d3v1n\PycharmProjects\Adv-Python-Programming-23-24\Brick Breaker Game\Cutimg.png"
	image2 = pygame.image.load(imgpath)
	image2 = pygame.transform.scale(image2, (25, 25)) 
	image2rect = image2.get_rect()

	img2path = r"C:\Users\d3v1n\PycharmProjects\Adv-Python-Programming-23-24\Brick Breaker Game\Cutimg.png"
	image_10 = pygame.image.load(img2path)
	image_10 = pygame.transform.scale(image_10, (40, 40)) 

	striker = Striker(0, HEIGHT-50, 100, 20, 10, WHITE) 
	strikerXFac = 0

	ball = Ball(0, HEIGHT-150, 7, 5, RED) 

	blockWidth, blockHeight = 40, 15
	horizontalGap, verticalGap = 20, 20

	listOfBlocks = populateBlocks( 
		blockWidth, blockHeight, horizontalGap, verticalGap) 

	
	powerup = False
	powerup2 = False
	present = 0
	present2 = 0
	# Game loop 
	while running: 
		screen.fill(BLACK) 
		score_line = pygame.draw.line(screen, RED, (0,450), (700,450), width=3) #This is the score line 
		screen.blit(scoreText, scoreTextRect) 
		screen.blit(livesText, livesTextRect) 
		if powerup == True: #Display the lives+1 power-up if powerup is true
			scorerect = pygame.draw.rect(screen, (0,0,0), pygame.Rect(ballx, bally, 25, 25))
			screen.blit(image2, (ballx, bally))
			bally+=1
		if powerup2 == True: #Display the score+10 power-up if powerup2 is true
			scorerect2 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(ballx, bally, 25, 25))
			screen.blit(image_10, (ballx, bally))
			bally+=1
		
		scoreText = font.render("Score : " + str(score), True, WHITE) 
		livesText = font.render("Lives : " + str(lives), True, WHITE) 

		# If all the blocks are destroyed, then we repopulate them 
		if not listOfBlocks: 
			listOfBlocks = populateBlocks( 
				blockWidth, blockHeight, horizontalGap, verticalGap) 

		# All the lives are over. So, the gameOver() function is called 
		if lives <= 0: 
			running = gameOver() 
			while listOfBlocks: 
				listOfBlocks.pop(0) 
			lives = 3
			score = 0
			listOfBlocks = populateBlocks( 
				blockWidth, blockHeight, horizontalGap, verticalGap) 

		# Event handling 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				running = False
			if event.type == pygame.KEYDOWN: #checks if a key is pressed
				if event.key == pygame.K_a: #if the a key is pressed, the platform will move to the left
					strikerXFac = -1
				if event.key == pygame.K_d: #if the d key is pressed, the platform will move to the right
					strikerXFac = 1
				if event.key == pygame.K_SPACE: #if the space key is pressed a the right time, the powerup is collected 
					if powerup == True:
						if 465 > scorerect.y > 435: 
							lives+=1
							pygame.mixer.Channel(2).play(pygame.mixer.Sound(r"C:\Users\d3v1n\PycharmProjects\Adv-Python-Programming-23-24\Brick Breaker Game\Hearteffect.ogg"))
					if powerup2 == True:
						if 480 > scorerect2.y > 450: 
							score+=10
							pygame.mixer.Channel(3).play(pygame.mixer.Sound(r"C:\Users\d3v1n\PycharmProjects\Adv-Python-Programming-23-24\Brick Breaker Game\plusten.ogg"))
			if event.type == pygame.KEYUP: 
				if event.key == pygame.K_a or event.key == pygame.K_d: #Once you let go of the key, the platform will stop moving 
					strikerXFac = 0

		# Collision check 
		if(collisionChecker(striker.getRect(), 
							ball.getRect())): 
			ball.hit() 

		if( score > 10*mult): #Every ten points, the game will speed up 
			mult+=1 
			global FPS
			FPS += 10
		
		for block in listOfBlocks: 
			if(collisionChecker(block.getRect(), ball.getRect())): 
				ball.hit() 
				block.hit() 
				if( block.color == WHITE ):
					block.changeColor( YELLOW )
				if( block.color == PURPLE):
					block.changeColor(BLUE)
				elif( block.color == BLUE):
					block.changeColor(LIGHT_BLUE)
			
				if block.getHealth() <= 0: 					
					if( block.color == LIGHT_BLUE ):
						pygame.mixer.Channel(1).play(pygame.mixer.Sound(r"C:\Users\d3v1n\PycharmProjects\Adv-Python-Programming-23-24\Brick Breaker Game\Rockbreak.ogg"))
						score += 4
						
					if( block.color == YELLOW ):
						pygame.mixer.Channel(1).play(pygame.mixer.Sound(r"C:\Users\d3v1n\PycharmProjects\Adv-Python-Programming-23-24\Brick Breaker Game\Rockbreak.ogg"))
						score += 2
						if present == 0:
							powerup = True
							bally = ball.getbally()
							ballx = ball.getballx() 
							present += 1
							start_time = pygame.time.get_ticks()
							target_time = 10000				
						elif present == 1:
							elapsed_time = pygame.time.get_ticks() - start_time
							remaining_time = max(0, target_time - elapsed_time)
							seconds = remaining_time / 1000
							text = font.render(f"Time: {seconds} seconds", True, WHITE)
							if seconds <= 0:
								target_time = 10000
								present -= 1

					if( block.color == GREEN ):
						pygame.mixer.Channel(1).play(pygame.mixer.Sound(r"C:\Users\d3v1n\PycharmProjects\Adv-Python-Programming-23-24\Brick Breaker Game\Rockbreak.ogg"))
						score += 1
						if present2 == 0:
							powerup2 = True
							bally = ball.getbally()
							ballx = ball.getballx() 
							present2 += 1
							start_time2 = pygame.time.get_ticks()
							target_time2 = 5000				
						elif present2 == 1:
							elapsed_time2 = pygame.time.get_ticks() - start_time2
							remaining_time2 = max(0, target_time2 - elapsed_time2)
							seconds2 = remaining_time2 / 1000
							text2 = font.render(f"Time: {seconds2} seconds", True, WHITE)
							if seconds2 <= 0:
								target_time2 = 5000
								present2 -= 1
						
					listOfBlocks.pop(listOfBlocks.index(block)) 
		
			
		
		# Update 
		striker.update(strikerXFac) 
		lifeLost = ball.update() 

		if lifeLost: 
			lives -= 1
			ball.reset() 
			print(lives) 

		# Display 
		striker.display() 
		ball.display() 
		for block in listOfBlocks: 
			block.display() 
		pygame.display.update()
		clock.tick(FPS) 

if __name__ == "__main__": 
	pygame.mixer.music.load(r"C:\Users\d3v1n\PycharmProjects\Adv-Python-Programming-23-24\Brick Breaker Game\MainGameAudio.ogg") #loads the music file
	pygame.mixer.music.play(loops=-1, start=0.0) #keeps the music looping infinitely 
	main() 
	pygame.quit() 