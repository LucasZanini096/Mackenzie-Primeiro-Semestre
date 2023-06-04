
candidatos = []
eleitores = []
lista_votos_brancos = []
lista_votos_nulos = []
lista_votos_totais = []
    

def cadrastro_candidato(lista_candidatos):

    lista_candidatos_possiveis = ["Governador", "Prefeito", "Presidente"]

    while True: 
        
        candidato = []
        
        nome = input("Digite o nome do candidato:").capitalize()
        candidato.append(nome)
        
        numero = input("Digite o número correspondente deste candidato:")
        
        try:
            numero = int(numero)
            numero = str(numero)
            candidato.append(numero)
        
        except Exception:
            
            print("Reescreva o número do candidato, realizando novamente o seu cadastro")
            continue
    
        partido = input("Digite o seu partido correspondente:").capitalize()
        candidato.append(partido)
        
        cargo = input("Digite o cargo desse candidato:").capitalize()

        if cargo in lista_candidatos_possiveis:
            candidato.append(cargo)
        else:
            print("Reescreva o cargo do candidato, realizando novamente o seu cadastro")
            continue 
        
        lista_candidatos.append(candidato)

        print()
        opcao = input("Digite [S]im para cadrastrar um novo usuário ou [N]ão para sair:").upper()
        print()

        if opcao == "N":
            
            return lista_candidatos

def verificacao_cpf(cpf):
  
  #Primeiro dígito

  lista_nums_cpf = []
  soma_1 = 0
  soma_2 = 0
  cpf_valido = ""

  nove_digitos_cpf = cpf[:9]
  
  for num in nove_digitos_cpf:
    lista_nums_cpf.append(int(num))
    
  contador_1 = 0 
  
  for i in range(10,1,-1):
    
    soma_1 += lista_nums_cpf[contador_1] * i
    contador_1 += 1
  
  
  
  resto_divisao_n_1 = soma_1 % 11

  if resto_divisao_n_1 < 2:
    primeiro_digito = 0
  
  else:
    
    primeiro_digito = 11 - resto_divisao_n_1
    lista_nums_cpf.append(primeiro_digito)

  #Segundo Dígito

  contador_2 = 0 
  
  for i in range(11,1,-1):
    
    soma_2 += lista_nums_cpf[contador_2] * i
    contador_2 += 1
  

  resto_divisao_2 = soma_2 % 11

  if resto_divisao_2 < 2:
    segundo_digito = 0
  
  else: 
    segundo_digito = 11 - resto_divisao_2
    lista_nums_cpf.append(segundo_digito)

  for num in lista_nums_cpf:
    cpf_valido += str(num)
  

  #Verificação final do cpf
  
  if cpf == cpf_valido:
    print("O usuário digitou um CPF válido")
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
  
  else:
    print("O usuário digitou um CPF inválido")
    return None 

    

def cadrastro_eleitor(lista_eleitores):
    
    while True:
        
        eleitor = []
        
        nome = input("Digite o nome do eleitor:")
        eleitor.append(nome)
       
        cpf = input("Digite o CPF respectivo desse eleitor:")       

        if len(cpf) == 11:
            
          try:
              
              cpf = int(cpf)
              cpf = str(cpf)

              cpf = verificacao_cpf(cpf)

              if cpf == None:
                print("Você deve digitar um CPF válido, digite-o novamente")

                continue
              
              else:
                eleitor.append(cpf)
                
             
          except ValueError:
              
              print("O usuário deve digitar um CPF válido, digite-o novamente")
              continue
        
        else:
          
          print("O usuário deve digitar um CPF válido, digite-o novamente")
          continue
          
        
        lista_eleitores.append(eleitor)

        print() 
        opcao = input("Digite [S]im para cadrastrar um novo usuário ou [N]ão para sair:").upper()
        print()

        if opcao == "N":
            
            return lista_eleitores
        
def votar(lista_candidatos, lista_eleitores): 

    for x in lista_candidatos:
        if len(x) == 5: #Verificação para o início de uma nova eleição, caso já tenho ocorrido uma anteriormente 
            del x[4]

    voto_branco_prefeito = 0
    voto_nulo_prefeito = 0
    votos_totais_prefeito = 0
    voto_branco_governador = 0
    voto_nulo_governador = 0
    votos_totais_governador = 0
    voto_validos_presidente = 0
    voto_branco_presidente = 0
    voto_nulo_presidente = 0
    votos_totais_presidente = 0
    lista_votos_brancos = []
    lista_votos_nulos = []
    lista_votos_totais = []
    
    
        
    for candidato in lista_candidatos:
            
            voto_validos_prefeito = 0
            
    
            
            if candidato[3] == "Prefeito":
                
                for eleitor in lista_eleitores:

                    
                    nome, numero, partido, cargo = candidato
                    
                    print (f"""
                     ----------------------------
                     | Informações do candidato | 
                     ----------------------------

                    -----------------------------
                       Nome: {nome}               
                       Numero: {numero}                                       
                       Partido: {partido}                            
                       Cargo: {cargo}           
                    -----------------------------                    
                    """)
                    
                    print(f"""
                    ------------------------------------------ 
                    |  Instruções para o eleitor: {eleitor[0]}    |
                    ------------------------------------------
                   
                   ------------------------------------------------ 
                     Voto para o candidato {nome}: Digitar {numero}       
                     Voto branco: Digitar -1                       
                     Voto nulo: Digitar -2                           
                   ------------------------------------------------- 
                    """)

                    opcao = input(f"Digite o voto do eleitor {eleitor[0]}:")
                    
                    if opcao == numero:
                        voto_validos_prefeito += 1
                        votos_totais_prefeito += 1
                    
                    elif opcao == "-1":
                        voto_branco_prefeito += 1
                        votos_totais_prefeito += 1
                    
                    
                    elif opcao == "-2":
                        voto_nulo_prefeito += 1
                        votos_totais_prefeito += 1
                    
                    else:
                         continue
                    
                if voto_validos_prefeito == 0:
                    candidato.append(0)
                
                else:    
                    candidato.append(voto_validos_prefeito) #Número de votos do determinado candidato
        
    lista_votos_brancos.append(voto_branco_prefeito)
    lista_votos_nulos.append(voto_nulo_prefeito)
    lista_votos_totais.append(votos_totais_prefeito)
        
                    
    for candidato in lista_candidatos:
            
            voto_validos_governador = 0
            
           
            
            if candidato[3] == "Governador":
                
                for eleitor in lista_eleitores:

                    
                    nome, numero, partido, cargo = candidato
                    
                    print (f"""
                     ----------------------------
                     | Informações do candidato | 
                     ----------------------------

                    -----------------------------
                       Nome: {nome}               
                       Numero: {numero}                                       
                       Partido: {partido}                            
                       Cargo: {cargo}           
                    -----------------------------                    
                    """)
                    
                    print(f"""
                    ------------------------------------------ 
                    |  Instruções para o eleitor: {eleitor[0]}    |
                    ------------------------------------------
                   
                   ------------------------------------------------ 
                     Voto para o candidato {nome}: Digitar {numero}       
                     Voto branco: Digitar -1                       
                     Voto nulo: Digitar -2                           
                   ------------------------------------------------- 
                    """)


                    opcao = input(f"Digite o voto do eleitor {eleitor[0]}:")
                    
                    if opcao == numero:
                        voto_validos_governador += 1
                        votos_totais_governador += 1
                    
                    elif opcao == "-1":
                        voto_branco_governador += 1
                        votos_totais_governador += 1
                    
                    
                    elif opcao == "-2":
                        voto_nulo_governador += 1
                        votos_totais_governador += 1
                    
                    else:
                         continue
                
                if voto_validos_governador == 0:
                    candidato.append(0)
                else:
                    candidato.append(voto_validos_governador) #Número de votos do determinado candidato
        
    lista_votos_brancos.append(voto_branco_governador)
    lista_votos_nulos.append(voto_nulo_governador)
    lista_votos_totais.append(votos_totais_governador)
        
                
    for candidato in lista_candidatos:
            
            voto_validos_presidente = 0
            
           
            
            if candidato[3] == "Presidente":
                
                for eleitor in lista_eleitores:

                    
                    nome, numero, partido, cargo = candidato
                    
                    print (f"""
                     ----------------------------
                     | Informações do candidato | 
                     ----------------------------

                    -----------------------------
                       Nome: {nome}               
                       Numero: {numero}                                       
                       Partido: {partido}                            
                       Cargo: {cargo}           
                    -----------------------------                    
                    """)
                    
                    print(f"""
                    ------------------------------------------ 
                    |  Instruções para o eleitor: {eleitor[0]}    |
                    ------------------------------------------
                   
                   ------------------------------------------------ 
                     Voto para o candidato {nome}: Digitar {numero}       
                     Voto branco: Digitar -1                       
                     Voto nulo: Digitar -2                           
                   ------------------------------------------------- 
                    """)


                    opcao = input(f"Digite o voto do eleitor {eleitor[0]}:")
                    
                    if opcao == numero:
                        voto_validos_presidente += 1
                        votos_totais_presidente += 1
                    
                    elif opcao == "-1":
                        voto_branco_presidente += 1
                        votos_totais_presidente += 1
                    
                    
                    elif opcao == "-2":
                        voto_nulo_presidente += 1
                        votos_totais_presidente += 1
                    
                    else:
                         continue
                
                if voto_validos_prefeito == 0:
                    candidato.append(0)
                else:
                    candidato.append(voto_validos_prefeito) #Número de votos do determinado candidato
        
    lista_votos_brancos.append(voto_branco_presidente)
    lista_votos_nulos.append(voto_nulo_presidente)
    lista_votos_totais.append(votos_totais_presidente)
        
        
    return lista_candidatos,lista_votos_nulos,lista_votos_brancos,lista_votos_totais
             
            
#Parte 04 - Prints 

def apurar_resultados(lista_cadidatos,lista_votos_brancos,lista_votos_nulos, lista_votos_totais):

    
    lista_votos_prefeito = []
    lista_votos_governador = []
    lista_votos_presidente = []

#Presidente

    print(         
         f"""                                                                                                                               
    -------------------------------------------------------------------------------------------                                                    
    |                           RANKING DO RESULTADO PARA PRESIDENTE                          | 
    |-----------------------------------------------------------------------------------------|        
    |    Nome       |       Partido      |     Total de Votos    |      % votos Válidos       |
    -------------------------------------------------------------------------------------------                                                                               
    """)  

    
    for candidato in lista_cadidatos:
        
        if candidato[3] == "Presidente":
            
            lista_votos_presidente.append(candidato[4])
            
    lista_votos_presidente.reverse()
    
    contador = 1        
    for candidato in lista_cadidatos:

        if candidato[3] == "Presidente":


            for num in lista_votos_presidente:

                if num == candidato[4]:
                        
                        #print(f'      {contador}.{candidato[0]}    {candidato[2]}          {num}                {num/lista_votos_totais[1]}            ')
                        #print()

                        texto_1 = f"{contador}.{candidato[0]}"
                        texto_2 = f"{candidato[2]}"
                        texto_3 = f"{num}"
                        texto_4 = f"{(num/lista_votos_totais[1])*100} %"
                        
                        print(f"""
    |{"-"*88}|
  {texto_1: ^19}|{texto_2: ^20}|{texto_3: ^21} |{texto_4: ^30}
    |{"-"*88}|
                            """)
                        contador += 1
    print(
        
        f"""
    ----------------------------------------
    | Total de votos = {lista_votos_totais[2]}                   |    
    | Total de votos válidos = {sum(lista_votos_prefeito)} -> {sum(lista_votos_prefeito)/lista_votos_totais[2]} %  | 
    | Total de votos brancos = {lista_votos_brancos[2]} -> {lista_votos_brancos[2]/lista_votos_totais[2]} %  |  
    | Total de votos nulos = {lista_votos_nulos[2]} -> {lista_votos_nulos[2]/lista_votos_totais[2]}  %   |
    ----------------------------------------         
                    
    """
    ) 
    
    print(         
         f"""                                                                                                                               
    -------------------------------------------------------------------------------------------                                                    
    |                           RANKING DO RESULTADO PARA GOVERNADOR                          | 
    |-----------------------------------------------------------------------------------------|        
    |    Nome       |       Partido      |     Total de Votos    |      % votos Válidos       |
    -------------------------------------------------------------------------------------------                                                                               
    """)  
    
    
    for candidato in lista_cadidatos:
        
        if candidato[3] == "Governador":
            
            lista_votos_governador.append(candidato[4])
    
    lista_votos_governador.reverse()

    contador = 1            
    for candidato in lista_cadidatos:

        if candidato[3] == "Governador":
    
            for num in lista_votos_governador:
                    
                      

                    if num == candidato[4]:
                        
                            texto_1 = f"{contador}.{candidato[0]}"
                            texto_2 = f"{candidato[2]}"
                            texto_3 = f"{num}"
                            texto_4 = f"{(num/lista_votos_totais[1])*100} %"
                            
                            print(f"""
    |{"-"*88}|
  {texto_1: ^19}|{texto_2: ^20}|{texto_3: ^21} |{texto_4: ^30}
    |{"-"*88}|
                            """)
                            contador += 1

    print(
        
        f"""
    ----------------------------------------
    | Total de votos = {lista_votos_totais[1]}                   |    
    | Total de votos válidos = {sum(lista_votos_prefeito)} -> {sum(lista_votos_prefeito)/lista_votos_totais[1]} %  | 
    | Total de votos brancos = {lista_votos_brancos[1]} -> {lista_votos_brancos[1]/lista_votos_totais[1]} %  |  
    | Total de votos nulos = {lista_votos_nulos[1]} -> {lista_votos_nulos[1]/lista_votos_totais[1]}  %   |
    ----------------------------------------         
                    
    """
    ) 

    print(         
         f"""                                                                                                                               
    -------------------------------------------------------------------------------------------                                                    
    |                           RANKING DO RESULTADO PARA PREFEITO                            | 
    |-----------------------------------------------------------------------------------------|        
    |    Nome       |       Partido      |     Total de Votos    |      % votos Válidos       |
    -------------------------------------------------------------------------------------------                                                                               
    """)  
    
    
    for candidato in lista_cadidatos:
        
        if candidato[3] == "Prefeito":
            
            lista_votos_prefeito.append(candidato[4])
    
    lista_votos_prefeito.reverse()
            

    contador = 1        
    for candidato in lista_cadidatos:

        if candidato[3] == "Prefeito":

            for num in lista_votos_prefeito:

                if num == candidato[4]:
                
                        texto_1 = f"{contador}.{candidato[0]}"
                        texto_2 = f"{candidato[2]}"
                        texto_3 = f"{num}"
                        texto_4 = f"{(num/lista_votos_totais[1])*100} %"         
                    
                        print(f"""
    |{"-"*88}|
  {texto_1: ^19}|{texto_2: ^20}|{texto_3: ^21} |{texto_4: ^30}
    |{"-"*88}|   
                            """)
                        contador += 1
        
    print(        
        f"""
     ----------------------------------------
     | Total de votos = {lista_votos_totais[0]}                   |    
     | Total de votos válidos = {sum(lista_votos_prefeito)} -> {sum(lista_votos_prefeito)/lista_votos_totais[0]} % | 
     | Total de votos brancos = {lista_votos_brancos[0]} -> {lista_votos_brancos[0]/lista_votos_totais[0]} %  |  
     | Total de votos nulos = {lista_votos_nulos[0]} -> {lista_votos_nulos[0]/lista_votos_totais[0]} %   |
     ----------------------------------------    
    """)      

def relatorio_e_estatisticas(lista_eleitores,lista_candidatos,lista_votos_t):
    
    #Exibição da lista de eleitores
    
    print("""            
           ------------------------
           | Relatório da votação |             
           ------------------------  

    1. Eleitores e seus CPF's

      ------------------------------------
      | NOME                         CPF |
      ------------------------------------
    """)
    
    contador = 1
    
    for eleitor in lista_eleitores:
        
        nome,cpf = eleitor
        texto_1 = f"{contador}. {nome}"
        texto_2 = f"{cpf}"
        simbolo = "|"
        

        print(f'''
     -------------------------------------  
      {texto_1: ^12}   {texto_2: ^29}
     -------------------------------------   
        
        ''')

        contador += 1
    
    #Verificação da quantidade de eleitores em relação ao total de votos
    
    print("""
    
      2. Verificação de votos
    
    """)

    if len(lista_eleitores) * len(lista_candidatos) == sum(lista_votos_t):
        
        print("A quantidade de eleitores bate com o total de votos")
    
    else:
        
        print("A quantidade de eleitores não bate com o total de votos")
    
    print()
    print("3. Partidos com mais votos e com menos votos")
    print()
    
    lista_partidos = []
    
    for candidato in lista_candidatos:
        lista_partidos.append(candidato[2])
    
    Partidos = set(lista_partidos)


    print("""
   -----------------------------------
   | PARTIDO          TOTAL DE VOTOS |
   -----------------------------------
    
    """)
    

    for partido in Partidos:

        contador_partido = 0
        
        for candidato in lista_candidatos:
            if partido == candidato[2]:
                contador_partido += candidato[4]
        
        print(f"""
   -----------------------------------       
{partido: ^20} {contador_partido: ^21}
   -----------------------------------                 
                 """)
        

while True:
    print()
    titulo = "+++++++ MENU - SIMULADOR DE SISTEMA DE VOTAÇÃO +++++++"
    print(f'{titulo: ^110}')
    print()

    opcao_1 = "1. Cadastrar Candidatos"
    opcao_2 = "2. Cadastrar Eleitores"
    opcao_3 = "3. Votar"
    opcao_4 = "4. Apurar resultados"
    opcao_5 = "5. Relatório e Estatísticas"
    opcao_6 = "6. Encerrar"

    print(f"{opcao_1: >64}")
    print(f"{opcao_2: >63}")
    print(f"{opcao_3: >49}")
    print(f"{opcao_4: >61}")
    print(f"{opcao_5: >68}")
    print(f"{opcao_6: >52}")

    print()

   
    opcao = input("Digite uma das opções apresentadas:")
    print()


    if opcao == "1":
        cadrastro_candidato(candidatos)
        print()
        
    elif opcao ==  "2":
        cadrastro_eleitor(eleitores)
        print()
        
    elif opcao == "3":
        candidatos,lista_votos_nulos,lista_votos_brancos,lista_votos_totais = votar(candidatos,eleitores)
        print()

    elif opcao == "4":
        apurar_resultados(candidatos,lista_votos_brancos,lista_votos_nulos,lista_votos_totais)
        print()

    elif opcao == "5":
        relatorio_e_estatisticas(eleitores,candidatos,lista_votos_totais)
        print()
        
    elif opcao == "6":
        
        print(f"""
        
        ---------------------------------
        |    Opções para o usuário      |
        ---------------------------------
        | Sim -> Sair do programa       | 
        | Não -> Permanecer no programa | 
        ---------------------------------


        """)
        
        escolha_saida = input("Você deseja realmente sair deste programa? :").capitalize()

        if escolha_saida == "Sim":
            print("Você está saindo deste programa !")
            break 
            
        else:
            print ("Você deve escolher outra opção")
            continue
    else:
        print("Você não digitou uma das opções apresentadas, digite novamente uma opção")
        continue