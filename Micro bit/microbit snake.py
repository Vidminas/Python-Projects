from microbit import *
from random import randint

gridMaxX = 5
gridMaxY = 5

directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]

class Snake:
    """ This class contains the functions that operate
        on our game as well as the state of the game.
        It's a handy way to link the two.
    """

    def __init__(self):
        """ Special function that runs when you create
            a "Snake", ie. when you run
                game = Snake()
            init stands for "Initialisation"
        """
        ## UNCOMMENT AND FILL IN THE # LINES BELOW WITH START VALUES
        ## current direction is a string with up, down, left or right
        self.current_direction = 0
        ## snake is a list of the pixels that the snake is at
        self.snake = [[2, 2]]
        ## food is the co-ords of the current food
        self.food = [0, 0]
        ## whether or not to end the game, used after update
        self.end = False

    def handle_input(self):
        """ We'll use this function to take input from the
            user to control which direction the snake is going
            in.
        """
        if button_a.get_presses() > 0:
            self.current_direction -= 1
            self.current_direction %= len(directions)
                
        elif button_b.get_presses() > 0:
            self.current_direction += 1
            self.current_direction %= len(directions)
       
    def move(self):
        # The line below makes a copy of the head of the snake
        # you will be working with that copy in this function
        new_head = list(self.snake[-1])
        
        new_head[0] += directions[self.current_direction][0]
        new_head[0] %= gridMaxX
        new_head[1] += directions[self.current_direction][1]
        new_head[1] %= gridMaxY
        
        if self.snake[-1] in self.snake[:len(self.snake) - 1]:
            self.end = True
            
        else:
            self.snake = self.snake[1:]
            self.snake.append(new_head)
        
    def eat_food(self):
        if self.snake[-1] == self.food:
            new_head = list(self.snake[-1])
            new_head[0] += directions[self.current_direction][0]
            new_head[0] %= gridMaxX
            new_head[1] += directions[self.current_direction][1]
            new_head[1] %= gridMaxY
            self.snake.append(new_head)
        
            self.food = [randint(0, gridMaxX-1),
                         randint(0, gridMaxY-1)]
                         
            while self.food in self.snake:
                self.food = [randint(0, gridMaxX-1),
                             randint(0, gridMaxY-1)]
        
    def update(self):
        """ This function will update the game state
            based on the direction the snake is going.
        """
        self.move()
        self.eat_food()

    def draw(self):
        """ This makes the game appear on the LEDs. """
        display.clear()
        
        if not self.end:
            display.set_pixel(self.food[0], self.food[1], 5)
            
            for part in self.snake[:len(self.snake)-1]:
                display.set_pixel(part[0], part[1], 7)
                
            display.set_pixel(self.snake[-1][0], self.snake[-1][1], 9)
            
        else:
            display.show(Image.SAD)

# game is an "instance" of Snake
game = Snake()

# this is called our "game loop" and is where everything
# happens
while not game.end:
    game.handle_input()
    game.update()
    game.draw()
    # this makes our micro:bit do nothing for 500ms
    sleep(500)
