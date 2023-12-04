import pygame 

pygame.init()
#Screen 
screen = pygame.display.set_mode((750,500)) #Initialize the Window  
pygame.display.set_caption("Tutorial Screen") #Window Name
screen.fill((210,180,140)) #Set The Window Color 
pygame.display.flip() #Updates the screen 

image_path = r"C:\Users\d3v1n\PycharmProjects\Adv-Python-Programming-23-24\Brick Breaker Game\brickbreaktut.png"# Replace with the path to your image file
image = pygame.image.load(image_path)
image = pygame.transform.scale(image, (750, 550))  # Resize the image to fit the window
screen.blit(image,(0, -15))
pygame.display.flip() #Updates the screen 


while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 