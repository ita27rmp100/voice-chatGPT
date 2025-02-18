import openai , pyttsx3 , speech_recognition as sr
openai.api_key = 'your-key'

conversation_history = []

i = ''
ra = pyttsx3.init()
ra.setProperty('rate',125)
r = sr.Recognizer()

def reply(message):
    ra.say(message)
    ra.runAndWait()
    print('ChatGPT: ' + message)
def send_message(message):
    global conversation_history
    conversation_history.append('User: ' + message)
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',  # Or use 'gpt-4'
            messages=[{"role": "system", "content": "You are a helpful assistant."}] + 
                    [{"role": "user", "content": msg} for msg in conversation_history],
            temperature=0.7,
            max_tokens=100
        )
        response_text = response.choices[0].text.strip()
        conversation_history.append(response_text)
        return response_text
    except Exception as e:
        return f"Error: {str(e)}"
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('user :')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="en")
            print('   '+text)
            return text
        except sr.UnknownValueError:
            return '...'
        except sr.RequestError as e:
            return "..." + str(e)
# Single conversation
def discuss() :
    reply('Hello! How can I assist you ?')
    user_input = recognize_speech()
    response = send_message(user_input)
    reply(response)