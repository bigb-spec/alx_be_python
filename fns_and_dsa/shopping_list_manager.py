def display_menu():
    print("Shopping list manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            #prompt for and add an item
            item = input("Enter the item to add: ")
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("Item name cannot be empty.")
                
        elif choice == '2':
            #prompt for and remove an item
            item = input("Enter the item to remove: ")
            if item:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
        
        elif choice == '3':
            #Display the shopping list
            if shopping_list:
                print("Current shopping list: ")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Shopping list is currently empty.")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()