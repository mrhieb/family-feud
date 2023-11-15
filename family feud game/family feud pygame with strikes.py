import pygame
import pandas as pd
pygame.init()
background = pygame.image.load('Familyfeud2.jpg')
strike_one_image = pygame.image.load('one_strike.png')
strike_one_image = pygame.transform.scale(strike_one_image, (200, 200))
strike_two_image = pygame.image.load('two_strikes.png')
strike_two_image = pygame.transform.scale(strike_two_image, (420, 200))
strike_three_image = pygame.image.load('three strikes.png')
strike_three_image = pygame.transform.scale(strike_three_image, (640, 200))
background = pygame.transform.scale(background, (1600, 800))
surface = pygame.display.set_mode((1600, 800))
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
strike_show = True
team_1_points = 0
team_2_points = 0
points = 0
strikes = 1
answers = []
values = []

SHEET_ID = '1mbHIF4vIXpRT-k5J9RBk-p93WHzCgKRnp1ABuqU_ixY'
#SHEET_NAME is the name of the tab
SHEET_NAME = 'Q1'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
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

team_1_score_box = pygame.draw.rect(surface, (40, 40, 230), (10, 10, 250, 120))
team_2_score_box = pygame.draw.rect(surface, (40, 40, 230), (1350, 10, 250, 120))
strike_box = pygame.draw.rect(surface, (40, 40, 230), (10, 710, 250, 120))
level_2 = False
level_3 = False
level_4 = False
level = 1
strikes = 0
while True:
    events = pygame.event.get()
    for event in events:
        if event == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if strike_box.collidepoint(pos):
                strikes = strikes + 1
                print(strikes)
                strike_show = False
            if team_1_score_box.collidepoint(pos):
                team_1_points += points
                strikes = 0
                points = 0
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
                level = level + 1
                if level == 2:
                    level_2 = True
                if level == 3:
                    level_3 = True
                if level == 4:
                    level_4 = True
                
            elif team_2_score_box.collidepoint(pos):
                team_2_points += points
                points = 0
                strikes = 0
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
                level = level + 1
                if level == 2:
                    level_2 = True
                if level == 3:
                    level_3 = True
                if level == 4:
                    level_4 = True
                
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
                    
    if level_2 == True:
        SHEET_ID = '1mbHIF4vIXpRT-k5J9RBk-p93WHzCgKRnp1ABuqU_ixY'
        #SHEET_NAME is the name of the tab
        SHEET_NAME = 'Q2'
        url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
        df = pd.read_csv(url)
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
        level_2 = False
    
    if level_3 == True:
        SHEET_ID = '1mbHIF4vIXpRT-k5J9RBk-p93WHzCgKRnp1ABuqU_ixY'
        #SHEET_NAME is the name of the tab
        SHEET_NAME = 'Q3'
        url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
        df = pd.read_csv(url)
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
        level_3 = False
    
    if level_4 == True:
        SHEET_ID = '1mbHIF4vIXpRT-k5J9RBk-p93WHzCgKRnp1ABuqU_ixY'
        #SHEET_NAME is the name of the tab
        SHEET_NAME = 'Q4'
        url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
        df = pd.read_csv(url)
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
        level_4 = False
    
    
    surface.blit(background, (0,0))
    #The code below colors the answer boxes blue
    box_x = 316
    box_y = 225
    boxes = []
    
    for i in range(4):
        box_object = pygame.draw.rect(surface, (40, 40, 230), (box_x, box_y, 500, 100))
        boxes.append(box_object)
        box_x = box_x + 515
        box2_object = pygame.draw.rect(surface, (40, 40, 230), (box_x, box_y, 500, 100))
        boxes.append(box2_object)
        box_y = box_y + 130
        box_x = box_x - 515
    clicking_box = pygame.draw.rect(surface, (40, 40, 230), (650, 0, 350, 150))
    score_words = arial_150.render(str(points), True, (255, 255, 255))
    score_width = score_words.get_width()
    surface.blit(score_words, (850-score_width, 30))
    #Light Blue section for point totals on each answer
#     pygame.draw.rect(surface, (80, 80, 255), (530, 480, 80, 100))
    words_x = 550
    words_y = 240
    
   
    for i in range(len(answers)):
        words = arial_50.render(str(i+1), True, (255, 255, 255))
        surface.blit(words, (words_x, words_y))
        words_y = words_y + 130
        if words_y >700:
            words_x = words_x + 510
            words_y = 240
    if box_1 =='correct':
        pygame.draw.rect(surface, (40, 40, 230), (316, 225, 370, 100))
        answer_block_1 = arial_50.render(answers[0], True, (255, 255, 255))
        surface.blit(answer_block_1, (350, 240))
        points_block_1 = arial_50.render(str(int(values[0])), True, (255, 255, 255))
        surface.blit(points_block_1, (730, 240))
        if box_1_scored == False:
            points = points + int(values[0])
            box_1_scored = True
    if box_2 == 'correct':
        pygame.draw.rect(surface, (40, 40, 230), (316, 355, 370, 100))
        answer_block_2 = arial_50.render(answers[1], True, (255, 255, 255))
        surface.blit(answer_block_2, (350, 370))
        points_block_2 = arial_50.render(str(int(values[1])), True, (255, 255, 255))
        surface.blit(points_block_2, (730, 370))

        if box_2_scored == False:
            points = points + int(values[1])
            box_2_scored = True
    if box_3 == 'correct':
        pygame.draw.rect(surface, (40, 40, 230), (316, 485, 370, 100))
        answer_block_2 = arial_50.render(answers[2], True, (255, 255, 255))
        surface.blit(answer_block_2, (350, 500))
        points_block_2 = arial_50.render(str(int(values[2])), True, (255, 255, 255))
        surface.blit(points_block_2, (730, 500))
        
        if box_3_scored == False:
            points = points + int(values[2])
            box_3_scored = True
    if box_4 == 'correct':
        pygame.draw.rect(surface, (40, 40, 230), (316, 615, 370, 100))
        answer_block_2 = arial_50.render(answers[3], True, (255, 255, 255))
        surface.blit(answer_block_2, (350, 630))
        points_block_2 = arial_50.render(str(int(values[3])), True, (255, 255, 255))
        surface.blit(points_block_2, (730, 630))
        
        if box_4_scored == False:
            points = points + int(values[3])
            box_4_scored = True
    if box_5 == 'correct':
        pygame.draw.rect(surface, (40, 40, 230), (825, 225, 370, 100))
        answer_block_2 = arial_50.render(answers[4], True, (255, 255, 255))
        surface.blit(answer_block_2, (850, 240))
        points_block_2 = arial_50.render(str(int(values[4])), True, (255, 255, 255))
        surface.blit(points_block_2, (1250, 240))
        if box_5_scored == False:
            points = points + int(values[4])
            box_5_scored = True
    if box_6 == 'correct':
        pygame.draw.rect(surface, (40, 40, 230), (825, 355, 370, 100))
        answer_block_2 = arial_50.render(answers[5], True, (255, 255, 255))
        surface.blit(answer_block_2, (850, 370))
        points_block_2 = arial_50.render(str(int(values[5])), True, (255, 255, 255))
        surface.blit(points_block_2, (1250, 370))
        
        if box_6_scored == False:
            points = points + int(values[5])
            box_6_scored = True
    if box_7 == 'correct':
        pygame.draw.rect(surface, (40, 40, 230), (825, 485, 370, 100))
        answer_block_2 = arial_50.render(answers[6], True, (255, 255, 255))
        surface.blit(answer_block_2, (850, 500))
        points_block_2 = arial_50.render(str(int(values[6])), True, (255, 255, 255))
        surface.blit(points_block_2, (1250, 500))
        
        if box_7_scored == False:
            points = points + int(values[6])
            box_7_scored = True
    if box_8 == 'correct':
        pygame.draw.rect(surface, (40, 40, 230), (825, 615, 370, 100))
        answer_block_2 = arial_50.render(answers[7], True, (255, 255, 255))
        surface.blit(answer_block_2, (850, 630))
        points_block_2 = arial_50.render(str(int(values[7])), True, (255, 255, 255))
        surface.blit(points_block_2, (1250, 630))
        
        if box_8_scored == False:
            points = points + int(values[7])
            box_8_scored = True
    team_1_score_box = pygame.draw.rect(surface, (40, 40, 230), (10, 10, 250, 120))
    answer_block_2 = arial_50.render('Team 1', True, (255, 255, 255))
    surface.blit(answer_block_2, (50, 10))
    points_block_2 = arial_50.render(str(team_1_points), True, (255, 255, 255))
    surface.blit(points_block_2, (50, 60))
    
    team_2_score_box = pygame.draw.rect(surface, (40, 40, 230), (1350, 10, 250, 120))
    answer_block_2 = arial_50.render('Team 2', True, (255, 255, 255))
    surface.blit(answer_block_2, (1350, 10))
    points_block_2 = arial_50.render(str(team_2_points), True, (255, 255, 255))
    strike_box = pygame.draw.rect(surface, (40, 40, 230), (10, 710, 250, 120))
    strike_block_2 = arial_50.render('Strikes', True, (255, 255, 255))
    surface.blit(strike_block_2, (50, 710))
    surface.blit(points_block_2, (1350, 60))
    if strikes == 1:
        if strike_show == False:
            surface.blit(strike_one_image, (500, 400))
            pygame.display.update()
            pygame.time.delay(1000)
            
            strike_show = True
    elif strikes == 2:
        if strike_show == False:
            surface.blit(strike_two_image, (500, 400))
            pygame.display.update()
            pygame.time.delay(1000)
            
            strike_show = True
    elif strikes == 3:
        if strike_show == False:
            surface.blit(strike_three_image, (500, 400))
            pygame.display.update()
            pygame.time.delay(1000)
            
            strike_show = True
    
    
    pygame.display.update()
