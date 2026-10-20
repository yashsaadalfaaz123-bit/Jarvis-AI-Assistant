to_do_list=[]
while True:
    try:
        user_input=input("Enter your task: ")


        if(user_input=="exit"):
            break

        to_do_list.append(user_input)
        print(to_do_list)

        with open("memory.txt","a") as f:
            f.write(user_input + "\n")


    except Exception as e:
        print("kuch gadbad ha ",e)
        break
print("finally",to_do_list)