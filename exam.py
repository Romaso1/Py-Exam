import json

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_data()  # Завантаження даних при ініціалізації

    def add_task(self, title, description, priority):
        if not self.is_duplicate(title):
            task = {'title': title, 'description': description, 'priority': priority, 'status': 'нове'}
            self.tasks.append(task)
            print(f"Завдання '{title}' додано.")
            self.save_data()  # Збереження даних після змін
        else:
            print(f"Завдання з назвою '{title}' вже існує. Введіть унікальну назву.")

    def remove_task(self, title):
        for task in self.tasks:
            if task['title'] == title:
                self.tasks.remove(task)
                print(f"Завдання '{title}' видалено.")
                self.save_data()  # Збереження даних після змін
                return
        print(f"Завдання '{title}' не знайдено.")

    def edit_task(self, title, new_title, new_description, new_priority, new_status):
        if not self.is_duplicate(new_title, title):
            for task in self.tasks:
                if task['title'] == title:
                    task['title'] = new_title if new_title else title
                    task['description'] = new_description if new_description else task['description']
                    task['priority'] = new_priority if new_priority else task['priority']
                    task['status'] = new_status if new_status else task['status']
                    print(f"Завдання '{title}' відредаговано.")
                    self.save_data()  # Збереження даних після змін
                    return
            print(f"Завдання '{title}' не знайдено.")
        else:
            print(f"Завдання з назвою '{new_title}' вже існує. Введіть унікальну назву.")

    def is_duplicate(self, title, current_title=None):
        for task in self.tasks:
            if task['title'] == title and title != current_title:
                return True
        return False

    def search_task(self, title):
        for task in self.tasks:
            if task['title'] == title:
                print(f"Знайдено завдання '{title}':")
                print(f"Опис: {task['description']}")
                print(f"Пріорітет: {task['priority']}")
                print(f"Статус: {task['status']}")
                return
        print(f"Завдання '{title}' не знайдено.")

    def display_tasks(self):
        if not self.tasks:
            print("Список завдань порожній.")
        else:
            print("Список завдань:")
            for task in self.tasks:
                print(f"Назва: {task['title']}")
                print(f"Опис: {task['description']}")
                print(f"Пріорітет: {task['priority']}")
                print(f"Статус: {task['status']}")
                print("----------------------------")

    def save_data(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file)

    def load_data(self):
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            pass  # Якщо файл не знайдено, залишити список завдань порожнім


def main():
    task_manager = TaskManager()

    while True:
        print("\n1. Додати завдання")
        print("2. Видалити завдання")
        print("3. Редагувати завдання")
        print("4. Пошук завдання")
        print("5. Вивести список завдань")
        print("6. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == '1':
            title = input("Введіть назву завдання: ")
            description = input("Введіть опис завдання: ")
            priority = input("Введіть пріорітет завдання: ")
            task_manager.add_task(title, description, priority)

        elif choice == '2':
            title = input("Введіть назву завдання для видалення: ")
            task_manager.remove_task(title)

        elif choice == '3':
            title = input("Введіть назву завдання для редагування: ")
            new_title = input("Введіть нову назву (залиште порожньо, якщо не потрібно змінювати): ")
            new_description = input("Введіть новий опис (залиште порожньо, якщо не потрібно змінювати): ")
            new_priority = input("Введіть новий пріорітет (залиште порожньо, якщо не потрібно змінювати): ")
            new_status = input("Введіть новий статус (залиште порожньо, якщо не потрібно змінювати): ")
            task_manager.edit_task(title, new_title, new_description, new_priority, new_status)

        elif choice == '4':
            title = input("Введіть назву завдання для пошуку: ")
            task_manager.search_task(title)

        elif choice == '5':
            task_manager.display_tasks()

        elif choice == '6':
            print("Дякую за використання програми. До побачення!")
            task_manager.save_data()  # Збереження даних перед виходом
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
