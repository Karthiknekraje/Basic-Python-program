todo_list = []

def add_task(task):
    todo_list.append(task)

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)

def show_tasks():
    print("To-Do List:")
    for idx, task in enumerate(todo_list, 1):
        print(f"{idx}. {task}")

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Show tasks")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please choose again
