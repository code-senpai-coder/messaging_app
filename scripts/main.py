#imoporting scripts
import sing_up_script
import clear_messages
import login_script
import logout_script
import message_reader
import send_message
import time

print("Welcome to the messaging app: \n")
#Main loop function

def main():
    print("Chose your action: \n")
    print("To signup type signup\nTo login type in login\n")
    action  = input("Enter action: ")

    #getting user action info
    if action == "signup":
        sing_up_script.signup()
    elif action == "login":
        login_script.login()
    
    #getting logged user info
    user_logged_info = open("data\logged_user_info.txt", "r+")
    logged_name = user_logged_info.readline()
    user_logged_info.close()

main()