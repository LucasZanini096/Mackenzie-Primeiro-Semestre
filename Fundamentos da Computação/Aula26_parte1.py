import turtle 

tartaruga_1 = turtle.Turtle()
tartaruga_1.shape("arrow") #Tipo de indicador para a "tartaruga" que irá realiazar o desenho 
tartaruga_1.speed(5) #Velocidade da tartaruga

tartaruga_2 = turtle.Turtle()
tartaruga_2.shape("circle")
tartaruga_2.speed(1)

def quadrado(a,color,tartaruga):
    tartaruga.color(color)
    for i in range(2):
        tartaruga.forward(a)
        tartaruga.left(90)
        tartaruga.forward(a)
        tartaruga.left(90)
   


def triangulo_equilatero(a,color,tartaruga):
    tartaruga.color(color)
    tartaruga.begin_fill
    for j in range(2):
        tartaruga.forward(a)
        tartaruga.left(120) #Ângulo de rotação com direção para a esquerda 
    tartaruga.home() #Volta para o ponto de origem (0,0)
    tartaruga.end_fill()


#quadrado(100,"blue",tartaruga_1)
#triangulo_equilatero(100,"red",tartaruga_2)


tartaruga_2.setx(100)
tartaruga_2.setpos(100,100)
tartaruga_2.setpos(0,100)
tartaruga_2.home()