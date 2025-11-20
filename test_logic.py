from classes import Task, TaskManager
import os

# 1. Создаем менеджер (загрузка из пустого файла)
manager = TaskManager("test_tasks.json")
print(f"Начальное количество задач: {len(manager.tasks)}")

# 2. Добавляем задачи
task1 = Task("Купить молоко", "Обезжиренное", "2025-11-21")
task2 = Task("Сделать отчет", "Отчет по продажам за ноябрь", "2025-11-25")
manager.add_task(task1)
manager.add_task(task2)
print(f"Количество задач после добавления: {len(manager.tasks)}")

# 3. Проверяем сохранение
print(f"Файл test_tasks.json существует: {os.path.exists('test_tasks.json')}")

# 4. Создаем новый менеджер для проверки загрузки
manager2 = TaskManager("test_tasks.json")
print(f"Количество задач после загрузки: {len(manager2.tasks)}")
print(f"Первая задача: {manager2.tasks[0].title}")

# 5. Проверяем удаление
manager2.delete_task(0)
print(f"Количество задач после удаления: {len(manager2.tasks)}")

# 6. Проверяем, что удаление сохранилось
manager3 = TaskManager("test_tasks.json")
print(f"Количество задач после повторной загрузки: {len(manager3.tasks)}")

# 7. Очистка
os.remove("test_tasks.json")
print("Тестовый файл удален.")
