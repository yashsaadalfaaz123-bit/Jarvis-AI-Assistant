import edge_tts
import os

import pygame
import requests
import duckduckgo_search
import webbrowser
import asyncio
import datetime
import speech_recognition as sr
from pycaw.pycaw import AudioUtilities ,  IAudioEndpointVolume
import json
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
#========= CAMARA KA LAYA =========================
import cv2 
import requests     # Ollama ke local server par HTTP request bhejne ke liye
import base64
import time
import threading
import google.generativeai as genai
# ====================================================
from dotenv import load_dotenv
load_dotenv()
# File ke sabse upar yahan apni key rakh de
# File ke sabse upar yahan apni key rakh de
# GitHub safe configuration: Environment variable se key uthayega
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# API key configure karna
genai.configure(api_key=GEMINI_API_KEY)

# Gemini vision model ko variable mein set karna
model = genai.GenerativeModel('gemini-3.6-flash')
#=================Advanced File Automation==================
import os
import shutil
import pathlib
#===========================================================
#================battry percentage==========================
import psutil

async def speak(text):

 cominatek=edge_tts.Communicate(text,"hi-IN-MadhurNeural")
 await cominatek.save("voice.mp3")
 pygame.init()
 pygame.mixer_music.load("voice.mp3")

 pygame.mixer_music.play()

 while pygame.mixer_music.get_busy():
  pygame.time.Clock().tick(10)
 pygame.mixer_music.unload()

def listen():
 r=sr.Recognizer()
 with sr.Microphone() as source:

  print("LETINIENG....")

  audio=r.listen(source)
  try:
    e=r.recognize_google(audio,language='en-IN')
    print(e)
    e.lower()
    return e.lower()
  except:
   return ""


def chat(prompt):
 try:
  final_prompt=prompt
  with  open("clint_prosnal_memory.json","r") as f:
    h=json.load(f)
    history_list = h.get("history", [])
    history_text = "\n".join(history_list)
    final_prompt = f"History:\n{history_text}\n\nUser: {prompt}"
 except Exception as n:
  print(n)
  final_prompt = (
                "You are JARVIS, a helpful personal voice assistant. "
                "Here is the past conversation history with the user:\n"
                f"{history_text}\n\n"
                "Based on the above history, answer the user's latest question naturally and smartly in Hinglish/English.\n"
                f"User's latest question: {prompt}"
            )
 except Exception as n:
        print(n)
        final_prompt = prompt
 
 url="http://localhost:11434/api/generate"
 

  
 payload={
     "model":"llama3:latest",
     
     "prompt":final_prompt,
     "stream":False
 }

 response=requests.post(url,json=payload)

 if response.status_code==200:
  result = response.json().get("response")
  print("AI:",result)
  asyncio.run(speak(result))
 else:
  
   print( "kuch gadbad ha",response.status_code )


def weather(city):
 
 weather_res = requests.get(f"https://wttr.in/{city}?format=3")
 asyncio.run(speak(weather_res.text))



def search(query):
  url=(F"https://api.duckduckgo.com/?q={query}&format=json")
  respinse=requests.get(url)
  data=respinse.json()
  answer= data.get("AbstractText")
  if answer:  
   print(answer)
  else:
   
   

   topics=data.get("RelatedTopics")

   if topics:
    for topic in topics:
     
     
     print("Text")
     print(topic["Text"])
     asyncio.run(speak(topic["Text"]))
     break


def app_opner(app_name):
 url=( f"https://www.{app_name}.com")
 webbrowser.open(url)
 asyncio.run(speak(f"Opening {app_name}"))
def tell_time():
 current_time=datetime.datetime.now()
 clen_time=current_time.strftime("%I:%M %p")
 asyncio.run(speak(f"sir the time is {clen_time}"))
def tell_date():
 current_date=datetime.datetime.now()
 clen_date=current_date.strftime("%d:%B:%Y")
 asyncio.run(speak(f"sir the date is {clen_date}"))
def shutdown ():
  os.system("shutdown /s /t 1")
def restart():
  os.system("restart /r /t /1")
  

 
def long_term_memory(command):
    memory_file = "clint_prosnal_memory.json"
    
    if os.path.exists(memory_file):
        try:
            with open(memory_file, "r") as f:
                data = json.load(f)
                # Yeh check karega ki agar file mein history key nahi hai, toh nayi bana le
                if not isinstance(data, dict) or "history" not in data:
                    data = {"history": []}
        except json.JSONDecodeError:
            data = {"history": []}
    else:
        data = {"history": []}

    # Naye sentence ko history list mein append kar do
    data["history"].append(command)

    # Wapas file mein save kar do
    with open(memory_file, "w") as f:
        json.dump(data, f, indent=4)

def valume(level):
  devices= AudioUtilities.GetSpeakers()

  interface=devices.EndpointVolume
  
  interface.SetMasterVolumeLevelScalar(level/100,None)

def send_gemini(frame):
      
    # 1. Frame ko snapshot.jpg mein save karna
       cv2.imwrite("snapshot.jpg", frame)
    
    # 2. Image ko base64 mein read karna
       with open("snapshot.jpg", "rb") as f:
        image_bytes = f.read()
       image_base64 = base64.b64encode(image_bytes).decode("utf-8")
       url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={GEMINI_API_KEY}"
       paylode={
         "contents":[{"role":"user",
                       "parts":[{"text":"Is image mein kya dikh raha hai?",
                              
                                 },
                     { "inline_data":{ "mime_type": "image/jpeg",
                                      "data": image_base64
                                      
                                      },}]
                      }],
        
       }
       response=requests.post(url,json=paylode)
       if response.status_code==200:
         result=response.json()
         gemini_generat_answer= result.get("candidates")
         content=gemini_generat_answer[0].get("content")
         part=content.get("parts")
         answer=part[0].get("text")
         asyncio.run(speak(answer))
       
       else:
         print("Gemini Error:", response.status_code, response.text)

latest_frame = None
def camera_loop():

  cap= cv2.VideoCapture(0)
  if not cap.isOpened():
    print("camara nahi chal rha ha ")
    return
  
  while True:
      
       

        
        
          ret,frame=cap.read()
          if not ret:
              print("camara nahi mila !")
              break
          global latest_frame
          latest_frame = frame.copy()
          cv2.imshow("JARVIS VISION",frame)
          cv2.imwrite("snapshot.jpg", frame)
          
          if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

  cap.release()
  cv2.destroyAllWindows()

def organize_files():
  try:
    downlode_path=r"C:\Users\Official_Javed\Videos\my python chapters\organize_files"
    file_list=os.listdir(downlode_path) #listdir ka kakam  ha ke hum jo bhi path isa da ga ya us patha ma ka file kao ak ak kar ka dooga ga
    #our use ka  name laga our ak python list ma rakha da ga
    print(file_list)
    for i in file_list:
      print(i)#("""ya file_list majitna file ho ga aa gaya ga our print ho gya ga """)
      extension= os.path.splitext(i)[1] #fir hum iska use kar ka file ka index 1 ya na kefile ka akhari word kanikala ga jasa(.py,.jpg,.txt)""")
      sourse=os.path.join(downlode_path,i)
      

      if ".py" in extension: # fir agar file ma .py ha matlag python file ha to 
        print("python file ha: py file ha ")# ya print kar da ga\
        destanition=r"C:\Users\Official_Javed\Videos\my python chapters" # ya wo patha hajaha hama apna file move karvana ha 
        shutil.move(sourse,destanition)    # ya sourse matlab jo hamara terminal ka path ha us ko sahi sa destination pa move karta\ ha

      elif ".jpg" in extension or ".jpeg" in extension :# ya check kar aga ke kay .jpg ha agar ha 
        print("photo file ha : .jpg file ha ")
        destanition=r"C:\Users\Official_Javed\Videos\my python chapters"  

        shutil.move(sourse,destanition)    
      elif ".png" in extension:
        print("screen sort ha:png file ha")
        destanition=r"C:\Users\Official_Javed\Videos\my python chapters" 

        shutil.move(sourse,destanition)   
      elif ".pdf" in extension :
        print("pdf file ha")
        destanition=r"C:\Users\Official_Javed\Videos\my python chapters" 
        shutil.move(sourse,destanition)   
      elif ".txt" in extension:
        print(".txt file ha")
        destanition=r"C:\Users\Official_Javed\Videos\my python chapters" 
        shutil.move(sourse,destanition)   
      elif ".mp3" in extension:
        print(".mp3 file ha isa move kaya ja raha")
        destanition=r"C:\Users\Official_Javed\Videos\my python chapters" 
        shutil.move(sourse,destanition)   
      else:
        print("koy file nah mila")
  except Exception as n:
    print("kuch galti ho gay ha ",n)
  finally:
   asyncio.run(speak("File succes fully move ho gay ha "))

def learn_leptop_battry():
  battry=psutil.sensors_battery() # psutil ya window sa puchata ha battery ka ka kay hal chal ha 
  percentage=battry.percent # percent yaha  pa percentage aata ha  
  if battry.power_plugged: # ya pata karta ha ke leptop charging pa ha ya nahi
    print(f"battery percentage {percentage} hai our leptop charge laga hai") # pahla ya terminal pa print ho ga 
    asyncio.run(speak(f"battery percentage {percentage} hai or leptop charge laga hai"))# fir jarvis ya bola ga 
  else:
    battry_backep=battry.secsleft # ya baata ha ke batttery kab takchala ga 
  
    if battry_backep and battry_backep > 0:
        minutes = battry_backep // 60
        print(f"battery percentage {percentage} hai abhi leptop charge pay nahi hai Mere Khayal Se leptop lagbag {minutes} minute tak chala gaa")# phala ya terminal pa print ho ga
        asyncio.run(speak(f"battery percentage {percentage} hai abhi leptop charge pay nahi hai Mere Khayal Se  leptop lagbag {minutes} minute tak Chalega"))# fir jarvis ya bola ga
    else:
        print(f"battery percentage {percentage} hai or leptop charge pay nahi hai")
        asyncio.run(speak(f"battery percentage {percentage} hai or leptop charge pay nahi hai"))
   

  





def main_command():
 asyncio.run(speak("hi sir may online hu"))
 while True:

  user_command=listen()
  if not user_command:
    continue
  if user_command:
    long_term_memory(user_command)
  
  if("mousam" in user_command or"weather"in user_command):
    replace=["mousam","weather","ka","batayo","ajj","kasa","ha"]
    for i in replace:
       user_command=user_command.replace(i,"")
       
  
    weather(user_command.strip())
  
 
    
  elif "search" in user_command or "patakaro" in user_command:
    search(user_command)
  elif "open" in user_command or "kholo" in user_command:
   replace=["open","khola","crome","pa",]
   for i in replace:
    app_name=user_command.replace(i,"")

    app_opner(app_name.strip())
  elif "time" in user_command or "samay" in user_command:
   tell_time()
  elif "date" in user_command or "din" in user_command:
   tell_date()
   
  elif "volume" in user_command or "awaj" in user_command:
   word=user_command.split()
   level=None
   for i in word:
     number_tex=i.replace("%","")
     if number_tex.isdigit():
       level=int(number_tex)
   if level is None:
    print("koy number nahi mila")
   
   else:
     if( level> 100):
      print("app na glat persantage bola ha ya  100 sa jada ha")
     
   
  
     else:
     
       valume(level)
       asyncio.run(speak(f"volume {level} par set kar dia hay"))

  elif "shutdown" in user_command or " band karo" in user_command:
    shutdown()
  elif any(word in user_command for word in["battery","charge","power"]): # any matlab koy bhi mat is ma sa koy bhi word sentenc ma ho to is ko call kar do 
    learn_leptop_battry()
  elif "restart" in user_command :
    restart()
  elif any(word in user_command for word in["file","organize","orgenise"] ):
    organize_files()
  

  
  elif any(word in user_command for word in [
      "kya hai", "kay hai", "kya dikh raha",
      "dikh raha hai", "what is this", "what do you see"
  ]):
      if latest_frame is not None:
          threading.Thread(
              target=send_gemini,
              args=(latest_frame.copy(),),
              daemon=True
          ).start()
      else:
          asyncio.run(speak("Camera frame abhi available nahi hai."))

  else:
   chat(user_command)
threading.Thread(target=camera_loop, daemon=True).start()
main_command()
  


