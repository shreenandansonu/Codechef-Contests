from gtts import gTTS
from playsound import playsound
mytext ="mama kan karuchu? aaji kan khali chuda kadali khaiba ki . aau kichi tarkari warkari habani ki ?"
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("Sc.mp3")
playsound("Sc.mp3")
