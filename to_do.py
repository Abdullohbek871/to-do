

tasks = {}

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Title: ")
        description = input("Description: ")
        due_date = input("Due date (YYYY-MM-DD): ")
        status = "Not Completed"

        if len(due_date) == 10 and due_date[4] == '-' and due_date[7] == '-' and due_date[:4].isdigit() and due_date[
                                                                                                            5:7].isdigit() and due_date[
                                                                                                                               8:].isdigit():
            try:

                tasks[title] = {"description": description, "due_date": due_date, "status": status}
                print(f"Task '{title}' added successfully.")
            except ValueError:
                print("Invalid date. Please make sure the date is valid.")
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")

    elif choice == "2":
        title = input("Enter the title of the task to remove: ")
        if title in tasks:
            del tasks[title]
            print(f"Task '{title}' removed successfully.")
        else:
            print("Task not found.")

    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            for title, details in tasks.items():
                print(
                    f"Title: {title}\nDescription: {details['description']}\nDue Date: {details['due_date']}\nStatus: {details['status']}\n")

    elif choice == "4":
        title = input("Enter the title of the task to mark as completed: ")
        if title in tasks:
            tasks[title]["status"] = "Completed"
            print(f"Task '{title}' marked as completed.")
        else:
            print("Task not found.")

    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")