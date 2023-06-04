def TabelaDeTemperatura(ci,cf, z = None):
    if z is None:
        for c in range(ci,cf+1,5):
            f = ((9/5) * c) + 32
            print (f'{c} ° C <-> {f} ° F')
    else:
        for c in range(ci,cf+1,z):
            f = ((9/5) * c) + 32
            print (f'{c} ° C <-> {f} ° F')

TabelaDeTemperatura(-10,10,2)
