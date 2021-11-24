from gtts import gTTS           # we have imported this module for text to speech conversion
import os
text = input()      # give the text

# to read from a file we need to give file name and read function

''' variable=open('filename.txt')
    text=variable.read()'''

language = 'en'     # language of that text
obj = gTTS(text=text, lang=language, slow=False)         # slow=false because the audio will be in normal speed
obj.save("p1.mp3")
# to automatically open the mp3 file we need to import os
os.system("p1.mp3")
