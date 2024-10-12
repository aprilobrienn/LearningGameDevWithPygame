import pygame

pygame.init()

SCREEN_WIDTH = 800 
SCREEN_HEIGHT = 600 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fox Game Practice")

fox = pygame.image.load("foxright1.png").convert_alpha() #will find 'foxright1.png' in folder so that 
#fox is set to look like 'foxright1.png.png'
#.convert_alpha ensures that the transparent backgrounf that foxright1.png originally has

foxright = [pygame.image.load("foxright1.png"),
            pygame.image.load("foxright2.png"), #groups the right-facing fox images together
            pygame.image.load("foxright3.png")]

foxleft = [pygame.image.load("foxleft1.png"),
           pygame.image.load("foxleft2.png"), #groups the left-facing fox images together
           pygame.image.load("foxleft3.png")]

foxup = [pygame.image.load("foxup1.png"),
         pygame.image.load("foxup2.png"), #groups the up-facing fox images together
         pygame.image.load("foxup3.png")]

foxdown = [pygame.image.load("foxdown1.png"),
           pygame.image.load("foxdown2.png"), #groups the down-facing fox images together
           pygame.image.load("foxdown3.png")]

rect_1 = pygame.Rect(200, 100, 150, 100) #x,y,width,height
rect_1.width = 400 #this will change the width of rect_1
rect_1.height = 150 #this will change the height of rect_1
print(rect_1) #will output the data from the rectangle

rect_2 = fox.get_rect() #rect_2 will match the sixe of the fox variable
print (rect_2) #will output the data from the second rectangle which will be the fox
rect_2.topleft = (200, 200) #rectangle topleft moved 200,200
#other commands, topleft midleft, bottomleft, midtop,center, midbottom etc
#can also pass  individual coordinates eg left = (200) so only x coordinate changes


clock = pygame.time.Clock() 

run = True
while run:

    clock.tick(60)

    screen.fill((173, 216, 230)) #fill screen with light blue colour

    #screen.blit(fox, (0, 0)) #will put the fox at coordinates 0,0
    screen.blit(fox, rect_2) #this will put the fox at same coordinates as rect_2

    #creating controls for the rect_2/fox sprite
    key = pygame.key.get_pressed()

    if key[pygame.K_a] == True: #if statement for pressing 'a' key
        rect_2.move_ip(-5, 0) #variable will move ip(in place) x -5, y 0 aka left
    elif key[pygame.K_d] == True: #else if statement for 'd' key
        rect_2.move_ip(+5, 0) 
    elif key[pygame.K_w] == True: #else if statement for 'w' key
        rect_2.move_ip(0, -5) 
    elif key[pygame.K_s] == True: #else if statement for 's' key
        rect_2.move_ip(0, +5) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()