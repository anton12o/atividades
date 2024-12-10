from collections import deque

fila = deque()

# Inserindo elementos na fila (FIFO)
fila.append(1)  # Adiciona 1 no final
fila.append(2)  # Adiciona 2 no final

# Removendo elementos da fila (FIFO)
primeiro = fila.popleft()  # Remove o primeiro elemento (1)

print(fila)  # deque([2])
print(primeiro)  # 1
