import pygame

pygame.init()

SCREEN_WIDTH = 800 #336
SCREEN_HEIGHT = 600 #236

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fox Game Practice")

fox = pygame.image.load("foxright1.png").convert_alpha() #will find 'foxright1.png' in folder so that 
#fox is set to look like 'foxright1.png.png'
#.convert_alpha ensures that the transparent backgrounf that foxright1.png originally has

foxright = [pygame.image.load("foxright1.png"),
            pygame.image.load("foxright2.png"), #groups the right-facing fox images together
            pygame.image.load("foxright1.png"),
            pygame.image.load("foxright3.png")]

foxleft = [pygame.image.load("foxleft1.png"),
           pygame.image.load("foxleft2.png"), #groups the left-facing fox images together
           pygame.image.load("foxleft1.png"),
           pygame.image.load("foxleft3.png")]

foxup = [pygame.image.load("foxup1.png"),
         pygame.image.load("foxup2.png"), #groups the up-facing fox images together
         pygame.image.load("foxup1.png"),
         pygame.image.load("foxup3.png")]

foxdown = [pygame.image.load("foxdown1.png"),
           pygame.image.load("foxdown2.png"), #groups the down-facing fox images together
           pygame.image.load("foxdown1.png"),
           pygame.image.load("foxdown3.png")]

current_direction = "down"
current_sprites = foxdown

background_image = pygame.image.load("temp.png") #defines variable background_image
background_rec = background_image.get_rect(center = [SCREEN_WIDTH//2,SCREEN_HEIGHT//2]) #defines background_rec, in centre at a size of half screen wdith/height

fox_rect = foxright[0].get_rect() 
fox_rect.x = 366
fox_rect.y = 236

speed = 5 #movement speed is set to 5
frame_rate = 10

background_x = 0
background_y = 0
current_frame = 0

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

    

    #screen.blit(fox, (0, 0)) #will put the fox at coordinates 0,0
    screen.blit(fox, rect_2) #this will put the fox at same coordinates as rect_2

    #creating controls for the rect_2/fox sprite
    key = pygame.key.get_pressed()

    if key[pygame.K_a] == True: #if statement for pressing 'a' key
        current_direction = "left"
        current_sprites = foxleft
        current_frame += 0.2 #it cant non-whole numbers so this being 0.2 will go to 0.4 etc until it can round to nearest whole number(1), then 1.2..... and so on. This is good because otherwise character cycles through animations too quickly
        background_x += speed #will move backgrounds x coords by minus speed (which is set to 5 right now)
        #rect_2.move_ip(-5, 0) #variable will move ip(in place) x -5, y 0 aka left
    elif key[pygame.K_d] == True: #else if statement for 'd' key
        current_direction = "right"
        current_sprites = foxright
        current_frame += 0.2
        background_x -= speed #will move backgrounds x coords by plus speed (which is set to 5 right now)
        #rect_2.move_ip(+5, 0) 
    elif key[pygame.K_w] == True: #else if statement for 'w' key
        current_direction = "up"
        current_sprites = foxup
        current_frame += 0.2
        background_y += speed #will move backgrounds y coords by minus speed (which is set to 5 right now)
        #rect_2.move_ip(0, -5) 
    elif key[pygame.K_s] == True: #else if statement for 's' key
        current_direction = "down"
        current_sprites = foxdown
        current_frame += 0.2
        background_y -= speed #will move backgrounds y coords by plus speed (which is set to 5 right now)
        #rect_2.move_ip(0, +5) 

        
    screen.fill((173, 216, 230)) #fill screen with light blue colour

    if current_frame >= len(current_sprites): #if the current frame greater than/equal to current sprites
        current_frame = 0 #the frame will be set back to 0 so that the "idle" sprite is shown
    if current_frame == 4: #fail safe in case first if statement doesnt work
        current_frame = 0

    screen.blit(background_image, (background_x, background_y)) #blits the background image onto the screen
    screen.blit(current_sprites[int(current_frame)], fox_rect) #blits the sprite group onto the screen // int will make it so that the decimal 0.2 from earlier is rounded
#will blit the current spites to the closest int, to display current_frame, using fox_rect


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

    clock.tick(30) #will run at 30 fps

pygame.quit()