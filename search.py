import duckduckgo_search
import requests
while True:

    user=input("kay search karna ha: ")
    url = requests.get(f"https://api.duckduckgo.com/?q={user}&format=json")
    data=url.json()


            
    for i in data["RelatedTopics"]:
        if "Text" in i:
            print(i["Text"])
        