import io
import pygame
from gtts import gTTS
from googletrans import Translator
translator = Translator()

def speak(text):
    with io.BytesIO() as file:
        gTTS(text=text, lang="hi").write_to_fp(file)
        file.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

if __name__ == '__main__':
    text=input("what should i say? > ")

    speak(text)