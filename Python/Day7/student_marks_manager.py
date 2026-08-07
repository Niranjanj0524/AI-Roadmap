def display_menu():
    print("\n==============================")
    print(" STUDENT MARKS MANAGER ")
    print("==============================")
    print("1. Display all marks")
    print("2. Add new marks")
    print("3. Remove a mark")
    print("4. Find Highest, Lowest, and Average")
    print("5. Sort marks (Highest to Lowest)")
    print("6. Exit")
    print("==============================")

def main():
    # Initial list storing student marks
    marks = [78, 92, 85, 64, 89]
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        # 1. Displays all marks
        if choice == '1':
            if len(marks) == 0:
                print("\nThe list is empty. No marks to display.")
            else:
                print("\nCurrent Student Marks:")
                index = 1
                for mark in marks:
                    print("Student", index, ":", mark)
                    index = index + 1
        
        # 2. Adds new marks
        elif choice == '2':
            new_mark = int(input("\nEnter the new mark to add: "))
            if new_mark >= 0 and new_mark <= 100:
                marks.append(new_mark)
                print("Mark added successfully.")
            else:
                print("Error: Marks should be between 0 and 100.")
                
        # 3. Removes marks
        elif choice == '3':
            if len(marks) == 0:
                print("\nThe list is empty. Nothing to remove.")
            else:
                remove_mark = int(input("\nEnter the exact mark to remove: "))
                
                # Check if mark exists in the list before removing
                if remove_mark in marks:
                    marks.remove(remove_mark)
                    print("Mark removed successfully.")
                else:
                    print("Error: Mark not found in the list.")
                
        # 4. Finds Highest, Lowest, and Average marks
        elif choice == '4':
            if len(marks) == 0:
                print("\nNo data available to calculate statistics.")
            else:
                highest = max(marks)
                lowest = min(marks)
                
                # Calculate average using basic math
                total_sum = sum(marks)
                total_count = len(marks)
                average = total_sum / total_count
                
                print("\n--- Performance Summary ---")
                print("Highest Mark :", highest)
                print("Lowest Mark  :", lowest)
                print("Average Mark :", average)
                
        # 5. Sorts marks
        elif choice == '5':
            if len(marks) == 0:
                print("\nThe list is empty. Nothing to sort.")
            else:
                marks.sort(reverse=True)
                print("\nMarks sorted in descending order:")
                print(marks)
                
        # 6. Exit
        elif choice == '6':
            print("\nThank you for using Student Marks Manager. Goodbye!")
            break
            
        else:
            print("\nInvalid choice! Please select an option between 1 and 6.")

# Run the program
if __name__ == "__main__":
    main()







# # 1. Create a list of five numbers
# numbers = [42, 17, 89, 17, 23]
# print("Original List:", numbers)

# # 2. Print the first and last element
# print("First Element:", numbers[0])
# print("Last Element:", numbers[-1])

# # 3. Find the length of a list
# print("Length of List:", len(numbers))

# # 4. Find the maximum element
# print("Maximum Element:", max(numbers))

# # 5. Find the minimum element
# print("Minimum Element:", min(numbers))

# # 6. Find the sum of all elements
# print("Sum of Elements:", sum(numbers))

# # 7. Sort the list in ascending order
# numbers.sort()
# print("Sorted (Ascending):", numbers)

# # 8. Sort the list in descending order
# numbers.sort(reverse=True)
# print("Sorted (Descending):", numbers)

# # 9. Reverse a list
# numbers.reverse()
# print("Reversed List:", numbers)

# # 10. Count duplicate values (e.g., counting how many times 17 appears)
# print("Count of 17:", numbers.count(17))

# # 11. Remove an element (removes the first occurrence of 89)
# numbers.remove(89)
# print("After removing 89:", numbers)

# # 12. Insert an element (inserts 99 at index 2)
# numbers.insert(2, 99)
# print("After inserting 99 at index 2:", numbers)

# # 13. Traverse a list using a loop
# print("Traversing list elements:")
# for num in numbers:
#     print(num, end=" ")
# print("\n")  # Newline for clarity

# # 14. Create a nested list
# students_data = [
#     ["Alice", "Grade A"],
#     ["Bob", "Grade B"],
#     ["Charlie", "Grade A"]
# ]
# print("Nested List:", students_data)

# # 15. Print student names from a nested list
# print("Student Names:")
# for student in students_data:
#     print(student[0])
