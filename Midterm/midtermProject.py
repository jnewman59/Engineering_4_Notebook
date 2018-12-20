import pygame, sys, time

pygame.display.init()

screen_size = (640,640)
window = pygame.display.set_mode(screen_size)
pygame.display.flip()

pygame.display.set_caption('yoink')

blue = (0,0,255)
red = (255,0,0)

window.fill(blue)
pygame.display.update()

#recc = pygame.draw.rect(window, red, (50, 50, 10, 10))
pygame.display.update()

running = True
for j in range(0, int(screen_size[1]/10)):
        for i in range(0, int(screen_size[0]/10)):
            red = 255-(i+j)*255/(int(screen_size[1]/10)+int(screen_size[0]/10))
            green = (i+64-j)*255/(int(screen_size[1]/10)+int(screen_size[0]/10))
            blue = (i+j)*255/(int(screen_size[1]/10)+int(screen_size[0]/10))
            pygame.draw.rect(window, (red, green, blue), (10*i, 10*j, 10, 10))
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print('the program should be over by now')

            pygame.quit()
            print('stopping')
    
