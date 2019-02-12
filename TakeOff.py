import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound('crashsound.ogg')
pygame.mixer.music.load('Game music 1.mp3')

display_width = 1000
display_height = 700

bgcrash = pygame.image.load('crashed.png')

black = (50, 50, 50)
white = (255, 255, 255)
red = (165, 42, 42)
hoverred = (180, 36, 36)
green = (113, 148, 41)
hovergreen = (34, 139, 34)
blue = (25, 25, 112) 
hoverblue = (5, 5, 132)
purple = (106, 90, 205)
hoverpurple = (132, 112, 255)

iconimg = pygame.image.load('spaceshipicon.png')
rocketImg = pygame.image.load('spaceshipdefault.png')
helione = pygame.image.load('Helicopter.png')
jet = pygame.image.load('Jet.png')
sata = pygame.image.load('Satalite.png')
bird = pygame.image.load('Bird 1.png')
pausedbg = pygame.image.load('bgpaused.png')
crashbg = pygame.image.load('crashed.png')
levelbg = pygame.image.load('levelbg.png')
bgend = pygame.image.load('endbg.png')

pygame.display.set_icon(iconimg)

pause = False
#crash = True
victory = False

rocket_width = 135
rocket_height = 250

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Take-Off')
clock = pygame.time.Clock()


def victory():

    victory = True
    while victory:
        gameDisplay.blit(bgend, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        largeText = pygame.font.Font('ARCADECLASSIC.ttf', 90)
        TextSurf, TextRect = text_objects("Victory!", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        button(" Again?", 150, 560, 100, 50, purple, hoverpurple, level_one)
        button(" Quit!", 750, 560, 100, 50, purple, hoverpurple, quitgame)
    
        pygame.display.update()
        clock.tick(15)

def elevation(km):
    font = pygame.font.Font('ARCADECLASSIC.ttf', 30)
    text = font.render("Kilometres: " + str(km), True, black)
    gameDisplay.blit(text, (1, 1))

def things(thing_startx, thing_starty, image):
    gameDisplay.blit(image, (thing_startx, thing_starty))

def message_display(text):
    largeText = pygame.font.Font('ARCADECLASSIC.ttf', 60)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(3)

    level_one()

def crash():
    pygame.mixer.Sound.play(crash_sound)
    
    while True:
        gameDisplay.blit(crashbg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        largeText = pygame.font.Font('ARCADECLASSIC.ttf', 60)
        TextSurf, TextRect = text_objects("CRASH! Game Over!", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        
        button(" Again?", 150, 560, 100, 50, red, hoverred, level_one)
        button(" Quit!", 750, 560, 100, 50, red, hoverred, quitgame)

        pygame.display.flip()
        clock.tick(15)

def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font('ARCADECLASSIC.ttf', 25)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    

def paused():

    pygame.mixer.music.pause()
    
    while pause:
        pausedbg = pygame.image.load('bgpaused.png')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.blit(pausedbg, (0, 0))
        largeText = pygame.font.Font('ARCADECLASSIC.ttf', 60)
        TextSurf, TextRect = text_objects(" Game Paused", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        button(" Go on!", 150, 560, 100, 50, blue, hoverblue, unpause)
        button(" Quit!", 750, 560, 100, 50, blue, hoverblue, quitgame)

        pygame.display.update()
        clock.tick(15)

def quitgame():
    pygame.quit()
    quit()

def game_intro():
    pygame.mixer.music.play(-1)
    
    intro = True

    while intro:
        bgintro = pygame.image.load('introbg.png')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.blit(bgintro, (0, 0))
        largeText = pygame.font.Font('ARCADECLASSIC.ttf', 60)
        TextSurf, TextRect = text_objects(" Take Off", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        button(" Play!", 150, 560, 100, 50, green, hovergreen, level_one)
        button(" Quit!", 750, 560, 100, 50, green, hovergreen, quitgame)

        pygame.display.update()
        clock.tick(15)
    

def level_one():
    global pause
    
    def rocket(x, y):
        gameDisplay.blit(rocketImg, (x, y))

    rocketImg = pygame.image.load('spaceshipdefault.png')
    bgone = pygame.image.load('levelone.png')
    bgtwo = pygame.image.load('leveltwo.png')
    bgthree = pygame.image.load('levelthree.png')
    bgfour = pygame.image.load('levelfour.png')
    bgend = pygame.image.load('endbg.png')
    bgintro = pygame.image.load('introbg.png')
    bgcrash = pygame.image.load('crashed.png')
    rocketleft = pygame.image.load('spaceshipleft.png')
    rocketright = pygame.image.load('spaceshipright.png')
    rocketup = pygame.image.load('spaceshiphigh.png')
    rocketdown = pygame.image.load('spaceshiplow.png')
    helione = pygame.image.load('Helicopter.png')
    jet = pygame.image.load('Jet.png')
    sata = pygame.image.load('Satalite.png')
    bird = pygame.image.load('Bird 1.png')

    x = (display_width * 0.45)
    y = (display_height * 0.47)

    height = 0

    x_change = 0
    y_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -750
    thing_speed = 6.4
    thing_height = 75
    thing_width = 100

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -8.6
                    rocketImg = rocketleft
                elif event.key == pygame.K_RIGHT:
                    x_change = 8.6
                    rocketImg = rocketright
                elif event.key == pygame.K_UP:
                    y_change = -8.6
                    rocketImg = rocketup
                elif event.key == pygame.K_DOWN:
                    y_change = 8.6
                    rocketImg = rocketdown
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change       
        gameDisplay.blit(bgone, (0, 0))

        things(thing_startx, thing_starty, bird)
        thing_starty += thing_speed
        
        rocket(x, y)
        elevation(height)

        if x > display_width - rocket_width or x < 0:
            crash()
        elif y > display_height - rocket_height or y < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            height += 2
            thing_speed += 0.43

        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width and not y + rocket_height < thing_starty + thing_height or x + rocket_width > thing_startx and x + rocket_width < thing_startx + thing_width and not y + rocket_height < thing_starty + thing_height :
                crash()
        if height == 20:
            level_two()
 
        pygame.display.flip()                
        clock.tick(70)

def level_two():
    gameDisplay.blit(levelbg, (0, 0))
    largeText = pygame.font.Font('ARCADECLASSIC.ttf', 90)
    TextSurf, TextRect = text_objects("Level Two", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    global pause
    
    def rocket(x, y):
        gameDisplay.blit(rocketImg, (x, y))

    rocketImg = pygame.image.load('spaceshipdefault.png')
    bgone = pygame.image.load('levelone.png')
    bgtwo = pygame.image.load('leveltwo.png')
    bgthree = pygame.image.load('levelthree.png')
    bgfour = pygame.image.load('levelfour.png')
    bgend = pygame.image.load('endbg.png')
    bgintro = pygame.image.load('introbg.png')
    bgcrash = pygame.image.load('crashed.png')
    rocketleft = pygame.image.load('spaceshipleft.png')
    rocketright = pygame.image.load('spaceshipright.png')
    rocketup = pygame.image.load('spaceshiphigh.png')
    rocketdown = pygame.image.load('spaceshiplow.png')
    helione = pygame.image.load('Helicopter.png')
    jet = pygame.image.load('Jet.png')
    sata = pygame.image.load('Satalite.png')
    bird = pygame.image.load('Bird 1.png')

    x = (display_width * 0.45)
    y = (display_height * 0.47)

    height = 20

    x_change = 0
    y_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -750
    thing_speed = 7
    thing_height = 70
    thing_width = 140

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -9.2
                    rocketImg = rocketleft
                elif event.key == pygame.K_RIGHT:
                    x_change = 9.2
                    rocketImg = rocketright
                elif event.key == pygame.K_UP:
                    y_change = -9.2
                    rocketImg = rocketup
                elif event.key == pygame.K_DOWN:
                    y_change = 9.2
                    rocketImg = rocketdown
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change       
        gameDisplay.blit(bgtwo, (0, 0))

        things(thing_startx, thing_starty, helione)
        thing_starty += thing_speed
        
        rocket(x, y)
        elevation(height)

        if x > display_width - rocket_width or x < 0:
            crash()
        elif y > display_height - rocket_height or y < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            height += 2
            thing_speed += 0.43

        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width and not y + rocket_height < thing_starty + thing_height or x + rocket_width > thing_startx and x + rocket_width < thing_startx + thing_width and not y + rocket_height < thing_starty + thing_height :
                crash()
        if height == 40:
            level_three()
            
 
        pygame.display.flip()                
        clock.tick(70)

def level_three():
    gameDisplay.blit(levelbg, (0, 0))
    largeText = pygame.font.Font('ARCADECLASSIC.ttf', 90)
    TextSurf, TextRect = text_objects("Level Three", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    global pause
    
    def rocket(x, y):
        gameDisplay.blit(rocketImg, (x, y))

    rocketImg = pygame.image.load('spaceshipdefault.png')
    bgone = pygame.image.load('levelone.png')
    bgtwo = pygame.image.load('leveltwo.png')
    bgthree = pygame.image.load('levelthree.png')
    bgfour = pygame.image.load('levelfour.png')
    bgend = pygame.image.load('endbg.png')
    bgintro = pygame.image.load('introbg.png')
    bgcrash = pygame.image.load('crashed.png')
    rocketleft = pygame.image.load('spaceshipleft.png')
    rocketright = pygame.image.load('spaceshipright.png')
    rocketup = pygame.image.load('spaceshiphigh.png')
    rocketdown = pygame.image.load('spaceshiplow.png')
    helione = pygame.image.load('Helicopter.png')
    jet = pygame.image.load('Jet.png')
    sata = pygame.image.load('Satalite.png')
    bird = pygame.image.load('Bird 1.png')

    x = (display_width * 0.45)
    y = (display_height * 0.47)

    height = 40

    x_change = 0
    y_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -750
    thing_speed = 7.2
    thing_height = 120
    thing_width = 260

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -9.8
                    rocketImg = rocketleft
                elif event.key == pygame.K_RIGHT:
                    x_change = 9.8
                    rocketImg = rocketright
                elif event.key == pygame.K_UP:
                    y_change = -9.8
                    rocketImg = rocketup
                elif event.key == pygame.K_DOWN:
                    y_change = 9.8
                    rocketImg = rocketdown
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change       
        gameDisplay.blit(bgthree, (0, 0))

        things(thing_startx, thing_starty, jet)
        thing_starty += thing_speed
        
        rocket(x, y)
        elevation(height)

        if x > display_width - rocket_width or x < 0:
            crash()
        elif y > display_height - rocket_height or y < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            height += 2
            thing_speed += 0.43

        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width and not y + rocket_height < thing_starty + thing_height or x + rocket_width > thing_startx and x + rocket_width < thing_startx + thing_width and not y + rocket_height < thing_starty + thing_height :
                crash()
        if height == 60:
            level_four()
            
 
        pygame.display.flip()                
        clock.tick(70)

def level_four():
    gameDisplay.blit(levelbg, (0, 0))
    largeText = pygame.font.Font('ARCADECLASSIC.ttf', 90)
    TextSurf, TextRect = text_objects("Level Four", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    global pause
    
    def rocket(x, y):
        gameDisplay.blit(rocketImg, (x, y))

    rocketImg = pygame.image.load('spaceshipdefault.png')
    bgone = pygame.image.load('levelone.png')
    bgtwo = pygame.image.load('leveltwo.png')
    bgthree = pygame.image.load('levelthree.png')
    bgfour = pygame.image.load('levelfour.png')
    bgend = pygame.image.load('endbg.png')
    bgintro = pygame.image.load('introbg.png')
    bgcrash = pygame.image.load('crashed.png')
    rocketleft = pygame.image.load('spaceshipleft.png')
    rocketright = pygame.image.load('spaceshipright.png')
    rocketup = pygame.image.load('spaceshiphigh.png')
    rocketdown = pygame.image.load('spaceshiplow.png')
    helione = pygame.image.load('Helicopter.png')
    jet = pygame.image.load('Jet.png')
    sata = pygame.image.load('Satalite.png')
    bird = pygame.image.load('Bird 1.png')

    x = (display_width * 0.45)
    y = (display_height * 0.47)

    height = 60

    x_change = 0
    y_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -750
    thing_speed = 7.5
    thing_height = 210
    thing_width = 250

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -11
                    rocketImg = rocketleft
                elif event.key == pygame.K_RIGHT:
                    x_change = 11
                    rocketImg = rocketright
                elif event.key == pygame.K_UP:
                    y_change = -11
                    rocketImg = rocketup
                elif event.key == pygame.K_DOWN:
                    y_change = 11
                    rocketImg = rocketdown
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change       
        gameDisplay.blit(bgfour, (0, 0))

        things(thing_startx, thing_starty, sata)
        thing_starty += thing_speed
        
        rocket(x, y)
        elevation(height)

        if x > display_width - rocket_width or x < 0:
            crash()
        elif y > display_height - rocket_height or y < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            height += 2
            thing_speed += 0.43

        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width and not y + rocket_height < thing_starty + thing_height or x + rocket_width > thing_startx and x + rocket_width < thing_startx + thing_width and not y + rocket_height < thing_starty + thing_height :
                crash()
        if height == 80:
            victory()
            
 
        pygame.display.flip()                
        clock.tick(70)


game_intro()
level_one()
pygame.quit()
quit()
