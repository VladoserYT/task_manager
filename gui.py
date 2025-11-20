import tkinter as tk
from tkinter import ttk, messagebox
# Импортируем классы из созданного файла classes.py
from classes import Task, TaskManager

class TaskManagerApp:
    def __init__(self, root):
        self.manager = TaskManager()
        self.root = root
        self.root.title("Менеджер задач")
        self.setup_ui()

    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(main_frame, text="Название:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.title_entry = ttk.Entry(main_frame, width=40)
        self.title_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(main_frame, text="Описание:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.desc_text = tk.Text(main_frame, height=3, width=30)
        self.desc_text.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(main_frame, text="Срок (ГГГГ-ММ-ДД):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.date_entry = ttk.Entry(main_frame, width=40)
        self.date_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Добавить задачу", command=self.add_task).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Удалить выбранную", command=self.delete_task).pack(side=tk.LEFT, padx=5)

        ttk.Label(main_frame, text="Список задач:").grid(row=4, column=0, sticky=tk.W, pady=5)
        
        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL)
        self.tasks_listbox = tk.Listbox(list_frame, width=50, height=10, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tasks_listbox.yview)
        
        self.tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.update_listbox()
        
        main_frame.columnconfigure(1, weight=1)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)


    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_text.get("1.0", tk.END).strip()
        due_date = self.date_entry.get()
        
        if not title or not description or not due_date:
            messagebox.showwarning("Ошибка ввода", "Пожалуйста, заполните все поля: Название, Описание и Срок выполнения.")
            return

        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Ошибка формата даты", "Срок выполнения должен быть в формате ГГГГ-ММ-ДД (например, 2025-12-31).")
            return
            
        task = Task(title, description, due_date)
        self.manager.add_task(task)
        self.update_listbox()
        self.clear_inputs()
        messagebox.showinfo("Успех", "Задача успешно добавлена!")

    def delete_task(self):
        selected = self.tasks_listbox.curselection()
        if selected:
            index_to_delete = selected[0]
            self.manager.delete_task(index_to_delete)
            self.update_listbox()
            messagebox.showinfo("Успех", "Задача успешно удалена!")
        else:
            messagebox.showwarning("Ошибка", "Пожалуйста, выберите задачу для удаления.")

    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for i, task in enumerate(self.manager.tasks):
            display_text = f"{i+1}. {task.title} (до {task.due_date})"
            self.tasks_listbox.insert(tk.END, display_text)
            

    def clear_inputs(self):
        self.title_entry.delete(0, tk.END)
        self.desc_text.delete("1.0", tk.END)
        self.date_entry.delete(0, tk.END)

if __name__ == "__main__":
    from datetime import datetime 
    
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
