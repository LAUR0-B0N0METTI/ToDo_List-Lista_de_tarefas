import os

class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        print("=== Lista de Tarefas ===")
        if not self.tasks:
            print("Nenhuma tarefa disponível.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        print("========================")

    def add_task(self, new_task):
        self.tasks.append(new_task)
        print(f'Tarefa "{new_task}" adicionada com sucesso.')

    def edit_task(self, task_index, new_task):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1] = new_task
            print(f'Tarefa {task_index} editada para "{new_task}".')
        else:
            print("Índice de tarefa inválido.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f'Tarefa {task_index} "{deleted_task}" removida com sucesso.')
        else:
            print("Índice de tarefa inválido.")

    def save_to_file(self):
        # Obtém o caminho do desktop no ambiente Windows
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        
        # Define o caminho completo do arquivo
        file_path = os.path.join(desktop_path, "Lista.txt")

        # Abre o arquivo em modo de escrita
        with open(file_path, "w") as file:
            # Escreve cada tarefa no arquivo, uma por linha
            for task in self.tasks:
                file.write(f"{task}\n")

        print(f'Tarefas salvas com sucesso no arquivo "{file_path}".')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    todo_list = ToDoList()

    while True:
        clear_screen()
        todo_list.display_tasks()

        print("\nEscolha uma opção:")
        print("1. Adicionar Tarefa")
        print("2. Editar Tarefa")
        print("3. Excluir Tarefa")
        print("4. Salvar e Sair")

        # Obtém a escolha do usuário
        choice = input("Digite o número da opção desejada: ")

        if choice == "1":
            new_task = input("Digite a nova tarefa: ")
            todo_list.add_task(new_task)
        elif choice == "2":
            task_index = int(input("Digite o número da tarefa que deseja editar: "))
            new_task = input("Digite a nova descrição da tarefa: ")
            todo_list.edit_task(task_index, new_task)
        elif choice == "3":
            task_index = int(input("Digite o número da tarefa que deseja excluir: "))
            todo_list.delete_task(task_index)
        elif choice == "4":
            todo_list.save_to_file()
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()