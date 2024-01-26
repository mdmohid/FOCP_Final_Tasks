import getpass

def passwd(): # defines a function named passwd that handles the process of changing a user's password
    username = input("User: ").lower()  # asks the user to input their username and converts it to a lowercase
    current_password = getpass.getpass("Current Password: ")  # asks the user to enter their current password

    with open("passwd.txt", "r") as file: # opens the file "passwd.txt" in read mode
        lines = file.readlines()

    found = False  # initialize a flag to track if the user is found and password changed successfully
    with open("passwd.txt", "w") as file: # opens the file in write mode to overwrite the existing content.
        for line in lines:
            passwd_txt = line.split(":")
            if passwd_txt[0].lower() == username and passwd_txt[2].strip() == current_password:

                # asks the user for new password and confirm it
                new_password = getpass.getpass("New Password: ") 
                confirm_password = getpass.getpass("Confirm: ")

                if new_password == confirm_password: # check if the new password is matched with confirm password and update it to the file
                    file.write(f"{passwd_txt[0]}:{passwd_txt[1]}:{new_password}\n") 
                    found = True
                    print("Password changed.")
                else:
                    print("Passwords do not match. Nothing changed.")
                    
            else:
                file.write(line) # If the username and password do not match then write the unchanged user data to the file

    # check the user if the user is not found or the current password is incorrect
    if not found:
        print("User not found or incorrect password. Nothing changed.")

if __name__ == "__main__":
    passwd()  # Calls the deluser function when the script is executed


