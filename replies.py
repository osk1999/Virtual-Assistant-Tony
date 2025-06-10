from datetime import datetime
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from llama_cpp import Llama

#greet the user back
def greet():
    time = datetime.now()
    current = int(time.strftime("%H"))
    if current < 12:
        return f"Good morning"
    else:
        return f"Good evening"

#say farewell
def farewell():
    farewells = ["Goodbye", "See you later", "farewell"]
    return f"{farewells[random.randint(0, 2)]}"

#unknown request handling
def unknownRequest():
    return "I apologise, I do not understand your request. Your request may be beyond my current capabilities or you could attempt to ask your request in more simple terms"

#generate a password
def genpassword(l=random.randint(8, 16)):
    possible = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    ]
    password = ''
    for i in range(0, l):
        password += possible[random.randint(0, len(possible)-1)]
    return password

#return current time
def tellTheTime():
    time = datetime.now()
    currentHour = time.strftime("%H")
    currentMinute = time.strftime("%M")
    return f"The time is {currentHour} and {currentMinute} minutes"

#It's go time
def gotime():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.pornhub.com/video/search?search=lana+rhoades")

#LLM model response
llm = Llama(
    model_path='C:/Users/User/AppData/Local/nomic.ai/GPT4All/mistral-7b-instruct-v0.1.Q4_0.gguf',
    last_n_tokens_size=32,
    n_ctx=5000,
    stop = ['Q:']
    )

def giveResponse(prompt):
    response = llm.create_chat_completion(
        messages=[
            {
                'role': 'AI Assistant',
                'content': 'Give clear, conversational and concise answers to prompts'
            },
            {
                'role': 'user',
                'content': f'{prompt}'
            }
        ]
    )['choices'][0]['message']['content']
    return response