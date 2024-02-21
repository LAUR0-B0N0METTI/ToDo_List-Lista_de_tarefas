import tkinter as tk
from tkinter import simpledialog, messagebox
import os

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")
        self.tasks = []

        # Criar widgets
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack()

        self.edit_button = tk.Button(root, text="Editar Tarefa", command=self.edit_task)
        self.edit_button.pack()

        self.delete_button = tk.Button(root, text="Excluir Tarefa", command=self.delete_task)
        self.delete_button.pack()

        self.save_button = tk.Button(root, text="Salvar", command=self.save_to_file)
        self.save_button.pack()

        # Preencher a lista com tarefas existentes
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        new_task = simpledialog.askstring("Adicionar Tarefa", "Digite a nova tarefa:")
        if new_task:
            self.tasks.append(new_task)
            self.update_task_listbox()

    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            edited_task = simpledialog.askstring("Editar Tarefa", "Digite a nova descrição da tarefa:")
            if edited_task:
                self.tasks[selected_index] = edited_task
                self.update_task_listbox()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            deleted_task = self.tasks.pop(selected_index)
            messagebox.showinfo("Tarefa Excluída", f'Tarefa "{deleted_task}" removida com sucesso.')
            self.update_task_listbox()

    def save_to_file(self):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, "todolist_gui.txt")

        with open(file_path, "w") as file:
            for task in self.tasks:
                file.write(f"{task}\n")

        messagebox.showinfo("Tarefas Salvas", f'Tarefas salvas com sucesso no arquivo "{file_path}".')

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
