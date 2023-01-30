import pygame
pygame.init()
pygame.display.set_caption("My Game")
#ตั้งค่าสี (RGB)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
#ขนาดหน้าจอเกม
SCREEN_W = 600
SCREEN_H = 300
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
#แสดงหน้าจอเกม
screen.fill(WHITE)
#ตั้งค่าข้อความและฟอนต์
custom_font = pygame.font.Font("Font/Coiny.ttf",20)
title_text = custom_font.render("Hello Pygame",True,RED)

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    screen.blit(title_text,(80,100))
    pygame.display.update()
pygame.quit()