# Voices List --- Contains all the voices available in the system that the assistant can use and the user sets.
# Voices consist of a name and an id. The id is used to set the voice of the assistant.

class voice:
    def __init__(self, name, id, stability, similarity, style, speakerBoost):
        self.name = name
        self.id = id
        self.stability = stability
        self.similarity = similarity
        self.style = style
        self.speakerBoost = speakerBoost
        
    def getName(self):
        return self.name
    
    def getId(self):
        return self.id
    
    def getStability(self):
        return self.stability
    
    def getSimilarity(self):
        return self.similarity
    
    def getStyle(self):
        return self.style
    
    def getSpeakerBoost(self):
        return self.speakerBoost
    
# List of voices
# Enumerate as needed
voices = [
   voice("Taron", "Trr0A4w9Xb9LI5l7Vdqa", 0.35, 0.72, 0.55, True)
]