import os

# Function to register a new user
def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    user_data = f"Username: {username}\nPassword: {password}\n"

    user_folder = f"users/{username}"

    # Check if the user folder already exists
    if os.path.exists(user_folder):
        print("User already exists. Please choose a different username.")
        return

    # Create a user folder and save user data
    os.makedirs(user_folder)
    with open(f"{user_folder}/user_info.txt", "w") as file:
        file.write(user_data)
    print("Registration successful!")

# Function to log in
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user_folder = f"users/{username}"

    # Check if the user folder exists
    if not os.path.exists(user_folder):
        print("User not found. Please register or check your credentials.")
        return

    # Check if the provided password matches the saved password
    with open(f"{user_folder}/user_info.txt", "r") as file:
        saved_data = file.read()
        if f"Password: {password}" in saved_data:
            print("Login successful!")
            view_data(user_folder)
        else:
            print("Incorrect password. Please try again.")

# Function to view user data
def view_data(user_folder):
    with open(f"{user_folder}/user_data.txt", "r") as file:
        user_data = file.read()
        print("Your data:")
        print(user_data)

# Main program loop
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose a valid option.")
