import getpass

def adduser():  # defines a function named adduser that handles the process of creating a new user account
    username = input("Enter new username: ").lower() # asks the user to input new username and converts it to a lowercase
    real_name = input("Enter user's real name: ")  # asks to input user's real name
    password = getpass.getpass("Enter password: ") # asks for the password without echoing(displaying) to the console
    
    with open("passwd.txt", "r" ) as file: # open the file "passwd.txt" in read mode
        lines = file.readlines()
        for line in lines:
            existing_username = line.split(":")[0].lower() # extracts the username from the current line

    if username == existing_username:  # Checks if the entered username matches any existing username in the file
        print("Cannot add. Username already exists.")
    else:
        with open("passwd.txt", "a") as file: # opens the file in append mode to add the new user's information
            file.write(f"{username}:{real_name}:{password}\n") # write the details of new user to the file

        print("User Created.")

if __name__ == "__main__":
    adduser()  # Calls the adduser function when the script is executed


