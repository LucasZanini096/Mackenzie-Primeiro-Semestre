def valor_pagamento():
    cont = 1
    lista_pagamentos = []
    while True:
        
        pagamento = float(input(f'Digite o valor do pagamento [{cont}]:'))
        
        if pagamento == 0:
            print ("Relatório do Dia")
            for indice, valor in enumerate(lista_pagamentos):
                print (f'Pagamento [{indice + 1}] -- R$ {valor}')
            break

        n_dias_atraso = int(input(f'Digite quantos dias ocorreu o atraso do pagamento [{cont}]:'))       
 
        if n_dias_atraso > 0:
            pagamento += (pagamento * 0.03) + (pagamento * 0.001) * n_dias_atraso
            lista_pagamentos.append(pagamento)
            cont += 1
        
        else:
            lista_pagamentos.append(pagamento)
            cont += 1



valor_pagamento()
