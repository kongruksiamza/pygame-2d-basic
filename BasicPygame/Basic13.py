import pygame
pygame.init()
pygame.display.set_caption("My Game")
#ตั้งค่าสี (RGB)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

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
#โหลดภาพ
paddle=pygame.image.load("Image/paddle.png")
#ปรับขนาดภาพ
paddle=pygame.transform.scale(paddle,(120,30))

#ตั้งค่าคุณสมบัติ paddle
paddle_rect = paddle.get_rect()
paddle_rect.centerx = SCREEN_W // 2
paddle_rect.centery = SCREEN_H // 2

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
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
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()