from openai import OpenAI
from main_config import OPEN_AI_API_KEY, USER_NAME

RESPONSE_SYSTEM_CONTEXT = "You are a personal assistant. Answer any questions I have and help me with simple requests."
# client = OpenAI()

# OpenAI Defintions -------------------------------------
  
# Assistant Definition (NOT USED YET) 
'''
assistant = client.beta.assistants.create(
  name="Myra",
  instructions=RESPONSE_SYSTEM_CONTEXT,
  tools=[{
      "type": "code_interpreter",
      "type": "retrieval"
      }],
  model="gpt-3.5-turbo",
)
thread = client.beta.threads.create()
'''
# ----------------------------------------------------------------