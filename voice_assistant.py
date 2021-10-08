#link : https://pypi.org/project/pyttsx3/ (pyttxs3)
# link2 : https://pypi.org/project/SpeechRecognition/ (speech recognition)
# 3 things to install in cmd !!!
import pyttsx3
import datetime
import speech_recognition as sr 
engine = pyttsx3.init('sapi5')          #first set up engine
# get you the details of current voice
voices = engine.getProperty('voices')     #print type of voive avialable
for everyVoice in voices:
    print(everyVoice)                  #run cmd in the file of ai.py

# 0 -- Male  1 -- Female
engine.setProperty('voice',voices[1].id)    #choose female voice

# wish greet me function
def wishme():
    hour = int(datetime.datetime.now().hour)     #just wan get hours
    if hour>=0 and hour<12:
        speak('Good morning')                   #depend on the live time
    elif hour >=12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')

def speak(audio):
    engine.say(audio)             #we type text and it will speak for us
    #without this command the speech is not audible to us
    engine.runAndWait()

# function to take commands

def takeCommand():       #check microphone is working fine or not
    # It takes microphone input from user and return
    # string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)#only when got error stuck with multi microphone
        print('Listening...')      
        r.pause_threshold = 1      #wait for 1 sec
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # using google for voice recognition
        query = r.recognize_google(audio,language='en-in')
        # User query will be printed
        print(f"User Said : {query}\n")
    except Exception as e:
        # print(e) use this only if you want to print the error
        print("Say That Again PLease....")
        return "None"

    return query
        

# cls in cmd is clear the code before all
wishme()
speak('Hello Hou Kuang, I am Hinata , your artificial intelligence assistance  PLease tell me How may I help you')
takeCommand()
