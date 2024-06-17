import pyttsx3
import speech_recognition as sr
import requests
import playsound

from config import ELEVENLABS_API_KEY
from audio.config import voices




# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def takeCommand():

	r = sr.Recognizer()

	# from the speech_Recognition module 
	# we will use the Microphone module
	# for listening the command
	with sr.Microphone() as source:
		print('Listening')
		
		# seconds of non-speaking audio before 
		# a phrase is considered complete
		r.pause_threshold = 0.7
		audio = r.listen(source)
		
		# Now we will be using the try and catch
		# method so that if sound is recognized 
		# it is good else we will have exception 
		# handling
		try:
			print("Recognizing")
			

			Query = r.recognize_google(audio, language='en-in')
			print("the command is printed=", Query)
			
		except Exception as e:
			print(e)
			print("Retrying...")
			return "NONE"
		
		return Query

# Default Speak -- No Elevenlabs API Call
def Speak(audio):
	
	engine = pyttsx3.init()
	# getter method(gets the current value
	# of engine property)
	voices = engine.getProperty('voices')
	
	# setter method .[0]=male voice and 
	# [1]=female voice in set Property.
	engine.setProperty('voice', voices[1].id)
	
	# Method for the speaking of the assistant
	engine.say(audio) 
	
	# Blocks while processing all the currently
	# queued commands
	engine.runAndWait()
 
 
 # Eleven Labs API Call ---- Speaking Logic

# Eleven Labs API URL minus the voice ID
EL_url = "https://api.elevenlabs.io/v1/text-to-speech/"
CHUNK_SIZE = 1024
CURRENT_VOICE = "Taron"

headers = {
    "Content-Type": "application/json",
	"xi-api-key": "<string>"
}
payload = {
    "text": "<string>",
    "model_id": "<string>",
    "voice_settings": {
        "stability": 123,
        "similarity_boost": 123,
        "style": 123,
        "use_speaker_boost": True
    },
    "pronunciation_dictionary_locators": [
    ],
    "seed": 123,
    "previous_text": "<string>",
    "next_text": "<string>",
    "previous_request_ids": ["<string>"],
    "next_request_ids": ["<string>"]
}
 
def Say(text):
    
	# Find the voice in the voices list
	for voice in voices:
		
		if voice.getName() == CURRENT_VOICE:
			# Build the URL
			url = f"{EL_url}{voice.getId()}"
		
			# Build the header
			headers["xi-api-key"] = ELEVENLABS_API_KEY
			
			# Build the payload
			payload["text"] = text
			payload["model_id"] = "eleven_multilingual_v2"
			payload["voice_settings"]["stability"] = voice.getStability()
			payload["voice_settings"]["similarity_boost"] = voice.getSimilarity()
			payload["voice_settings"]["style"] = voice.getStyle()
			payload["voice_settings"]["use_speaker_boost"] = voice.getSpeakerBoost()
		
			# # DEBUG print headers and payload
			# print(headers)
			# print(payload)
			
			# Make the request and save the response
			response = requests.post(url, json=payload, headers=headers)
		
			# Save the response to a file
			with open("audio/output/response.mp3", "wb") as f:
				f.write(response.content)
    
			# Play the response
			playsound.playsound("audio/output/response.mp3")
    
			break;

    