
mixed_list = [3, "apple", 1, "banana", 2, "cherry"]

user_choice = input("Would you like to sort or reverse the list? (Enter 'sort' or 'reverse'): ").strip().lower()

if user_choice == 'sort':
    sorted_list = sorted(mixed_list, key=lambda x: str(x))
    print("Sorted list:", sorted_list)
elif user_choice == 'reverse':
    reversed_list = mixed_list[::-1]
    print("Reversed list:", reversed_list)
else:
    print("Invalid choice. Please enter 'sort' or 'reverse'.")