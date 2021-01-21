def sendMessage():
    #importing modules
    import datetime
    #get user message input
    message = input("Enter message: ")
    user_info_file = open("data\logged_user_info.txt", "r+")
    name = user_info_file.read()
    user_info_file.close()
    time_sent = datetime.datetime.now()
    #contructing message
    final_message = name + ": " + message + "\t \t" +str(time_sent)
    #sent message to database
    message_database = open("data\message_database.txt","a")
    message_database.write(final_message + "\n")
    message_database.close()