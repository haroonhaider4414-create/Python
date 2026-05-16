# 1. Setup our empty lists
tasks = []
status = [] # This will store True or False for each task

while True:
    # 2. Calculate Progress
    total_tasks = len(tasks)
    
    if total_tasks > 0:
        completed_count = status.count(True)
        percent = (completed_count / total_tasks) * 100
        # Create a simple visual bar
        bar = "█" * int(percent / 5) 
        print(f"\nProgress: [{bar:<20}] {int(percent)}%")
    else:
        print("\nYour list is empty!")

    # 3. Show the current tasks
    print("\n--- TO-DO LIST ---")
    for i in range(len(tasks)):
        mark = "[X]" if status[i] == True else "[ ]"
        print(f"{i + 1}. {mark} {tasks[i]}")

    # 4. User Menu
    print("\nWhat would you like to do?")
    print("1. Add Task  2. Complete Task  3. Remove Task  4. Exit")
    choice = input("Enter choice (1-4): ")

    if choice == "1":
        new_task = input("What is the task? ")
        tasks.append(new_task)
        status.append(False) # New tasks start as not finished

    elif choice == "2":
        num = int(input("Enter the task number to mark finished: "))
        status[num - 1] = True # Changes False to True

    elif choice == "3":
        num = int(input("Enter the task number to remove: "))
        tasks.pop(num - 1)
        status.pop(num - 1)

    elif choice == "4":
        print("Goodbye!")
        break