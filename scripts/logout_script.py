def logout():
    info  = open("data\logged_user_info.txt", "w+")
    info.write("")
    info.close()