import pyttsx3
import speech_recognition as sr
import requests
import playsound

from config import ELEVENLABS_API_KEY
from audio.config import *

global useTrueVoice
global activeVoice
global previousText

useTrueVoice = True
activeVoice = voice("", "", 0.45, 0.72, 0.80, True)
previousText = ""

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
			print("the command is = ", Query)
			
		except Exception as e:
			print(e)
			print("Retrying...")
			return "NONE"
		
		return Query

 
 
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
        "stability": 0.45,
        "similarity_boost": 0.72,
        "style": 0.80,
        "use_speaker_boost": True
    },
  	"previous_text": "<string>",
  	"next_text": "<string>",
  	"previous_request_ids": [
    "<string>"
  	],
  	"next_request_ids": [
    "<string>"
  	]
}
    
 
def Say(text):
	
	if (useTrueVoice == False):
		engine = pyttsx3.init()
		voices = engine.getProperty('voices')
		
		# setter method .[0]=male voice and 
		# [1]=female voice in set Property.
		engine.setProperty('voice', voices[1].id)
		
		# Method for the speaking of the assistant
		engine.say(text) 
		
		# Blocks while processing all the currently
		engine.runAndWait()
	
	else:
		global activeVoice
		global previousText
  
		# Build the URL		
		url = f"{EL_url}{activeVoice.getId()}"
	
		# Build the header
		headers["xi-api-key"] = ELEVENLABS_API_KEY
		
		# Build the payload
		payload["text"] = text
		payload["model_id"] = "eleven_multilingual_v2"
		payload["voice_settings"]["stability"] = activeVoice.getStability()
		payload["voice_settings"]["similarity_boost"] = activeVoice.getSimilarity()
		payload["voice_settings"]["style"] = activeVoice.getStyle()
		payload["voice_settings"]["use_speaker_boost"] = activeVoice.getSpeakerBoost()

	
		# # DEBUG print headers and payload
		# print(url)
		# print(headers)
		# print(payload)
		
		# Make the request and save the response
		response = requests.post(url, json=payload, headers=headers)
		print("Response: " + str(response.status_code))
	
		# Save the response to a file
		with open("audio/output/response.mp3", "wb") as f:
			f.write(response.content)

		# Play the response
		playsound.playsound("audio/output/response.mp3")
		
		# Close the file
		f.close()



def setPostCall():
    
    
    pass

def setVoice(voiceName):
	global activeVoice
	for v in voices:
		if v.getName() == voiceName:
			activeVoice = v
			break
		else:
			print("Voice not found. Using default voice.")
			activeVoice = voices[0]
			break
	

    