def BusquedaLineal(objeto,lista):
    buscar = False
    position = 0
    while position < len(lista) and not buscar:
        if lista[position] == objeto:
            buscar = True
        position = position + 1
    return buscar


mochila = ['libro','lapiz','lapicero','laptop','borrador','regla']
objeto = input('Que objeto deseas buscar en la mochila?')
objetoencontrado = BusquedaLineal(objeto,mochila)
if objetoencontrado:
    print ('Si, el objeto se encuentra en la mochila')
else:
    print ('No, el objeto no se encuentra en la mochila')