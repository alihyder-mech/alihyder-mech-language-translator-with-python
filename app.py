import speech_recognition as spr
from googletrans import Translator,LANGUAGES
from gtts import gTTS
import os
import io
import time
import pyglet

recog = spr.Recognizer()
# code to viwe the microphone index and select sys default

for index, name in enumerate(spr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
mc = spr.Microphone(device_index=6)
pyglet.options["audio"] = ("pulse",)
def speak(text: str, lang: str="en"):
    with io.BytesIO() as f:
        gTTS(text=text, lang=lang, slow=False).write_to_fp(f)
        f.seek(0)
        player = pyglet.media.load('_.mp3', file=f).play()
        while player.playing:
            pyglet.app.platform_event_loop.dispatch_posted_events()
            pyglet.clock.tick()


print("***** "*15)

def input_ask(prompt_message:str="speak something"):
    with mc as source:
        print("Alexis: ",prompt_message)
        speak(prompt_message)
        recog.adjust_for_ambient_noise(source, duration = 0.2)
        audio = recog.record(source,duration = 5)
        print("Recognizing the recieved input....")
        query = recog.recognize_google(audio)
        print('Recognition successfull....')
        print('initiating input read....')
        query = query.lower()
    return query


# with mc as source:
#     print("Alexis : I'm Alexis, A language translation bot")
#     speak("Hi, I'm Alexis, A language translation bot")
#     recog.adjust_for_ambient_noise(source, duration = 0.2)
#     audio = recog.record(source,duration = 5)
#     print("Recognizing the recieved input....")
#     query = recog.recognize_google(audio)
#     print('Recognition successfull....')
#     print('initiating input read....')
#     query = query.lower()

query = input_ask("Hi, I'm Alexis, a language translation bot. Try saying something like 'translate to french'")
while 'stop' not in query:   
    if 'translate' in query:
        to_lang = query.strip().split()[-1]
        languages = LANGUAGES
        try:
            to_lang=[lang for lang in languages.keys() if languages[lang] == to_lang][0]
            translator = Translator()
        
            get_sentence = input_ask("Please start speaking in your language.")

            try:
                print("Translating input....")
                print("To be Translated :"+ get_sentence)
                from_lang = translator.detect(get_sentence).lang
                text_to_translate = translator.translate(get_sentence,src=from_lang, dest=to_lang)
                text = text_to_translate.text
                speak(text, to_lang)

            except spr.UnknownValueError:
                print("Unable to Understand the Input")
                pass
            except spr.RequestError as e:
                print("Unable to provide Required Output".format(e))
                pass
        except IndexError:
            print('Alexis: Please be more clear')
            speak('Please be more clear')
            pass
    query = input_ask("To stop, say Stop! or continue as above." )
    
print("Alexis: Good Bye cowpoke!")
speak('Good bye Cowpoke!')
