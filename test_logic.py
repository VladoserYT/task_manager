from classes import Task, TaskManager
import os

manager = TaskManager("test_tasks.json")
print(f"Начальное количество задач: {len(manager.tasks)}")

task1 = Task("Купить молоко", "Обезжиренное", "2025-11-21")
task2 = Task("Сделать отчет", "Отчет по продажам за ноябрь", "2025-11-25")
manager.add_task(task1)
manager.add_task(task2)
print(f"Количество задач после добавления: {len(manager.tasks)}")

print(f"Файл test_tasks.json существует: {os.path.exists('test_tasks.json')}")

manager2 = TaskManager("test_tasks.json")
print(f"Количество задач после загрузки: {len(manager2.tasks)}")
print(f"Первая задача: {manager2.tasks[0].title}")

manager2.delete_task(0)
print(f"Количество задач после удаления: {len(manager2.tasks)}")

manager3 = TaskManager("test_tasks.json")
print(f"Количество задач после повторной загрузки: {len(manager3.tasks)}")

os.remove("test_tasks.json")
print("Тестовый файл удален.")
