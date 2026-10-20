import edge_tts
import pygame
import requests
import duckduckgo_search
import webbrowser
import asyncio

async def speak(text):

 cominatek=edge_tts.Communicate(text,"hi-IN-MadhurNeural")
 await cominatek.save("voice.mp3")
 pygame.init()
 pygame.mixer_music.load("voice.mp3")

 pygame.mixer_music.play()

 while pygame.mixer_music.get_busy():
  pygame.time.Clock().tick(10)
 pygame.mixer_music.unload()
  


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
def main_command():
 while True:
  user_command=input("app aj kay karna chata ha : ")
 
   

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
    

  
  else:
   chat(user_command)

main_command()


  


