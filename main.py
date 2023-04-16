import pygame

# Initialize Pygame

pygame.init()

# Set up the game window

width = 800

height = 600

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Pong")
class Ball:

    def __init__(self, x, y):

        self.x = x

        self.y = y

        self.radius = 10

        self.speed_x = 5

        self.speed_y = 5

    def move(self):

        self.x += self.speed_x

        self.y += self.speed_y

        # Bounce off the top and bottom walls

        if self.y - self.radius < 0 or self.y + self.radius > height:

            self.speed_y *= -1

    def draw(self):

        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)

class Paddle:

    def __init__(self, x, y):

        self.x = x

        self.y = y

        self.width = 10

        self.height = 100

        self.speed = 5

    def move_up(self):

        self.y -= self.speed

        # Don't let the paddle go off the screen

        if self.y < 0:

            self.y = 0

    def move_down(self):

        self.y += self.speed

        # Don't let the paddle go off the screen

        if self.y + self.height > height:

            self.y = height - self.height

    def draw(self):

        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))

class Scoreboard:

    def __init__(self, x, y):

        self.x = x

        self.y = y

        self.font = pygame.font.SysFont("Arial", 30)

        self.score = 0

    def add_point(self):

        self.score += 1

    def draw(self):

        score_text = self.font.render(str(self.score), True, (255, 255, 255))

        screen.blit(score_text, (self.x, self.y))
def game_loop():

    # Set up the game objects

    ball = Ball(width // 2, height // 2)

    player1 = Paddle(50, height // 2 - 50)

    player2 = Paddle(width - 50 - 10, height // 2 - 50)

    scoreboard1 = Scoreboard(width // 2 - 100, 50)

    scoreboard2 = Scoreboard(width // 2 + 100, 50)

    # Set up the clock

    clock = pygame.time.Clock()

    # Game loop

    while True:

        # Handle

def game_loop():

    # Set up the game objects

    ball = Ball(width // 2, height // 2)

    player1 = Paddle(50, height // 2 - 50)

    player2 = Paddle(width - 50 - 10, height // 2 - 50)

    scoreboard1 = Scoreboard(width // 2 - 100, 50)

    scoreboard2 = Scoreboard(width // 2 + 100, 50)

    # Set up the clock

    clock = pygame.time.Clock()

    # Game loop

    while True:

        # Handle

           # Handle events

           for event in pygame.event.get():

               if event.type == pygame.QUIT:

                   pygame.quit()

                   sys.exit()

               elif event.type == pygame.KEYDOWN:

                   if event.key == pygame.K_w:

                       player1.move_up()

                   elif event.key == pygame.K_s:

                       player1.move_down()

                   elif event.key == pygame.K_UP:

                       player2.move_up()

                   elif event.key == pygame.K_DOWN:

                       player2.move_down()

           # Update the game objects

           ball.move()

           # Check for collisions between the ball and paddles

           if ball.x - ball.radius < player1.x + player1.width and \

                   player1.y < ball.y < player1.y + player1.height:

               ball.speed_x *= -1

           elif ball.x + ball.radius > player2.x and \

                   player2.y < ball.y < player2.y + player2.height:

               ball.speed_x *= -1

           # Check for points scored

           if ball.x - ball.radius < 0:

               scoreboard2.add_point()

               ball = Ball(width // 2, height // 2)

           elif ball.x + ball.radius > width:

               scoreboard1.add_point()

               ball = Ball(width // 2, height // 2)

           # Draw the game objects

           screen.fill((0, 0, 0))

           ball.draw()

           player1.draw()

           player2.draw()

           scoreboard1.draw()

           scoreboard2.draw()

           # Update the display

           pygame.display.update()

           # Limit the frame rate

           clock.tick(60)

   # Start the game loop

   game_loop()



