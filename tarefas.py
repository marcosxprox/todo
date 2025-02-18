TAREFAS_ARQUIVO = "files/tarefas.txt"

def adicionar_tarefa(tarefa):
    """Adiciona uma nova tarefa ao arquivo"""
    with open(TAREFAS_ARQUIVO, "a") as f:
        f.write(tarefa + "\n")
    print(f"Tarefa '{tarefa}' adicionada!")

def listar_tarefas():
    """Lista todas as tarefas armazenadas"""
    try:
        with open(TAREFAS_ARQUIVO, "r") as f:
            tarefas = f.readlines()
            if not tarefas:
                print("Nenhuma tarefa encontrada.")
                return
            print("Tarefas:")
            for i, tarefa in enumerate(tarefas, 1):
                print(f"{i}. {tarefa.strip()}")
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")

if __name__ == "__main__":
    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa = input("Digite a tarefa: ")
            adicionar_tarefa(tarefa)
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")