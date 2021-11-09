import speech_recognition as spr
from googletrans import Translator,LANGUAGES
from gtts import gTTS
import os
import io
import time
import pyglet

recog1 = spr.Recognizer()

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

with mc as source:
    print("Try saying 'translate to french'")
    print("******************************************")
    recog1.adjust_for_ambient_noise(source, duration = 0.2)
    audio = recog1.listen(source)
    print("Recognizing the recieved input....")
    query = recog1.recognize_google(audio)
    print('Recognition successfull....')
    print('initiating input read....')
    query = query.lower()

    
if 'translate' in query:
    to_lang = query.strip().split()[-1]
    languages = LANGUAGES
    to_lang=[lang for lang in languages.keys() if languages[lang] == to_lang][0]
    translator = Translator()
    
    with mc as source:
        print("Speak something")
        speak('please start speaking in your language.')
        recog1.adjust_for_ambient_noise(source, duration=0.2)
        audio = recog1.listen(source)
        get_sentence = recog1.recognize_google(audio)

    try:
        print("To be Translated :"+ get_sentence)
        print("Translating input....")
        from_lang = translator.detect(get_sentence).lang
        text_to_translate = translator.translate(get_sentence,src=from_lang, dest=to_lang)
        text = text_to_translate.text
        speak(text, to_lang)

    except spr.UnknownValueError:
        print("Unable to Understand the Input")
    except spr.RequestError as e:
        print("Unable to provide Required Output".format(e))
