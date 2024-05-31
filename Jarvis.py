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
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_MainWindow
from PyQt5.QtCore import QThread
import sys
from sys import exit


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices', voices[0].id)
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


class MainThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        self.TaskExecution()

    def takecommand(self):
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing....")
                self.query = command.recognize_google(audio, language='en-in')
                print(f"You Said {self.query}")

            except Exception as Error:
                return "none"

            return self.query.lower()

    def TaskExecution(self):

        def Music():
            Speak("Tell Me The Name Of The Song!")
            musicName = self.takecommand()

            if 'achko machko' in musicName:
                os.startfile("E:\\Old Jarvis\\music\\Achko Machko.mp3")

            elif 'breakup party' in musicName:
                os.startfile("E:\\Old Jarvis\\music\\Breakup Party.mp3")

            else:
                pywhatkit.playonyt(musicName)

            Speak("Your Song Has Been Started!, Enjoy Sir!")

        def Whatsapp():
            Speak("Tell Me The Name Of The Person!")
            name = self.takecommand()

            if 'mummy' in name:
                Speak("Tell Me The Message! ")
                msg = self.takecommand()
                Speak("Tell Me The Time Sir!")
                Speak("Time in Hour!")
                hour = int(self.takecommand())
                Speak("Time in Minutes!")
                min = int(self.takecommand())
                pywhatkit.sendwhatmsg(+917666319766, msg, hour, min, 20)
                Speak("Ok Sir, Sending Whatsapp Message! ")

            elif 'Tiwari' in name:
                Speak("Tell Me The Message! ")
                msg = self.takecommand()
                Speak("Tell Me The Time Sir!")
                Speak("Time in Hour!")
                hour = int(self.takecommand())
                Speak("Time in Minutes!")
                min = int(self.takecommand())
                pywhatkit.sendwhatmsg("+91 8080280421", msg, hour, min, 20)
                Speak("Ok Sir, Sending Whatsapp Message! ")

            else:
                Speak("Tell Me The Phone Number!")
                phone = int(self.takecommand())
                ph = '+91' + phone
                Speak("Tell Me The Message! ")
                msg = self.takecommand()
                Speak("Tell Me The Time Sir!")
                Speak("Time in Hour!")
                hour = int(self.takecommand())
                Speak("Time in Minutes!")
                min = int(self.takecommand())
                pywhatkit.sendwhatmsg(ph, msg, hour, min, 20)
                Speak("Ok Sir, Sending Whatsapp Message! ")

        def screenshot():
            Speak("Ok Sir!, What Should I Name That File?")
            path = self.takecommand()
            path1name = path + ".png"
            path1 = "E:\\Old Jarvis\\ss\\" + path1name
            ss = pyautogui.screenshot()
            ss.save(path1)
            os.startfile("E:\\Old Jarvis\\ss")
            Speak("Here Is Your Screenshot Sir!")

        def OpenApps():
            Speak("Ok Sir, Wait A Second!")

            if 'vs code' in self.query:
                os.startfile("C:\\Users\\Deepak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

            elif 'photoshop' in self.query:
                os.startfile("C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe")

            elif 'chrome' in self.query:
                os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            elif 'facebook' in self.query:
                webbrowser.open("https://en-gb.facebook.com/")

            elif 'instagram' in self.query:
                webbrowser.open("https://instagram.com/")

            elif 'maps' in self.query:
                webbrowser.open("https://www.google.com/maps")

            Speak("Your Command Has Been Completed Sir!")

        def CloseAPPS():
            Speak("Ok Sir , Wait A second!")

            if 'chrome' in self.query:
                os.system("TASKKILL /F /im chrome.exe")

            elif 'instagram' in self.query:
                os.system("TASKKILL /F /im chrome.exe")

            elif 'facebook' in self.query:
                os.system("TASKKILL /F /im chrome.exe")

            elif 'vs code' in self.query:
                os.system("TASKKILL /F /im code.exe")

            elif 'photoshop' in self.query:
                os.system("TASKKILL /F /im Photoshop.exe")

            elif 'maps' in self.query:
                os.system("TASKKILL /F /im chrome.exe")

            Speak("Your Command Has Been Succesfully Completed!")

        def YoutubeAuto():
            Speak("Whats Your Command ?")
            comm = self.takecommand()

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

            command = self.takecommand()

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
            probl = self.takecommand()

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

            self.query = self.takecommand()

            if 'hello' in self.query:
                Speak("Hello Sir, I Am Jarvis.")
                Speak("Your Personal AI Assistant!")
                Speak("How May I Help You?")

            elif 'wake up' in self.query:
                Speak("Hello Sir, How May I Help You?")

            elif 'how are you' in self.query:
                Speak("I Am Absolutely Fine")
                Speak("Whats About You Sir?")

            elif 'you need a break' in self.query:
                Speak("Ok Sir, You Can Call Me Anytime")
                break

            elif 'bye' in self.query:
                Speak("Ok Sir, Bye!")
                break

            elif 'shut up' in self.query:
                Speak("")
                break

            elif 'youtube search' in self.query:
                Speak("Ok Sir, This is What i Found")
                self.query = self.query.replace("jarvis", "")
                self.query = self.query.replace("youtube search", "")
                web = 'https://www.youtube.com/results?search_query=' + self.query
                webbrowser.open(web)
                Speak('Done Sir!')

            elif 'google search' in self.query:
                Speak("This is What i Found")
                self.query = self.query.replace("jarvis", "")
                self.query = self.query.replace("google search", "")
                pywhatkit.search(self.query)
                Speak("Done Sir!")

            elif 'open website' in self.query:
                Speak("Ok Sir, Launching....")
                self.query = self.query.replace("jarvis", "")
                self.query = self.query.replace("website", "")
                self.query = self.query.replace(" ", "")
                web1 = self.query.replace("open", "")
                web2 = 'https://www.' + web1 + '.com'
                webbrowser.open(web2)
                Speak("Launched!")

            elif 'launch' in self.query:
                Speak("Tell Me The Name Of The Website!")
                name = self.takecommand().lower()  # Get user input
                web = 'https://www.' + name + '.com'  # Corrected the variable name
                webbrowser.open(web)
                Speak("Done Sir!")

            elif 'music' in self.query:
                Music()

            elif 'wikipedia' in self.query:
                Speak("Searching Wikipedia")
                self.query = self.query.replace("jarvis", "")
                self.query = self.query.replace("wikipedia", "")
                self.query = self.query.strip()  # Remove leading/trailing spaces
                wiki = wikipedia.summary(self.query, sentences=2)
                Speak(f"According To Wikipedia: {wiki}")

            elif 'whatsapp message' in self.query:
                Whatsapp()

            elif 'screenshot' in self.query:
                screenshot()

            elif 'open vs code' in self.query:
                OpenApps()

            elif 'open phtoshop' in self.query:
                OpenApps()

            elif 'open chrome' in self.query:
                OpenApps()

            elif 'open facebook' in self.query:
                OpenApps()

            elif 'open instagram' in self.query:
                OpenApps()

            elif 'open maps' in self.query:
                OpenApps()

            elif 'close chrome' in self.query:
                CloseAPPS()

            elif 'close instagram' in self.query:
                CloseAPPS()

            elif 'close facebook' in self.query:
                CloseAPPS()

            elif 'phone number info' in self.query:
                Speak("Sure, please provide the phone number.")
                user_phone_number = input("Enter a phone number (with country code): ")
                get_phone_number_info(user_phone_number)

            elif 'pause' in self.query:
                keyboard.press('k')
                
            elif 'play' in self.query:
                keyboard.press('k')

            elif 'restart' in self.query:
                keyboard.press('0')

            elif 'mute' in self.query:
                keyboard.press('m')

            elif 'forward' in self.query:
                keyboard.press('l')

            elif 'back' in self.query:
                keyboard.press('j')

            elif 'full screen' in self.query:
                keyboard.press('f')

            elif 'theatre view' in self.query:
                keyboard.press('t')

            elif 'exit theatre view' in self.query:
                keyboard.press('t')

            elif 'mini player view' in self.query:
                keyboard.press('i')

            elif 'exit mini player view' in self.query:
                keyboard.press('i')

            elif 'youtube tools' in self.query:
                YoutubeAuto()

            elif 'close this tab' in self.query:
                keyboard.press_and_release('ctrl + w')

            elif 'open new tab' in self.query:
                keyboard.press_and_release('ctrl + t')

            elif 'open new window' in self.query:
                keyboard.press_and_release('ctrl + n')

            elif 'history' in self.query:
                keyboard.press_and_release('ctrl + h')

            elif 'jump to the next tab' in self.query:
                keyboard.press_and_release('ctrl + tab')

            elif 'close the current tab' in self.query:
                keyboard.press_and_release('ctri + w')

            elif 'minimize' in self.query:
                keyboard.press_and_release('alt + space + n')

            elif 'download' in self.query:
                keyboard.press_and_release('ctrl + j')

            elif 'chrome automation' in self.query:
                ChromeAuto()

            elif 'joke' in self.query:
                get = pyjokes.get_joke()
                Speak(get)

            elif 'repeat my words' in self.query:
                Speak("Speak Sir!")
                jj = self.takecommand()
                Speak(f"You Said : {jj}")

            elif 'my location' in self.query:
                Speak("Ok Sir, Wait A Second!")
                webbrowser.open("https://www.google.com/maps/place/Sonam+Pushpanjali+Co-op+Hsg+Society/@19.2945074,72.8620256,66m/data=!3m1!1e3!4m15!1m8!3m7!1s0x3be7b024b4bdad7d:0xe6ca8af64f31eb81!2sMira+Bhayandar,+Maharashtra+401105!3b1!8m2!3d19.3053477!4d72.8663173!16s%2Fg%2F1hhlsgv80!3m5!1s0x3be7b03712d54817:0x42ba84c17bc9b5d6!8m2!3d19.2943128!4d72.861884!16s%2Fg%2F11ckvkys6h?entry=ttu")

            elif 'dictionary' in self.query:
                Dict()   

    # TaskExe()

        
startExecution = MainThread()
        
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
            
    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../Downloads/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Downloads/Jarvis_Loading_Screen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
        
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
        
    
        
app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

