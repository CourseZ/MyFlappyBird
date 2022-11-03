import sys, pygame
from tkinter import font
from random import randint

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()

WIDTH, HEIGHT = 400, 700
WHITE = (255,255,255)
game_font = pygame.font.Font('./font/04B_19.TTF',40)
score = 0
high_score = 0

game_over_surface = pygame.image.load('./img/message.png') #290x420
game_over_surface = pygame.transform.scale2x(game_over_surface)
game_over_rect = game_over_surface.get_rect(center=(200,350))

#tube x
tube1_x = 400
tube2_x = 600
tube3_x = 800
TUBE_WIDTH = 50
TUBE_GAP = 150
TUBE_VELOCITY = 3
tube1_height = randint(100,350)
tube2_height = randint(100,350)
tube3_height = randint(100,350)

tube1_op_height = HEIGHT - (tube1_height + TUBE_GAP + 100)
tube2_op_height = HEIGHT - (tube2_height + TUBE_GAP + 100)
tube3_op_height = HEIGHT - (tube3_height + TUBE_GAP + 100)

#load ảnh ống 
tube_img = pygame.image.load('./img/tube.png')  #ống trên
tube_opposite_img = pygame.image.load('./img/tube_op.png') #ống dưới

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('FLappy Bird')
clock = pygame.time.Clock()

#load background và sàn
background_img = pygame.image.load('./img/background-night.png')
background_img = pygame.transform.scale(background_img,(WIDTH,HEIGHT))
floor = pygame.image.load('./img/floor.png')
floor = pygame.transform.scale(floor,(WIDTH,100))
floor_x_pos = 0

#ảnh chim đập cánh
# bird_downflap = pygame.image.load('./img/yellowbird-downflap.png')
# bird_down = pygame.transform.scale(bird_downflap,(35,35))
# bird_midflap = pygame.image.load('./img/yellowbird-midflap.png')
# bird_mid = pygame.transform.scale(bird_midflap,(35,35))
# bird_upflap = pygame.image.load('./img/yellowbird-upflap.png')
# bird_up = pygame.transform.scale(bird_upflap,(35,35))
# bird_list = [bird_down,bird_mid,bird_up]
# bird_index = 0
# bird_current = bird_list[bird_index]

#load ảnh chim
bird_img = pygame.image.load('./img/yellowbird-midflap.png')
bird_img = pygame.transform.scale(bird_img,(35,35))
x_bird = 50
y_bird = 300
bird_drop_velocity = 0
gravity = 0.5
RED = (255,0,0)

tube1_pass = False
tube2_pass = False
tube3_pass = False

#chèn âm thanh
flap_sound = pygame.mixer.Sound('./sound/sfx_wing.wav') #âm thanh khi chim bay lên
hit_sound = pygame.mixer.Sound('./sound/sfx_hit.wav') #âm thanh khi chim chạm cột
score_sound = pygame.mixer.Sound('./sound/sfx_point.wav') #âm thanh khi cộng điểm
score_sound_countdown = 1
dem = 1
game_active = False
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)
    screen.blit(background_img,(0,0))

    #vẽ sàn
    floor_x_pos -= 2
    floor1 = screen.blit(floor,(floor_x_pos,600))
    floor2 = screen.blit(floor,(floor_x_pos+WIDTH,600))
 
    if floor_x_pos <= -WIDTH:
        floor_x_pos = 0

    #vẽ trời
    sky = pygame.draw.rect(screen,WHITE,(0,-10,WIDTH,11))
    if game_active:
        #vẽ ống trên
        tube1_img = pygame.transform.scale(tube_img,(TUBE_WIDTH,tube1_height))
        tube1 = screen.blit(tube1_img,(tube1_x,0))
        tube2_img = pygame.transform.scale(tube_img,(TUBE_WIDTH,tube2_height))
        tube2 = screen.blit(tube2_img,(tube2_x,0))
        tube3_img = pygame.transform.scale(tube_img,(TUBE_WIDTH,tube3_height))
        tube3 = screen.blit(tube3_img,(tube3_x,0))

        #vẽ ống đối diện
        tube1_op_img = pygame.transform.scale(tube_opposite_img,(TUBE_WIDTH,tube1_op_height))
        tube1_op = screen.blit(tube1_op_img,(tube1_x,TUBE_GAP+tube1_height))
        tube2_op_img = pygame.transform.scale(tube_opposite_img,(TUBE_WIDTH,tube2_op_height))
        tube2_op = screen.blit(tube2_op_img,(tube2_x,TUBE_GAP+tube2_height))
        tube3_op_img = pygame.transform.scale(tube_opposite_img,(TUBE_WIDTH,tube3_op_height))
        tube3_op = screen.blit(tube3_op_img,(tube3_x,TUBE_GAP+tube3_height))

        #ống di chuyển sang trái
        tube1_x -= TUBE_VELOCITY
        tube2_x -= TUBE_VELOCITY
        tube3_x -= TUBE_VELOCITY

        #tạo ống mới
        if tube1_x < -TUBE_WIDTH:
            tube1_x = 550
            tube1_height = randint(100,350)
            tube1_op_height = HEIGHT - (tube1_height + TUBE_GAP + 100)
            tube1_pass = False
        if tube2_x < -TUBE_WIDTH:
            tube2_x = 550
            tube2_height = randint(100,350)
            tube2_op_height = HEIGHT - (tube2_height + TUBE_GAP + 100)
            tube2_pass = False
        if tube3_x < -TUBE_WIDTH:
            tube3_x = 550
            tube3_height = randint(100,350)
            tube3_op_height = HEIGHT - (tube3_height + TUBE_GAP + 100)
            tube3_pass = False
        #ghi điểm
        score_txt = game_font.render("Score: " + str(score),True,WHITE)
        screen.blit(score_txt,(120,5))

        #tính điểm
        if tube1_x + TUBE_WIDTH <= x_bird and tube1_pass == False:
            score += 1
            tube1_pass = True
            score_sound.play()
        if tube2_x + TUBE_WIDTH <= x_bird and tube2_pass == False:
            score += 1
            tube2_pass = True
            score_sound.play()
        if tube3_x + TUBE_WIDTH <= x_bird and tube3_pass == False:
            score += 1
            tube3_pass = True
            score_sound.play()

        #vẽ chim
        bird = screen.blit(bird_img,(x_bird,y_bird))
        y_bird += bird_drop_velocity
        bird_drop_velocity += gravity
        #tiến hóa chim

        #vẽ vật phẩm, ăn vật phẩm r tiến hóa chim,x2 điểm
        vat_pham = pygame.draw.rect(screen,RED,(200,200,10,10))
        
        #tăng tốc khi 5 điểm
        if score >= 5:
            TUBE_VELOCITY = 4

        #kiểm tra sự va chạm
        tubes = [tube1,tube2,tube3,tube1_op,tube2_op,tube3_op,floor1,floor2,sky]
        for tube in tubes:
            if bird.colliderect(tube):
                hit_sound.play()
                # pygame.mixer.pause()
                TUBE_VELOCITY = 0
                bird_drop_velocity = 0
                game_active = False
                if high_score < score:
                    high_score = score
    
    else:
        your_score_txt = game_font.render("Your score: " + str(score),True,WHITE)
        screen.blit(your_score_txt,(65,5))
        high_score_txt = game_font.render("High score: " + str(high_score),True,WHITE)
        screen.blit(high_score_txt,(65,65))
        screen.blit(game_over_surface,game_over_rect)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_drop_velocity = 0
                bird_drop_velocity -= 7
                flap_sound.play()
                if game_active == False:
                    game_active = True
                    pygame.mixer.unpause()
                    x_bird = 50
                    y_bird = 300
                    tube1_x = 400
                    tube2_x = 600
                    tube3_x = 800
                    TUBE_VELOCITY = 3
                    score = 0
    
    pygame.display.flip()