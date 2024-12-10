# Criando uma lista
lista = [1, 2, 3, 4, 5]

# Inserindo elementos
lista.append(6)  # Adiciona 6 no final
lista.insert(2, 10)  # Insere 10 na posição 2

# Removendo elementos
lista.remove(4)  # Remove o elemento 4
ultimo_elemento = lista.pop()  # Remove o último elemento (6)

# Buscando um elemento
indice = lista.index(3)  # Encontra a posição do elemento 3

print(lista)  # [1, 2, 10, 3]
print(indice)  # 2
