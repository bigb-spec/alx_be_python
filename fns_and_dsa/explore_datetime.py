from datetime import datetime, timedelta

def display_current_datetime():
    #get current date and time
    current_datetime = datetime.now()
    
    #format the current date and time as "YYYY-MM-DD HH-MM-SS"
    format_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current Date and Time: {format_datetime}")
    
    #call the function when the script runs
if __name__ == "__main__":
        display_current_datetime()

number_of_days = int(input("Enter number of days to add to the current date: "))
def calculate_future_date():
    #prompt user for number of days
    
        future_date = datetime.now() + timedelta(days=number_of_days)
    
        formatted_future = future_date.strftime("%Y-%m-%d %H:%M:%S")
        print("Future Date after", number_of_days, "days:", formatted_future)

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
    