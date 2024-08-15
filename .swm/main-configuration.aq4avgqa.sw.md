---
title: Main Configuration
---
<SwmSnippet path="/main_config.py" line="1">

---

Configuration Variables

```
OPEN_AI_API_KEY = "KEY_HERE"
ELEVENLABS_API_KEY = "KEY_HERE"

USER_NAME = "Boss"

BUILD_SETTINGS = {
  "systemVoice" : True,
  "starterVoice": "Taron",
  "currentVoice": "Taron",
}
```

---

</SwmSnippet>

<SwmPath>[main_config.py](/main_config.py)</SwmPath> contains the main configuration variables for Myra including API keys, user variables and preferences, etc. All API keys must be filled with a usable API key for certain parts of the assistant to work.

The current required keys are:

- Open AI API
- Elevenlabs (if using customizable voice)

## Future Expansions

The configuration currently is a .py file instead of a typical configuration file format. In order for the data to be modified outside of python's runtime and manual editing, a separate configuration file must be read from and these variables can be changed with a potential service during build time. An example of when this might occur would be when a UI is fully functional, and the user wishes to change on of their keys on the UI.

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="PCAA"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
