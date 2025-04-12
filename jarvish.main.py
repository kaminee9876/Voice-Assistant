import datetime
import pyttsx3
import speech_recognition
import requests
from  bs4 import BeautifulSoup
import os
import pyautogui

for i in range(3):
     a = input("Enter Password to open jarvis :- ")
     pw_file = open("password.txt","r")
     pw = pw_file.read().strip()
     pw_file.close()
     if (a==pw):
          print("WELCOME MAM ! PLZ SPEAK [GET UP] TO LOAD ME UP")
          break
     elif (i==2 and a!=pw):
          exit()
                     
     elif (a!=pw):
          print("Try Again")

     
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand(): 
     r= speech_recognition.Recognizer()
     with speech_recognition. Microphone() as source:
          print("Listening.....")
          r.pause_threshold = 1
          r.energy_threshold = 300
          audio = r.listen(source,0,4)

          try:
               print("Understanding..")
               query = r.recognize_google(audio,language='en-in')
               print(f"you said: {query}\n")
          except Exception as e:
               print("say that again")
               return "None"
          return query
     
def alarm(query):
     timehere = open("Alarmtext.txt","a")
     timehere.write(query)
     timehere.close()
     os.startfile("alarm.py")   
     
if __name__ == "__main__":
     while True:
          query = takeCommand().lower()
          if "get up" in query:
               from GreetMe import greetMe
               greetMe()    

               while True:
                    query = takeCommand().lower()
                    if "go to sleep" in query:
                         speak("ok mam , you can call  me anytime")
                         break

                    elif "change password" in query:
                         speak("What's the new password\n")
                         new_pw = input("Enter the new password\n")
                         new_password = open("password.txt","w")
                         new_password.write(new_pw)
                         new_password.close()
                         speak("Done mam")
                         speak(f"Your new password is {new_pw}")


                    elif "translate" in query:
                         from Translator import translategl
                         query = query.replace("jarvis","")
                         query = query.replace("translate","") 
                         translategl(query)


                    elif "open"in query:
                         query = query.replace("open","")
                         query = query.replace("jarvis","")
                         pyautogui.press("super")
                         pyautogui.typewrite(query)
                         pyautogui.sleep(2)
                         pyautogui.press("enter")
                         



                          
                    elif "hello" in query:
                         speak("Hello mam, how are you ?")
                    elif "i am fine" in query:
                         speak("that's great, mam")
                    elif "how are you" in query:
                         speak("Perfect, mam")
                    elif "thank you" in query:
                         speak("you are welcome, mam") 

                    elif "pause" in query:
                         pyautogui.press("k")
                         speak("video paused")
                    elif "play" in query:
                         pyautogui.press("k") 
                         speak("video played")
                    elif "mute" in query:
                         pyautogui.press("m")  
                         speak("video muted")   

                    elif "volume up" in query:
                         from keyboard import volumeup
                         speak("Turning volume up,mam") 
                         volumeup()
                    elif "volume down" in query:
                         from keyboard import volumedown
                         speak("Turning volume down,mam")
                         volumedown()
                          

                         
                    elif "open" in query:
                         from Dictapp import openappweb
                         openappweb(query)
                    elif "close" in query:
                         from Dictapp import closeappweb
                         closeappweb(query)    
                                     
                     
                    elif "google" in query:
                         from SearchNow import searchGoogle
                         searchGoogle(query)
                    elif "youtube" in query:
                         from SearchNow import searchYoutube
                         searchYoutube(query)
                    elif "wikipedia" in query:
                         from SearchNow import searchWikipedia
                         searchWikipedia(query)
 
                    elif "news" in query:
                         from NewsRead import latestnews
                         latestnews()

                    elif "calculate" in query:
                         from Calculatenumbers import WolfRamAlpha
                         from Calculatenumbers import Calc
                         query = query.replace("calculate","")
                         query = query.replace("jarvis","")
                         Calc(query)

                    elif "whatsapp" in query:
                         from Whatsapp import sendMessage
                         sendMessage()


                    elif "temperature" in query:
                         search = "temperature in bhopal"
                         url = f"https://www.google.com/search?q={search}"
                         r = requests.get(url)
                         data = BeautifulSoup(r.text,"html.parser")
                         temp = data.find("div", class_ = "BNeawe").text 
                         speak(f"current{search} is {temp}")     

                    elif "weather" in query:
                         search = "temperature in bhopal"
                         url = f"https://www.google.com/search?q={search}"
                         r = requests.get(url)
                         data = BeautifulSoup(r.text,"html.parser")

                         temp = data.find("div", class_ = "BNeawe").text 
                         speak(f"current{search} is {temp}")  

                    elif "set an alarm" in query:
                         print("input time example:- 10 and 10 and 10") 
                         speak("set the time")
                         a = input("please tell the time :- ")
                         alarm(a) 
                         speak("Done,mam") 
                         

                    elif "the time" in query :
                         strTime = datetime.datetime.now().strftime("%H:%M") 
                         speak(f"mam, the time is {strTime}") 

                    elif "finally sleep" in query:
                         speak("Going to sleep,mam")    
                         exit()

                    elif "remember that" in query:
                         rememberMessage = query.replace("remember that","")
                         rememberMessage = query.replace("jarvis","")
                         speak("You told  me "+rememberMessage)
                         remember = open("Remember.txt","w")
                         remember.write(rememberMessage)
                         remember.close()
                    elif "what do you remember" in query:
                         remember = open("Remember.txt","r")
                         speak("You told me " + remember.read())

                    elif "shutdown system" in query:
                         speak("Are You sure you want to shutdown")
                         shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                         if shutdown == "yes":
                              os.system("shutdown /s /t 1")

                         elif shutdown == "no":
                              break

                    

