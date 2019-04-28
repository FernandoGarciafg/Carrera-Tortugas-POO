import turtle
import random

class Circuito(): # creamos un objeto que va a ser el circuito
    corredores = [] # la clase circuito va a tener como atributos los corredores y la pantalla
    __posStartY = (-30, -10, 10 , 30)
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    def __init__(self, width, height): # creamos el constructor de nuestra clase con los atributos ancho y altura que van a ser los
                                       # de la pantalla de nuestro juego
        self.width = width
        self. height = height
        
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startLine = -width / 2 + 20
        self.__finishLine = width / 2 - 20
        
        self.__crearCorredores()
        
    def __crearCorredores(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
            
            self.corredores.append(new_turtle)
            
    def competir(self):
        hayGanador = False
        
        while not hayGanador:
            for tortuga in self.corredores:
                
                avance = random.randint(1, 6)
                tortuga.forward(avance)
                
                if tortuga.position()[0] >= self.__finishLine:
                    hayGanador = True
                    print("La tortuga de color {} ha ganado".format(tortuga.color()[0]))
                    break
                
if __name__ == '__main__':
    circuito = Circuito(640, 480)
    circuito.competir()
        
# c = Circuito(320, 320) crear instancia del objeto                                       
                                       