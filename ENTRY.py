from command.QUERY import *
from testing.TESTING import Run_Test_Suite
from build import *

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
      
      pass