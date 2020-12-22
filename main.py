import pygame
import random

pygame.mixer.init()
pygame.init()

#Creating the screen
screen_x = 500
screen_y = 500
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("SNAKE GAME")

#Loading images
background_image = pygame.image.load("bg.jpg")
snake_image = pygame.image.load("bg2.png")
gameover_image = pygame.image.load("gameover1.png")

font = pygame.font.SysFont(None,40)
clock = pygame.time.Clock()
pygame.display.update()

#Defining colors
red = (255,0,0)
black= (0,0,0)
white= (255,255,255)
text_color=(237, 233, 12)

def font_screen(text, color, x, y):
    score_text = font.render(text, True, color)
    screen.blit(score_text, [x,y])

def draw_snake(screen, color, snake_list, snake_size):
    for x,y in snake_list:
        snake_rect = pygame.Rect([x, y, snake_size, snake_size])
        pygame.draw.rect(screen, red, snake_rect)

def welcome_screen():
    exit_game= False
    while not exit_game:
        screen.blit(background_image, [0, 0])
        font_screen("SNAKE GAME WITH RAVEENA",black,50,200)
        font_screen("Press ENTER to START",pygame.Color('blue'),95,230)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load('Lagoon - AShamaluevMusic.mp3')
                    pygame.mixer.music.play(100)
                    loop()
        pygame.display.update()
        clock.tick(60)

def loop():
    snake_x = 25
    snake_y = 55
    snake_size = 25
    food_x = 45
    food_y = 45
    velocity_x = 0
    velocity_y = 0
    score= 0
    snake_list= []
    snake_length= 1
    red = (255,0,0)
    with open("highscore.txt", "r") as f:
        highscore = f.read()
    running = True
    game_over= False
    food_x = random.randint(20,screen_x/2)
    food_y = random.randint(20,screen_y/2)
    while running:
        if game_over:
            with open("highscore.txt","w") as f:
               f.write(str(highscore))
            screen.blit(gameover_image,[0,0])
            font_screen("GAME OVER!!",red,screen_x/2-90,screen_y/2-50)
            font_screen("Press ENTER to continue",(37, 12, 166),screen_x/2-160,screen_y/2-10)
            font_screen("Press ESCAPE to quit", (37, 12, 166),screen_x/2-140,screen_y/2+20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome_screen()

                    if event.key == pygame.K_ESCAPE:
                        running = False

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 1.5
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -1.5
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -1.5
                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = 1.5
                    #if event.key == pygame.K_r:   #cheat code
                    #    score +=5
            snake_x = snake_x +velocity_x
            snake_y = snake_y +velocity_y

            if abs(snake_x - food_x) <9 and abs(snake_y - food_y) <9:
                    score += 10
                    food_x = random.randint(20, screen_x /2)
                    food_y = random.randint(20, screen_y /2)
                    snake_length+=10
                    if score>int(highscore):
                        highscore= score

            screen.blit(snake_image, [0, 0])
            font_screen("SCORE: " + str(score) +"            "+ "HIGH SCORE: " + str(highscore) ,text_color, 5, 5)

            food_rect = pygame.Rect([food_x,food_y, snake_size, snake_size])
            pygame.draw.rect(screen, pygame.Color('black'), food_rect)

            snake_head= []
            snake_head.append(snake_x)
            snake_head.append(snake_y)
            snake_list.append(snake_head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if snake_head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('Explosion+4.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_x or snake_y<0 or snake_y>screen_y:
                game_over = True
                pygame.mixer.music.load('Explosion+4.mp3')
                pygame.mixer.music.play()

            draw_snake(screen,red, snake_list, snake_size)

        clock.tick(60)
        pygame.display.update()
    pygame.quit()
    quit()
welcome_screen()