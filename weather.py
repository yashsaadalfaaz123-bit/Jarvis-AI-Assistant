import requests
n=input("inter your states: ")
w=requests.get(f"https://wttr.in/{n}")
print(w.text)
