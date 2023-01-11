import pygame
from random import *

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("quiz")

clock = pygame.time.Clock()

background = pygame.image.load("C:/Users/오지원/Desktop/PythonWork Space/pygame_basic/제목 없음.png")

#캐릭터
character = pygame.image.load("C:/Users/오지원/Desktop/PythonWork Space/pygame_basic/character.png")
character_width = 70
character_height = 70
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height

#적
enemy = pygame.image.load("C:/Users/오지원/Desktop/PythonWork Space/pygame_basic/enemy.png")
enemy_width = 70
enemy_height = 70
enemy_x_pos = randint(0,screen_width - enemy_width)
enemy_y_pos = 0

to_x = 0

speed = 0.6

running = True 

while running:
    dt = clock.tick(30)
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:  
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= speed
            elif event.key == pygame.K_RIGHT:
                to_x += speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos >screen_width - 70:
        character_x_pos = screen_width - 70
    

    screen.blit(background, (0, 0))    
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy,(enemy_x_pos, enemy_y_pos))
    enemy_y_pos += speed *10
    if enemy_y_pos > screen_height:
        enemy_x_pos = randint(0, screen_width - enemy_width)
        enemy_y_pos = 0 



    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):      #적 캐릭터와 충돌했는가
        print("충돌했어요")
        running = False
    pygame.display.update()     

pygame.quit()