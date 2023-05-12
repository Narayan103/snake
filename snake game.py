import pygame
import time
import random
pygame.init()
# Importing mysql(connecting mysql)
'''import mysql.connector
mycon=mysql.connector.connect(host='localhost',user='root',passwd='students',database='snake')
cur=mycon.cursor()'''
# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
# Window for the game
dis_width = 1000
dis_height = 500
dis = pygame.display.set_mode((dis_width, dis_height))
# Game Title
pygame.display.set_caption('Snake Game by Team 10')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("Times New Roman", 25)
score_font = pygame.font.SysFont("Times New Roman", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block,snake_block])
def message(msg, color,x,y):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [x,y])
def gameLoop():
    global score
# Game specific variables
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    # Reading Hiscore
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0)* 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0)* 10.0
    score=0
    while not game_over:
        if game_close:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
        while game_close == True:
            dis.fill(green)
            message("You Lost! Press P-Play Again or Q-Quit",black,100,250)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
            x1 += x1_change
            y1 += y1_change
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) /10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block)/ 10.0) * 10.0
                Length_of_snake += 1
                score+=1
                if score > int(hiscore):
                    hiscore = score
                #q="delete from snake"
                #cur.execute(q)
                #s="insert into snake(score) values ({})".format(hiscore)
                #cur.execute(s)
                #mycon.commit()
            dis.fill(green)
            message("Score: " + str(score) + " Highscore: "+str(hiscore),black,5,5)
            pygame.draw.rect(dis, red, [foodx, foody, snake_block,snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            our_snake(snake_block, snake_List)
        pygame.display.update()
        clock.tick(snake_speed)
    pygame.quit()
    quit()
gameLoop()
