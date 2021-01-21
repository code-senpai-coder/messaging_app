def signup():
    #get user info
    name = str(input("Enter you name: "))
    password = str(input("Enter your password: "))
    data = [name,"\n",password]
    #save to database
    database = open("data\\" + name + ".txt", "w")
    database.writelines(data)
    database.close()
    user_logged_info = open("data\logged_user_info.txt", "w+")
    user_logged_info.write(name)
    user_logged_info.close()
