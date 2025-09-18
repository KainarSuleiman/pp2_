



# Step 1: Define functions
def add_task(tasks, name, description):
    tasks[name] = description
    print(f"Task '{name}' added.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for name, description in tasks.items():
            print(f"- {name}: {description}")


def delete_task(tasks, name):
    if name in tasks:
        del tasks[name]
        print(f"Task '{name}' deleted.")
    else:
        print(f"Task '{name}' not found.")


# Step 2: Main program
def task_organizer():
    tasks = {}  # Dictionary to store tasks
    while True:
        action = input("Choose action: add, view, delete, quit: ").strip().lower()

        if action == "add":
            name = input("Enter task name: ").strip()
            description = input("Enter task description: ").strip()
            add_task(tasks, name, description)
        elif action == "view":
            view_tasks(tasks)
        elif action == "delete":
            name = input("Enter task name to delete: ").strip()
            delete_task(tasks, name)
        elif action == "quit":
            print("Exiting Task Organizer.")
            break
        else:
            print("Invalid action. Please try again.")


# Call the task organizer function
task_organizer()
