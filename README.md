This code implements an AI chatbot using the OpenAI API and Google Text-to-Speech (gTTS) library.

**Prerequisites**

- OpenAI API Key
- SpeechRecognition library
- gTTS library
- mpg321

**Functionality**

1. Speech to Text Conversion: The speech from the user is recorded using a microphone and converted to text using the Google Speech Recognition API.
2. OpenAI API response: The text obtained from the previous step is passed as a prompt to the OpenAI API and the AI's response is obtained.
3. Text to Speech Conversion: The AI's response is converted to speech using the gTTS library.
4. The code runs continuously and logs the conversation between the human and the AI in a file called "chat.log".

***Usage***

1. Clone the repository
2. Install the required libraries.
3. Obtain an OpenAI API key and set it as an environment variable.
4. Run the code using the command python talk2ai.py
5. Speak your query to the microphone and the AI's response will be played back.


***Note**: The code terminates when the user says "bye".*
