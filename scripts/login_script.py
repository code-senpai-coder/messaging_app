def login():
    #get user info
    name = input("Enter you name: ")
    password = input("Enter your password: ")
    #check with database
    user_file = open("data\\" + name + ".txt", "r+")
    extracted_data = user_file.readlines()
    extracted_data[0] = extracted_data[0][:-1]
    if extracted_data[0] == name and extracted_data[1] == password:
        user_info_file = open("data\logged_user_info.txt", "w")
        user_info_file.write(name)
        user_info_file.close()
        print("Logged in")
    else:
        print("Wrong name or password")
        login()
    user_file.close()