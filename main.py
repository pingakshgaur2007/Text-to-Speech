import pyttsx3

engine = pyttsx3.init()

# =============================================================================

"""VOICES"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

"""RATE"""
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)

"""VOLUME"""
volume = engine.getProperty('volume')
engine.setProperty('volume', 1)

# engine.say("Hello World.")
# engine.runAndWait()

# =============================================================================

def speak(audio):
    print("\nComputer : " + audio)
    engine.say(audio)
    engine.runAndWait()
    
speak("Hello World.")
