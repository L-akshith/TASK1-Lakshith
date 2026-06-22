from datetime import datetime
import random

def hello():
    name = input("Enter your Name\n")
    print("Hello,", name, "How can I Help you??")

def show_date():
    print(datetime.now().strftime("%d-%m-%Y"))

def show_time():
    print(datetime.now().strftime("%H:%M"), "(24hrs format)")

def show_weather():
    weather = ["Sunny", "Rainy", "Cloudy", "Windy"]
    print("Current Weather:", random.choice(weather))

commands = {
    "hello": hello,
    "date": show_date,
    "time": show_time,
    "weather": show_weather
}

print("Hello!!! Welcome to the AI world\n")

while True:
    word = input("Enter Something You want to fulfilled by AI..\n")
    word = word.lower().strip()

    if word in ["bye", "exit"]:
        print("Thank you!!!!")
        print("For interacting with me stay connected")
        print("Keep Smiling :)")
        break

    if word in commands:
        commands[word]()      #
    else:
        print("Sorry, I don't understand that command.")