# Build File ----------------------------------------------
# Any tasks that need to be done before the assistant is ready to take queries
# which improves performance or functionality.
#
#
#
# -----------------------------------------------------
from audio.AUDIO import *

def Build(buildSettings):
  setVoice(buildSettings["starterVoice"])
  pass
