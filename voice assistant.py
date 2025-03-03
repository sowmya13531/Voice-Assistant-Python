import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
#

# Initialize the text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_amazon(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        speak("Sorry, I couldn't reach the speech recognition service.")
        return None


def respond_to_greeting(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "hi" in command:
        speak("Hi there! How can I help?")


def tell_time():
    now = datetime.datetime.now()
    time = now.strftime("%I:%M %p")
    speak(f"The current time is {time}.")


def tell_date():
    now = datetime.datetime.now()
    date = now.strftime("%B %d, %Y")
    speak(f"Today's date is {date}.")


def web_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    speak(f"Here are the search results for {query}.")


def voice_assistant():
    speak("Hello, I am your voice assistant. How can I help you today?")

    while True:
        command = listen()
        if command:
            if "hello nova" in command or "hi" in command:
                respond_to_greeting(command)
            elif "time" in command:
                tell_time()
            elif "date" in command:
                tell_date()
            elif "search" in command:
                query = command.replace("search", "").strip()
                if query:
                    web_search(query)
                else:
                    speak("Please specify what you'd like to search for.")
            elif "exit" in command or "quit" in command:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I didn't catch that. Please try again.")
if __name__ == "__main__":
    voice_assistant()
