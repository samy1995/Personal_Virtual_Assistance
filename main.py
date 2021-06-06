
import speech_recognition as spre
import pyttsx3
import datetime
import googlesearch
import wikipedia
import pyjokes
import pywhatkit


listener = spre.Recognizer()
engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with spre.Microphone() as source:
            print("Listening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command()
            if 'hey sam' in command:
                command = command.replace('hey sam', ' ')
                print(command)
    except:
        pass
    return command


def run_sam():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current Time is ' + time)
    elif 'please tell me about' in command:
        person = command.replace('please tell me about', ' ')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk("Sorry, I have a Headache")

    elif 'are you single' in command:
        talk("I have a girlfriend named Wifi")

    elif 'joke' in command:
        talk("I think your life is one, isn't it ?")
        #talk(pyjokes.get_joke())

    else:
        talk("I Am Sorry. I didn't get that! ")


while True:
    run_sam()


