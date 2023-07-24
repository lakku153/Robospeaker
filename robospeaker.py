import pyttsx3
if __name__=="__main__":
    print("Welcome to robospeaker")
    engine=pyttsx3.init()
    while True:
        x=input("Enter what you want me to speak:")
        if x=="exit":
            engine.say("Bye Bye")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()