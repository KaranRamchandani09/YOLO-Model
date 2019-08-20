# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
from pygame import mixer
import sys
import json
import os
import subprocess
from invoke import run


myCmd="python flow --imgdir sample_img/ --model cfg/tiny-yolo.cfg --load bin/tiny-yolo.weights --json"

result = run(myCmd, hide=True, warn=True)
print(result.ok)



with open("sample_img//out//"+str(sys.argv[1])+".json") as f:
    d = json.load(f)
    JSON=d
	

  
# This module is imported so that we can  
# play the converted audio 
import os 
  
# The text that you want to convert to audio 
data = JSON

mytext="there is a "
for i in range(0,len(data)):
	if(i==len(data)-1):
		mytext=mytext+data[i]["label"]+" with a surity of "+str(data[i]["confidence"])
		continue
		
	
	
	mytext=mytext+data[i]["label"]+" with a surity of "+str(data[i]["confidence"])+" and "
	

print(mytext)
  
# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome.mp3") 

mixer.init()
mixer.music.load("welcome.mp3")
mixer.music.play()
  
# Playing the converted file 
