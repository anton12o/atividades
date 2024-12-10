class GerenciadorDeTarefas:
    def __init__(self):
        # Inicializa as listas de tarefas e estados
        self.tarefas = []
        self.estados = []

    def adicionar_tarefa(self, tarefa):
        """Adiciona uma nova tarefa à lista de tarefas com o estado 'pendente'"""
        self.tarefas.append(tarefa)
        self.estados.append('pendente')
        print(f"Tarefa '{tarefa}' adicionada com sucesso.")

    def marcar_como_concluida(self, tarefa):
        """Marca uma tarefa como concluída"""
        if tarefa in self.tarefas:
            indice = self.tarefas.index(tarefa)
            self.estados[indice] = 'concluída'
            print(f"Tarefa '{tarefa}' marcada como concluída.")
        else:
            print(f"Tarefa '{tarefa}' não encontrada.")

    def remover_tarefa(self, tarefa):
        """Remove uma tarefa da lista"""
        if tarefa in self.tarefas:
            indice = self.tarefas.index(tarefa)
            self.tarefas.pop(indice)
            self.estados.pop(indice)
            print(f"Tarefa '{tarefa}' removida com sucesso.")
        else:
            print(f"Tarefa '{tarefa}' não encontrada.")

    def listar_tarefas(self):
        """Lista todas as tarefas, separadas por estado"""
        print("\nTarefas Pendentes:")
        for i in range(len(self.tarefas)):
            if self.estados[i] == 'pendente':
                print(f"- {self.tarefas[i]}")
        
        print("\nTarefas Concluídas:")
        for i in range(len(self.tarefas)):
            if self.estados[i] == 'concluída':
                print(f"- {self.tarefas[i]}")

    def pesquisar_tarefa(self, tarefa):
        """Pesquisa uma tarefa pelo nome"""
        if tarefa in self.tarefas:
            indice = self.tarefas.index(tarefa)
            print(f"Tarefa '{tarefa}' encontrada. Estado: {self.estados[indice]}.")
        else:
            print(f"Tarefa '{tarefa}' não encontrada.")

# Função principal para interação com o usuário
def main():
    gerenciador = GerenciadorDeTarefas()
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar tarefa")
        print("2. Marcar tarefa como concluída")
        print("3. Remover tarefa")
        print("4. Listar tarefas")
        print("5. Pesquisar tarefa")
        print("6. Sair")
        
        opcao = input("Opção: ")
        
        if opcao == '1':
            tarefa = input("Digite o nome da tarefa: ")
            gerenciador.adicionar_tarefa(tarefa)
        
        elif opcao == '2':
            tarefa = input("Digite o nome da tarefa para marcar como concluída: ")
            gerenciador.marcar_como_concluida(tarefa)
        
        elif opcao == '3':
            tarefa = input("Digite o nome da tarefa para remover: ")
            gerenciador.remover_tarefa(tarefa)
        
        elif opcao == '4':
            gerenciador.listar_tarefas()
        
        elif opcao == '5':
            tarefa = input("Digite o nome da tarefa para pesquisar: ")
            gerenciador.pesquisar_tarefa(tarefa)
        
        elif opcao == '6':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
