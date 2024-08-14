---
title: Entry / Main Function
---
This is the main function for Myra that runs as the program's main execution thread. First, the program will be set to a default operating mode: Assistant, then it will Build using the build settings, and then run on a loop in the designated mode for the user.

<SwmSnippet path="/ENTRY.py" line="5">

---

Main Function for Myra

```python
if __name__ == "__main__":
  
  # Initialization
  Current_Mode = "ASSISTANT"
  Build()
  
  # Engagment Loop
  while(True):
    
    if Current_Mode == "TESTING":
      # Run the test suite if the mode is TESTING
      # Ensure the test suite is configured before use
      Run_Test_Suite()
      break
    
    
    elif Current_Mode == "ASSISTANT":
      # Begin the assistant's main loop to take queries
      Get_Query()
      
    
    elif Current_Mode == "CONVERSE":
      
```

---

</SwmSnippet>

&nbsp;

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="PCAA"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
