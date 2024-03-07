import pygame #Imports Pygame library into your Python script.
import sys #This statement imports the 'sys' module into your Python script. 

pygame.init() #Initializes all necessary Pygame modules required for the game to run smoothly.

WIDTH, HEIGHT = 600, 400 #WIDTH & HEIGHT constants that define the size of window.
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 60 #Constants that define the size of the paddles.
BALL_SIZE = 15 #Constant that defines size of the ball. Diameter of 15 pixels
FPS = 60 #Defines a constant that represents the rate at which the game's main loop will update and redraw the screen.

WHITE = (255,255,255) #Constant that represents the color white.
BLACK = (0,0,0) #Constant that represents the color black.

screen = pygame.display.set_mode((WIDTH,HEIGHT)) #Creates game window with specified width and height
pygame.display.set_caption("Pong") #Sets the title of the game window 

clock = pygame.time.Clock() #Creates a Pygame clock object, which is used to control the frame rate of the game.
#Creates a rectangular paddle for player 1 using Rect.
player1_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

#Creates a rectangular paddle for player 2 using Rect.
player2_paddle = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
#Creates a rectangular paddle for the game ball.
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
#Speed of the game ball initialized. First element horizontal speed. Second element vertical speed.
ball_speed = [5,5]

#Scores for each player
player1_score = 0
player2_score = 0

#Initializes a font object using default system font and sets its size to '36'.
font = pygame.font.Font(None, 36)

while True:
    #This initiates a loop by iterating over all the events that have been generated since the last iteration of the loop.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Checks to see if it is a quit event, which indicates that user has attempted to close.
            pygame.quit() #Shuts down the game module.
            sys.exit() #Terminates the environment and exits the program immediately.
    #Retrieves the state of all keyboard keys at the current moment.
    #pygame.key.get_pressed() returns a list-like object where the elements is 'True' if the key is pressed. 'False' otherwise.
    keys = pygame.key.get_pressed()
    #Checks if the 'w' key is pressed and ensures the top edge of paddle is not at top edge of game window.
    if keys[pygame.K_w] and player1_paddle.top > 0:
        player1_paddle.y -= 5
    #Checks if the 's' key is pressed and ensures the bottom of paddle is not at the bottom edge of the game window.
    if keys[pygame.K_s] and player1_paddle.bottom < HEIGHT:
        player1_paddle.y += 5
    #Checks if the 'UP' key is pressed and ensures the top edge of paddle is not at the top edge of game window.
    if keys[pygame.K_UP] and player2_paddle.top > 0:
        player2_paddle.y -= 5
    #Checks if the 'DOWN' key is pressed and ensures the bottom edge of paddle is not at the bottome edge of game window.
    if keys[pygame.K_DOWN] and player2_paddle.bottom < HEIGHT:
        player2_paddle.y += 5
        
    ball.x += ball_speed[0] #This line increments the x-coordinate by the value stored in first element.
    ball.y += ball_speed[1] #This line increments the y-coordinate by the value stored in second element.
    #Checks if the ball hits the top of the window of bottom of window.
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1] #Reverses the vertical direction of the ball's movement.
    #Checks if the ball hits the paddle of player 1 or player 2
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_speed[0] = -ball_speed[0] #Reverse the horizontal direction of the ball's movement.
    
    #Checks if the left edge of the ball's bounding rectangle has gone beyond or equal to the left edge of window.
    if ball.left <= 0:
        player2_score += 1 #Increments score for player 2.
        #Resets ball
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2 
    #Checks if the right edge of ball's bounding rectangel has gone beyond or equal to the right edge of window.
    elif ball.right >= WIDTH:
        player1_score += 1 #Increments score for player 1.
        ball.x = WIDTH // 2 - BALL_SIZE // 2 
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
    
    screen.fill(BLACK) #This fills the entire screen with the color black.
    pygame.draw.rect(screen, WHITE, player1_paddle) #Draws player 1's paddle on the screen.
    pygame.draw.rect(screen, WHITE, player2_paddle) #Draws player 2's paddle on the screen.
    pygame.draw.ellipse(screen, WHITE, ball) #This line draws the ball on the screen as an ellipse(circle)
    
    #Renders the score of player 1
    player1_text = font.render(f"Player 1: {player1_score}", True, WHITE)
    #Renders the score of player 2
    player2_text = font.render(f"Player 2: {player2_score}", True, WHITE)
    #Takes the two arguments to draw the image of the score for player 1
    screen.blit(player1_text, (20,20))
    #Takes the two arguments to draw the image of the score for player 2
    screen.blit(player2_text, (WIDTH - player2_text.get_width() - 20, 20))
    
    
    pygame.display.flip() #Updates the contents of the entire display window.
    
    clock.tick(FPS) #Regulates the frame rate of the game.
            



