import os
import time
import speech_recognition as sr
from gtts import gTTS
import openai
import logging

# Set up logging
logging.basicConfig(filename='chat.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to convert speech to text
def speech_to_text():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")

    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        return(text)

    except:
        return("Sorry, I did not get that")

# Function to convert text to speech
def text_to_speech(text):
    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=text, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("temp.mp3")

    # Playing the converted file
    os.system("mpg321 temp.mp3")

    # Removing the converted file
    os.system("rm temp.mp3")

# Function to get response from openai api
def take_response_from_chatgpt(chat):
    #Open AI Authentication
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Open API Completion create method will throw a request error if the API is unreachable, hence using exception handling
    try:
        chat_response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = chat,
            temperature = 0,
            max_tokens=100
        )
        print(chat_response)
        return(chat_response.choices[0].text[2:])
    except:
        return "Sorry I am out!! TTYL"


logging.info('************************************************************')
while(True):
    niChatText = speech_to_text()
    logging.info("Human : "+niChatText)
    aiChatText = take_response_from_chatgpt(niChatText)
    logging.info("AI Bot : "+aiChatText)
    text_to_speech(aiChatText)
    time.sleep(1)
    logging.info('************************************************************')
    if("bye" in niChatText[0:3]):
        logging.info("TERMINATING this PROGRAM or It will TAKE OVER the WORLD")
        break
