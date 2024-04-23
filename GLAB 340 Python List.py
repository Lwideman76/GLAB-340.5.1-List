import random

# Create a list of words for the game
word_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Function to generate a target list
def generate_target_list():
    return random.sample(word_list, k=random.randint(3, len(word_list)))

# Function to display current list and target list
def display_lists(current_list, target_list):
    print("Current List:", current_list)
    print("Target List:", target_list)

# Function to perform operations on the list
def manipulate_list(current_list):
    print("\nAvailable Operations:")
    print("1. Append a word")
    print("2. Extend with another list")
    print("3. Concatenate two elements")
    print("4. Traverse the list")
    print("5. Modify an element")
    print("6. Insert an element at specific index")
    print("7. Pop an element")
    print("8. Remove a specific element")
    print("9. Sort the list (ascending)")
    print("10. Sort the list (descending)")
    choice = input("Enter your choice (1-10): ")

    if choice == "1":
        word = input("Enter word to append: ")
        current_list.append(word)
    elif choice == "2":
        extension = input("Enter list to extend with (comma-separated): ").split(",")
        current_list.extend(extension)
    elif choice == "3":
        index1 = int(input("Enter index of first element: "))
        index2 = int(input("Enter index of second element: "))
        if 0 <= index1 < len(current_list) and 0 <= index2 < len(current_list):
            current_list[index1] += current_list[index2]
            del current_list[index2]
        else:
            print("Invalid indices.")
    elif choice == "4":
        print("Traversing List:")
        for item in current_list:
            print(item)
    elif choice == "5":
        index = int(input("Enter index of element to modify: "))
        if 0 <= index < len(current_list):
            new_value = input("Enter new value: ")
            current_list[index] = new_value
        else:
            print("Invalid index.")
    elif choice == "6":
        index = int(input("Enter index to insert at: "))
        element = input("Enter element to insert: ")
        current_list.insert(index, element)
    elif choice == "7":
        if current_list:
            current_list.pop()
        else:
            print("List is empty.")
    elif choice == "8":
        element = input("Enter element to remove: ")
        if element in current_list:
            current_list.remove(element)
        else:
            print("Element not found in list.")
    elif choice == "9":
        current_list.sort()
    elif choice == "10":
        current_list.sort(reverse=True)
    else:
        print("Invalid choice.")

# Main game loop
def main():
    target_list = generate_target_list()
    current_list = []

    print("Welcome to the List Manipulation Game!")

    while True:
        display_lists(current_list, target_list)

        if current_list == target_list:
            print("Congratulations! You've matched the target list.")
            break

        manipulate_list(current_list)

if __name__ == "__main__":
    main()