# Python Program to create a To-Do list:

tasks = []


def displaytasks():
    print("<-----Your To-Do list----->")
    print("Task No  |  Task Name  |  Status")
    for task in tasks:
        print(
            f"{task['Task No']} \t\t | {task['Task Name']}  |  {'Completed' if task['Completion Status'] else 'Not Completed'}")


def add_task():
    task_name = input("Enter The task : ")
    task_number = len(tasks) + 1
    task_dict = {"Task No": task_number, "Task Name": task_name, "Completion Status": False}
    tasks.append(task_dict)
    print(f"Task '{task_name}' added to your to-do list.")


def mark_as_completed():
    task_number_to_complete = int(input("Enter the task number to mark as completed: "))
    for task in tasks:
        if task['Task No'] == task_number_to_complete:
            task['Completion Status'] = True
            print(f"Task {task_number_to_complete} marked as completed.")
            break
    else:
        print("Invalid Task Number...Task not found")


def remove_task():
    task_number_to_remove = int(input("Enter the task number to remove: "))
    for task in tasks:
        if task['Task No'] == task_number_to_remove:
            removed_task = tasks.pop(task_number_to_remove - 1)
            print(f"Task '{removed_task['Task No']}' removed from your to-do list.")
            break
    else:
        print("Invalid Task Number...Task not found")

    for index, task in enumerate(tasks):
        task['Task No'] = index + 1


def main():
    while True:
        print("\n*****  Welcome to To-Do list Program  *****\n")
        print("1] Display the Tasks")
        print("2] Add the Tasks")
        print("3] Mark the Tasks as Completed")
        print("4] Remove the Tasks")
        print("5] Exit")

        choice = int(input("Choose The Option (1-5) : "))

        match choice:
            case 1:
                if len(tasks) == 0:
                    print("Your To-Do list is Empty....No Task to display!!")
                else:
                    displaytasks()

            case 2:
                add_task()

            case 3:
                if len(tasks) == 0:
                    print("Your To-Do list is Empty....No Task to mark as complete!!")
                else:
                    displaytasks()
                    mark_as_completed()

            case 4:
                if len(tasks) == 0:
                    print("Your To-Do list is Empty....No Task to Remove!!")
                else:
                    displaytasks()
                    remove_task()

            case '5':
                print("Exiting the To-Do List Application. Goodbye!")
                break

            case _:
                print("Invalid option. Please enter a valid option (1-5).")


if __name__ == "__main__":
    main()
