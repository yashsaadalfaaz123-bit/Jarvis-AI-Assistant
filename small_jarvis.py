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
import cv2 



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

def openCV():

  cap= cv2.VideoCapture(0)
  if not cap.isOpened():
    print("camara nahi chal rha ha ")
    return
  
  while True:

    
    ret,frame=cap.read()
    if not ret:
      print("camara nahi mila !")
    cv2.imshow("JARVIS VISION",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
  cap.release()
  cv2.destroyAllWindows()
openCV()
  


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
  elif "restart" in user_command :
    restart()

  
  else:
   chat(user_command)

main_command()


  


