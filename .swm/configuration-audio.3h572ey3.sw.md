---
title: Configuration (Audio)
---
## Config

This the configuration doc for any audio related settings.

## Main Settings

The main features of audio configuration are:

- Class voice
- voices\[\]

## Class voice

<SwmSnippet path="/audio/config.py" line="4">

---

Structure for voice class

```python
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
```

---

</SwmSnippet>

Class voice is an object that defines a voice Myra can use and is based on the Elevenlabs capability to produce voices. Each contain a customizable name independent of Elevenlabs, and settings that pertain to their voices API:

- id: A usable Elevenlabs Voice ID (string)
- stability: voice stability setting (float, 0-1)
- similarity: voice similarity setting (float, 0-1)
- style: voice style setting (float, 0-1)
- speakerBoost: boost to audio similarity which limits generation speed (boolean)

## voices\[\]

<SwmSnippet path="audio/config.py" line="33">

---

Empty Voices Array

```
voices = [
   voice("Taron", "Trr0A4w9Xb9LI5l7Vdqa", 0.35, 0.72, 0.55, True)
]
```

---

</SwmSnippet>

Voices array containing the preset voices that Myra can use. Initially with one customized voice, but more voices can be added using the constructor for class voice.

## 

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="PCAA"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
