task = input("Enter your task:")
priority = input("What is the task priority?(high, medium, low):").lower()
time_bound = input("Is the task time bound?(yes or no):").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a high priority task. Try to work on it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that requires attention today!")
        else:
            print(f"Reminder: {task} is a medium priority task. Plan to do it when convenient.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low priority task but time-sensitive!")
        else:
            print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter high, medium or low")