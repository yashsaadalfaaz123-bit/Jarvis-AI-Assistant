import requests
import webbrowser
import duckduckgo_search
def weather(city_input):
    faltu_words = ["weather", "mousam", "ka", "aaj", "app", "deakhana", "ko", "mein"]
    
    city = city_input.lower()
    for word in faltu_words:
        city = city.replace(word, "")
    
    city = city.strip()
    
    # Step 1: Geocoding API se Lat/Lon nikalna
    geo_url = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}")
    data = geo_url.json()
    
    if "results" in data and len(data["results"]) > 0:
        lat = data["results"][0]["latitude"]
        lon = data["results"][0]["longitude"]
        city_name = data["results"][0]["name"]
        
        # Step 2: Open-Meteo Forecast API (current_weather=true ke sath)
        weather_url = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")
        w_data = weather_url.json()
        
        if "current_weather" in w_data:
            temp = w_data["current_weather"]["temperature"]
            wind = w_data["current_weather"]["windspeed"]
            print(f"Mausam Report: {city_name} mein abhi {temp}°C temperature hai (Windspeed: {wind} km/h)!")
        else:
            print("Mausam ka data nahi mil paya.")
    else:
        print("Sahi city ka naam nahi mila, bhai!")


def opner(app):
      
      
      webbrowser.open(f"https://www.google.com/search? q={app}")
def chat(prompt):
     
     url= "http://localhost:11434/api/generate"


     payload={
          "model":"llama3:latest",
          "prompt": prompt,
          "stream":False,
     }
   

     response=requests.post(url, json=payload)

     if response.status_code==200:
          result=response.json()
          print("AI:",result.get("response"))

     else:
          print("kucha gaktiho gaya ha",response.status_code)


def search(query):
     
     url=requests.get(f"https://api.duckduckgo.com/?q={query}&format=json")
     data =url.json()


            
     for i in data["RelatedTopics"]:
        if "Text" in i:
             print(i["Text"])
def main():
    while True:
     user_input=input("Enter aaj app kay karna chatay ho: ").lower()

     if "weather" in user_input or "mousam" in user_input:
            print("mousam  ka haal bata raha hu ")

            weather(city_input=user_input)

     elif "open" in user_input or "kholo" in user_input:
      print ("app kay kholna chatah ha")
      opner(app=user_input)
     elif "search" in user_input or "patakaro" in user_input:
          print("search kar rha hu: ")
          search(query=user_input)


     elif "close" in user_input or "band" in user_input:
            break
     else:
            print("AI se baat kar rahe hain...")
            chat(prompt=user_input)
      
        
main()