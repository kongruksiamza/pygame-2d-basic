import pygame
#ประกาศใช้งาน pygame
pygame.init()
#หัวข้อเกม
pygame.display.set_caption("My Game")
#ขนาดหน้าจอเกม
SCREEN_W = 600
SCREEN_H = 300
pygame.display.set_mode((SCREEN_W,SCREEN_H))
#แสดงหน้าจอเกม
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
pygame.quit()