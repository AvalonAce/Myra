---
title: Entry
---
<SwmSnippet path="/ENTRY.py" line="4">

---

Main Function for Myra

```python
if __name__ == "__main__":
  
  # Initialization
  Current_Mode = "ASSISTANT"
  Build()
  
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
```

---

</SwmSnippet>

This is the main function for Myra that runs as the program's main execution thread. First, the program will be set to a default operating mode: Assistant, then it will Build using the build settings, and then run on a loop in the designated mode for the user.

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="PCAA"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
