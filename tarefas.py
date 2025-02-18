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


def remover_tarefa(numero):
    """Remove uma tarefa específica pelo número"""
    try:
        with open(TAREFAS_ARQUIVO, "r") as f:
            tarefas = f.readlines()

        if 1 <= numero <= len(tarefas):
            tarefa_removida = tarefas.pop(numero - 1)
            with open(TAREFAS_ARQUIVO, "w") as f:
                f.writelines(tarefas)
            print(f"Tarefa removida: {tarefa_removida.strip()}")
        else:
            print("Número inválido.")
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")

if __name__ == "__main__":
    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa = input("Digite a tarefa: ")
            adicionar_tarefa(tarefa)
        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            numero = int(input("Digite o número da tarefa a remover: "))
            remover_tarefa(numero)

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")