from command.QUERY import *
from testing.TESTING import run_test_suite
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
      run_test_suite()
      break
    
    
    elif Current_Mode == "ASSISTANT":
      # Begin the assistant's main loop to take queries
      Get_Query()
      
    
    elif Current_Mode == "CONVERSE":
      
      pass