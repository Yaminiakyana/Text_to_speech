# Import the gTTS library for text-to-speech conversion
# gTTS means google-text-to-speech API.
from gtts import gTTS

# Import the os module for interacting with the operating system
import os

# Define the text to be converted to speech
text = "Hello everyone. I am Yamini Akyana."

# Specify the language for the speech (English in this case)
lang = "en"

# Create a gTTS object with the specified text and language
# 'slow=False' means the speech will be at normal speed
obj = gTTS(text=text, lang=lang, slow=False)

# Save the speech to an MP3 file named "hello.mp3"
obj.save("hello.mp3")

# Play the MP3 file using the default system application
# Note: This may not work as expected on all operating systems
os.system("hello.mp3")
