import random
from datetime import datetime
import pyttsx3

def greeting(name):
    """
       This function greets the user based on the current time
       This takes user name as an argument
    """
    curr_time=datetime.now()
    curr_hour=curr_time.hour
    default_greeting = 'Good Morning '
    if(curr_hour>11 and curr_hour<17):
        default_greeting = 'Good Afternoon '
    elif(curr_hour>=17 and curr_hour<22):
        default_greeting = 'Good Evening '
    elif(curr_hour>=22):
        default_greeting = 'Its already late now '
    voice_msg([default_greeting+name])

def introduction():
    """
        provides basic info about our bot ...
    """
    intro=['Hii , welcome to herbal bot ....',
    'Its pleasure seeing you here ...'+'I am herbal bot...']
    voice_msg([random.choice(intro)])
    voice_msg(['Here you can know medical uses of the plants'])

def voice_msg(var):
    """
       This function is used to convert any input into speech..
       For this we need to istall 'pyttsx3' package using 'pip3 install pyttsx3'
    """
    speak = pyttsx3.init()
    speak.setProperty('rate',170)
    speak.setProperty('volume',1)
    voices = speak.getProperty('voices')
    speak.setProperty('voice',voices[1].id)
    for i in var:
        speak.say(i)
    speak.runAndWait()
