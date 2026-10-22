import edge_tts
import pygame
import requests
import duckduckgo_search
import webbrowser
import asyncio
import datetime
import speech_recognition as sr
import json



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

  
def long_term_memory():
 with open("clint_prosnal_memory.json") as f:
  r=json.load(f)

  r["key_name"]="Value"


  with open("clint_prosnal_memory.json","w") as f:
   json.dump(r,f,indent=4)
   

def get_name():
    try:
        
        with open("clint_prosnal_memory.json", "r") as f:
            data = json.load(f)
            data["key_name"]="Value"
            return data.get("name", "dost") # Agar naam na mile toh 'dost' bol dega
    except FileNotFoundError:
        return "dost"


def chat(prompt):
 
 url="http://localhost:11434/api/generate"


 payload={
     "model":"llama3:latest",
     "prompt":prompt,
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
 
def main_command():
 asyncio.run(speak("hi sir may online hu"))
 while True:
  user_command=listen()

 
   

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
  elif "save" in user_command or "yadkaro" in user_command or "sev" in user_command :
   long_term_memory()
   asyncio.run(speak("yes sar ma na save kar leya ha "))
  elif "mera naam kya hai" in user_command or "what is my name" in user_command:
            saved_name = get_name()
            asyncio.run(speak(f"Aapka naam {saved_name} hai"))
    

  
  else:
   chat(user_command)

main_command()


  


