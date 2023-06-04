#Corrida de tartarugas 
#Passo 01 -> Importar bibliotecas 

import random
import turtle 

tartaruga_1 = turtle.Turtle()
tartaruga_2 = turtle.Turtle()
tartaruga_3 = turtle.Turtle()
tartaruga_4 = turtle.Turtle()
tartaruga_5 = turtle.Turtle()

tartaruga_1.shape("turtle")
tartaruga_2.shape("turtle")
tartaruga_3.shape("turtle")
tartaruga_4.shape("turtle")
tartaruga_5.shape("turtle")

#Passo 02 - posicionar as tartarugas 

#Plano das ordenadas 
tartaruga_1.setpos(0,0)
tartaruga_2.penup()
tartaruga_2.sety(-40)
tartaruga_2.pendown()
tartaruga_3.penup()
tartaruga_3.sety(-80)
tartaruga_3.pendown()
tartaruga_4.penup()
tartaruga_4.sety(-120)
tartaruga_4.pendown()
tartaruga_5.penup()
tartaruga_5.sety(-160)
tartaruga_5.pendown()

#Plano das absissas 
tartaruga_1.penup()
tartaruga_1.setpos(-400,0)
tartaruga_1.pendown()
tartaruga_2.penup()
tartaruga_2.setpos(-400,-40)
tartaruga_2.pendown()
tartaruga_3.penup()
tartaruga_3.setpos(-400,-80)
tartaruga_3.pendown()
tartaruga_4.penup()
tartaruga_4.setpos(-400,-120)
tartaruga_4.pendown()
tartaruga_5.penup()
tartaruga_5.setpos(-400,-160)
tartaruga_5.pendown()


#Passo 03, aderir uma velocidade a elas
tartaruga_1.speed(random.randint(1,10))
tartaruga_2.speed(random.randint(1,10))
tartaruga_3.speed(random.randint(1,10))
tartaruga_4.speed(random.randint(1,10))
tartaruga_5.speed(random.randint(1,10))

#Passo 04 - aderir cores a elas 
tartaruga_1.color("red")
tartaruga_2.color("green")
tartaruga_3.color("yellow")
tartaruga_4.color("blue")
tartaruga_5.color("orange")

#Passo 05 - aderir uma determinada distância a elas
tartaruga_1.forward(800)
tartaruga_2.forward(800)
tartaruga_3.forward(800)
tartaruga_4.forward(800)
tartaruga_5.forward(800)


