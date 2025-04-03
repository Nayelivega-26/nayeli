def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]  # Intercambiar los elementos
    return lista

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista desordenada:", lista)
lista_ordenada = burbuja(lista)
print("Lista ordenada:", lista_ordenada)
