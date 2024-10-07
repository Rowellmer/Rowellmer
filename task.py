numbers_list = []
num_elements = int(input("How many numbers do you want to add to the list? "))

for i in range(num_elements):
    number = float(input(f"Enter number {i + 1}: "))
    numbers_list.append(number)
print("The list of number you entered is:", numbers_list)