import os
import webbrowser
import sys
import subprocess
import time
import datetime
import tinytuya
import requests
#import pyautogui as pg
import voice
#import tkvlc
from  pyrogram import Client,filters
try:
    import requests		#pip install requests
except:
    pass

#def browser():
    '''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

    #webbrowser.open('https://www.youtube.com/watch?v=UgCef_KBFBg&t=2363s', new=2)
def radioON():
    '''включаем радиа '''








def radioOFF():
    '''откл радиа'''



def game():
    '''Нужно разместить путь к exe файлу любого вашего приложения'''
    try:
        subprocess.Popen('C:/Program Files/paint.net/PaintDotNet.exe')
    except:
        voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')


def offlight():
    #Эта команда вкл свет

    #os.system('shutdown \s')

    # Connect to Device - pytuya Method
    d = tinytuya.OutletDevice('bf0d280b893f02fa3dakzp', '192.168.88.120', '54a536f422143fb9')
    d.set_version(3.3)



    # Get Status
    data = d.status()

    d.turn_off()

def onlight():
    #Эта команда отключает свет


    # Connect to Device - pytuya Method
    d = tinytuya.OutletDevice('bf0d280b893f02fa3dakzp', '192.168.88.120', '54a536f422143fb9')
    d.set_version(3.3)

    data = d.status()

    d.turn_on()
def offterm():
    #Эта команда викл термостат

    # Connect to Device - pytuya Method
    d = tinytuya.OutletDevice('80160345e098069be879', '192.168.88.240', '6cb38443f9b27511')
    d.set_version(3.3)



    # Get Status
    data = d.status()

    d.turn_off()
def onterm():
    #Эта команда викл термостат

    # Connect to Device - pytuya Method
    d = tinytuya.OutletDevice('80160345e098069be879', '192.168.88.240', '6cb38443f9b27511')
    d.set_version(3.3)



    # Get Status
    data = d.status()

    d.turn_on()
##################################################################################################
def girlight():
    '''включаем гирлянду'''
    from pyrogram import Client, filters

    api_id = '27358548'
    api_hash = '7ef0da2c48149e83dd4b05949c02cba2'
    #phone_number = "952113189"
    # pathlib.Path("users.txt").touch(exist_ok=True)
    # text ="ok"
    app = Client(name="siri", api_id=api_id, api_hash=api_hash)
   # print(message)
    try:
        app.start()
        app.send_message(chat_id="6001579489", text="гирлянда")
        app.stop()
    except:
        voice.speaker('не почув')


#################################################################################################
def weather():
    '''Для работы этого кода нужно зарегистрироваться на сайте
    https://openweathermap.org или переделать на ваше усмотрение под что-то другое'''
    try:

        par = {"lang":"ru",
    "lat": 50.720050,
    "lon": 30.629926,
    "appid": "84061a2a5ff54b490d63bd38d557b06d",
    "units": "metric"}
        response = requests.get('http://api.openweathermap.org/data/2.5/weather?', params = par)
        if not response:
            raise
        w = response.json()
        voice.speaker(f"На вулыци {w['weather'][0]['description']} {round(w['main']['temp'])} градус . мррмяу!")

    except:
        voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def time():
    '''Для работы этого кода нужно зарегистрироваться на сайте
    https://openweathermap.org или переделать на ваше усмотрение под что-то другое'''
    try:


        now = datetime.datetime.now()
        voice.speaker(f"зараз " + str(now.hour) + ":" + str(now.minute) + "Мяу")
    except:
        voice.speaker("Сейчас " + str(now.hour) + ":" + str(now.minute)+"Мяу")

def help():
    "екстреннае сообщение"

    try:
        import speech_recognition
        from notifiers import get_notifier
        import time
        bot_token = "6001579489:AAH9qY5ey2v2AgpD7XGL8lYXaxobcT1IpUQ"
        chatID = "-802281463"


        telegram = get_notifier("telegram")
        telegram.notify(token=bot_token, chat_id=chatID, message="help")


        voice.speaker('мяу')
    except:
        voice.speaker('не почув')


def note():
    '''заметка'''

    try:
        import speech_recognition
        from notifiers import get_notifier
        import time
        bot_token = "5804822784:AAEIwCoTPsUjx_ae8Vbpp_P-FghOCcRatUQ"
        chatID = "952113189"

        sr = speech_recognition.Recognizer()
        sr.pause_threshold = 0.5
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            queru = sr.recognize_google(audio_data=audio, language="ru-RU").lower()
            telegram = get_notifier("telegram")
            telegram.notify(token=bot_token, chat_id=chatID, message=queru)

        print(queru)
        time.sleep(3)
        voice.speaker ( "лыста" + str(queru)+' видправыв мяу')
    except:
        voice.speaker('не почув')

#######################################################################
def mess():
    '''сообщение'''
    try:
        import speech_recognition
        from pyrogram import Client, filters
        import time
        api_id = '27358548'
        api_hash = '7ef0da2c48149e83dd4b05949c02cba2'

        sr = speech_recognition.Recognizer()
        sr.pause_threshold = 0.5
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            queru = sr.recognize_google(audio_data=audio, language="ru-RU").lower()
            app = Client(name="siri", api_id=api_id, api_hash=api_hash)
            app.start()
            app.send_message(chat_id="6001579489", text=queru)
            app.stop()

        print(queru)
        time.sleep(3)
        voice.speaker("лыста" + str(queru) + ' видправыв мяу')
    except:
        voice.speaker('не почув')




################################################################
def run():
    '''будильник'''

    try:
        import speech_recognition
        from notifiers import get_notifier
        import time
        bot_token = "5804822784:AAEIwCoTPsUjx_ae8Vbpp_P-FghOCcRatUQ"
        chatID = "952113189"

        sr = speech_recognition.Recognizer()
        sr.pause_threshold = 0.5
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            queru = sr.recognize_google(audio_data=audio, language="ru-RU").lower()
            telegram = get_notifier("telegram")
            telegram.notify(token=bot_token, chat_id=chatID, message=queru)
            s = str(queru)
            I = s.split()
            s1 = ":".join(I)
            tim = str(time.strftime("%H:%M:%S", time.localtime()))
            i=True
            while True:
                if tim[:5] == f"{s1}"and i:
                    i=webbrowser.open('https://www.youtube.com/watch?v=UgCef_KBFBg&t=2363s', new=2)
                    break

                time.sleep(1)


        voice.speaker ( "будыльнык" + str(queru)+' поставыв, мяу')
    except:
        voice.speaker('не почув')





#########################################################################
def offBot():
    '''Отключает бота'''
    sys.exit()


def passive():
    '''Функция заглушка при простом диалоге с ботом'''
    pass

