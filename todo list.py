def display_menu():
    print("Todo List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")


def add_task(todo_list):
    task_name = input("Enter task name: ")
    todo_list[task_name] = False
    print("Task added successfully!")


def view_tasks(todo_list):
    print("Todo List:")
    for index, task in enumerate(todo_list, start=1):
        status = "Completed" if todo_list[task] else "Not Completed"
        print(f"{index}. {task} - {status}")


def mark_completed(todo_list):
    view_tasks(todo_list)
    task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
    tasks = list(todo_list.keys())
    task_name = tasks[task_index]
    todo_list[task_name] = True
    print(f"{task_name} marked as completed!")


def delete_task(todo_list):
    view_tasks(todo_list)
    task_index = int(input("Enter the index of the task to delete: ")) - 1
    tasks = list(todo_list.keys())
    task_name = tasks[task_index]
    del todo_list[task_name]
    print(f"{task_name} deleted from the todo list!")


def main():
    todo_list = {}

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            mark_completed(todo_list)
        elif choice == '4':
            delete_task(todo_list)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
     
