import json
import os

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                try:
                    self.tasks = json.load(file)
                except json.JSONDecodeError:
                    self.tasks = []
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()

    def show_tasks(self):
        if not self.tasks:
            print("Nenhuma tarefa encontrada.")
            return
        for i, task in enumerate(self.tasks):
            status = "✔" if task["completed"] else "✘"
            print(f"{i}. [{status}] {task['task']}")

if __name__ == "__main__":
    todo = ToDoList()
    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Completar Tarefa")
        print("4. Listar Tarefas")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            tarefa = input("Digite a tarefa: ")
            todo.add_task(tarefa)
        elif opcao == "2":
            todo.show_tasks()
            index = int(input("Digite o número da tarefa para remover: "))
            todo.remove_task(index)
        elif opcao == "3":
            todo.show_tasks()
            index = int(input("Digite o número da tarefa para completar: "))
            todo.complete_task(index)
        elif opcao == "4":
            todo.show_tasks()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")
