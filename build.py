# Build File ----------------------------------------------
# Any tasks that need to be done before the assistant is ready to take queries
# which improves performance or functionality.
#
#
#
# -----------------------------------------------------
from audio.AUDIO import Set_Voice
from main_config import BUILD_SETTINGS

def Build():
  Set_Voice(BUILD_SETTINGS["starterVoice"])
  pass
