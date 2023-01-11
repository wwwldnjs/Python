import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임이름

#배경이미지 불러오기
background = pygame.image.load("C:/Users/오지원/Desktop/PythonWork Space/pygame_basic/제목 없음.png")

# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get():    #어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT:   #창이 닫히는 이벤트가 발생하였는가
            running = False         #게임 진행중이 아님

    #screen.fill((0, 0, 255))       (다른 스크린채우기 방법) 
    screen.blit(background, (0, 0))     #배경그리기

    pygame.display.update()     #게임화면을 다시 그리기!
#pygame.종료
pygame.quit()