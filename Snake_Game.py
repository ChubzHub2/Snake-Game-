#Creatign a simple snake game using Phyton 3 (Beginner Level)
# Created by: Akeme Moore

import turtle
import time
import random

delay = 0.1 # Delay for the game loop

#score variables
score = 0 # Current score of the player
high_score = 0 # High score of the player

# Set up the screen
wn = turtle.Screen()
wn.title("Serpent Surge by Akeme Moore")# Title of the game
wn.bgcolor("black") # Background color of the game
wn.bgpic("C:\\Users\\sxdeonarine\\Desktop\\Akeme Moore\\Sanke Game\\Rotating_earth_(large).gif") # Background image of the game
wn.setup(width=600, height=600) # Window size
wn.tracer(0) # Turns off the screen updates


#Creation of Snake Head
head= turtle.Turtle() #Class of the turtle
head.speed(0)# Fastest animation speed of the turtle
head.shape("triangle") # Shape of the snake head
head.color("orange")#Color of the turtle
head.penup() # Prevents the turtle from drawing a line
head.goto(0,0) # Position of the snake head
head.direction = "stop" # Initial direction of the snake head

#Creation of Snake Food
food = turtle.Turtle()# Class of the turtle for food
food.speed(0)# Fastest animation speed of the turtle
food.shape("square")# Shape of the food
food.color("red")# Color of the food
food.penup()#   Prevents the turtle from drawing a line
food.goto(0, 100)# Position of the food

#Creation of the Snake Body
segments = []

#Creating a turtle to use as a pen
pen = turtle.Turtle() # Class of the turtle for the pen
pen.speed(0) # Fastest animation speed of the turtle
pen.shape("square") # Shape of the pen
pen.color("white") # Color of the pen
pen.penup() # Prevents the turtle from drawing a line
pen.hideturtle() # Hides the pen turtle
pen.goto(0, 260) # Position of the pen
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal")) # Displays the score and high score


# Function to move the snake head up
def go_up():
    if head.direction != "down": # Prevents the snake from moving in the opposite direction
        head.direction = "up" # Sets the direction of the snake head to up
# Function to move the snake head down
def go_down():
    if head.direction != "up": # Prevents the snake from moving in the opposite direction
        head.direction = "down" # Sets the direction of the snake head to down
# Function to move the snake head left
def go_left():
    if head.direction != "right": # Prevents the snake from moving in the opposite direction
        head.direction = "left" # Sets the direction of the snake head to left
# Function to move the snake head right
def go_right():
    if head.direction != "left": # Prevents the snake from moving in the opposite direction
        head.direction = "right" # Sets the direction of the snake head to right

def move():
    if head.direction == "up":
        y= head.ycor()
        head.sety(y+20) # Moves the snake head up by 20 pixels

    if head.direction == "down":
        y= head.ycor()
        head.sety(y-20) # Moves the snake head down by 20 pixels

    if head.direction == "left":
        x= head.xcor()
        head.setx(x-20) # Moves the snake head left by 20 pixels

    if head.direction == "right":
        x= head.xcor()
        head.setx(x+20) # Moves the snake head right by 20 pixels
       
  #Keyboard bindings    
  # This allows the user to control the snake head using the arrow keys
wn.listen() # Listens for keyboard input
wn.onkeypress(go_up, "w") # Binds the up arrow key to the go_up function
wn.onkeypress(go_down, "s") # Binds the down arrow key to the go_down function
wn.onkeypress(go_left, "a") # Binds the left arrow key to the go_left function
wn.onkeypress(go_right, "d") # Binds the right arrow key to the go_right function

#Main game loop 
while True:
    wn.update()#updates the screen

    #Check for collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290: # Checks if the snake head is outside the border
        time.sleep(1) # Pauses the game for 1 second
        head.goto(0,0) # Moves the snake head back to the center of the screen
        head.direction = "stop" # Stops the snake head from moving

        #hide the segments
        for segment in segments:# Loops through each segment in the segments list
            segment.goto(1000, 1000) # Moves the segment off the screen

        segments.clear() # Clears the segments list

        #Reset the score
        score = 0
        pen.clear() # Clears the previous score display
        pen.write("Score: {} High Score:{}".format(score, high_score), align="center", font=("Courier", 24, "normal")) # Updates the score and high score display

    #Check for collision with food
    if head.distance(food)< 20:# Checks if the snake head is close to the food
        x=random.randint(-290,290)# Generates a random x-coordinate for the food
        y=random.randint(-290,290)# Generates a random y-coordinate for the food
        food.goto(x,y)# Moves the food to a random position

        # Add a segment to the snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0) # Fastest animation speed of the turtle
        new_segment.shape("circle") # Shape of the snake body segment
        new_segment.color("green") # Color of the snake body segment
        new_segment.penup()# Prevents the turtle from drawing a line
        segments.append(new_segment) # Adds the new segment to the segments list
    
        #Increase the score
        score += 10 # Increases the score by 10

        if score> high_score:# Checks if the current score is greater than the high score
           high_score = score # Sets the high score to the current score

        pen.clear() # Clears the previous score display
        pen.write("Score: {} High Score:{}".format(score, high_score), align="center", font=("Courier", 24, "normal")) # Updates the score and high score display

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1): # Loops through the segments in reverse order
        x = segments[index-1].xcor() # Gets the x-coordinate of the previous segment
        y = segments[index-1].ycor() # Gets the y-coordinate of the previous segment
        segments[index].goto(x, y) # Moves the current segment to the position of the previous segment

    # Move segment 0 to where the head is
    if len(segments) > 0:# Checks if there are any segments in the segments list
        x = head.xcor()# Gets the x-coordinate of the snake head
        y = head.ycor()# Gets the y-coordinate of the snake head
        segments[0].goto(x, y)# Moves the first segment to the position of the snake head


    move() # Calls the move function to move the snake head

    #check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20: # Checks if the snake head is close to any segment
            time.sleep(1)# Pauses the game for 1 second
            head.goto(0, 0)# Moves the snake head back to the center of the screen
            head.direction= "stop"# Stops the snake head from moving

            # Hide the segments
            for segment in segments:# Loops through each segment in the segments list
                segment.goto(1000, 1000) # Moves the segment off the screen

            segments.clear() # Clears the segments list

            # Reset the score
            score = 0
            pen.clear()# Clears the previous score display
            pen.write("Score: {} High Score:{}".format(score, high_score), align="center", font=("Courier", 24, "normal"))  # Updates the score and high score display

    time.sleep(delay) # Adds a delay to control the speed of the game

wn.mainloop() # Keeps the window open
