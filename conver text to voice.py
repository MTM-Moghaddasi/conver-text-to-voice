import pyttsx3
text = input("Please enter your Text : ")
sound = pyttsx3.init()
sound.setProperty('rate' , 110)
sound.say(text)
sound.runAndWait()


print("enter ro bezan ta khareg shi")
q = input()