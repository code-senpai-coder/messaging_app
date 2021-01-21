def clearMessages():
    message_database = open("data\message_database.txt", "w")
    message_database.write("")
    message_database.close()