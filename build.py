# Build File ----------------------------------------------
# Any tasks that need to be done before the assistant is ready to take queries
# which improves performance or functionality.
#
#
#
# -----------------------------------------------------
from audio.AUDIO import setVoice
from main_config import BUILD_SETTINGS

def Build():
  setVoice(BUILD_SETTINGS["starterVoice"])
  pass
