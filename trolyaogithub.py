import speech_recognition
import pyttsx3
from datetime import date, datetime


sgc_mouth = pyttsx3.init()
sgc_brain = ""
sgc_ear = speech_recognition.Recognizer()

with speech_recognition.Microphone() as mic:
	print("SGC: Listening...")
	audio= sgc_ear.listen(mic)

try:
	you = sgc_ear.recognize_google(audio)
except:
	you ==""
print("Guess:" + you)



if you =="":
	sgc_brain = "I can't hear you, try again"
elif "hello" in you:
	sgc_brain = "Hello , i'am SGC. How can i help you?"
elif "time" and "what" in you:
	
	now = datetime.now()
	sgc_brain = now.strftime("%H:%M:%S")
	print("Current Time =", sgc_brain)

elif you =="today":
	today = date.today()
	sgc_brain = today.strftime("%d/%m/%Y")
	print("Today's date:", sgc_brain)

else:
	sgc_brain = "i'm fine thank you and you"