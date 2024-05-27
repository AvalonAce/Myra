import speech_recognition as sr

from audio.AUDIO import Speak, takeCommand
from command.Simple_Requests import Simple_Requests
# from openai import OpenAI
# from config import OPEN_AI_API_KEY


def Get_Query():
    
    Introduction()
    
    while(True):
        
        query = takeCommand().lower()
        
        # Execute the query
        if 'exit' in query: # Exit the program
            print('Exiting...')
            break
        
        # Recite Name
        elif 'name' in query:
            Speak("My name is Myra. I am your personal assistant.")
            continue
        
        # Simple Requests ----------------------------------------------
        # Simple Requests are requests that are simple to execute that do not require 
        # any external API calls or complex logic. 
        # Examples include telling the time, opening a website, etc.
        # -------------------------------------------------------------

        # Tell Time
        elif 'time' in query:
            Simple_Requests.tellTime()
            continue
                
        # Open Google
        elif "google" in query:
            Simple_Requests.openWebSearch()
            continue
        
        
def Introduction():
	Speak("Hello Rye. How can I help you?")