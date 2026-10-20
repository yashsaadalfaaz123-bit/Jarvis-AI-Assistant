import os
import webbrowser
def app_open():
    while True:
        user=input("Enter kon sa app kholna ha : ")
        if(user=="break"):
            break
                    

        url =webbrowser.open( f"https://www.google.com/search?q={user}")
app_open()
                
