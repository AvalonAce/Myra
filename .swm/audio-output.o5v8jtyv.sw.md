---
title: Audio Output
---
## Introduction

This doc gives a high level overview of **Audio Output** aka the voice of the assistant. Any audio-related files and functionality should be within the **audio** folder.

## Main Files

The main files of **Audio Output** are:

- <SwmPath>[audio/AUDIO.py](/audio/AUDIO.py)</SwmPath>
- <SwmPath>[audio/Response_Variation.py](/audio/Response_Variation.py)</SwmPath>

## <SwmPath>[audio/AUDIO.py](/audio/AUDIO.py)</SwmPath>

This is the main audio production file for Myra. There are two operating voice modes which Myra can use currently, system and custom. The system voice is the basic computer-generated voice created by python, custom voice is the alternative voice which uses Elevenlabs audio and can be customized accordingly. See <SwmLink doc-title="Voice Customization">[Voice Customization](/.swm/voice-customization.zladkama.sw.md)</SwmLink> for how to use and customize available voices.

Here are the available functions:

- <SwmToken path="/audio/AUDIO.py" pos="21:2:2" line-data="def takeCommand():">`takeCommand`</SwmToken>
- <SwmToken path="/audio/AUDIO.py" pos="88:2:4" line-data="def Say(text):">`Say(text`</SwmToken>)
- <SwmToken path="/audio/AUDIO.py" pos="149:2:4" line-data="def setVoice(voiceName):">`setVoice(voiceName`</SwmToken>)

### <SwmToken path="/audio/AUDIO.py" pos="21:2:4" line-data="def takeCommand():">`takeCommand()`</SwmToken>

This function uses python's base speech recognition and audio recognition to recognize a user's voice and turn it into a query.

<SwmSnippet path="/audio/AUDIO.py" line="21">

---

Function definition.&nbsp;

```python
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
```

---

</SwmSnippet>

### <SwmToken path="/audio/AUDIO.py" pos="88:2:4" line-data="def Say(text):">`Say(text`</SwmToken>)

This function produces the audio reponse needed from a query. It chooses between using the system or custom voice and says the text parameter that was passed into the function. If the custom voice option is being used, the function will make a HTTP post call to Elevenlabs, and assuming successful, will write to a <SwmToken path="/audio/AUDIO.py" pos="133:10:12" line-data="		with open(&quot;audio/output/response.mp3&quot;, &quot;wb&quot;) as f:">`response.mp3`</SwmToken> audio file in the audio output folder and play the file as the response.&nbsp;

<SwmSnippet path="/audio/AUDIO.py" line="88">

---

&nbsp;

```python
def Say(text):
	
	if (useSystemVoice == False):
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
```

---

</SwmSnippet>

## 

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="PCAA"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
