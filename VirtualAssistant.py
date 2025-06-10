from vosk import Model, KaldiRecognizer
import pyaudio
import replies
import pyttsx3
import pyautogui as autoinput
from re import search

engine = pyttsx3.init()
engine.setProperty('rate', 150)

model = Model("C:/Users/User/Desktop/lab/Python/basicRobot/robot-venv/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

def speak():
    engine.runAndWait()

def main():
    while True:
        command = listen()
        if search(r"\b(password)\b", command):
            engine.say("Sure")
            autoinput.write(replies.genpassword())
            speak()
        if search(r"\b(hello)\b", command):
            engine.say(replies.greet())
            speak()
        if "bye" in command:
            engine.say(replies.farewell())
            speak()
        if search(r"\b(time)\b", command) and "it's go time" not in command:
            engine.say(replies.tellTheTime())
            speak()
        if search(r"\btony\b", command):
            engine.say("How you doin?")
            speak()
            command = listen()
            normalResponse(command)

def normalResponse(command):
    engine.say('Let me think')
    speak()
    engine.say(replies.giveResponse(command))
    speak()


def listen():
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    while True:
        data = stream.read(4096, exception_on_overflow=False)

        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            sentence = text[14:-3]
            print(sentence)
            return sentence
        
main()
