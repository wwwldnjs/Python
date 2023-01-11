import pygame
#########################################################################
                        #기본 초기화(반드시 해야하는 것들)
pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 640 #가로크기
screen_height = 480 #세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Pang")

#FPS
clock = pygame.time.Clock()
#########################################################################

            # 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)   


#배경
background = pygame.image.load("C:\\Users\\오지원\\Desktop\\PythonWork Space\\pygame_project\\image\\background.png")
#스테이지
stage = pygame.image.load("C:\\Users\\오지원\\Desktop\\PythonWork Space\\pygame_project\\image\\stage.png")
stage_size = stage.get_rect().size
stage_height = stage_size[1]

#캐릭터 만들기
character = pygame.image.load("C:\\Users\\오지원\\Desktop\\PythonWork Space\\pygame_project\\image\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - stage_height - character_height

#캐릭터 이동방향
character_to_x = 0

#캐릭터 이동속도
character_speed = 5

#무기만들기
weapon = pygame.image.load("C:\\Users\\오지원\\Desktop\\PythonWork Space\\pygame_project\\image\\weapon.png")
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기는 한번에 여러 발 발사 가능(무기들을 리스트로 관리)
weapons = []

#무기이동 속도
weapon_speed = 10

#스테이지
    #########################################################################

# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(30) #게임화면의 초당 프레임 수를 설정



    #2. 이벤트 처리(키보드, 마우스 등)

    for event in pygame.event.get():    
        if event.type == pygame.QUIT:  
            running = False       

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + character_width / 2 - weapon_width/2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
            

        
    #3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos =0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

         #무기 위치조정
    weapons = [ [w[0], w[1]-weapon_speed] for w in weapons]
        #천장에 닿은 무기 없애기
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons if w[1] > 0 ]
    #4. 충돌 처리


    #화면에 그리기
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage,(0, screen_height - stage_height))
    screen.blit(character,(character_x_pos, character_y_pos))

   

    pygame.display.update()     #게임화면을 다시 그리기!


#pygame.종료
pygame.quit()