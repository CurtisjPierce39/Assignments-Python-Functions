#Question 2 Task 1

shopping_list = ['apple', 'banana', 'toilet paper towels']

def shopping_list_management():
    while True:
        print("\nShopping List")
        print("1. Add item")
        choice = input("Choose number: ")
        
        if choice == "1":
            item_to_add = input("Enter new item: ")
            shopping_list.append(item_to_add)
            print(f"{item_to_add} has been added to the shopping list!")

shopping_list_management()


#Question 2 Task 2

shopping_list = ['apple', 'banana', 'toilet paper towels']

def shopping_list_management():
    while True:
        print("\nShopping List")
        print("1. Add item")
        print("2. Remove Item")
        print("3. Display List")
        choice = input("Choose number: ")
        
        if choice == "1":
            item_to_add = input("Enter new item: ")
            shopping_list.append(item_to_add)
            print(f"{item_to_add} has been added to the shopping list!")
            
        elif choice == "2":
            item_to_remove = input("Enter item to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"{item_to_remove} has been removed from the shopping list!")

shopping_list_management()


#Question 2 Task 3

shopping_list = ['apple', 'banana', 'toilet paper towels']

def shopping_list_management():
    while True:
        print("\nShopping List")
        print("1. Add item")
        print("2. Remove Item")
        print("3. Display List")
        choice = input("Choose number: ")
        
        if choice == "1":
            item_to_add = input("Enter new item: ")
            shopping_list.append(item_to_add)
            print(f"{item_to_add} has been added to the shopping list!")
            
        elif choice == "2":
            item_to_remove = input("Enter item to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"{item_to_remove} has been removed from the shopping list!")
            
        elif choice == "3":
            print("\nCurrent Shopping List:")
            print(shopping_list)

shopping_list_management()