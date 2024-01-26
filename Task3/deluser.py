def deluser(): # defines  a function named deluser that handles the process of deleting a user account
    username = input("Enter username: ").lower() # asks the user to input username and converts it to a lowercase

    with open("passwd.txt", "r") as file: # open the file "passwd.txt" in read mode
        lines = file.readlines()

    found = False  # initialize a flag to track whether the specified user is found in the file

    with open("passwd.txt", "w") as file: # opens the file "passwd.txt" in write mode to overwrite the existing content.
        for line in lines:
            existing_username = line.split(":")[0].lower() # extracts the username from the current line
            if existing_username != username: # Checks if the entered username does not matche any existing username in the file and write to it
                file.write(line)
            else:
                found = True   # sets flag that user has been found and deleted
    if found:
        print("User Deleted")  # prints "User Deleted" messege if the user is found and deleted 
    else:
        print("No user found. Nothing changed.")   # prints "No user found. Nothing changed." messege if the user is not found              

if __name__ == "__main__":
    deluser()  # Calls the deluser function when the script is executed