---
title: Querying
---
## Introduction

This doc gives a high level overview of how querying works for Myra. The assistant's ability to take and recognize **commands** from the user operates from the main <SwmPath>[command/QUERY.py](/command/QUERY.py)</SwmPath> file.&nbsp;

## <SwmPath>[command/QUERY.py](/command/QUERY.py)</SwmPath>

The main functions of <SwmPath>[command/QUERY.py](/command/QUERY.py)</SwmPath> are:

- <SwmToken path="/command/QUERY.py" pos="11:2:4" line-data="def Introduction():">`Introduction()`</SwmToken>
- <SwmToken path="/command/QUERY.py" pos="15:2:4" line-data="def Get_Query():">`Get_Query()`</SwmToken>

## Design Decisions & Expansions

A singular function is used to determine queries for **Assistant Mode.** A singular if statement functions well-enough for the current use-cases. This structure may be changed if need be. Please ensure you update this section if you are changing the structure of **Querying.**

Regarding expansions, more functions can be made and are possibly necessary for other modes and needed for more functionality. It is encouraged to keep querying a simple as possible.

## <SwmToken path="/command/QUERY.py" pos="15:2:4" line-data="def Get_Query():">`Get_Query()`</SwmToken>

This function is the **main query** **loop** for **Assistant Mode**. It starts with an <SwmToken path="/command/QUERY.py" pos="11:2:4" line-data="def Introduction():">`Introduction()`</SwmToken> and follows a while loop to take in a query from <SwmToken path="/audio/AUDIO.py" pos="15:2:2" line-data="def Take_Command():">`Take_Command`</SwmToken> and respond to the query accordingly.&nbsp;

The current functionality of the function are:

- Return name of assistant
- Opening Google

<SwmSnippet path="/command/QUERY.py" line="15">

---

Function Definition

```python
def Get_Query():
    
    Introduction()
    
    while(True):
        
        # Initialize the query ----------------------------------------
        query = Take_Command().lower()
        if query == "NONE": continue
        print(f"User: {query}")
        
        # Chat gpt integration (NOT USED YET)
        '''
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=query
        )
        '''
        
        # Execute the query -------------------------------------------
        
        # Exit Condition
        if 'never mind' in query: 
            Say("Okay... See you later...")
            break
        
        # Question Parsing --------------------------------------------
        # Myra will accept currently 2 types of questions:
        # 1. Questions about herself
        # 2. General questions
        # 
        # Questions about Myra will be answered with a specific response for now. TO DO: Implement a more complex response which involves a call to personality API from character.ai.
        # General questions which are not about Myra will be met with a ChatGPT response.
        #
        elif Question_Parse.Is_Question(query):
            
            
            # Identity 
            # TO DO: Consider all of the possible ways to ask for the name, account for variation
            if 'you' or 'your name' in query:
                Say("I'm Myra, dummy... Your personal assistant.")
                continue
            
            
            # General Questions ---------------------------------------
            # 
            
            # Start GPT Response (NOT USED YET)
            '''
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
                    Say(response.choices[0].message.content)
                    notResponded = False
                else:
                    print('Waiting for response...')
            '''
            
            
            
            
            
            
            
                            
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
            Say("Opening Google.")
            Open_Websearch()
            continue
```

---

</SwmSnippet>

## <SwmToken path="/command/QUERY.py" pos="11:2:4" line-data="def Introduction():">`Introduction()`</SwmToken>

This is the introduction function used to introduce the assistant. It serves two purposes, to introduce Myra on startup and indicate that the user has switched from any other mode to **Assistant Mode**.&nbsp;

<SwmSnippet path="/command/QUERY.py" line="10">

---

Function Definition

```python

def Introduction():
	Say(f"Hey {USER_NAME}, What's up?...")
 
```

---

</SwmSnippet>

## 

## 

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="PCAA"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
