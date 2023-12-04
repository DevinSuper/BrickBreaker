import pygame 
import subprocess
import sys

pygame.init()
#Screen 
screen = pygame.display.set_mode((800,600)) #Initialize the Window  
pygame.display.set_caption("Start Menu") #Window Name
screen.fill((210,180,140)) #Set The Window Color 
pygame.display.flip() #Updates the screen 

#Main Title Image 
image_path = r"C:\Users\d3v1n\Downloads\Gameimg.png"# Replace with the path to your image file
image = pygame.image.load(image_path)
image = pygame.transform.scale(image, (500, 500))  # Resize the image to fit the window
screen.blit(image,(180, -15))

#Music File to Import
pygame.mixer.music.load(r"C:\Users\d3v1n\PycharmProjects\Adv-Python-Programming-23-24\Brick Breaker Game\RPReplay_Final1700950435.ogg")
pygame.mixer.music.play(loops=-1, start=0.0) #Make sure the music is looped and never ends 

font = pygame.font.Font(None, 36)
#Game Loop 
while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
    pygame.draw.rect(screen, (90,65,55), pygame.Rect(300, 350, 225, 70))
    pygame.draw.rect(screen, (90,65,55), pygame.Rect(300, 450, 225, 70))
    pygame.draw.rect(screen, (90,65,55), pygame.Rect(750, 550, 40, 40))
    text = font.render("Start Game!", True, (210,180,140)) #Creation of the Start Button
    text_rect = text.get_rect()
    text_rect.center = (415,380)
    screen.blit(text, text_rect)
    text2 = font.render("Quit", True, (210,180,140)) #Creation of the Quit Button
    text_rect2 = text2.get_rect()
    text_rect2.center = (415,485)
    screen.blit(text2, text_rect2)
    text3 = font.render("By: Devin & Walker", True, (100,80,60)) 
    text_rect3 = text3.get_rect()
    text_rect3.center = (125,580)
    screen.blit(text3, text_rect3)
    text4 = font.render("?", True, (210,180,140)) #Creation of the Start Button
    text_rect4 = text4.get_rect()
    text_rect4.center = (770,570)
    screen.blit(text4, text_rect4)
    pygame.display.update() #Updates The Screen 
    #Checks if a Button is Pressed
    if event.type == pygame.MOUSEBUTTONDOWN: 
    #Check Which Button is Pressed: Then either quit game or open the game
        if 300 <= pygame.mouse.get_pos()[0] <= 525 and 350 <= pygame.mouse.get_pos()[1] <= 420: 
            pygame.mixer.music.stop()
            subprocess.run(["python", r"C:\Users\d3v1n\PycharmProjects\Adv-Python-Programming-23-24\Brick Breaker Game\Break_Breaker_New_Code.py"])
            sys.exit()
        if 300 <= pygame.mouse.get_pos()[0] <= 525 and 450 <= pygame.mouse.get_pos()[1] <= 520: 
            pygame.quit()
        if 750 <= pygame.mouse.get_pos()[0] <= 790 and 550 <= pygame.mouse.get_pos()[1] <= 590: 
            subprocess.run(["python", r"C:\Users\d3v1n\PycharmProjects\Adv-Python-Programming-23-24\Brick Breaker Game\Tutscreen.py"])
