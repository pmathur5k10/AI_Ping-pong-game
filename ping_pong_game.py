import pygame
#Used for GUI game development in python
import random
#used to randomise the starting location of the ball

#initialising the game environment
#frames per second for the game// frame rate
FPS=60

#dimensioms of the game window
WINDOW_WIDTH=400
WINDOW_HEIGHT=400

#dimensions of ball, visualised as a small rectangle
BALL_WIDTH=10
BALL_HEIGHT=10

#dimensions of paddle
PADDLE_BUFFER=10
#the istance between window edge and paddle
PADDLE_WIDTH=10
PADDLE_HEIGHT=60

#speed of ball in x and y direction motion in 2d space
BALL_X_SPEED=3
BALL_Y_SPEED=2

#speed of paddle in y direction
PADDLE_SPEED=2

#setting up the game screen of requisite dimensions
screen=pygame.display.set_mode(WINDOW_WIDTH,WINDOW_HEIGHT)


#RGB colors of game
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)



def drawBall(BALL_X_POS,BALL_Y_POS):

	ball=pygame.Rect(BALL_X_POS,BALL_Y_POS,BALL_WIDTH,BALL_HEIGHT)
	pygame.draw.rect(screen,RED,ball)



def drawPaddle1(PADDLE_Y_POSITION):
	paddle1=pygame.Rect(PADDLE_BUFFER,PADDLE_Y_POSITION,PADDLE_WIDTH,PADDLE_HEIGHT)
	pygame.draw.rect(screen,WHITE,paddle1)



def drawPaddle2(PADDLE_Y_POSITION):
	paddle2=pygame.Rect(WINDOW_WIDTH- PADDLE_BUFFER- PADDLE_WIDTH,PADDLE_Y_POSITION,PADDLE_WIDTH,PADDLE_HEIGHT)
	pygame.draw.rect(screen,BLUE,paddle2)



def updateBall(Paddle1_Y_Pos,Paddle2_Y_Pos,Ball_X_Pos,Ball_Y_Pos,Ball_X_Direction,Ball_Y_Direction):


	#update the position of the ball
	Ball_X_Pos=Ball_X_Pos+ Ball_X_Direction* BALL_X_SPEED
	Ball_Y_Pos=Ball_Y_Pos+ Ball_Y_Direction* BALL_Y_SPEED
	#set score to zero
	score=0

	#update the ball direction and score if it touches the left paddle
	if(Ball_X_Pos<=PADDLE_BUFFER+ PADDLE_WIDTH and Ball_Y_Pos+ BALL_HEIGHT>=Paddle1_Y_Pos and Ball_Y_Pos- BALL_HEIGHT<= Paddle1_Y_Pos + PADDLE_HEIGHT ):
		Ball_Y_Direction=1
	
	
	elif(Ball_X_Pos<=0):
		Ball_X_Direction=1
		score= -1
		return [score,Paddle1_Y_Pos,Paddle2_Y_Pos,Ball_X_Pos,Ball_Y_Pos,Ball_X_Direction,Ball_Y_Direction]	


	

	#update the ball direction and score if the ball touches the right paddle
	if(Ball_X_Pos>=WINDOW_WIDTH- PADDLE_WIDTH- PADDLE_BUFFER and Ball_X_Pos+ BALL_HEIGHT>=Paddle2_Y_Pos and Ball_Y_Pos - BALL_HEIGHT<= Paddle2_Y_Pos+ PADDLE_HEIGHT):
		Ball_X_Direction= -1

	
	elif(Ball_X_Pos>=WINDOW_WIDTH- BALL_WIDTH):
		Ball_X_Direction=1
		score=1
		return [score,Paddle1_Y_Pos,Paddle2_Y_Pos,Ball_X_Pos,Ball_Y_Pos,Ball_X_Direction,Ball_Y_Direction]

	
	#update the ball direction and position if it touches the upper or lower edge of the window
	if (Ball_Y_Pos<=0):
		Ball_Y_Direction=1
		Ball_Y_Pos=0

	
	elif(Ball_Y_Pos>=WINDOW_HEIGHT- BALL_HEIGHT):
		Ball_Y_Pos=WINDOW_HEIGHT- BALL_HEIGHT
		Ball_Y_Direction=-1

	return [score,Paddle1_Y_Pos,Paddle2_Y_Pos,Ball_X_Pos,Ball_Y_Pos,Ball_X_Direction,Ball_Y_Direction]



def updatePaddle1(action,Paddle1Pos):

	#move down
	if(action[1]==1):
		Paddle1Pos=Paddle1Pos- PADDLE_SPEED

	#move up
	if(action[2]==1):
		Paddle1Pos=Paddle1Pos- PADDLE_SPEED

	#applying boundary conditions
	if(Paddle1Pos<0):
		Paddle1Pos=0

	
	
	if(Paddle1Pos>WINDOW_HEIGHT- PADDLE_WIDTH):
		Paddle1Pos=WINDOW_HEIGHT- PADDLE_WIDTH

	return Paddle1Pos	


def updatePaddle2(BallPos,Paddle2Pos):

	if(Paddle2Pos+ PADDLE_HEIGHT/2< BallPos+ BALL_HEIGHT/2):
		Paddle2Pos=Paddle2Pos + PADDLE_SPEED

	
	if(Paddle2Pos+ PADDLE_HEIGHT/2 > BallPos + BALL_HEIGHT/2):
		Paddle2Pos= Paddle2Pos + PADDLE_SPEED

	if(Paddle2Pos<0):
		Paddle2Pos=0

	
	
	if(Paddle2Pos>WINDOW_HEIGHT- PADDLE_WIDTH):
		Paddle2Pos=WINDOW_HEIGHT- PADDLE_WIDTH

	return Paddle2Pos




class PongGame:
	def __init__(self):

		self.tally=0
		self.Paddle1_Y_Pos=WINDOW_HEIGHT/2 + PADDLE_HEIGHT/2 
		self.Paddle2_Y_Pos=WINDOW_HEIGHT/2 + PADDLE_HEIGHT/2

		self.Ball_X_Pos=WINDOW_WIDTH/2

		num=random.randint(0,9)

		self.Ball_Y_Pos=num*(WINDOW_HEIGHT)/9

		if(num<=2 && num>=0):
			self.Ball_X_Direction=1
			self.Ball_Y_Direction=1

		
		if(num>=3 && num<=5):
			self.Ball_X_Direction=-1
			self.Ball_Y_Direction=1

		
		if(num>=6 && num<=7):
			self.Ball_X_Direction=1
			self.Ball_Y_Direction=-1

		
		
		if(num>=8 && num<=9):
			self.Ball_X_Direction=-1
			self.Ball_Y_Direction=-1

		

	def getPresentFrame(self):

		pygame.event.pump()
		screen.fill(BLACK)

		drawPaddle1(self.Paddle1_Y_Pos)

		drawPaddle2(self.Paddle2_Y_Pos)

		drawBall(self.Ball_X_Pos,self.Ball_Y_Pos)

		image_data=pygame.surfarray.array3d(pygame.display.get_surface())

		pygame.display.flip()


	
	
	def getNextFrame(self,action):

		pygame.event.pump()
		screen.fill(BLACK)

		score=0


		self.Paddle1_Y_Pos=updatePaddle1(action,self.Paddle1_Y_Pos)
		drawPaddle1(Paddle1_Y_Pos)

		self.Paddle2_Y_Pos=updatePaddle2(Ball_Y_Pos,Paddle2_Y_Pos)
		drawPaddle2(Paddle2_Y_Pos)

		[score,Paddle1_Y_Pos,Paddle2_Y_Pos,Ball_X_Pos,Ball_Y_Pos,Ball_X_Direction,Ball_Y_Direction] = updateBall(Paddle1_Y_Pos,Paddle2_Y_Pos,Ball_X_Pos,Ball_Y_Pos,Ball_X_Direction,Ball_Y_Direction)

		drawBall(Ball_X_Pos,Ball_Y_Pos)

		image_data=pygame.surfarray.array3d(pygame.display.get_surface())

		pygame.display.flip()\

		self.tally = self.tally + score

		print "Tally is " + str(self.tally)

		return [score,image_data]






		








		








	


		












