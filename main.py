import pyttsx3

text = 'Hello World'
engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-100)
engine.say(text)
engine.save_to_file(text, 'text.mp3')
engine.runAndWait()