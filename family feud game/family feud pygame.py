import pygame
import pandas as pd
pygame.init()
background = pygame.image.load('Familyfeud2.jpg')
background = pygame.transform.scale(background, (1200, 800))
surface = pygame.display.set_mode((1200, 800))
arial_50 = pygame.font.SysFont('Helvetica condensed', 70)
arial_150 = pygame.font.SysFont('Helvetica condensed', 150)
clicking_box = pygame.draw.rect(surface, (40, 40, 230), (12, 12, 370, 100))
boxes = []
boxes.append(clicking_box)
box_1 = 'incorrect'
box_2 = 'incorrect'
box_3 = 'incorrect'
box_4 = 'incorrect'
box_5 = 'incorrect'
box_6 = 'incorrect'
box_7 = 'incorrect'
box_8 = 'incorrect'
box_1_scored = False
box_2_scored = False
box_3_scored = False
box_4_scored = False
box_5_scored = False
box_6_scored = False
box_7_scored = False
box_8_scored = False

SHEET_ID = '1mbHIF4vIXpRT-k5J9RBk-p93WHzCgKRnp1ABuqU_ixY'
#SHEET_NAME is the name of the tab
SHEET_NAME = 'Q1'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
points = 0
answers = []
values = []
for i in range(8):
    val = df.iloc[i][0]
    if val == 'empty':
        break
    else:
        answers.append(val)
for j in range(8):
    val = df.iloc[j][1]
    if val == 'empty':
        break
    else:
        values.append(val)
while True:
    events = pygame.event.get()
    for event in events:
        if event == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            print(pos)
            for box in boxes:
                if box.collidepoint(pos):
                    if boxes.index(box) == 0:
                        print('number 1 answer')
                        box_1 = 'correct'
                    elif boxes.index(box) == 1:
                        print('number 5 answer')
                        box_5 = 'correct'
                    elif boxes.index(box) == 2:
                        print('number 2 answer')
                        box_2 = 'correct'
                    elif boxes.index(box) == 3:
                        print('number 6 answer')
                        box_6 = 'correct'
                    elif boxes.index(box) == 4:
                        print('number 3 answer')
                        box_3 = 'correct'
                    elif boxes.index(box) == 5:
                        print('number 7 answer')
                        box_7 = 'correct'
                    elif boxes.index(box) == 6:
                        print('number 4 answer')
                        box_4 = 'correct'
                    elif boxes.index(box) == 7:
                        print('number 8 answer')
                        box_8 = 'correct'
                    
                    
    surface.blit(background, (0,0))
    #The code below colors the answer boxes blue
    box_x = 240
    box_y = 220
    boxes = []
    
    for i in range(4):
        box_object = pygame.draw.rect(surface, (40, 40, 230), (box_x, box_y, 370, 100))
        boxes.append(box_object)
        box_x = box_x + 380
        box2_object = pygame.draw.rect(surface, (40, 40, 230), (box_x, box_y, 370, 100))
        boxes.append(box2_object)
        box_y = box_y + 130
        box_x = box_x - 380
    clicking_box = pygame.draw.rect(surface, (40, 40, 230), (480, 0, 270, 150))
    score_words = arial_150.render(str(points), True, (255, 255, 255))
    score_width = score_words.get_width()
    surface.blit(score_words, (670-score_width, 30))
    #Light Blue section for point totals on each answer
#     pygame.draw.rect(surface, (80, 80, 255), (530, 480, 80, 100))
    words_x = 400
    words_y = 240
    
   
    for i in range(len(answers)):
        words = arial_50.render(str(i+1), True, (255, 255, 255))
        surface.blit(words, (words_x, words_y))
        words_y = words_y + 130
        if words_y >700:
            words_x = words_x + 380
            words_y = 240
    if box_1 =='correct':
        pygame.draw.rect(surface, (40, 40, 230), (240, 220, 370, 100))
        answer_block_1 = arial_50.render(answers[0], True, (255, 255, 255))
        surface.blit(answer_block_1, (280, 240))
        points_block_1 = arial_50.render(str(int(values[0])), True, (255, 255, 255))
        surface.blit(points_block_1, (530, 240))
        if box_1_scored == False:
            points = points + int(values[0])
            box_1_scored = True
    if box_2 == 'correct':
        pygame.draw.rect(surface, (40, 40, 230), (240, 350, 370, 100))
        answer_block_2 = arial_50.render(answers[1], True, (255, 255, 255))
        surface.blit(answer_block_2, (280, 370))
        points_block_2 = arial_50.render(str(int(values[1])), True, (255, 255, 255))
        surface.blit(points_block_2, (530, 370))

        if box_2_scored == False:
            points = points + int(values[1])
            box_2_scored = True
    if box_3 == 'correct':
        pygame.draw.rect(surface, (40, 40, 230), (240, 480, 370, 100))
        answer_block_2 = arial_50.render(answers[2], True, (255, 255, 255))
        surface.blit(answer_block_2, (280, 500))
        points_block_2 = arial_50.render(str(int(values[2])), True, (255, 255, 255))
        surface.blit(points_block_2, (530, 500))
        
        if box_3_scored == False:
            points = points + int(values[2])
            box_3_scored = True
    if box_4 == 'correct':
        pygame.draw.rect(surface, (40, 40, 230), (240, 610, 370, 100))
        answer_block_2 = arial_50.render(answers[3], True, (255, 255, 255))
        surface.blit(answer_block_2, (280, 630))
        points_block_2 = arial_50.render(str(int(values[3])), True, (255, 255, 255))
        surface.blit(points_block_2, (530, 630))
        
        if box_4_scored == False:
            points = points + int(values[3])
            box_4_scored = True
    if box_5 == 'correct':
        pygame.draw.rect(surface, (40, 40, 230), (620, 220, 370, 100))
        answer_block_2 = arial_50.render(answers[4], True, (255, 255, 255))
        surface.blit(answer_block_2, (640, 240))
        points_block_2 = arial_50.render(str(int(values[4])), True, (255, 255, 255))
        surface.blit(points_block_2, (890, 240))
        if box_5_scored == False:
            points = points + int(values[4])
            box_5_scored = True
    if box_6 == 'correct':
        pygame.draw.rect(surface, (40, 40, 230), (620, 350, 370, 100))
        answer_block_2 = arial_50.render(answers[5], True, (255, 255, 255))
        surface.blit(answer_block_2, (640, 370))
        points_block_2 = arial_50.render(str(int(values[5])), True, (255, 255, 255))
        surface.blit(points_block_2, (890, 370))
        
        if box_6_scored == False:
            points = points + int(values[5])
            box_6_scored = True
    if box_7 == 'correct':
        pygame.draw.rect(surface, (40, 40, 230), (620, 480, 370, 100))
        answer_block_2 = arial_50.render(answers[6], True, (255, 255, 255))
        surface.blit(answer_block_2, (640, 500))
        points_block_2 = arial_50.render(str(int(values[6])), True, (255, 255, 255))
        surface.blit(points_block_2, (890, 500))
        
        if box_7_scored == False:
            points = points + int(values[6])
            box_7_scored = True
    if box_8 == 'correct':
        pygame.draw.rect(surface, (40, 40, 230), (620, 610, 370, 100))
        answer_block_2 = arial_50.render(answers[7], True, (255, 255, 255))
        surface.blit(answer_block_2, (640, 630))
        points_block_2 = arial_50.render(str(int(values[7])), True, (255, 255, 255))
        surface.blit(points_block_2, (890, 630))
        
        if box_8_scored == False:
            points = points + int(values[7])
            box_8_scored = True
        
    
    pygame.display.update()
