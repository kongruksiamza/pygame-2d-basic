import pygame
import random

pygame.init()
pygame.display.set_caption("My Game")
#ตั้งค่าสี (RGB)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

#ความเร็วการเคลื่อนที่ 
SPEED = 5
BALL_SPEED=2
#FPS
FPS = 60
clock=pygame.time.Clock()
#ขนาดหน้าจอเกม
SCREEN_W = 600
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
#แสดงหน้าจอเกม
screen.fill(BLACK)

#paddle object
paddle=pygame.image.load("Image/paddle.png")
paddle=pygame.transform.scale(paddle,(120,30))
paddle_rect = paddle.get_rect()
paddle_rect.centerx = SCREEN_W // 2
paddle_rect.centery = SCREEN_H // 2 + 200

#ball object
ball = pygame.image.load("Image/ball.png")
ball = pygame.transform.scale(ball,(50,50))
ball_rect = ball.get_rect()
ball_rect.x = random.randint(0,SCREEN_W-32)
ball_rect.y= 0 

#score system
score = 0
font = pygame.font.Font("Font/Coiny.ttf",30)
score_txt = font.render("Score : "+str(score),True,WHITE)
score_rect = score_txt.get_rect()
score_rect.topleft=(10,10)

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    #การชน
    if paddle_rect.colliderect(ball_rect):
       score+=10
       score_txt = font.render("Score : "+str(score),True,WHITE)
       ball_rect.x = random.randint(0,SCREEN_W-32)
       ball_rect.y= 0 
    
    #รับค่าจากผู้เล่น
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_rect.left>0:
        paddle_rect.x-=SPEED
    if keys[pygame.K_RIGHT] and paddle_rect.right<SCREEN_W:
        paddle_rect.x+=SPEED
    
    #การเคลื่อนที่ลูกบอล
    if ball_rect.y < SCREEN_H:
        ball_rect.y+=BALL_SPEED
    else:
        #ทะลุหน้าจอเกม
        ball_rect.x = random.randint(0,SCREEN_W-32)
        ball_rect.y= 0 

    #แสดงภาพ     
    screen.fill(BLACK)   
    screen.blit(paddle,paddle_rect)  
    screen.blit(ball,ball_rect)  
    screen.blit(score_txt,score_rect)  
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()