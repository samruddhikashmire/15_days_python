''' Question 1: 
Write a Python program that takes a user-inputted integer and prints whether it is an evenor odd number. 
Additionally, ensure that the program handles potential errors gracefully(e.g., non-integer inputs) and prompts the user to input a valid integer. '''

n = input("Enter a number: ")
if n.isnumeric() or (n[0] == '-' and n[1:].isnumeric()):
    n = int(n)
    if n % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
else:
    print("Please enter a valid number!")


'''Question 2: 
Create a Python script to implement a basic "To-Do List" using a list or a dictionary. The program should allow the user to add tasks,
mark tasks as completed, and view the current list of tasks. Ensure that the program includes error handling for invalid inputs and provides a user-friendly interface.'''

def add_task(dic):
    task = input("Enter the task: ")
    dic[task] = False
    print(f"Task '{task}' added to the To-Do List.")

def mark_completed(dic):
    print("Tasks in To-Do List:")
    for task, completed in dic.items():
        print(f"{task} - {'Completed' if completed else 'Not Completed'}")
    
    task_to_mark = input("Enter the task to mark as completed: ")
    if task_to_mark in dic:
        dic[task_to_mark] = True
        print(f"Task '{task_to_mark}' marked as completed.")
    else:
        print(f"Task '{task_to_mark}' not found in the To-Do List.")

def view_tasks(dic):
    if not dic:
        print("To-Do List is empty.")
    else:
        print("Current To-Do List:")
        for task, completed in dic.items():
            print(f"{task} - {'Completed' if completed else 'Not Completed'}")

def main():
    dic = {}
    while True:
        print("\n")
        print("To-Do List Menu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        choice = int(choice)
        if choice == 1:
                add_task(dic)
        elif choice == 2:
                mark_completed(dic)
        elif choice == 3:
                view_tasks(dic)
        elif choice == 4:
                print("Exiting To-Do List program.")
                break
        else:
                print("Invalid choice !!! Please enter a number between 1 and 4.")
        main()
