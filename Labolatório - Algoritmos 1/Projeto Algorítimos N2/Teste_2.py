candidatos = [['Lucas', '12', 'Pt', 'Prefeito', 2], ['Ivan', '45', 'Psol', 'Governador', 2], ['Bruna', '15', 'Republicanos', 'Prefeito', 1], ['Claudia', '16', 'Psdb', 'Presidente', 2]]
lista_votos_brancos = [0, 0, 0]
lista_votos_nulos = [1, 0, 1]
lista_votos_totais = [4, 2, 2]


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
          

apurar_resultados(candidatos,lista_votos_brancos,lista_votos_nulos, lista_votos_totais)