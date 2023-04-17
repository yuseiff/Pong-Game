from classes.Player import Player
from classes.Ball import Ball
from classes.Map import Map
import turtle
import sys,os
m1=Map('Black',800,600)


#intialize the objects

p1=Player('blue',-350,0)
p2=Player('Red',350,0)
ball=Ball('white',0,0)
#------------------------------

score=turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0,260)
score.write(f"Player 1: {p1.get_score()} Player 2: {p2.get_score()}",align='center',font=('Courier',24,'normal'))

#---------------------------------
#movement
m1.move(p1.move_up,'w')
m1.move(p1.move_down,'s')

m1.move(p2.move_up,'Up')
m1.move(p2.move_down,'Down')

os.system('cls')
while True:
    try:
        
        m1.Update()
        ball.move()
        
        ball.check_up()
        ball.check_down()
        
        if ball.get_right_ref() ==True:
            p1.score_update()
            score.clear()
            score.write(f"Player 1: {p1.get_score()} Player 2: {p2.get_score()}",align='center',font=('Courier',24,'normal'))
        elif ball.get_left_ref() ==True:
            p2.score_update()
            score.clear()
            score.write(f"Player 1: {p1.get_score()} Player 2: {p2.get_score()}",align='center',font=('Courier',24,'normal'))
        
        
        ball.check_right_rocket(p2.get_x(),p2.get_y())
        ball.check_left_rocket(p1.get_x(),p1.get_y())
        
        
    except Exception as e:
        pass

sys.exit()
              
    
    