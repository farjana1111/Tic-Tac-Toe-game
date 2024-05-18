# import tkinter as tk
# from tkinter import messagebox

# def check_winner():
#     for combo in[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:      #horizontal,vertical & diagoonals
#         if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":
#             buttons[combo[0]].config(bg="green")
#             buttons[combo[1]].config(bg="green")
#             buttons[combo[2]].config(bg="green")
#             messagebox.showinfo("Tic-Tac-Toe",f"player {buttons[combo[0]]['text']} wins!")
#             root.quit()

# # To be in loop of game (game is still on)
# def button_click(index):
#     if buttons[index]["text"] == "" and not winner:
#         buttons[index]["text"] = current_player
#         check_winner()
#         toggle_player()


# #Current player to next player shuffle
# def toggle_player():
#     global current_player
#     current_player = "X" if current_player == "O" else"O"
#     label.config(text=f"player {current_player}'s turn")
# #making rootname

# root = tk.Tk()
# root.title("Tic-Tac-Toe")

# #Making buttons we use list comprehension

# buttons =[tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i:button_click(i)) for i in range(9)]

# #make button as grid

# for i, button in enumerate(buttons):
#     button.grid(row=i //3, column = i%3)
# #starting the game with current player with "X"

# current_player ="X"
# winner = False
# #tells user whos turn is next
# label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
# #Making players name in down side
# label.grid(row=3, column=0, columnspan=3)
# #runnign the game
# root.mainloop()



























# ---------------------------------------------------------
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query


if __name__ == '__main__':

    speak("Farjana assistance activated ")
    speak("How can i help you")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'are you' in query:
            speak("I am amigo developed by Jaspreet Singh")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'sleep' in query:
            exit(0)
