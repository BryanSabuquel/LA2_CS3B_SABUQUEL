def userReg():
    print("REGISTRATION FORM\nFill in the form below.\n")
    
# Ask and collect the user details
    fName = input("Enter your first name: ")
    lName = input("Enter your last name: ")
    course = input("Enter your Course: ")
    yearLevel = input("Enter your year Level: ")
    section = input("Enter your section: ")
    username = input("\nCreate a username: ")
    password = input("Create a password: ")

# Create a pin code
    pinCode = input("Create an 8-digit pin code: ")
# Ensure that the pin code is exactly 8 digits long and contains only numbers
    while len(pinCode) != 8 or not pinCode.isdigit():
        print("Pin code is invalid. It must contain exactly 8 digit numbers.")
        pinCode = input("Create an 8-digit pin code: ")
        
# Store all the collected user info in a list   
    userInfo = [fName, lName, course, yearLevel, section, username, password, pinCode]
    
    return userInfo

def userLogIn(userInfo):

# Loop until username and password are correct
    while True:
        print("\nLog in with your username and password")
        enterUsername = input("Enter Username: ")
        enterPassword = input("Enter Password: ")
        
# Check if the password and username matched what you have registered   
        if enterUsername == userInfo[5] and enterPassword == userInfo[6]:
            print("\nYou are now successfully logged in.")
            
# Loop until you got the correct pin code           
            while True:
                enterPin = input("Enter your 8 digit pin code to continue:\n ")
                if enterPin == userInfo[7]:           	
# Display user details       
                    print(f"\nHERE ARE YOUR DETAILS.")
                    print(f"Name: {userInfo[0]} {userInfo[1]}")
                    print(f"Course, Year, Section: {userInfo[2].upper()}, {userInfo[3]}{userInfo[4].upper()}")
                    print(f"Username: {userInfo[5]}")
                    return 
                else:
                    print("Incorrect pin code. Please try again.") # Tell the user that the pin is incorrect
        else:
            print("Incorrect username or password. Please try again.") # Tell the user that the password or username is incorrect

def func():
# Register the user and save their info    
    userInfo = userReg()
    print("\nCongratulations! You have successfully registered.")
# Ask the user if he/she wants to log in
    logOption = input("Do you want to log in? YES or NO? ").strip().upper()
# Log in if the user entered "YES", else exit
    if logOption == "YES":
        userLogIn(userInfo)
    else:
        print("Have a good day, BYE!")
        
if __name__ == "__main__":
    func()