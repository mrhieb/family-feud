import pygame
pygame.init()
answers = {'hockey':40, 'football':30, 'baseball':10, 'tennis':10, 'boxing':5, 'wrestling':5}
background = pygame.image.load('Familyfeud2.jpg')
background = pygame.transform.scale(background, (1200, 800))
surface = pygame.display.set_mode((1200, 800))
arial_50 = pygame.font.SysFont('Helvetica condensed', 70)
surface.blit(background, (0,0))
#The code below colors the answer boxes blue
box_x = 240
box_y = 220
for i in range(4):
    pygame.draw.rect(surface, (40, 40, 230), (box_x, box_y, 370, 100))
    box_x = box_x + 380
    pygame.draw.rect(surface, (40, 40, 230), (box_x, box_y, 370, 100))
    box_y = box_y + 130
    box_x = box_x - 380

#Light Blue section for point totals on each answer
#pygame.draw.rect(surface, (80, 80, 255), (530, 480, 80, 100))
words_x = 400
words_y = 240
for i in range(len(answers)):
    words = arial_50.render(str(i+1), True, (255, 255, 255))
    surface.blit(words, (words_x, words_y))
    words_y = words_y + 130
    if words_y >700:
        words_x = words_x + 380
        words_y = 240
    
pygame.display.update()