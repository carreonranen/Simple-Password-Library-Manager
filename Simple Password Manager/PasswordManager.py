# The purpose of this practice is to create a simple account manager that holds details

#Import required libraries
from cryptography.fernet import Fernet

#Function to load the secret key. Without it we can't decrypt the file. Or we need to generate a new password using the generate_key.py again
def load_key():
    return open('Projects/Password Manager/secret.key', 'rb').read()
key = load_key()
fernet = Fernet(key)

# Create the class that will hold our account details
class User:
    # Constructor that initialize our data
    def __init__(self, website, username, password, email):
        self.website = website
        self.username = username
        self.password = password
        self.email = email


##############################################################################################################################
#
############ Main functions ##############
def add_db():
    # Prompt the user questions
    website = input("What's the website name? ")
    username = input("\nWhat's the username? ")
    password = input("\nWhat's the password? ")
    email = input("\nWhat's the email? ")

    # Create an instance of the user class
    new_account = User(website, username, password, email)

    # Format the data from object into a single string
    account_string = f"Website: {new_account.website}, User: {new_account.username}, Password: {new_account.password},Email: {new_account.email}"

    # Encode this string
    # Encode the formatted string to bytes or it will throw error
    account_bytes = account_string.encode()

    # Encrypt the new_account information
    encryptedAccount = fernet.encrypt(account_bytes)

    # Write the information to database
    with open('database.bin', 'ab') as f:
        # Write the new information
        f.write(encryptedAccount + b'\n')

    # Output successful
    print("\nAccount successfully added! ")
    input("Press enter to continue...")

    # Go back to main menu
    # Menu() #Leaving it here to prevent from future use and a reminder. This creates recursion problem. Best way is to do While True: in main menu


def sub_db():
    print("This subtracts data to db")


def user_db():
    # Read the database again for any new changes
    print("\n--- All Accounts ---")
    try:
        with open('database.bin', 'rb') as f:
            for line in f:
                if not line.strip():
                    continue

                # Decrypt the line
                decrypted_line = fernet.decrypt(line.strip())

                # Decode from bytes back to a string and print
                print(decrypted_line.decode())

                #Add an input to prevent from going back to main menu automatically
                pause_enter = input("Press enter to return back to menu")

    except FileNotFoundError:
        print("Database does not exist yet. Add an account to create it.")
        returnMenu = input("Press enter to return ")
    except Exception as e:
        print(f"An error ocurred: {e}")


def selected_option(user_input):
    # This is the function that holds nested loops
    if (user_input == 1):
        # Call the function for the database
        user_db()
    elif (user_input == 2):
        # Call the function that edits the user_db function
        add_db()
    elif (user_input == 3):
        # Call the function that remove edits the user_db function
        sub_db()
    elif (user_input == 4):
        # Exit
        exit()
    else:
        print("Error must put an integer between 1 - 4")
        exit()


def Menu():
    while True:  # This is the proper way to loop back to main menu after you finish adding/subtracting

        # variable to hold input and prompt
        print("\n\n1) View accounts\n")
        print("2) Add user to account manager\n")
        print("3) Remove user to account manager\n")
        print("4) Exit\n")
        prompt = "\nWelcome Ranen. What would you like to do? "
        user_input = input(prompt)

        # Convert that input string into integer
        try:
            user_input = int(user_input)
            # Print to the user the main menu
            print(f"\n You chose to: {user_input}")
            selected_option(user_input)
        except ValueError:
            print('Invalid input')
            continue


Menu()

#######################################################################################################################################
