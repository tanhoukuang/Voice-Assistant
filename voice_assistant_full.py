import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os.path # required to fetch the contents from the specified folder/directory

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) # 0 --> male voice  1 --> Female voice

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    # it takes microphone input from the user and returns the string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Listening....')
        r.pause_threshold = 1
        user_audio = r.listen(source)
    try:
        print('Recognizing User Input...')
        # using google for voice recognition
        query = r.recognize_google(user_audio,language='en-in')
        print(f"User Said : {query}\n")
    except Exception as e:
        #print(e) # use only if you want to print error
        print('Say that again please...')
        return "None"
    return query
    
if __name__ == '__main__':
    wishMe()
    speak('Hello Kuang , I am Hinata your personal voice assistant, please tell me how i can help you')
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query: 
            speak('Searching Wikipedia')
            query = query.replace('wikipedia','')
            query = query.replace(' ','_')
            results = wikipedia.summary(query,sentences=3) # 3 refer to 3 sentence in wikipedia
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application'))
            webbrowser.get('chrome').open('https://www.youtube.com/')

        elif 'open Google' in query:
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application'))
            webbrowser.get('chrome').open('https://www.google.com/')

        elif 'search' in query:
            query = query.replace('search ','') #remove search
            query = query.replace(' ','+')      #remove spacing between words
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application'))
            webbrowser.get('chrome').open('https://www.google.com/search?q='+query)

        elif 'play music' in query:
            speak('playing music from your playlist')
            music_dir = 'song file location'
            songs = os.listdir(music_dir) #list out all the song
            os.startfile(os.path.join(music_dir,songs[0])) #start playing songs fromt firdt song [0]

        elif 'time' in query:
            ctime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Kuang the time is {ctime}')
          
        elif 'exit' in query:
            speak('Bye Bye , i am signing out, Good day to you , See you next time')
            quit()
                  
            
    
