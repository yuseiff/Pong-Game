import turtle
class Player :
    def __init__(self,color,x,y):
        
        #Create a rocket
        self.__rocket= turtle.Turtle()
        self.__rocket.speed(0)
        self.__rocket.color(color.lower())
        self.__rocket.shape('square')
        self.__rocket.penup()
        self.__rocket.goto(x,y)
        self.__rocket.shapesize(stretch_wid=5,stretch_len=1)
        
        self.__score=0
        self.__is_lose=False
    
    def get_score(self):
        return self.__score
    
    def get_is_lose(self):
        return self.__is_lose
    
    def move_up(self):
        
        y=self.__rocket.ycor()
        if y <= 250:
            y+=40
            self.__rocket.sety(y)
        
    def move_down(self):
        y=self.__rocket.ycor()
        if y >= -250:
            y-=40
            self.__rocket.sety(y)
        
    def score_update(self):
        self.__score +=1
        
        
    def get_x(self):
        return self.__rocket.xcor()
    
    def get_y(self):
        return self.__rocket.ycor()
    
    