def save_memory(msg):
    try:
     with open("ultron_chat.txt","a") as f:
        f.write(msg+"\n")
    except FileNotFoundError:
       print("file nahi mile ,sahi sa check karo")
def read_memory():
   try:
      with open("ultron_chat.txt","r") as f:
         r=f.read()
         print(r)
   except FileNotFoundError:
      print("file nahi mila")
   
while True:
   choise=input("chose youe number ")
   if(choise=="1"):
       
       msg = input("Kya save karna hai?: ")

       save_memory(msg)
     
   elif(choise=="2"):
     read_memory()
   elif(choise=="3"):
      break