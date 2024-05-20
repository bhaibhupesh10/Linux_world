import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Get user input
text_to_speak = input("Enter text to speak: ")

# Set properties (optional)
engine.setProperty('rate', 160)  # Speed of speech, default is 200
engine.setProperty('volume', 9.0)  # Volume (0.0 to 1.0)

# Say the input text
engine.say(text_to_speak)

# Wait for speech to complete
engine.runAndWait()
