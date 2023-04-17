import turtle

class Map:
    def __init__(self,color,x,y):
        #to create the window
        self.__Map=turtle.Screen()
        self.__Map.title("Ping Pong Game")
        
        color=color.lower()
        self.__Map.bgcolor(color.lower())
        self.__Map.setup(width=x,height=y)
        self.__Map.tracer(0)
    
    def Update(self):
        self.__Map.update()
        
    def move(self,rocket, button):
        self.__Map.listen()
        if len(button)<2:
            self.__Map.onkeypress(rocket,button.lower())
        else:
            self.__Map.onkeypress(rocket,button)