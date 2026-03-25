from crud import add_user, view_users, update_user, delete_user

def menu():
    while True:
        print("\n===== CRUD MENU =====")
        print("1. Add User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            add_user(name, age)

        elif choice == "2":
            view_users()

        elif choice == "3":
            user_id = int(input("Enter user ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            update_user(user_id, name, age)

        elif choice == "4":
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()