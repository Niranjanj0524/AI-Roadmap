# Q1. Create and write to a file
with open("hello.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("I am learning AI.\n")
    file.write("Today I learned File Handling.\n")

print("File created and data written successfully!")


# Q2. Read the complete file using read()
with open("hello.txt", "r") as file:
    data = file.read()

print(data)


# Q3. Read one line using readline()
with open("hello.txt", "r") as file:
    line = file.readline()

print(line)


# Q4. Read all lines using readlines()
with open("hello.txt", "r") as file:
    lines = file.readlines()

print(lines)


# Q5. Append data to the file
with open("hello.txt", "a") as file:
    file.write("I am preparing for AI and ML.\n")

print("Data appended successfully!")


# Q6. Read the file after appending
with open("hello.txt", "r") as file:
    data = file.read()

print(data)


# Q7. Take user input and write it to a file
name = input("Enter your name: ")

with open("user.txt", "w") as file:
    file.write(f"Name: {name}\n")

print("Name saved successfully!")


# Q8. Take a note and append it
note = input("Enter a note: ")

with open("user.txt", "a") as file:
    file.write(f"Note: {note}\n")

print("Note added successfully!")


# Q9. Display saved data
with open("user.txt", "r") as file:
    data = file.read()

print(data)


print("\n================================")
print("       NOTES MANAGEMENT")
print("================================")


while True:

    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        note = input("Enter your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note added successfully!")


    elif choice == "2":

        with open("note.txt", "r") as file:
            notes = file.read()

        print("\n========== YOUR NOTES ==========")

        if notes:
            print(notes)
        else:
            print("No notes available.")

    elif choice == "3":

        print("Thank you for using Notes Management!")
        break

    else:

        print("Invalid choice! Please try again.")
