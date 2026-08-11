while True:
    print("\n===Notes Management===")
    print("1.Add Note")
    print("2.View Note")
    print("3.Exit")

    choice = input("Enter choice : ")

    if choice == "1":
        note = input("Enter your Note : ")

        with open("note.txt","w") as file:
            file.write(note + "\n")
        print("Note Added Successfuly!")
    elif choice == "2":
        with open("note.txt","r") as file:
            notes = file.read()

        print("\nYour Notes:")
        print(notes)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid Chioce")