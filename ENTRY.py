# from openai import OpenAI
# from config import OPEN_AI_API_KEY

from audio import Speak
from query import Get_Query, takeCommand


if __name__ == "__main__":
    Get_Query()





# code
def tellTime(self):
# This method will give the time
	time = str(datetime.datetime.now())
	# the time will be displayed like this "2020-06-05 17:50:14.582630"
	# nd then after slicing we can get time
	print(time)
	hour = time[11:13]
	min = time[14:16]
	self.Speak(self, "The time is sir" + hour + "Hours and" + min + "Minutes")	 





# client = OpenAI()

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)