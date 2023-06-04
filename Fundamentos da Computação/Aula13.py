#programa de relógio binário 
horario = input("Digite o horário:")
#Separar horas de minutos 
horario.split()
horas1 = horario[0]
horas2 = horario[1]
horas = horas1 + horas2
horas_int = int(horas)
minutos1 = horario[3]
minutos2 = horario [4]
minutos = minutos1 + minutos2
minutos_int = int(minutos) #Para transformar uma str em int ou float, segue este padrão: int ou float(alguma variável)
h_8 = 0
h_4 = 0
h_2 = 0
h_1 = 0
m_32 = 0
m_16 = 0
m_8 = 0
m_4 = 0
m_2 = 0
m_1 = 0
#horas 
while horas_int != 0:
  if horas_int >= 8:
    horas_int = horas_int - 8                                                  
    if horas_int <= 4 and horas_int >= 0:
      h_8 += 1                                       
  elif horas_int >= 4:
    horas_int = horas_int - 4
    if horas_int <= 3 and horas_int >= 0:
      h_4 += 1
  elif horas_int >= 2:
    horas_int = horas_int - 2
    if horas_int <= 1 and horas_int > 0:
      h_2 += 1
  else:
    horas_int = horas_int - 1
    if horas_int == 0:
      h_1 += 1
#minutos 
while minutos_int != 0:
   if minutos_int >= 32:
    minutos_int = minutos_int - 32
    if minutos_int >= 0 and minutos_int <= 27:
      m_32 += 1
   elif minutos_int >= 16:
    minutos_int = minutos_int - 16
    if minutos_int >= 0 and minutos_int <= 15:
     m_16 += 1
   elif minutos_int >= 8:
    minutos_int = minutos_int - 8
    if minutos_int >= 0 and minutos_int <= 7:
      m_8 += 1
   elif minutos_int >= 4:
    minutos_int = minutos_int - 4
    if minutos_int >= 0 and minutos_int <= 3:
      m_4 += 1
   elif minutos_int >= 2:
    minutos_int = minutos_int - 2
    if minutos_int >= 0 and minutos_int <= 1:
      m_2 += 1
   else:
    minutos_int = minutos_int - 1
    if minutos_int == 0:
      m_1 += 1
#Printar as horas em binário 
if h_8 == 1 and h_4 == 1:
  print (8,  4,  2,  1)
  print (''," ","o","o")
elif h_8 == 1 and h_2 == 1 and  h_1 == 1:
  print (8,  4,  2,  1)
  print('', 'o',' ',' ')
elif h_8 == 1 and h_1 == 1:
  print (8,  4,  2,  1)
  print(' ',"o","o",' ')
elif h_8 == 1:
  print (8,  4,  2,  1)
  print(' ',"o","o","o")
elif h_4 == 1 and h_2 == 1 and h_1 == 1:
  print (8,  4,  2,  1)
  print('o'," "," "," ")
elif h_4 == 1 and h_2 == 1:
  print(8,  4,  2,  1)
  print('o'," "," ","o")
elif h_4 == 1 and h_1 == 1:
  print (8,  4,  2,  1)
  print('o'," ","o"," ")
elif h_4 == 1:
  print (8,  4,  2,  1)
  print('o'," ","o","o")
elif h_2 == 1 and h_1 == 1:
  print (8,  4,  2,  1)
  print('o',"o"," "," ")
elif h_2 == 1:
  print (8,  4,  2,  1)
  print('o',"o"," ","o")
elif h_1 == 1:
  print (8,  4,  2,  1)
  print('o',"o","o"," ")
else:
  print(' ')
#Printar os minutos em binário 
if m_32 == 1 and m_16 == 1 and m_8 == 1 and m_4 == 1 and m_2 == 1 and m_1 == 1:
  print (" "," "," "," "," "," ")  
  print (32, 16, 8, 4, 2, 1)
elif m_32 == 1 and m_16 == 1 and m_8 == 1 and m_4 == 1 and m_2 == 1:
  print (" "," "," "," "," ","o")  
  print (32, 16, 8, 4, 2, 1)
elif m_32 == 1 and m_16 == 1 and m_8 == 1 and m_4 == 1:
  print (" "," "," "," ","o","o")  
  print (32, 16, 8, 4, 2, 1)
elif m_32 == 1 and m_16 == 1 and m_8 == 1:
  print (" "," "," ","o","o","o")  
  print (32, 16, 8, 4, 2, 1)
elif m_32 == 1 and m_16 == 1:
  print (" "," ","o","o","o","o")  
  print (32, 16, 8, 4, 2, 1)
elif m_32 == 1:
  print (" ","o","o","o","o","o")  
  print (32, 16, 8, 4, 2, 1)   
elif m_32 == 1 and m_16 == 1 and m_4 == 1 and m_2 == 1 and m_1 == 1:
  print (" "," ","o"," "," "," ")  
  print (32, 16, 8, 4, 2, 1)
elif m_32 == 1 and m_16 == 1 and m_2 == 1 and m_1 == 1:
  print (" "," ","o","o"," "," ")  
  print (32, 16, 8, 4, 2, 1)
elif m_32 == 1 and m_16 == 1 and m_1 == 1:
  print (" "," ","o","o","o"," ")  
  print (32, 16, 8, 4, 2, 1)
elif m_32 == 1 and m_8 == 1 and m_4 == 1 and m_2 == 1 and m_1 == 1:
  print (" ","o"," "," "," "," ")  
  print (32, 16, 8, 4, 2, 1)
elif m_32 == 1 and m_8 == 1 and m_2 == 1 and m_1 == 1:
  print (" ","o"," ","o"," "," ")  
  print (32, 16, 8, 4, 2, 1)
elif m_32 == 1 and m_8 == 1 and m_1 == 1:
  print (" ","o"," ","o","o"," ")  
  print (32, 16, 8, 4, 2, 1)
elif m_32 == 1 and m_4 == 1 and m_2 == 1 and m_1 == 1:
  print (" ","o","o"," "," "," ")  
  print (32, 16, 8, 4, 2, 1)
elif m_32 == 1 and m_4 == 1 and m_2 == 1:
  print (" ","o","o"," "," ","o")  
  print (32, 16, 8, 4, 2, 1)
elif m_32 == 1 and m_4 == 1 and m_1 == 1:
  print (" ","o","o"," ","o"," ")  
  print (32, 16, 8, 4, 2, 1)
elif m_32 == 1 and m_2 == 1 and m_1 == 1:
  print (" "," "," "," ","o","o")  
  print (32, 16, 8, 4, 2, 1)
elif m_32 == 1 and m_1 == 1:
  print (" ","o","o","o","o"," ")  
  print (32, 16, 8, 4, 2, 1)
elif m_16 == 1 and m_8 == 1 and m_4 == 1 and m_2 == 1 and m_1 == 1:
  print ("o"," "," "," "," "," ")  
  print (32, 16, 8, 4, 2, 1)
elif m_16 == 1 and m_8 ==1 and m_4 == 1 and m_2 == 1:
  print ("o"," "," "," "," ","o")  
  print (32, 16, 8, 4, 2, 1)
elif m_16 == 1 and m_8 ==1 and m_4 == 1:
  print ("o"," "," "," ","o","o")  
  print (32, 16, 8, 4, 2, 1)
elif m_16 == 1 and m_8 ==1:
  print ("o"," "," ","o","o","o")  
  print (32, 16, 8, 4, 2, 1)
elif m_16 == 1:
  print ("o"," ","o","o","o","o")  
  print (32, 16, 8, 4, 2, 1)
elif m_16 == 1 and m_4 == 1 and m_2 == 1 and m_1 == 1:
  print ("o","o"," "," "," "," ")  
  print (32, 16, 8, 4, 2, 1)
elif m_16 == 1 and m_4 == 1 and m_2 == 1:
  print ("o"," ","o"," "," ","o")  
  print (32, 16, 8, 4, 2, 1) 
elif m_16 == 1 and m_4 == 1 and m_1 == 1:
  print ("o"," ","o"," ","o"," ")  
  print (32, 16, 8, 4, 2, 1)  
elif m_16 == 1 and m_4 == 1:
  print ("o"," ","o"," ","o","o")  
  print (32, 16, 8, 4, 2, 1) 
elif m_16 == 1 and m_2 == 1 and m_1 == 1:
  print ("o"," ","o","o"," "," ")  
  print (32, 16, 8, 4, 2, 1) 
elif m_16 == 1 and m_2 == 1:
  print ("o"," ","o","o"," ","o")  
  print (32, 16, 8, 4, 2, 1)
elif m_16 == 1 and m_1 == 1:
  print ("o"," ","o","o","o"," ")  
  print (32, 16, 8, 4, 2, 1)   
elif m_8 == 1 and m_4 ==1 and m_2 == 1 and m_1 == 1:
  print ("o","o"," "," "," "," ")  
  print (32, 16, 8, 4, 2, 1)
elif m_8 == 1 and m_4 ==1 and m_2 == 1:
  print ("o","o"," "," "," ","o")  
  print (32, 16, 8, 4, 2, 1)
elif m_8 == 1 and m_4 ==1:
  print ("o","o"," "," ","o","o")  
  print (32, 16, 8, 4, 2, 1)
elif m_8 == 1 and m_2 == 1 and m_1 == 1:
  print ("o","o"," ","o"," "," ")  
  print (32, 16, 8, 4, 2, 1)
elif m_8 == 1 and m_1 == 1:
  print ("o","o"," ","o","o"," ")  
  print (32, 16, 8, 4, 2, 1)
elif m_8 == 1:
  print ("o","o"," ","o","o","o")  
  print (32, 16, 8, 4, 2, 1) 
elif m_4 ==1 and m_2 == 1 and m_1 == 1:
  print ("o","o","o"," "," "," ")  
  print (32, 16, 8, 4, 2, 1) 
elif m_4 ==1 and m_2 == 1:
  print ("o","o","o"," "," ","o")  
  print (32, 16, 8, 4, 2, 1)
elif m_4 == 1 and m_1 == 1:
  print ("o","o","o"," ","o"," ")  
  print (32, 16, 8, 4, 2, 1)
elif m_4 == 1:
  print ("o","o","o"," ","o","o")  
  print (32, 16, 8, 4, 2, 1)          
elif m_2 == 1 and m_1 == 1:
  print ("o","o","o","o"," "," ")  
  print (32, 16, 8, 4, 2, 1)  
elif m_2 == 1:
  print ("o","o","o","o"," ","o")  
  print (32, 16, 8, 4, 2, 1)
else:
  print ("o","o","o","o","o"," ")  
  print (32, 16, 8, 4, 2, 1)  
