from gtts import gTTS    #for importing google text to speech python library
import translators as ts  
import os      


def question():
	var= input("what language do you want to translate to      Igbo or Yoruba ") 
	
#this section lets you pick the language you want to be translated to


	if var == "igbo":  
		igboq= input("input the sentence for translation")
		igboAnswer = (ts.google(igboq ,from_language='en', to_language='ig')) 
		speech = igboAnswer
		language = 'en-NG'
		play = gTTS(text=speech)
		play.save("file.mp3")
		os.system("start file.mp3") 
		print(igboAnswer)
		print(question()) 

	elif var == "yoruba":  
		yorubaQuestion= input("input the sentence for translation")
		yorubaAnswer = (ts.google(yorubaQuestion ,from_language='en', to_language='yo')) 
		speech = yorubaAnswer
		language = 'en-NG'    
		play = gTTS(text=speech)
		play.save("file.mp3")
		os.system("start file.mp3")
		print(yorubaAnswer)
		print(question())  

	else :
		print("please enter a valid language")
		print(question())  

question()
