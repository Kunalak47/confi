class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description

    def __str__(self):
        return f"ID: {self.task_id}, Title: {self.title}, Description: {self.description}"
def create_task(task_list, next_id):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    new_task = Task(next_id, title, description)
    task_list.append(new_task)
    print("Task created successfully.")
    return next_id + 1
def read_tasks(task_list):
    if not task_list:
        print("No tasks available.")
    else:
        for task in task_list:
            print(task)
def update_task(task_list):
    task_id = int(input("Enter task ID to update: "))
    task = next((t for t in task_list if t.task_id == task_id), None)
    
    if task:
        new_title = input("Enter new title (leave blank to keep current): ")
        if new_title:
            task.title = new_title
        
        new_description = input("Enter new description (leave blank to keep current): ")
        if new_description:
            task.description = new_description
        
        print("Task updated successfully.")
    else:
        print("Task not found.")
def delete_task(task_list):
    task_id = int(input("Enter task ID to delete: "))
    task = next((t for t in task_list if t.task_id == task_id), None)
    
    if task:
        task_list.remove(task)
        print("Task deleted successfully.")
    else:
        print("Task not found.")
def main():
    task_list = []
    next_id = 1

    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            next_id = create_task(task_list, next_id)
        elif choice == "2":
            read_tasks(task_list)
        elif choice == "3":
            update_task(task_list)
        elif choice == "4":
            delete_task(task_list)
        elif choice == "5":
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
