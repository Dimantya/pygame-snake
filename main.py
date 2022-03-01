import pygame
import time
import random
#инициализация экрана
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 102)
green = (0, 255, 0)


#соотношение сторон и формула расчета еды плывут при простом изменении парметров
#оптимальные значения 600 на 400 и размер блока змейки 10
#с ними точно работает

dis_width = 800
dis_height = 600

#создание экрана
dis = pygame.display.set_mode((dis_width, dis_height))
#применяет изменения экрана, без параметров как в данном случае обновляет весь экран
pygame.display.set_caption('Best snake')

clock = pygame.time.Clock()

snake_block = 20
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

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
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        # pygame.draw.rect(dis, black, [x1,y1,snake_block, snake_block]) #[координаты, координаты, длина, ширина]

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 ==foody:
            foodx = round(random.randrange(0, dis_width - snake_block)/10.0)*10.0
            foody = round(random.randrange(0, dis_height - snake_block)/10.0)*10.00
            Length_of_snake += 1

        clock.tick(snake_speed)

        # print(event) #вывод на экран всех действий игры

    pygame.quit()
    quit()

gameLoop()

