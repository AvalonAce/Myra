# Voices List --- Contains all the voices available in the system that the assistant can use and the user sets.
# Voices consist of a name and an id. The id is used to set the voice of the assistant.

class voice:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def getName(self):
        return self.name
    
    def getId(self):
        return self.id
    
# List of voices
# Enumerate as needed
voices = [
    
]