candidatos = [['Bruna', '15', 'Republicanos', 'Prefeito', 1],['Lucas', '12', 'Pt', 'Prefeito', 2], ['Ivan', '45', 'Psol', 'Governador', 2], ['Claudia', '16', 'Psdb', 'Presidente', 2]]
eleitores = [["Gabriel","4789541558"],["Natalia","1254873954"]]






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
             

votar(candidatos,eleitores)