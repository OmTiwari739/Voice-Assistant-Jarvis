import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import wikipedia
import pyautogui

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate', 170)

def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    Assistant.runAndWait()
    
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
            os.startfile("E:\\Jarvis\\music\\Achko Machko.mp3")
    
        elif 'breakup party' in musicName:
            os.startfile("E:\\Jarvis\\music\\Breakup Party.mp3")

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
        path1 = "E:\\Jarvis\\ss\\" + path1name
        ss = pyautogui.screenshot()
        ss.save(path1)
        os.startfile("E:\\Jarvis\\ss")
        Speak("Here Is Your Screenshot Sir!")

    def OpenApps():
        Speak("Ok Sir, Wait A Second!")
        
        if 'vs code' in query:
            os.startfile("C:\\Users\\Deepak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            
        elif 'u torrent' in query:
            os.startfile("C:\\Users\\Deepak\\AppData\\Roaming\\uTorrent\\uTorrent.exe")   

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
            
        elif 'website' in query:
            Speak("Ok Sir, Launching....")
            query = query.replace("jarvis", "")
            query = query.replace("website", "")
            web1 = query.replace("open", "")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!")
            
        elif 'launch' in query:
            Speak("Tell Me The Name Of The Website!")
            name = takecommand()
            web = 'https://www.' + web1 + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")
            
        elif 'music' in query:
            Music()
            
        elif 'wikipedia' in query:
            Speak("Searching Wikipedia")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak("According To Wikipeida : {wiki}")
            
        elif 'whatsapp message' in query:
            Whatsapp()
            
        elif 'screenshot' in query:
            screenshot()
            
        elif 'open vs code' in query:
            OpenApps()
            
        elif 'open u torrent' in query:
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
            
takecommand()
TaskExe()
