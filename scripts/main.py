#imoporting scripts
import sing_up_script
import clear_messages
import login_script
import logout_script
import message_reader
import send_message
import time
import datetime

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

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    #getting logged user info
    user_logged_info = open("data\logged_user_info.txt", "r+")
    logged_name = user_logged_info.readline()
    user_logged_info.close()

    #getting everything to display on screen 
    screen = ""
    screen += f"logged as: {logged_name} \n"
    screen += f"time: {datetime.datetime.now()} \n"
    messages = message_reader.readMessage()
    for text in messages:
        screen += text 
        screen += "\n"

    print(screen)
    #temporary time to see answer
    time.sleep(10)
if __name__ == "__main__":
    main()