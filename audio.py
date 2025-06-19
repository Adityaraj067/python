import pyttsx3
import time

engine = pyttsx3.init()

# Set a slower rate for singing effect
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 30)  # Adjust as needed

# Happy Birthday lines
lines = [
    "ear Aditya",
    "Happy birthday to you",
    
    "Jai Shree Ram!"
]

# Speak each line with a pause in between
for line in lines:
    engine.say(line)
    engine.runAndWait()
    time.sleep(0.5)  # short pause between lines
