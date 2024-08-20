def insertion_sort(data):
    n = len(data)
    for j in range(1, n):
        tmp = data[j]
        i = j - 1
        while i >= 0 and tmp < data[i]:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = tmp

# Exemplo de uso
if __name__ == "__main__":
    lista = [5, 2, 9, 1, 5, 6]
    print("Lista original:", lista)
    insertion_sort(lista)
    print("Lista ordenada:", lista)
