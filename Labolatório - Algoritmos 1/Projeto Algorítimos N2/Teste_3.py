candidatos = [['Lucas', '12', 'Pt', 'Prefeito', 2], ['Ivan', '45', 'Psol', 'Governador', 2], ['Bruna', '15', 'Republicanos', 'Prefeito', 1], ['Claudia', '16', 'Psdb', 'Presidente', 2]]

lista_votos_brancos = [0, 0, 0]
lista_votos_nulos = [1, 0, 1]
lista_votos_totais = [4, 2, 2]

eleitores = [["Gabriel","4789541558"],["Natalia","1254873954"]]


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
      {texto_1: ^12}   {texto_2: ^31}
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


relatorio_e_estatisticas(eleitores,candidatos,lista_votos_totais)