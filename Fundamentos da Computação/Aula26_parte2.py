import turtle 

tartaruga_1 = turtle.Turtle()
tartaruga_2 = turtle.Turtle()
tartaruga_3 = turtle.Turtle()
tartaruga_4 = turtle.Turtle()
tartaruga_5 = turtle.Turtle()
tartaruga_1.shape("arrow")
tartaruga_2.shape("arrow")
tartaruga_3.shape("arrow")
tartaruga_4.shape("arrow")
tartaruga_5.shape("arrow")
tartaruga_1.speed(1)
tartaruga_2.speed(1)
tartaruga_3.speed(1)
tartaruga_4.speed(1)
tartaruga_5.speed(1)


def retangulo(a,b,color,tartaruga):
  tartaruga.begin_fill()
  tartaruga.fillcolor(color)
  for q in range(2):
    tartaruga.forward(a)
    tartaruga.left(90)
    tartaruga.forward(b)
    tartaruga.left(90)
  tartaruga.end_fill()  

def triangulo_equilátero(a,color,tartaruga):
  
  tartaruga.begin_fill()
  tartaruga.fillcolor(color)
  for i in range(2):
    tartaruga.forward(a)
    tartaruga.left(120)
  tartaruga.forward(a)
  tartaruga.end_fill()

def paralelogramo(a,b,color,tartaruga):
  
  tartaruga.fillcolor(color)
  tartaruga.begin_fill()
  for i in range(2):
    tartaruga.forward(a)
    tartaruga.left(120)
    tartaruga.forward(b)
    tartaruga.left(60)
  tartaruga.end_fill()


#Etapas:
#Passo 01 -> desenhar o quadrado laranja 
retangulo(100,100,"#FF8200", tartaruga_1)
#Passo 02 -> Fazer o triângulo equilátero 

tartaruga_2.penup()
tartaruga_2.sety(100)
tartaruga_2.pendown()

triangulo_equilátero(100,"#C0504D",tartaruga_2)

#Passo 03 - Retângulo amarelo 

tartaruga_3.penup()
tartaruga_3.setx(100)
tartaruga_3.pendown()
retangulo(200,100,"#FFC000",tartaruga_3)

#Passo 04 - Paralelogramo 

tartaruga_4.penup()
tartaruga_4.goto(100,100)
tartaruga_4.pendown()
paralelogramo(200,100,"#C00000",tartaruga_4)

#Passo 05 - Fazer as portas e janelas

tartaruga_5.penup()
tartaruga_5.forward(40)
tartaruga_5.pendown()
retangulo(30,60,"#000000",tartaruga_5)
tartaruga_5.penup()
tartaruga_5.forward(90)
tartaruga_5.left(90)
tartaruga_5.forward(40)
tartaruga_5.right(90)
tartaruga_5.pendown()
retangulo(50,30,"#000000",tartaruga_5)
tartaruga_5.penup()
tartaruga_5.forward(80)
tartaruga_5.pendown()
retangulo(50,30,"#000000",tartaruga_5)













