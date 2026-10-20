# import requests
# def chat():
#     user=input("kay bat karna ha : ")
#     url="http://localhost:11434/api/generate"
#     payload={
#         "model":"llama3:latest",
#         "prompt":user,
#         "stream":False
#     }
#     response=requests.post(url,json=payload)


#     if response.status_code == 200:
        
#         # STEP 4: Ollama ke JSON Jawab Ko Python Mein Badalna
#         # Ollama jo jawab bhejta hai wo JSON format mein hota hai, use .json() se Python Dictionary banate hain
#         result = response.json()
        
#         # STEP 5: Main Answer Extract Karke Print Karna
#         # Dictionary mein se sirf 'response' wali key ka text nikal kar print kar dete hain
#         print("AI:", result.get("response"))
        
#     else:
#         print("Error aa gaya bhai:", response.status_code)
# chat()



# import requests

# def chat():
#     user = input("Kay baat karna ha: ")
#     url = "http://localhost:11434/api/generate"
    
#     # STEP 1: Payload (Data Packet) Tayar Karna
#     # Humne saara saamaan ek Python dictionary mein pack kiya
#     payload = {
#         "model": "llama3:latest",
#         "prompt": user,
#         "stream": False
#     }
    
#     # STEP 2: Request Bhejna (JSON me convert karke)
#     # json=payload likhne se Python is dictionary ko JSON format mein badal kar Ollama ko bhej deta hai
#     response = requests.post(url, json=payload)
    
#     # STEP 3: Connection Check Karna
#     # 200 ka matlab hota hai ki Ollama tak message pahunch gaya aur usne jawab de diya
#     if response.status_code == 200:
        
#         # STEP 4: Ollama ke JSON Jawab Ko Python Mein Badalna
#         # Ollama jo jawab bhejta hai wo JSON format mein hota hai, use .json() se Python Dictionary banate hain
#         result = response.json()
        
#         # STEP 5: Main Answer Extract Karke Print Karna
#         # Dictionary mein se sirf 'response' wali key ka text nikal kar print kar dete hain
#         print("AI:", result.get("response"))
        
#     else:
#         print("Error aa gaya bhai:", response.status_code)

# chat()


















import requests

def chat():
    user=input("kay bat karna ha :")
    url="http://localhost:11434/api/generate"
    payload={
        "model":"llama3:latest",
        "user": user,
        "prompt":False


    }
    r=requests.post(url,json=payload)

    if(r.status_code==200):
        print("sab thek ha")
    else:
        print("kuch gad bad ha")
chat()