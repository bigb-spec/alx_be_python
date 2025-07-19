Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ").lower()
Time_Bound = input("Is it time-bound?(yes/no): ").lower()

match Priority:
    case "high":
        if Time_Bound == "yes":
            print(f"Reminder: '{Task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{Task}' is a high priority task. Try to work on it as soon as possible.")
    case "medium":
        if Time_Bound == "yes":
            print(f"Reminder: '{Task}' is a medium priority task that requires attention today!")
        else:
            print(f"Reminder: '{Task}' is a medium priority task. Plan to do it when convenient.")
    case "low":
        if Time_Bound == "yes":
            print(f"Reminder: '{Task}' is a low priority task but time-sensitive!")
        else:
            print(f"Reminder: '{Task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter high, medium or low")