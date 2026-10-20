import requests
import duckduckgo_search
def weather():
    
        user=input("app kaha ka weather dakhana chata ha: ")
        w=requests.get(f"https://wttr.in/{user}")
        print(w.text)


def search():
    user=input("what are you search today: ")
    url=requests.get(f"https://api.duckduckgo.com/?q={user}&format=json")
    data=url.json()
    for i in data["RelatedTopics"]:
        if "Text" in i:
            print(i["Text"])

def start ():
    user=input("inter what are you doing: ")
    if "weather" in user or "mousam" in user:
        
        weather()
        
    if "search" in user or "dhundhna" in user:
           search()
start()