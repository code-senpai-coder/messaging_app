def readMessage():  
    #importing modules
    import time

    database = open("data\message_database.txt", "r+")
    messages = database.readlines()
    database.close()
    #remove \n
    for i in range(0,len(messages)):
        messages[i] = messages[i][:-1]
    #prints messages one by one
    for text in messages:
        print(text)
    #temporary time w8
    time.sleep(10)