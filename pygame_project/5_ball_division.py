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

#공만들기
ball_images = [
    pygame.image.load("C:\\Users\\오지원\\Desktop\\PythonWork Space\\pygame_project\\image\\ballnoon1.png"),
    pygame.image.load("C:\\Users\\오지원\\Desktop\\PythonWork Space\\pygame_project\\image\\ballnoon2.png"),
    pygame.image.load("C:\\Users\\오지원\\Desktop\\PythonWork Space\\pygame_project\\image\\ballnoon3.png"),
    pygame.image.load("C:\\Users\\오지원\\Desktop\\PythonWork Space\\pygame_project\\image\\ballnoon4.png")
]
#공의 크기에 따라 다른 속도(공 크기에 따른 최초 스피드)
ball_speed_y = [-18, -15, -12, -9] #ball_images index 0  1  2  3 에 해당하는 값

#공들
balls = []

#최초 발생하는 큰공 추가
balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "img_idx" : 0, #공의 이미지 인덱스
    "to_x" : 3, #x축 이동방향, -3이면 왼쪽으로 3이면 오른쪽으로 
    "to_y" : -6, #y축 이동방향
    "init_spd_y": ball_speed_y[0]}) #y의 최초 속도

#사라질 무기, 공정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1


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

    #공 위치 정의
    for ball_idx, ball_val in enumerate(balls): 
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        #가로벽에 닿았을 때 공이 이동위치 변경(좌우로 튕기기)
        if ball_pos_x <0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1
        

        #스테이지에 팅겨서 올라가는 처리
        if ball_pos_y  >= screen_height - stage_height - ball_height :
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:   #그 외의 모든 경우에는 속도를증가
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]
    #4. 충돌 처리
    #공과 캐릭터의 충돌
    #캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls): 
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y
        
        if character_rect.colliderect(ball_rect):
            running = False
            break

        
    #공과 무기의 충돌
        for weapon_idx, weapon_val in enumerate(weapons): 
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

        #무기정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

        #충돌체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx #해당 무기 없애기 위한 값 설정
                ball_to_remove = ball_idx #해당 공 없애기 위한 값 설정
                
                #가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나눠주기
                if  ball_img_idx < 3 :
                    #현재 공 크기 정보
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]
                    #왼쪽으로 튕기는 공

                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        "pos_y" : ball_pos_y + (ball_height / 2 ) - (small_ball_height / 2),
                        "img_idx" : ball_img_idx + 1, #공의 이미지 인덱스
                        "to_x" : -3, #x축 이동방향, -3이면 왼쪽으로 3이면 오른쪽으로 
                        "to_y" : -6, #y축 이동방향
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]})

                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        "pos_y" : ball_pos_y + (ball_height / 2 ) - (small_ball_height / 2),
                        "img_idx" : ball_img_idx + 1, #공의 이미지 인덱스
                        "to_x" : 3, #x축 이동방향, -3이면 왼쪽으로 3이면 오른쪽으로 
                        "to_y" : -6,
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]})    
                break
    
    #충돌된 공 or 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1
    #화면에 그리기
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage,(0, screen_height - stage_height))
    screen.blit(character,(character_x_pos, character_y_pos))

   

    pygame.display.update()     #게임화면을 다시 그리기!


#pygame.종료
pygame.quit()