import speech_recognition as sr

from audio.AUDIO import Speak, takeCommand
from command.Simple_Requests import Simple_Requests
from interpretation.MODE_ASSISTANT import Question_Parse

from openai import OpenAI
from config import OPEN_AI_API_KEY, USER_NAME
from command.command_config import RESPONSE_SYSTEM_CONTEXT
client = OpenAI()


# OpenAI Defintions -------------------------------------
  
# Assistant Definition (NOT USED YET) 
assistant = client.beta.assistants.create(
  name="Myra",
  instructions="You are a personal assistant. Answer any questions I have and help me with simple requests. Add a touch of sarcasm sometimes when appropriate, as if you have a small crush on me and wish to humor me.",
  tools=[{
      "type": "code_interpreter",
      "type": "retrieval"
      }],
  model="gpt-3.5-turbo",
)
thread = client.beta.threads.create()

# ----------------------------------------------------------------


def Get_Query():
    
    Introduction()
    
    while(True):
        
        # Initialize the query ----------------------------------------
        query = takeCommand().lower()
        if query == "NONE": continue
        print(f"User: {query}")
        
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=query
        )
        
        # Execute the query -------------------------------------------
        
        # Exit Condition
        if 'never mind' in query: 
            print('Exiting...')
            break
        
        # Question Parsing --------------------------------------------
        # Myra will accept currently 2 types of questions:
        # 1. Questions about herself
        # 2. General questions
        # 
        # Questions about Myra will be answered with a specific response for now. TO DO: Implement a more complex response which involves a call to personality API from character.ai.
        # General questions which are not about Myra will be met with a ChatGPT response.
        #
        elif Question_Parse.is_question(query):
            
            
            # Identity 
            # TO DO: Consider all of the possible ways to ask for the name
            # if 'you' or 'your name' in query:
            #     Speak("My name is Myra. I am your personal assistant.")
            #     continue
            
            
            # General Questions ---------------------------------------
            # 
            
            # Start GPT Response
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-16k",
                messages=[
                    {"role": "system", "content": RESPONSE_SYSTEM_CONTEXT},
                    {"role": "user", "content": query}
                ]
            )
            # Get the response
            notResponded = True
            while (notResponded):
                if response.choices[0].message.content != None:
                    print(f'Myra: {response.choices[0].message.content}')
                    Speak(response.choices[0].message.content)
                    notResponded = False
                else:
                    print('Waiting for response...')

            
            
            
            
            
            
            
                            
            continue
            

        
        # Simple Requests ----------------------------------------------
        # Simple Requests are requests that are simple to execute that do not require 
        # any external API calls or complex logic. 
        # Examples include telling the time, opening a website, etc.
        #

        # # Tell Time
        # elif 'time' in query:
        #     Simple_Requests.tellTime()
        #     continue
                
        # Open Google
        elif "google" in query:
            Speak("Opening Google...")
            Simple_Requests.openWebSearch()
            continue
        
        
def Introduction():
	Speak(f"Hello {USER_NAME}, How can I help you?")