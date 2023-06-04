def dec_in_bin_oct_hex(num, base):
    lista_nums = ["0", "1","2","3","4","5",\
                "6", "7", "8", "9", "A",\
                "B", "C", "D", "E", "F"]
    if num == "0":
        return 0

    else:
        num_convertido = ''

    q = int(num) // base
    r = int(num) % base

    while q >= 0:
        if q != 0:
            digito = lista_nums[r]
            num_convertido += digito
        else:
            digito = lista_nums[r]
            num_convertido += lista_nums[r]
            break

        r = q % base
        q = q // base


    res = ''.join(list(num_convertido).__reversed__())

    return res


def bin_oct_hex_in_dec(num, base):

    num = str(num)
    k = len(num) - 1
    res = 0
    lista16 = ["A", "B", "C", "D", "E", "F"]
    base16 = [10, 11, 12, 13, 14, 15]

    for i in range(len(num)):
        if num[i] in (lista16) and base == 16:
            y = 0
            while num[i] != lista16[y]:
                y += 1
            n = base16[y]
            res += n * (base**k)
            k += -1
        else:
            n = int(num[i])
            res += n * (base**k)
            k += -1

    return res

#01 - Inputar a quantidade de inputs e o tipo de input 

while True:
   
   casos = int(input()) #Quantidade de inputs 
   
   for i in range (casos):
    num, base_num = input().split(' ')  
    num_upper_hex = num.upper() #Para hexadecimal 
 

    
    if len(base_num) > 3: #Verificacao do texto
      continue
   
    else:
     
      if base_num == 'hex':  #Conversao de base tipo 1
        num_dec = bin_oct_hex_in_dec(num_upper_hex,16)
        num_bin = dec_in_bin_oct_hex(num_dec, 2)
        
        print (f"""Case {i+1}:
         {num_dec} dec 
         {num_bin} bin""")
    
      elif base_num == 'bin': #Conversao de base tipo 2
        num_dec = bin_oct_hex_in_dec(num,2)
        num_hex = dec_in_bin_oct_hex(num_dec,16)
        
        print (f"""Case {i+1}:
         {num_dec} dec 
         {num_hex} hex""")
    
      else: #Conversao de base tipo 3
        num_bin = dec_in_bin_oct_hex(num,2)
        num_hex = dec_in_bin_oct_hex(num,16)
        
        print(f"""Case {i+1}:
        {num_bin} bin 
        {num_hex} hex""")
    
        