def remove_element_by_index(elements):
    try:
        index = int(input(f"Enter the index (0 to {len(elements) - 1}) of the element to remove: "))
        if 0 <= index < len(elements):
            removed_element = elements.pop(index)
            print(f"Removed element: {removed_element}")
        else:
            print("Invalid index. Please try again.")
    except ValueError:
        print("Please enter a valid integer.")

def remove_element_by_name(elements):
    name = input("Enter the name of the element to remove: ")
    if name in elements:
        elements.remove(name)
        print(f"Removed element: {name}")
    else:
        print("Element not found in the list.")

def main():
    elements = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print("Current elements:", elements)

    while True:
        choice = input("Do you want to remove an element by 'index' or by 'name'? (type 'exit' to quit): ").lower()
        
        if choice == 'index':
            remove_element_by_index(elements)
        elif choice == 'name':
            remove_element_by_name(elements)
        elif choice == 'exit':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please type 'index', 'name', or 'exit'.")
        
        print("Current elements:", elements)

if __name__ == "__main__":
    main()