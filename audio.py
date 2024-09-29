from gtts import gTTS
import os

def text_to_audio(text, filename='output.mp3', lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(filename)

    print(f"Audio saved as {filename}")
    os.system(f"start {filename}" if os.name == 'nt' else f"xdg-open {filename}")


if __name__ == "__main__":
    text = input('Write ot paste your text here: ')
    lang=input('choose your language("ru" for Russian or "en" for English: ')
    custom_filename = input('write filename:' ) + '.mp3'
    text_to_audio(text, filename=custom_filename, lang=lang)