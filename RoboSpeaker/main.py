import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
   
    while True:
        x = input("Enter the word you want me to speak: ")
        if x == "exit":
            break
        
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()
        
        # Speak the input text
        engine.say(x)
        
        # Blocks while processing all the currently queued commands
        engine.runAndWait()
