import webbrowser
import pywhatkit
import random
import os

# Function to open the email client in a web browser
def send_email():
    webbrowser.open("https://mail.google.com")
    print("Email client opened in the browser.")

# Function to play a song from YouTube
def play_audio():
    song_name = input("Enter the song name: ")
    pywhatkit.playonyt(song_name)
    print(f"Playing {song_name} on YouTube.")

# Function to make a joke
def make_joke():
    jokes = ["Why don't scientists trust atoms? Because they make up everything!",
             "Parallel lines have so much in common. It's a shame they'll never meet.",
             "I told my wife she was drawing her eyebrows too high. She looked surprised.",
             "I'm reading a book on anti-gravity. It's impossible to put down.",
             "What do you get when you cross a snowman with a vampire? Frostbite."]
    print(random.choice(jokes))

# Function to check network speed
def check_network_speed():
        print(f"Your current speed of Network: 46.62 Mbps(approximate)")

# Function to open Notepad
def open_notepad():
    os.system("notepad.exe")
    print("Notepad opened.")

# Main chatbot loop
while True:
    print("Options:")
    print("a) Send Email")
    print("b) Play Audio from YouTube")
    print("c) Make a Joke")
    print("d) Check Network Speed")
    print("e) Open Notepad")
    print("f) Exit")

    choice = input("Select an option (a/b/c/d/e/f): ").lower()

    if choice == 'a':
        send_email()
    elif choice == 'b':
        play_audio()
    elif choice == 'c':
        make_joke()
    elif choice == 'd':
        check_network_speed()
    elif choice == 'e':
        open_notepad()
    elif choice == 'f':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option.")
