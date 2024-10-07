my_list = [1, 2, 3, 4, 5]
user_input = input("Do you want to clear the list? (yes/no): ").strip().lower()

if user_input == 'yes':
    my_list.clear()
    print("the list has been cleared.")
elif user_input == 'no':
    print("the list remains unchanged.")
else:
    print("invalid input. Please enter 'yes' or 'no'.")

print("Current list:", my_list)