def merge(v, ini, meio, fim):
    tam = fim - ini + 1
    p1 = ini
    p2 = meio + 1
    temp = []

    while p1 <= meio and p2 <= fim:
        if v[p1] < v[p2]:
            temp.append(v[p1])
            p1 += 1
        else:
            temp.append(v[p2])
            p2 += 1

    while p1 <= meio:
        temp.append(v[p1])
        p1 += 1

    while p2 <= fim:
        temp.append(v[p2])
        p2 += 1

    for i in range(tam):
        v[ini + i] = temp[i]

if __name__ == "__main__":
    v = [38, 27, 43, 3, 9, 82, 10]
    merge(v, 0, 3, 6) 
    print(v)
