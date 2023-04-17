import turtle

class Ball:
    def __init__(self,color,x,y):
        
        #to create the ball
        self.__ball= turtle.Turtle()
        self.__ball.speed(0)
        self.__ball.color(color.lower())
        self.__ball.shape('square')
        self.__ball.penup()
        self.__ball.goto(x,y)
        self.__ball.dx=0.35
        self.__ball.dy=0.35    
        self.__right_ref=False
        self.__left_ref=False
    
    def move(self):
        self.__ball.setx(self.__ball.xcor()+self.__ball.dx)
        self.__ball.sety(self.__ball.ycor()+self.__ball.dy)
        
    def generate_pos(self):
        self.__ball.setx(0)
        self.__ball.sety(0)
        
    def check_up(self):
        if self.__ball.ycor()>290:
            self.__ball.sety(290)
            self.__ball.dy*=-1
            
        if self.__ball.xcor()>390:
            self.__ball.goto(0,0)
            self.__ball.dx *=-1
            
            self.__right_ref = True
        else:
            self.__right_ref=False
            
            
         
    def  check_down(self):
        
        if self.__ball.ycor() < -290:
            self.__ball.sety(-290)
            self.__ball.dy *=-1
            
        if self.__ball.xcor() < -390:
            self.__ball.goto(0,0)
            self.__ball.dx *=-1
            
            self.__left_ref = True
        else:
            self.__left_ref=False
        
    def get_right_ref(self):
        return self.__right_ref
    def get_left_ref(self):
        return self.__left_ref
            
    def get_x(self):
        return self.__ball.xcor()
    def get_y(self):
        return self.__ball.ycor()
    
    def set_x(self,x):
        self.__ball.setx(x)
        self.__ball.dx *= -1
    def set_y(self,y):
        self.__ball.sety(y)
        self.__ball.dy *=-1
    
    def check_right_rocket(self,x,y):
        if ((self.__ball.xcor() > 340) and (self.__ball.xcor() <350 )and(self.__ball.ycor() < y + 40 )and (self.__ball.ycor() > y - 40)):
            self.__ball.setx(340)
            self.__ball.dx *=-1
            
    def check_left_rocket(self,x,y):
        if ((self.__ball.xcor() < -340) and (self.__ball.xcor() > -350 )and(self.__ball.ycor() < y + 40 )and (self.__ball.ycor() > y - 40)):
            self.__ball.setx(-340)
            self.__ball.dx *=-1
