def readMessage():  
    #importing modules
    import time

    database = open("data\message_database.txt", "r+")
    messages = database.readlines()
    database.close()
    #remove \n
    for i in range(0,len(messages)):
        messages[i] = messages[i][:-1]
    #adds mesages for return
    result = []
    for text in messages:
        result.append(text)
    return result