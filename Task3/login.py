import getpass

def login(): # defines a function named login that handles the login process
    username = input("User: ").lower()  # asks the user to enter username and converts it to a lowercase
    password = getpass.getpass("Password: ")  # asks the user for password
 
    with open("passwd.txt", "r") as file:  # opens the file "passwd.txt" in read mode
        for line in file:
            passwd_txt = line.split(":")
            if passwd_txt[0].lower() == username and passwd_txt[2].strip() == password: # Check if the provided username and password match any entry in the file
                print("Access granted.")  # print "Access granted." messege if the provided username and password are matched
                return

    print("Access denied.")   # print "Access denied." messege if the provided username and password are  not matched

if __name__ == "__main__":
    login()  # calls login function when the script is executed


