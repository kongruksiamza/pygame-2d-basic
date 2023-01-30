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
#FPS
FPS = 60
clock=pygame.time.Clock()
#ขนาดหน้าจอเกม
SCREEN_W = 600
SCREEN_H = 300
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
#แสดงหน้าจอเกม
screen.fill(WHITE)

#paddle object
paddle=pygame.image.load("Image/paddle.png")
paddle=pygame.transform.scale(paddle,(120,30))
paddle_rect = paddle.get_rect()
paddle_rect.centerx = SCREEN_W // 2
paddle_rect.centery = SCREEN_H // 2

#ball object
ball = pygame.image.load("Image/ball.png")
ball = pygame.transform.scale(ball,(50,50))
ball_rect = ball.get_rect()
ball_rect.center=(SCREEN_W // 2 ,SCREEN_H // 2-100)


running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    #การชน
    if paddle_rect.colliderect(ball_rect):
        ball_rect.left=random.randint(0,SCREEN_W-32)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle_rect.top>0:
        paddle_rect.y-=SPEED
    if keys[pygame.K_DOWN] and paddle_rect.bottom<SCREEN_H:
        paddle_rect.y+=SPEED
    if keys[pygame.K_LEFT] and paddle_rect.left>0:
        paddle_rect.x-=SPEED
    if keys[pygame.K_RIGHT] and paddle_rect.right<SCREEN_W:
        paddle_rect.x+=SPEED
    #แสดงภาพ     
    screen.fill(WHITE)   
    screen.blit(paddle,paddle_rect)  
    screen.blit(ball,ball_rect)    
    #แสดงขอบเขตวัตถุ
    #pygame.draw.rect(screen,GREEN,paddle_rect,2)
    #pygame.draw.rect(screen,GREEN,ball_rect,2)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()