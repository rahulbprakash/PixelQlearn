import pygame, sys
from pygame.locals import *
import random

#Frames per second
FPS = 200
REWARD =10
#window features
WINDOWWIDTH = 200
WINDOWHEIGHT = 200
#paddle features
LINETHICKNESS = 10
PADDLESIZE = 50
PADDLEOFFSET = 20

#colours
BLACK     = (0  ,0  ,0  )
WHITE     = (255,255,255)

def drawArena():
    DISPLAYSURF.fill((0,0,0))
    #pygame.draw.rect(DISPLAYSURF, WHITE, ((0,0),(WINDOWWIDTH,WINDOWHEIGHT)), LINETHICKNESS*2)
    #vertical lines
    pygame.draw.line(DISPLAYSURF, WHITE,  (0,0) , (0,WINDOWHEIGHT-LINETHICKNESS)  ,(LINETHICKNESS*2))
    #Horizontal lines
    pygame.draw.line(DISPLAYSURF, WHITE,  (0,0) , (WINDOWWIDTH-LINETHICKNESS , 0)  ,(LINETHICKNESS*2))
    pygame.draw.line(DISPLAYSURF, WHITE,  (0,WINDOWHEIGHT) , (WINDOWWIDTH-LINETHICKNESS , WINDOWHEIGHT)  ,(LINETHICKNESS*2))

def drawBall(ball):
    pygame.draw.rect(DISPLAYSURF, WHITE, ball)

#moves the ball returns new position
def moveBall(ball, ballDirX, ballDirY):
    ball.x += ballDirX
    ball.y += ballDirY
    return ball

def drawPaddle(paddle):
    #Stops paddle moving too low
    if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
        paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
    #Stops paddle moving too high
    elif paddle.top < LINETHICKNESS:
        paddle.top = LINETHICKNESS
    #Draws paddle
    pygame.draw.rect(DISPLAYSURF, WHITE, paddle)


def checkEdgeCollision(ball, ballDirX, ballDirY):
    update = 0
    if ball.top == (LINETHICKNESS) or ball.bottom == (WINDOWHEIGHT - LINETHICKNESS):
        ballDirY = ballDirY * -1
    if ball.left == (LINETHICKNESS):
        ballDirX = ballDirX * -1   
    if ball.right == (WINDOWWIDTH - LINETHICKNESS):
        update = -1
        #print(REWARD)
        ballDirX = ballDirX * -1
    
    return ballDirX , ballDirY ,update

def checkHitBall(ball, paddle, ballDirX):
    if ballDirX == 1 and paddle.left == ball.right and paddle.top < ball.top and paddle.bottom > ball.bottom:
        #REWARD += 1
        return -1
    else: 
        return 1

def main():
    pygame.init()
    global DISPLAYSURF
    #REWARD

    REWARD = 0
    print(REWARD)
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 
    pygame.display.set_caption('lol')
    playerOnePosition = (WINDOWHEIGHT - PADDLESIZE) /2

    #REWARD = 0
    #Ball properties
    ballX = WINDOWWIDTH/2 - LINETHICKNESS/2
    ballY = WINDOWHEIGHT/2 - LINETHICKNESS/2
    #Initial movement dirs
    ballDirX = -1 ## -1 = left 1 = right # NOTE: it should be an odd number!':('
    ballDirY = 0
    
    #paddle properties
    paddle = pygame.Rect(WINDOWWIDTH - PADDLEOFFSET - LINETHICKNESS, playerOnePosition, LINETHICKNESS,PADDLESIZE)



    #Initialize all objexts on the arena
    ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)
    
    drawArena()
    drawPaddle(paddle)
    drawBall(ball)

    #MAIN GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                paddle.y = mousey

        drawArena()
        #NOTE:check order is nessacary for next two lines
        
        ball = moveBall(ball, ballDirX, ballDirY)
        ballDirX, ballDirY , REWARD_update = checkEdgeCollision(ball, ballDirX, ballDirY)
        REWARD += REWARD_update 
        if(checkHitBall(ball, paddle, ballDirX) == -1):
            ballDirX = ballDirX * -1#checkHitBall(ball, paddle, ballDirX)
            REWARD = REWARD + 1
        print(REWARD)
        
        drawBall(ball)
        drawPaddle(paddle)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__=='__main__':
    main()
