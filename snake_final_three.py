import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (6, 232, 122)
green = (0,0,0)
blue = (232, 6, 51)

firstPart = (66, 49, 17)
secondPart = (186, 143, 132)

gameDisplay = pygame.display.set_mode((800,600))
#gameDisplay = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption('Snake Game')

pygame.display.update()

clock = pygame.time.Clock()

font = pygame.font.SysFont('Courier New' , 15)

fixedX = 200
fixedY = 300

def finish_message(msg,color):
	screen_text = font.render(msg,True,color)
	gameDisplay.blit(screen_text,[fixedX-100,fixedY])
	
def check(X,Y):
	if( ( X > 0 and X < 795 ) and ( Y > 0 and Y < 595 ) ):
		return False
	else :
		return True
		
def makeRandomX(randAppleX):
	#return random.randrange(1,8)*100
	#temp = round(random.randrange(100,800)/10.0)*10
	temp = random.randrange(1,8)*100
	while temp == randAppleX :
		temp = random.randrange(1,8)*100
	return temp 
	
	
def makeRandomY(randAppleY):
	#return random.randrange(1,6)*100
	#temp = round(random.randrange(100,600)/10.0)*10
	temp = random.randrange(1,6)*100
	while temp == randAppleY :
		temp = random.randrange(1,6)*100
	return temp 
	
def print_border():
	pygame.draw.rect(gameDisplay, black, [0,0,3,600])
	pygame.draw.rect(gameDisplay, black, [0,0,800,3])
	pygame.draw.rect(gameDisplay, black, [0,597,800,3])
	pygame.draw.rect(gameDisplay, black, [797,0,4,600])
	
def print_apple(randAppleX,randAppleY,snake_width,snake_length):
	pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY,snake_width,snake_length])
	
def print_snake(snakeList,snake_width,snake_length) :
	#pygame.draw.rect(gameDisplay, black, [X,Y,snake_width,snake_length])
	counter = 0
	for XnY in snakeList :
		j = 0
		while j < len(snakeList[0]) :
			if j == 0 :
				pygame.draw.rect(gameDisplay, green,[ snakeList[0][j], snakeList[0][j+1], snake_width, snake_length])
			elif j == len(snakeList[0])-2 :
				pygame.draw.rect(gameDisplay, blue,[ snakeList[0][j], snakeList[0][j+1], snake_width, snake_length])
			else :
				if counter%2 == 0 :
					pygame.draw.rect(gameDisplay, firstPart,[ snakeList[0][j], snakeList[0][j+1], snake_width, snake_length])
				else :
					pygame.draw.rect(gameDisplay, secondPart,[ snakeList[0][j], snakeList[0][j+1], snake_width, snake_length])
			j += 2
			counter += 1
		#pygame.draw.rect(gameDisplay, black,[ XnY[0], XnY[1], snake_width, snake_length])
	
	"""
	j = 0
	while j < len(snakeList) :
		pygame.draw.rect(gameDisplay, black,[ snakeList[j], snakeList[j+1], snake_width, snake_length])
		j += 2
		"""
		
def getDirection(X_Change,Y_Change,step) :
	if Y_Change == 0 :
		if X_Change != step :
			return 'left'
		elif X_Change != -1*step :
			return 'right'
			
	if X_Change == 0 :
		if Y_Change != step :
			return 'up'
		elif Y_Change != -1*step :
			return 'down'
	"""
	if event.key == pygame.K_a and X_Change != step :#LEFT
		X_Change = -1*step
		Y_Change = 0
	elif event.key == pygame.K_d and X_Change != -1*step :#RIGHT
		X_Change = step
		Y_Change = 0
	elif event.key == pygame.K_s and Y_Change != -1*step:#DOWM
		X_Change = 0
		Y_Change = step
	elif event.key == pygame.K_w and Y_Change != step:#UP
		X_Change = 0
		Y_Change = -1*step
	"""
	
def eatApple(X,Y,randAppleX,randAppleY):
	if ( X == randAppleX and Y == randAppleY ) :
		return True
	else :
		return False
	
	
def checkCollision(snakeList,X,Y):
	arr = [X,Y]
	for XnY in snakeList :
		j = 2
		while j < len(snakeList[0]) :
			arr2 = [ snakeList[0][j], snakeList[0][j+1] ]
			if arr == arr2 :
				return True
			j += 2
	return False
	
def gameLoop() :
	collision = False
	pause = False
	eating = False
	gameExit = False
	textShow = False
	X_Change = 0
	Y_Change = 0
	fixedX = X = 400
	fixedY = Y = 300
	snake_width = 20
	snake_length = 20
	step = 20
	randAppleX = makeRandomX(0)
	randAppleY = makeRandomY(0)
	snakeList = []
	snakeHead = []
	snakeAdd = []
	counter = 0
	while not gameExit :
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT :
				gameExit = True
			if event.type == pygame.KEYDOWN:
				#step = 1
				if event.key == pygame.K_a and X_Change != step :#LEFT
					X_Change = -1*step
					Y_Change = 0
				elif event.key == pygame.K_d and X_Change != -1*step :#RIGHT
					X_Change = step
					Y_Change = 0
				elif event.key == pygame.K_s and Y_Change != -1*step:#DOWM
					X_Change = 0
					Y_Change = step
				elif event.key == pygame.K_w and Y_Change != step:#UP
					X_Change = 0
					Y_Change = -1*step
				elif event.key == pygame.K_SPACE:#PAUSE
					pause = True
				elif event.key == pygame.K_ESCAPE :
					gameExit = True
			
			"""
			if event.type == pygame.KEYUP :
				if event.key == pygame.K_a or event.key == pygame.K_d :
					X_Change = 0
				if event.key == pygame.K_w or event.key == pygame.K_s :
					Y_Change = 0
			"""	
		
		
		
		
		while pause == True :
			for event in pygame.event.get():
				if event.type == pygame.QUIT :
					gameExit = True
					pause = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						pause = False

			
			
		textShow = check(X,Y)

		if(bool(textShow)) :
			gameOver = True
			while gameOver == True :
				finish_message("You Lose ,Press Enter To Play Again ESC to Quit!",red)
				pygame.display.update()
				for event in pygame.event.get() :
					if event.type == pygame.QUIT :
						gameExit = True
						gameOver = False
					if event.type == pygame.KEYDOWN :
						if event.key == pygame.K_RETURN :
							textShow = False
							gameOver = False
							X = 400
							Y = 300
							X_Change = 0
							#Y_Change = -1*step
							Y_Change = 0
							randAppleX = makeRandomX(randAppleX)
							randAppleY = makeRandomY(randAppleY)
							snakeList = []
							snakeHead = []
						if event.key == pygame.K_ESCAPE :
							gameOver = False
							gameExit = True
							
		else :
			
			
								
			#snakeHead = []
			X_temp = X
			Y_temp = Y
			
			X += X_Change
			Y += Y_Change
			
			collision = checkCollision(snakeList,X,Y);
			
			if(collision == True) :
				#print_snake(snakeList,snake_width,snake_length)
				snakeList = []
				if( X == X_temp and Y == Y_temp ) :
					snakeHead = []
					#snakeHead.pop(0)
				#
				
				snakeHead.append(X)
				snakeHead.append(Y)
				snakeList.append(snakeHead)
				
				if eating != True :  #eatApple(X,Y,randAppleX,randAppleY) == False :
					if( len(snakeList[0]) > 2  ) :
						snakeList[0].pop(0)
						snakeList[0].pop(0)
						
				eating = False
				gameDisplay.fill(white)
				print_snake(snakeList,snake_width,snake_length)
				
				pygame.display.update()
				while collision :
					for event in pygame.event.get():
						if event.type == pygame.QUIT :
							collision = False
							gameExit = True
						if event.type == pygame.KEYDOWN :
							if event.key == pygame.K_RETURN :
								#gameExit = True
								collision = False
								X = 400
								Y = 300
								X_Change = 0
								#Y_Change = -1*step
								Y_Change = 0
								randAppleX = makeRandomX(randAppleX)
								randAppleY = makeRandomY(randAppleY)
								snakeList = []
								snakeHead = []
							if event.key == pygame.K_ESCAPE :
								collision = False
								gameExit = True
			
			#snakeHead.append( X )
			#snakeHead.append( Y )
			#print (snakeHead[0])
			#for i in range(len(snakeHead)) :
			#	print (i)
			
			#time.sleep(.5)
			
			if ( X == randAppleX and Y == randAppleY ) :#when snake eat the apple
				eating = True
				randAppleX = makeRandomX(randAppleX)
				randAppleY = makeRandomY(randAppleY)
				
				
			"""
				if getDirection(X_Change,Y_Change,step) == 'up' :
					X_temp -= 0
					Y_temp -= 10
				elif getDirection(X_Change,Y_Change,step) == 'down' :
					X_temp += 0
					Y_temp += 10
				elif getDirection(X_Change,Y_Change,step) == 'right' :
					X_temp -= 10
					Y_temp -= 0
				elif getDirection(X_Change,Y_Change,step) == 'left' :
					X_temp += 10
					Y_temp += 0
					
				snakeAdd.append(X_temp)
				snakeAdd.append(Y_temp)
				randAppleX = makeRandomX(randAppleX)
				randAppleY = makeRandomY(randAppleY)
				#print("randAppleX " + str(randAppleX))
				#print("randAppleY " + str(randAppleY))
			"""
			
			
			if ( gameExit == False ) :
				gameDisplay.fill(white)
				
				print_border()
				
				
				
				
				snakeList = []
				if( X == X_temp and Y == Y_temp ) :
					snakeHead = []
					#snakeHead.pop(0)
				#
				
				snakeHead.append(X)
				snakeHead.append(Y)
				
				#gg = getDirection(X_Change,Y_Change,step)
				
				"""if ( gg == 'left' or gg == 'right' or gg == 'up' or gg == 'down') :
					snakeHead.pop(0)
					snakeHead.pop(0)"""
				
				#if ( ( X_temp != X and Y_temp != Y ) or ( counter == 0 ) ) :
				snakeList.append(snakeHead)
				if eating != True :  #eatApple(X,Y,randAppleX,randAppleY) == False :
					if( len(snakeList[0]) > 2  ) :
						snakeList[0].pop(0)
						snakeList[0].pop(0)
						
				eating = False
					
				#counter+=1
				
				"""
				snakeList = []
				#snakeHead = [X,Y]
				snakeHead.append(X)
				snakeHead.append(Y)
				#snakeHead.append([X, Y])
				
				#snakeList.append(snakeAdd)
				
				i = 0
				while i < len(snakeAdd) :
					snakeAdd[i] += X_Change
					snakeAdd[i+1] += Y_Change
					i += 2
					
				snakeHead += snakeAdd
				snakeList = snakeHead
				"""
				
				print_snake(snakeList,snake_width,snake_length)
				#print (snakeList)
				print_apple(randAppleX,randAppleY,snake_width,snake_length)
				
				
				pygame.display.update()
				
				speed = 10
				clock.tick(speed + len(snakeList[0])/4)
				
				#clock.tick(20)
	

gameLoop()

pygame.quit()
quit()