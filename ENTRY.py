from command.QUERY import *
from build import *

buildSettings = {
  "starterVoice": "Taron",
  "currentVoice": "Taron",
}

if __name__ == "__main__":
  
  # Initialization
  Current_Mode = "ASSISTANT"
  Build(buildSettings)
  
  # Engagment Loop
  while(True):
    
    if Current_Mode == "STAND_BY":
      break
    # TO DO: Implement Alexa type functionality on standby activation
    
    elif Current_Mode == "ASSISTANT":
      Get_Query()
      Current_Mode = "STAND_BY"
      
    elif Current_Mode == "CONVERSE":
      
      Current_Mode = "STAND_BY"
      # TO DO: Implement Converse.py first


# Build ------------------------------------------------
# Any tasks that need to be done before the assistant is ready to take queries
# which improves performance or functionality.
#
#
#
# -----------------------------------------------------






# client = OpenAI()

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)