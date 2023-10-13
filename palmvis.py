import pyttsx3
import webbrowser
import requests
import gdata.calendar.data
import gdata.calendar.client
import gdata.auth
import speech_recognition as sr
import datetime
import os

api_key = 'https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=15&lon=100&appid={API key}'
location = 'Bangkok,TH'
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
website_url = 'https://www.google.com'
def create_calendar_event(title, location, start_time, end_time):
    client = gdata.calendar.client.CalendarClient(source='your-app-name')
    client.ClientLogin('your-email@gmail.com', 'your-password', client.source)
    event = gdata.calendar.data.CalendarEventEntry()
    event.title = atom.data.Title(text=title)
    event.where.append(gdata.data.Where(value_string=location))
    event.when.append(gdata.data.When(start=start_time, end=end_time))
    client.InsertEvent(event, '/calendar/feeds/default/private/full')
def calculate_math(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Sorry, I couldn't calculate that. Error: {str(e)}"
def get_weather():
    try:
               
        url =f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'
        response = requests.get(url)
        data = response.json()
        temperature = data['current']['temp_c']
        condition = data['current']['condition']['text']
        weather_message = f"The current temperature in {location} is {temperature} degrees Celsius, and the condition is {condition}."
        speak(weather_message)
    
    except Exception as e:
        speak("I encountered an error while fetching the weather.")
def play_music():
    try:
        webbrowser.open(website_url)
        speak("Playing music for you.")
    except Exception as e:
        speak("I encountered an error while playing music.")
def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 

def commands():
    

    r=sr.Recognizer()
      
    with sr.Microphone() as source: 
        print("Listening...")
        r.pause_threshold = 1 
        r.adjust_for_ambient_noise(source, duration=1) 
        audio = r.listen(source) 

    try: # ถ้ารับเสียงได้
        print("Recognizing...")
        # อินสแตนซ์ของ Recognizer โดยใช้ Google Speech Recognition AP
        query = r.recognize_google(audio, language='en-EN') # ภาษาไทย 

        print(f"User said: {query}\n") 

    except Exception as e: 
        print(e) # แสดงข้อความ error 
        print("Say that again please...") 
        return "None" 
    return query

def wishings():
    # รับชั่วโมงปัจจุบัน
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  

    speak("I am Palmvis Sir. Please tell me how may I help you")

if __name__ == "__main__":

    while True:
        wishings()# ให้เรียกใช้ฟังก์ชั่น wishings
        query = commands().lower()# รับคำสั่งจากฟังก์ชั่น commands และเปลี่ยนเป็นตัวพิมพ์เล็กทั้งหมด
        if 'time' in query:  
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}") 

        elif 'open browser' in query:
            speak("Opening Browser")
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
        elif 'play music' in query:
            
            speak("Playing music for you...")
            play_music()

        elif 'what is the weather today' in query:
    
            speak("The weather today is...")
            get_weather()
        elif "calculate" in query:
            query = query.replace("calculate", "").strip()
            result = calculate_math(query)
            speak(f"The result of {query} is {result}")
        elif "create event" in query:
            speak("What's the title of the event?")
            event_title = commands()
            
            speak("Where is the event located?")
            event_location = commands()
            
            speak("What's the start time and date for the event?")
            event_start_time = commands()
            
            speak("What's the end time and date for the event?")
            event_end_time = commands()
            create_calendar_event(event_title, event_location, event_start_time, event_end_time)
            speak("Event created successfully!")
            


