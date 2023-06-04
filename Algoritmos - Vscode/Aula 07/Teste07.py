#Fatorial de um número 
n = int(input())
nmulti = 0
multi = 1
if n > 1:
    
    while nmulti >= 0 and nmulti <= n-1:
        multi = multi * (nmulti + 1)
        print (multi)
        nmulti += 1
       
else: 
    print (1)

