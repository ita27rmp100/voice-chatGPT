import openai , pyttsx3 , speech_recognition as sr

openai.api_key = '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'

conversation_history = []

i = ''
ra = pyttsx3.init()
ra.setProperty('rate',125)
r = sr.Recognizer()

def reply(message) :
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        ra.say(message)
        ra.runAndWait()
        print('ChatGPT: '+ message)
        audio = r.listen(source)
def send_message(message):
    global conversation_history
    conversation_history.append('User: ' + message)
    prompt = 'You are a helpful assistant.\n' + '\n'.join(conversation_history)
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6
    )
    response_text = response.choices[0].text.strip()
    conversation_history.append(response_text)
    return response_text

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
reply('Hello! How can I assist you today?')
while True:
    user_input = recognize_speech()
    response = send_message(user_input)
    reply(response)