import datetime
def selection_sort(lista):
    n = len(lista)
    for j in range(n - 1):
        min_index = j
        for i in range(j + 1, n):
            if lista[i] < lista[min_index]:
                min_index = i

        if j != min_index:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux
        
    
    print(f"Lista ordenada: {lista}")

# Exemplo de uso
lista = [64, 25, 12, 22, 11]
tempoInicial = datetime.datetime.now()
selection_sort(lista)
tempoFinal = datetime.datetime.now()
somaDosTempos = tempoFinal - tempoInicial
print(somaDosTempos)
