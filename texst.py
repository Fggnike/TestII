import os
import sys
from io import BytesIO
from threading import Thread
from tkinter import Tk, Label, Button, messagebox
import tkinter
from PIL import Image, ImageTk
import requests
from speech_recognition import  (Recognizer, Microphone, UnknownValueError, RequestError)


def internet_status():
    try:
        requests.get('http://216.58.192.142', timeout=1)
    except requests.ConnectionError:
        Tk().withdraw()
        result = messagebox.showinfo(title="Сообщение об ошибке!", message="""Для работы приложения,\nтребуется доступ к сети Интернет.""")

        print(result)
        if result == "ok":
            sys.exit()
internet_status()


class VoiceAssistant(Tk):
    error = None
    status = ''
    command = ''
    def __init__(self):
        super().__init__()

        self.recognizer = Recognizer()

        self.user_interface()

    def user_interface(self):
        self.geometry("502x240+400+200")
        self.resizable(width=False, height=False)
        self.title("Голосовой ассистент")

        self.background_image = Label(self)
        self.background_image.pack()

        self.button_activate = Button(self, text="Активировать помощника")
        self.button_activate.pack(side="left")
        self.button_activate.config(font=("Times", 15, "bold"), fg="green")
        self.button_activate.configure(command=self.assistant)

        self.label_status = Label(self)
        self.label_status.pack(side="right")
        self.label_status.configure(font=("Times", 18, "bold"), fg="blue")
        self.label_status.config(padx=50, pady=5)

        image = self.get_image
        self.set_background_image(image)

        icon = self.get_icon
        self.set_icon(icon)

    @property
    def get_image(self):
        url = "https://recsquare.ru/upload/medialibrary/4c2/4c2f6c06ef7d87b3d4740109ce5c52a8.jpg"
        content = requests.get(url).content
        pil_image = Image.open(BytesIO(content))
        pil_image.thumbnail((500, 450), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(pil_image, master=self.background_image)
        return image

    @property
    def get_icon(self):
        url = "https://cdn.icon-icons.com/icons2/38/PNG/512/micro_microphone_4764.png"
        content = requests.get(url).content
        pil_image = Image.open(BytesIO(content))
        pil_image.thumbnail((100, 100), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(pil_image, master=self)
        return icon

    def set_background_image(self, image):
        self.background_image.configure(image=image)
        self.background_image = image
    def set_icon(self, icon):
        self.tk.call('wm', 'iconphoto', self._w, icon)

    def assistant(self):
        self.button_activate.configure(state="disabled")
        self.status = "speak"
        def run():
            try:
                with Microphone(device_index=0) as source:
                    audio = self.recognizer.listen(source)
                self.status = "recognition"
                result = self.recognizer.recognize_google(audio, language='ru-RU')
                result = result.lower()
                print(result)
                self.status = "success"
                self.command_handler(result)
            except UnknownValueError:
                self.error = "UnknownValueError"
                print(self.error)
                return
            except RequestError:
                self.error = "RequestError"
                print(self.error)
                return
        self.th = Thread(target=run)
        self.th.start()
        self.status_assistant()

    def status_assistant(self):
        print(self.status)
        if self.error == "UnknownValueError":
            self.button_activate.configure(state="normal")
            self.label_status['text'] = "Не распознано"
            self.error = None
            self.status = ""
            return
        elif self.error == "RequestError":
            self.button_activate.configure(state="normal")
            self.label_status['text'] = "Нет данных!"
            self.error = None
            self.status = ""
            return
        elif self.status == "speak":
            self.label_status['text'] = "Говорите!"
        elif self.status == "recognition":
            self.label_status['text'] = "Распознавание..."
        elif self.status == "success":
            self.label_status['text'] = "Выполняю..."
            self.button_activate.configure(state="normal")
        self.after(300, self.status_assistant)

    def command_handler(self, command):
        print(command)
        if command == "открой блокнот":
            os.system("notepad")
        self.label_status['text'] = "Завершено"
        self.status = ""

def main():
    application = VoiceAssistant()
    application.mainloop()

if __name__ == '__main__':
    main()