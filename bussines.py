def bussines():
 try:
  while True:

    d={}
    name=input("Inter your name: ")

    if(name=="exit"):
        break
    
    location=input("Enter addres: ")
    
    ammount=float(input("Inter your ammount: "))

    date=input("enter date:")
    phone_number = input("Enter your 10-digit phone number: ")
    if len(phone_number) == 10 and phone_number.isdigit():
        print("Phone number verified!")
    else:
        print("❌ Error: Phone number must be exactly 10 digits. Try again!")
        continue
            
      
        
    d["name"]=name
    d["location"]=location
    d["ammount"]=ammount
    d["date"]=date
    d["phone_number"]=phone_number

    print("Save Contact",d)
    
    with open("Costomer.txt","a") as f:
       f.write(f"Name: {d['name']}, Phone: {d['phone_number']}, Amount: {d['ammount']} ,date: {d['date']} ,location:  {d['location']}\n"
    )
       print("\n--- Updated Costomer List ---")
       with open("Costomer.txt","r") as f:
          d=f.read()
          print(d)
       print("\n------------------------------\n")
              
          
 except Exception as e:
    print("kuch galti ho gaya ha ",e)
     
    
bussines()



    