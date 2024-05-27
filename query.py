import speech_recognition as sr

from audio import Speak, takeCommand


def Get_Query():
    
    Hello()
    
    
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
        
        # Open Google
        elif "google" in query:
            Speak("Opening Google")
            webbrowser.open("www.google.com")
            continue
        
        
def Hello():
	# This function is for when the assistant 
	# is called it will say hello and then 
	# take query
	Speak("Hello Ry. How can I help you?")