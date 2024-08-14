---
title: Building
---
Myra needs to build specific classes and objects before she can run. The Build function takes care of this mainly. Any settings that need to be initialized or actions that need to be taken before Myra begins operating must start in the Build function.

Current Functions in <SwmToken path="/build.py" pos="11:2:4" line-data="def Build():">`Build()`</SwmToken>:

- <SwmToken path="/audio/AUDIO.py" pos="149:2:2" line-data="def setVoice(voiceName):">`setVoice`</SwmToken>

<SwmSnippet path="/build.py" line="11">

---

Current Build Function

```python
def Build():
  setVoice(BUILD_SETTINGS["starterVoice"])
  pass
```

---

</SwmSnippet>

&nbsp;

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="PCAA"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
