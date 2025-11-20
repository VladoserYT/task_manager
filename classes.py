import json
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_from_file()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_to_file()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_to_file()

    def save_to_file(self):
        data = [
            {
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date
            }
            for task in self.tasks
        ]
        # Используем ensure_ascii=False для корректного сохранения кириллицы
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_from_file(self):
        try:
            # Указываем кодировку utf-8 для чтения файла
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = [
                    Task(item["title"], item["description"], item["due_date"])
                    for item in data
                ]
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            # Обработка случая, когда файл пуст или содержит некорректный JSON
            self.tasks = []
