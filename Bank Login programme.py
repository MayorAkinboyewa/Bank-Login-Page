def create_castle_account():
    username = input("Enter your Username: ")
    password = input("Enter a Password: ")
    confirm_password = input("Re-enter the Password to confirm: ")
    if password == confirm_password:
        save_account(username, password)
        print("Castle Account created successfully!")
    else:
        print("Passwords do not match. Account creation failed.")
def save_account(username, password):
    with open("accounts.txt", "a") as file:
        file.write(f"{username}:{password}\n")
def login():
    username = input("Enter your username: ")
    password = input("Enter your Password: ")
    if validate_account(username, password):
        print("Castle Account Login successful!")
    else:
        print("Invalid username or Password. Try again!!")
def validate_account(username, password):
    with open("accounts.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                return True
    return False
def main():
    print("Welcome to the Castle Bank Login System")
    while True:
        print("\n1. Create Castle Account")
        print("2. Account Login")
        print("3. Exit App")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            create_castle_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Thanks for using our Banking app!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

