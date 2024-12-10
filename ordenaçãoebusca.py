# Selection Sort
def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

# Teste do Selection Sort
lista = [64, 25, 12, 22, 11]
sorted_lista = selection_sort(lista)
print("Lista ordenada com Selection Sort:", sorted_lista)

# Quick Sort
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    menores = [x for x in lista[1:] if x < pivot]
    maiores = [x for x in lista[1:] if x >= pivot]
    return quick_sort(menores) + [pivot] + quick_sort(maiores)

# Teste do Quick Sort
lista = [64, 25, 12, 22, 11]
sorted_lista = quick_sort(lista)
print("Lista ordenada com Quick Sort:", sorted_lista)
