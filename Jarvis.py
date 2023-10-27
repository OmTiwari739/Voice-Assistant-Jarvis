import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import wikipedia
import pyautogui
import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Diction

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate', 170)

def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    Assistant.runAndWait()
    
def get_phone_number_info(phone_number):
    # Parse the phone number
    parsed_number = phonenumbers.parse(phone_number)
    parsed_service_pro = phonenumbers.parse(phone_number)

    # Get location information
    location = geocoder.description_for_number(parsed_number, "en")
    Speak("Location: " + location)

    # Get carrier information
    service_provider = carrier.name_for_number(parsed_service_pro, "en")
    Speak("Service Provider: " + service_provider)

    # Set up OpenCageGeocode API key
    opencage_key = '9fa6367701aa4a40a3518a8aebda3fca'
    geocoder_instance = OpenCageGeocode(opencage_key)

    # Query location using the parsed location information
    query = str(location)
    results = geocoder_instance.geocode(query)
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    Speak("Latitude: " + str(lat))
    Speak("Longitude: " + str(lng))

    # Generate a link to open the Google Map
    google_map_link = f"https://www.google.com/maps/place/{lat},{lng}"
    # Speak("Google Map Link: " + google_map_link)

    # Automatically open the Google Map link in a web browser
    webbrowser.open(google_map_link)    
    
def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        command.pause_threshold = 1
        audio = command.listen(source)
        
        try:
            print("Recognizing....")
            query = command.recognize_google(audio, language='en-in')
            print(f"You Said {query}")

        except Exception as Error:
            return "none"
        
        return query.lower()
    
def TaskExe():
    
    def Music():
        Speak("Tell Me The Name Of The Song!")
        musicName = takecommand()
        
        if 'achko machko' in musicName:
            os.startfile("E:\\Old Jarvis\\music\\Achko Machko.mp3")
    
        elif 'breakup party' in musicName:
            os.startfile("E:\\Old Jarvis\\music\\Breakup Party.mp3")

        else:
            pywhatkit.playonyt(musicName)
            
        Speak("Your Song Has Been Started!, Enjoy Sir!")
        
    def Whatsapp():
        Speak("Tell Me The Name Of The Person!")
        name = takecommand()
        
        if 'Om' in name:
            Speak("Tell Me The Message! ")
            msg = takecommand()
            Speak("Tell Me The Time Sir!")
            Speak("Time in Hour!")
            hour = int(takecommand())
            Speak("Time in Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+91 Enter Number Here",msg,hour,min,20)
            Speak("Ok Sir, Sending Whatsapp Message! ")
            
        elif 'Tiwari' in name:
            Speak("Tell Me The Message! ")
            msg = takecommand()
            Speak("Tell Me The Time Sir!")
            Speak("Time in Hour!")
            hour = int(takecommand())
            Speak("Time in Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+91 Enter Number Here",msg,hour,min,20)
            Speak("Ok Sir, Sending Whatsapp Message! ")
            
        else:
            Speak("Tell Me The Phone Number!")
            phone = int(takecommand())
            ph = '+91' + phone
            Speak("Tell Me The Message! ")
            msg = takecommand()
            Speak("Tell Me The Time Sir!")
            Speak("Time in Hour!")
            hour = int(takecommand())
            Speak("Time in Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
            Speak("Ok Sir, Sending Whatsapp Message! ")

    def screenshot():
        Speak("Ok Sir!, What Should I Name That File?")
        path = takecommand()
        path1name = path + ".png"
        path1 = "E:\\Old Jarvis\\ss\\" + path1name
        ss = pyautogui.screenshot()
        ss.save(path1)
        os.startfile("E:\\Old Jarvis\\ss")
        Speak("Here Is Your Screenshot Sir!")

    def OpenApps():
        Speak("Ok Sir, Wait A Second!")
        
        if 'vs code' in query:
            os.startfile("C:\\Users\\Deepak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'phtoshop' in query:
            os.startfile("C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe")  

        elif 'chrome' in query:
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")   

        elif 'facebook' in query:
            webbrowser.open("https://en-gb.facebook.com/")

        elif 'instagram' in query:
            webbrowser.open("https://instagram.com/")

        elif 'maps' in query:
            webbrowser.open("https://www.google.com/maps")

        Speak("Your Command Has Been Completed Sir!")

    def CloseAPPS():
        Speak("Ok Sir , Wait A second!")
        
        if 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        elif 'facebook' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        elif 'vs code' in query:
            os.system("TASKKILL /F /im code.exe")
            
        elif 'photoshop' in query:
            os.system("TASKKILL /F /im Photoshop.exe")
            
        elif 'maps' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        Speak("Your Command Has Been Succesfully Completed!")

    def YoutubeAuto():
        Speak("Whats Your Command ?")
        comm = takecommand()
        
        if 'pause' in comm:
            keyboard.press('k')
            
        elif 'restart' in comm:
            keyboard.press('0')
            
        elif 'mute' in comm:
            keyboard.press('m')
            
        elif 'forward' in comm:
            keyboard.press('l')
            
        elif 'back' in comm:
            keyboard.press('j')
            
        elif 'full screen' in comm:
            keyboard.press('f')
            
        elif 'theatre view' in comm:
            keyboard.press('t')
            
        elif 'exit theatre view' in comm:
            keyboard.press('t')
            
        elif 'mini player view' in comm:
            keyboard.press('i')
            
        elif 'exit mini player view' in comm:
            keyboard.press('i')
            
        Speak("Done Sir!")

    def ChromeAuto():
        Speak("Chrome Automation started!")
        
        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')
            
        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')
            
        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')
            
        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')
            
        elif 'jump to the next tab' in command:
            keyboard.press_and_release('ctrl + tab')
            
        elif 'close the current tab' in command:
            keyboard.press_and_release('ctri + w')
            
        elif 'minimize' in command:
            keyboard.press_and_release('alt + space + n')
            
        elif 'download' in command:
            keyboard.press_and_release('ctrl + j')

    def Dict():
        Speak("Activated Dictionary!")
        Speak("Tell Me The Problem!")
        probl = takecommand ()

        if 'meaning' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("jarvis", "")
            probl = probl.replace("meaning of", "")
            result = Diction.meaning(probl)
            Speak(f"The Meaning Of {probl} is {result}")

        elif 'synonym' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("jarvis", "")
            probl = probl.replace("synonym of", "")
            result = Diction.synonym(probl)
            Speak(f"The Synonym Of {probl} is {result}")
            
        elif 'antonym' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("jarvis", "")
            probl = probl.replace("antonym of", "")
            result = Diction.antonym(probl)
            Speak(f"The Antonym Of {probl} is {result}")
            
        Speak("Exited Dictionary!")

    while True:
        
        query = takecommand()
        
        if 'hello' in query:
            Speak("Hello Sir, I Am Jarvis.")
            Speak("Your Personal AI Assistant!")
            Speak("How May I Help You?")
            
        elif 'wake up' in query:
            Speak("Hello Sir, How May I Help You?")
            
        elif 'how are you' in query:
            Speak("I Am Absolutely Fine")
            Speak("Whats About You Sir?")
            
        elif 'you need a break' in query:
            Speak("Ok Sir, You Can Call Me Anytime")
            break
        
        elif 'bye' in query:
            Speak("Ok Sir, Bye!")
            break
        
        elif 'shut up' in query:
            Speak("")
            break
            
        elif 'youtube search' in query:
            Speak("Ok Sir, This is What i Found")
            query = query.replace("jarvis", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak('Done Sir!')
            
        elif 'google search' in query:
            Speak("This is What i Found")
            query = query.replace("jarvis", "")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            Speak("Done Sir!")        
        
        elif 'open website' in query:
            Speak("Ok Sir, Launching....")
            query = query.replace("jarvis", "")
            query = query.replace("website", "")
            query = query.replace(" ", "")
            web1 = query.replace("open", "") 
            web2 = 'https://www.' + web1 + '.com'  
            webbrowser.open(web2)
            Speak("Launched!")

        elif 'launch' in query:
            Speak("Tell Me The Name Of The Website!")
            name = takecommand().lower()  # Get user input
            web = 'https://www.' + name + '.com'  # Corrected the variable name
            webbrowser.open(web)
            Speak("Done Sir!")
            
        elif 'music' in query:
            Music()
            
        elif 'wikipedia' in query:
            Speak("Searching Wikipedia")
            query = query.replace("jarvis", "")
            query = query.replace("wikipedia", "")
            query = query.strip()  # Remove leading/trailing spaces
            wiki = wikipedia.summary(query, sentences=2)
            Speak(f"According To Wikipedia: {wiki}")
            
        elif 'whatsapp message' in query:
            Whatsapp()
            
        elif 'screenshot' in query:
            screenshot()
            
        elif 'open vs code' in query:
            OpenApps()
                        
        elif 'open phtoshop' in query:
            OpenApps()
            
        elif 'open chrome' in query:
            OpenApps()
            
        elif 'open facebook' in query:
            OpenApps()
            
        elif 'open instagram' in query:
            OpenApps()
            
        elif 'open maps' in query:
            OpenApps()
            
        elif 'close chrome' in query:
            CloseAPPS()

        elif 'close instagram' in query:
            CloseAPPS()
            
        elif 'close facebook' in query:
            CloseAPPS()
            
        elif 'phone number info' in query:
            Speak("Sure, please provide the phone number.")
            user_phone_number = input("Enter a phone number (with country code): ")
            get_phone_number_info(user_phone_number)
            
        elif 'pause' in query:
            keyboard.press('k')
            
        elif 'restart' in query:
            keyboard.press('0')
            
        elif 'mute' in query:
            keyboard.press('m')
            
        elif 'forward' in query:
            keyboard.press('l')
            
        elif 'back' in query:
            keyboard.press('j')
            
        elif 'full screen' in query:
            keyboard.press('f')
            
        elif 'theatre view' in query:
            keyboard.press('t')
            
        elif 'exit theatre view' in query:
            keyboard.press('t')
            
        elif 'mini player view' in query:
            keyboard.press('i')
            
        elif 'exit mini player view' in query:
            keyboard.press('i')
            
        elif 'youtube tools' in query:
            YoutubeAuto()
            
        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')
            
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')
            
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')
            
        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
            
        elif 'jump to the next tab' in query:
            keyboard.press_and_release('ctrl + tab')
            
        elif 'close the current tab' in query:
            keyboard.press_and_release('ctri + w')
            
        elif 'minimize' in query:
            keyboard.press_and_release('alt + space + n')
            
        elif 'download' in query:
            keyboard.press_and_release('ctrl + j')
            
        elif 'chrome automation' in query:
            ChromeAuto()
            
        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)
            
        elif 'repeat my words' in query:
            Speak("Speak Sir!")
            jj = takecommand()
            Speak(f"You Said : {jj}")
         
        elif 'my location' in query:
            Speak("Ok Sir, Wait A Second!")
            webbrowser.open("https://www.google.com/maps/place/Sonam+Pushpanjali+Co-op+Hsg+Society/@19.2945074,72.8620256,66m/data=!3m1!1e3!4m15!1m8!3m7!1s0x3be7b024b4bdad7d:0xe6ca8af64f31eb81!2sMira+Bhayandar,+Maharashtra+401105!3b1!8m2!3d19.3053477!4d72.8663173!16s%2Fg%2F1hhlsgv80!3m5!1s0x3be7b03712d54817:0x42ba84c17bc9b5d6!8m2!3d19.2943128!4d72.861884!16s%2Fg%2F11ckvkys6h?entry=ttu")
            
        elif 'dictionary' in query:
            Dict()
        
TaskExe()
