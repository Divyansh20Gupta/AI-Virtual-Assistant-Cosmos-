from time import strftime
import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import datetime
import openai
import random
import numpy as np

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Harry: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]



def ai(prompt):
    openai.api_key = apikey
    t = f"openai response for prompt: {prompt} \n************\n\n"
    respone = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.8,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,)
    print(respone["choices"][0]["t"])
    t+= respone["choices"][0]["t"]
    if not os.path.exists("openai"):
        os.mkdir("openai")

    with open(f'openai/prompt - {random.randint(0,252556664646464)}',"w") as f:
        f.write(t)




def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            return "Something went wrong"


if __name__ == "__main__":
    print("pycharm")
    say("     HOla.    I am cosmos")
    while True:
        print("Listening...")
        text = takeCommand()
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"],["facebook","https://www.facebook.com"],["screener","https://www.screener.in"],["instagram","https://www.instagram.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in text.lower():
                say(f"Here is your {site[0]}")
                webbrowser.open(site[1])

        if "the time" in text.lower():
                strftime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Time is {strftime}")


        elif "chat".lower() in text.lower():
            ai(prompt=text)

        elif "Cosmos Quit".lower() in text.lower():
            exit()

        elif "reset chat".lower() in text.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(text)