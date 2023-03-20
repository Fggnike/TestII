import os, webbrowser, sys, requests, subprocess, pyttsx3, wikipedia
from colorama import Fore, Back, Style


wikipedia.set_lang("ru")
#инициализация голосового движка при старте программ
engine = pyttsx3.init()
engine.setProperty("rate", 180)   #скорость речи


def speaker(text):
    """озвучка текста"""
    engine.say(text)
    engine.runAndWait()



def browser():
    webbrowser.open("https//www.youtube.com", new=2)
    #print("браузер запущен")

# def weather():
#     print("weather")

def offBot():
    sys.exit()

def passive():
    pass

def searche():
    zadanie = input("Введите запрос: ")
    text_to_search = zadanie
    search_results = wikipedia.search(text_to_search, results=5)

    if len(search_results) == 0 or text_to_search == 'exit':
        print(f"По запросу '{text_to_search}' ничего не найдено")
        exit()

    for index, result in enumerate(search_results):
        print(f"{index}) {result}")

    get_one = input("Номер результата: ")
    search_result = search_results[int(get_one)]
    texts = wikipedia.summary(search_result)
    print(Fore.CYAN + texts)
    engine.say(texts)