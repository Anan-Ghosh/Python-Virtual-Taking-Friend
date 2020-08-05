import pyttsx3

speak=pyttsx3.init()
speech=input("Say Something:")

speak.say(speech)
speak.runAndWait()
