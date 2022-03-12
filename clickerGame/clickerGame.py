import pygame,os, sys
from pygame import mixer
from pygame.constants import MOUSEBUTTONDOWN
pygame.init()
pygame.mixer.init()
from pygame.display import update
from pygame.transform import scale

#screen options
width, height = 800,600
WIN = pygame.display.set_mode((width,height))
pygame.display.set_caption("Coffee maker")
font=pygame.font.SysFont('comic sans',40)
CYAN=(0,255,255)
BLACK=(0,0,0)
WHITE=(255,255,255)


#game setting
clock = pygame.time.Clock()
FPS = 60
clk=False
nbClicks=10000



#Assets png importing + scaling
normalBeanImage=pygame.image.load("cofbean.png"))#import bean png
normalBeanImage=pygame.transform.scale(normalBeanImage,(500,500))#scale bean
largeBeanImage=pygame.image.load(os.path.join("assets","norcofbean.png"))#import upgraded bean
largeBeanImage=pygame.transform.scale(largeBeanImage,(500,500))#scale upgraded bean
background=pygame.image.load(os.path.join("assets","background.png"))#import background
background=pygame.transform.scale(background,(width,height))#scale background
woodBackground=pygame.image.load(os.path.join("assets","woodback.png"))#import background
woodBackground=pygame.transform.scale(woodBackground,(400,700))#scale background
farmImage=pygame.image.load(os.path.join("assets","farm.png"))#need scaling
cofeMarchineImage=pygame.image.load(os.path.join("assets","cofmachine.png"))#need scaling
cupImage=pygame.image.load(os.path.join("assets","cup.png"))#need scaling
cupStart=pygame.transform.scale(cupImage,(300,300))#scale cup for menu
sugarImage=pygame.image.load(os.path.join("assets","sugar.png"))#need scaling
sugarStart=pygame.transform.scale(sugarImage,(300,300))#scale sugar for menu
shopImage=pygame.image.load(os.path.join("assets","shop.png"))#need scaling
startButtonImage=pygame.image.load(os.path.join("assets","startButton.png"))#import start button icon
startButtonImage=pygame.transform.scale(startButtonImage,(200,200))
optionsButtonImage=pygame.image.load(os.path.join("assets","optionButton.png"))#import option button icon
optionsButtonImage=pygame.transform.scale(optionsButtonImage,(200,200))
creditsButtonImage=pygame.image.load(os.path.join("assets","creditButton.png"))#import cerdits button icon
creditsButtonImage=pygame.transform.scale(creditsButtonImage,(200,200))
exitButtonImage=pygame.image.load(os.path.join("assets","exitButton.png"))#import exit button icon
exitButtonImage=pygame.transform.scale(exitButtonImage,(200,200))
backButtonImage=pygame.image.load(os.path.join("assets","backPannel.png"))#import back button icon
openUpgradeImage=pygame.image.load(os.path.join("assets","openUpgrades.png"))#import back button icon
unlockImage=pygame.image.load(os.path.join("assets","unlockIcon2.png"))#import back button icon
unlockImage=pygame.transform.scale(unlockImage,(350,150))
lvlupImage=pygame.image.load(os.path.join("assets","lvlupIcon.png"))#import back button icon
lvlupImage=pygame.transform.scale(lvlupImage,(350,150))
scorePannelImage=pygame.image.load(os.path.join("assets","scorePannel.png"))#import back button icon
scorePannelImage=pygame.transform.scale(scorePannelImage,(350,150))
coinImage=pygame.image.load(os.path.join("assets","coin.png"))
coinImage=pygame.transform.scale(coinImage,(80,80))
coinImage2=pygame.transform.scale(coinImage,(60,60))




#sound effects
bellSound=pygame.mixer.Sound(os.path.join("soundtracks","bell.mp3"))
elevatorMusic=pygame.mixer.Sound(os.path.join("soundtracks","elevetor.mp3"))
hipJazzMusic=pygame.mixer.Sound(os.path.join("soundtracks","hipJazz.mp3"))
royalJazzMusic=pygame.mixer.Sound(os.path.join("soundtracks","royalJazz.mp3"))
jazzPianoMusic=pygame.mixer.Sound(os.path.join("soundtracks","jazzPiano.mp3"))
jazzComedyMusic=pygame.mixer.Sound(os.path.join("soundtracks","jazzComedy.mp3"))


#text drawing fonction
def drawText(text,font,color,surface,x,y):
    textObj=font.render(str(text),1,color)
    textRect=textObj.get_rect()
    textRect.topleft=(x,y)
    surface.blit(textObj,textRect)




#menu fonction
def mainMenu():
    run=True
    #elevatorMusic.play() #loud
    while run:
        clock.tick(FPS)
        WIN.blit(background,(0,0))
        WIN.blit(cupStart,(450,150))
        mx,my=pygame.mouse.get_pos()
        drawText('Cofe Maker',font,BLACK,WIN,200,100)
        startGame=pygame.Rect(200,200,200,50)
        options=pygame.Rect(200,300,200,50)
        credits=pygame.Rect(200,400,200,50)
        exit=pygame.Rect(250,500,100,50)
        if startGame.collidepoint(mx,my):
            if clk:
                #pygame.mixer.pause()
                bellSound.play()
                game()
        if options.collidepoint(mx,my):
            if clk:
                bellSound.play()
                Options()
        if credits.collidepoint(mx,my):
            if clk:
                bellSound.play()
                Credits()
        if exit.collidepoint(mx,my):
            if clk:
                bellSound.play()
                sys.exit()

        WIN.blit(startButtonImage,(200,125))
        WIN.blit(optionsButtonImage,(200,225))
        WIN.blit(creditsButtonImage,(200,325))
        WIN.blit(exitButtonImage,(200,425))
        clk=False
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run=False
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    clk=True
        pygame.display.update()
    pygame.quit()


#game options 
def Options():
    running = True
    while running:
        clock.tick(FPS)
        WIN.blit(background,(0,0))
        mx,my=pygame.mouse.get_pos()
        back=pygame.Rect(10,10,50,50)
        WIN.blit(backButtonImage,(10,10))
        drawText('options', font, BLACK,WIN, 200, 100)
        if back.collidepoint(mx,my):
            if clk:
                bellSound.play()
                mainMenu()
        clk=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    clk=True
        
        pygame.display.update()
        
def Credits():
    running = True
    while running:
        clock.tick(FPS)
        mx,my=pygame.mouse.get_pos()
        WIN.blit(background,(0,0))
        back=pygame.Rect(10,10,50,50)
        WIN.blit(backButtonImage,(10,10))
        WIN.blit(sugarStart,(10,300))
        drawText('Credits',font,BLACK,WIN,350,100)
        drawText('music',font,BLACK,WIN,200,200)
        drawText('Bensound.com',font,BLACK,WIN,350,200)
        drawText('Music for Video Library',font,BLACK,WIN,350,300)
        if back.collidepoint(mx,my):
            if clk:
                bellSound.play()
                mainMenu()
        clk=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    clk=True
            
        pygame.display.update()
    


#main program
def game():
    global nbClicks
    running=True
    #royalJazzMusic.play() #music idk 
    WIN.blit(background,(0,0))
    n,r,w,u,a,b=0,0,0,0,0,0
    price1,price2,price3,price4,price5=100,1000,2000,5000,10000
    WIN.blit(woodBackground,(400,0))
    WIN.blit(unlockImage,(425,100))
    WIN.blit(unlockImage,(425,200))
    WIN.blit(unlockImage,(425,300))
    WIN.blit(unlockImage,(425,400))
    WIN.blit(unlockImage,(425,500))
    drawText(price1,font,BLACK,WIN,450,175)
    drawText(price2,font,BLACK,WIN,450,275)
    drawText(price3,font,BLACK,WIN,450,375)
    drawText(price4,font,BLACK,WIN,450,475)
    drawText(price5,font,BLACK,WIN,450,575)
    while running:
        pygame.display.update()
        clock.tick(FPS)
        price1=100+n*15
        price2=1000+r*150
        price3=2000+w*500
        price4=5000+u*800
        price5=10000+a*1500
        WIN.blit(coinImage2,(425,150))
        WIN.blit(coinImage2,(425,250))
        WIN.blit(coinImage2,(425,350))
        WIN.blit(coinImage2,(425,450))
        WIN.blit(coinImage2,(425,550))
        mx,my=pygame.mouse.get_pos()
        clkBean=pygame.Rect(212,255,100,100)
        WIN.blit(normalBeanImage,(0,0))
        quality=pygame.Rect(425,150,350,50)
        cup=pygame.Rect(425,250,350,50)
        sugar=pygame.Rect(425,350,350,50)
        machine=pygame.Rect(425,450,350,50)
        shop=pygame.Rect(425,550,350,50)
        WIN.blit(scorePannelImage,(425,0))
        WIN.blit(coinImage,(440,20))
        money=font.render(str(nbClicks),1,CYAN)
        WIN.blit(money,(500,50))

        if clkBean.collidepoint(mx,my):
            if cok:
                nbClicks=int(nbClicks+1)

        if quality.collidepoint(mx,my): #start of the upgrades 
            if cok and nbClicks>=price1:
                bellSound.play()
                n+=1
                WIN.blit(lvlupImage,(425,100))
                drawText(price1,font,BLACK,WIN,450,175)
                nbClicks-=100+n*15
                
        if cup.collidepoint(mx,my):
            if cok and nbClicks>=price2:
                bellSound.play()
                r+=1
                WIN.blit(lvlupImage,(425,200))
                drawText(price2,font,BLACK,WIN,450,275)
                nbClicks-=1000+r*150
                
        if sugar.collidepoint(mx,my):
            if cok and nbClicks>=price3:
                bellSound.play()
                w+=1
                WIN.blit(lvlupImage,(425,300))
                drawText(price3,font,BLACK,WIN,450,375)
                nbClicks-=2000+w*500
                
        if machine.collidepoint(mx,my):
            if cok and nbClicks>=price4:
                bellSound.play()
                u+=1
                WIN.blit(lvlupImage,(425,400))
                drawText(price4,font,BLACK,WIN,450,475)
                nbClicks-=5000+u*800
                
        if shop.collidepoint(mx,my):
            if cok and nbClicks>=price5:
                bellSound.play()
                a+=1
                WIN.blit(lvlupImage,(425,500))
                drawText(price5,font,BLACK,WIN,450,575)
                nbClicks-=10000+a*1500
        cok=False
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                running=False
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:   
                if event.button==1:
                    cok=True
        
    pygame.quit()
    sys.exit()


mainMenu() #start

