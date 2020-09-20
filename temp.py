import speech_recognition as sr 
from textblob import TextBlob
mic_name ="Microphone (Realtek High Defini"  #"Microphone (Realtek Audio)"
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()
mic_list = sr.Microphone.list_microphone_names()
print(mic_list)
for i, microphone_name in enumerate(mic_list):
    	if microphone_name == mic_name:
		    device_id = i
print(microphone_name)
with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    print("Say Something")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio, language='en-GB')
    print("You said " + text)
   
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
         print("Could not request results from Google Speech Recognition Service; {0}".format(e))
print(text)
text = TextBlob(text)    
pos= text.tags
print(pos)
senti = text.sentiment
print(senti)
senti = text.sentiment
print(senti)
if(senti.polarity<0):
    review = "Sorry to say it was Negative review, I appreciate your feedback"
    print("Negative review")
else:
    review = "Thanks for the positive review, I appreciate your feedback"
    print("Positive review")
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello this is Reshu talking")
engine.say("echoing your words")
engine.say(text)
engine.say(review)
engine.setProperty('rate',125)
engine.setProperty('volume',0.7)
engine.runAndWait() 