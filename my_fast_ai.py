def check_status():
    try:
     with open(".txt","r") as f:
        f.read()
    except FileNotFoundError:
       print("file nahi mila")