from command.QUERY import Get_Query


if __name__ == "__main__":
  
  Current_Mode = "ASSISTANT"
  
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
      
    










# client = OpenAI()

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)