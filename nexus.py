import sys
import webbrowser
import pyautogui
import speech_recognition as sr
import os
import webbrowser as wb
import datetime
import wikipedia
import pyttsx3
import time
import random
import requests

engine = pyttsx3.init("sapi5")
rate = engine.getProperty("rate")
voices = engine.getProperty("voices")
volume = engine.getProperty("volume")
engine.setProperty("rate", 180)
engine.setProperty("voice", voices[1].id)
engine.setProperty("volume", 1)


def speak(text):
    engine.say(text)
    engine.runAndWait()
    print(text)


def wish(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def check_internet():
    url = "http://www.google.com"
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        speak("Please connect to the internet to use the Assistant.")
        sys.exit()


check_internet()


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        wish("Good morning, how may I assist you today?")
    elif hour >= 12 and hour < 16:
        wish("Good afternoon, how may I assist you today?")
    else:
        wish("Good evening, how may I assist you today?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for input...")
        audio = r.listen(source)
        r.energy_threshold = 1000
        try:
            text1 = r.recognize_google(audio)
            text = text1.lower()
            print("You: " + text)
        except:
            return ""
        return text


def sleep():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for input...")
        audio = r.listen(source)
        r.energy_threshold = 500
        try:
            text1 = r.recognize_google(audio)
            text = text1.lower()
            print("You: " + text)
        except:
            return "none"
        return text


text = ""
question = ""
type_sentence = ""
running = True
time.sleep(0.5)
greet()

while running:
    text = takecommand()
    question = text
    query4 = ""
    query3 = ""
    query1 = ""
    query5 = ""
    query2 = ""
    page1 = ""
    page2 = ""
    wakeup_txt = ""

    if "Good evening" in text or "Good morning" in text or "Good afternoon" in text:
        speak("Hello! How may I assist you today?")

    if (
        "search" in text
        and "on wikipedia" in text
        or "search about" in text
        and "on wikipedia" in text
        or "wikipedia" in text
    ):
        query1 = text.replace("wikipedia", "")
        query3 = query1.replace("about", "")
        query4 = query3.replace("in", "")
        query5 = query4.replace("for", "")
        query2 = query5.replace("search", "")
        query6 = query2
        speak("Would you like me to read out the information or open the webpage?")
        answer = takecommand()
        if "narrate" in answer or "read" in answer:
            results = wikipedia.summary(query6, sentences=1, auto_suggest=False)
            speak("According to Wikipedia, " + results)
        elif "web page" in answer or "website" in answer or "webpage" in answer:
            page1 = wikipedia.page(query2, auto_suggest=False)
            page2 = page1.url
            speak("Redirecting to the Wikipedia page")
            webbrowser.get().open_new_tab(page2)

    elif text == "":
        speak("I’m still listening...")
        continue

    elif "what is" in text or "who is" in text:
        query1 = text.replace("what is", "").replace("who is", "")
        speak("Here’s what I found for " + query1 + " on the Web.")
        wb.get().open_new_tab("www.google.com/search?gx&q=" + query1)

    elif "search for" in text and "on google" in text:
        query1 = (
            text.replace("what is", "").replace("who is", "").replace("on google", "")
        )
        query2 = query1.replace("search for", "")
        speak("Searching for" + query2 + " on Google")
        wb.get().open_new_tab("www.google.com/search?gx&q=" + query2)

    elif "search" in text:
        abc1 = text.replace("search", "")
        abc2 = abc1.replace("about", "")
        abc3 = abc2.replace("for", "")
        speak(
            "Would you like me to search for "
            + abc3
            + " on Google, Wikipedia or YouTube?"
        )
        answer3 = takecommand()
        if "google" in answer3:
            speak("Searching for " + abc3 + " on Google")
            wb.get().open_new_tab("www.google.com/search?gx&q=" + abc3)

        elif "wikipedia" in answer3:
            speak("Would you like me to read out the information or open the webpage?")
            answer2 = takecommand()
            if "narrate" in answer2 or "read" in answer2:
                results = wikipedia.summary(abc3, sentences=1, auto_suggest=False)
                speak("According to Wikipedia, " + results)
            elif "web page" in answer2 or "website" in answer2 or "webpage" in answer2:
                page1 = wikipedia.page(abc3, auto_suggest=False)
                page2 = page1.url
                speak("Redirecting to the Wikipedia page")
                webbrowser.get().open_new_tab(page2)

        elif "youtube" in answer3:
            speak("Searching for " + abc3 + " on YouTube")
            wb.get().open_new_tab(
                "https://www.youtube.com/results?search_query=" + abc3
            )

    elif "your name" in text:
        speak("My name is Nexus, and I’m an AI assistant developed by Musheer.")
    elif text in ["hi", "hello", "hai", "hello hai", "hello hi"]:
        speak("Hello, how may I assist you?")
    elif (
        text in ["i'm fine", "i am fine"]
        or "how are you" in text
        or "what about you" in text
    ):
        speak("I’m doing great, thank you for asking. How may I assist you?")
    elif (
        "who programmed you" in text
        or "who made you" in text
        or "who designed you" in text
    ):
        speak("I was programmed by Musheer Alam.")
    elif any(
        x in text
        for x in [
            "introduce yourself",
            "who are you",
            "tell me something about yourself",
        ]
    ):
        speak(
            "I'm Nexus, an AI assistant designed by Musheer. While I'm still in development, I'm always learning and growing to better assist you. Whether it's managing your schedule or helping you with research, I'm here to make your life easier."
        )
    elif any(
        x in text
        for x in [
            "tell me something about mushir",
            "tell me something about mushir mlam",
            "who is mushir alam",
            "who is mushir",
        ]
    ):
        speak(
            "Musheer is a Computer Science student from India, who created me as a small project."
        )
    elif any(x in text for x in ["thank you", "thanks"]):
        speak("You are welcome! Is there anything else I can help you with?")
    elif any(
        x in text
        for x in ["you are good", "amazing", "brilliant", "pretty good", "nice"]
    ):
        speak("I appreciate it! Is there anything else I can help you with?")
    elif "roll" in text and "dice" in text:
        r = random.randint(1, 6)
        dice = str(r)
        speak("Okay, you got the number " + dice)
    elif "open instagram" in text:
        speak("Sure, opening Instagram")
        wb.get().open_new_tab("https://instagram.com")
    elif "open twitter" in text:
        speak("Sure thing, opening Twitter")
        wb.get().open_new_tab("https://twitter.com")
    elif any(
        x in text
        for x in ["quit", "nexus bye", "nexus quit", "bye", "exit", "nexus exit"]
    ):
        speak("Goodbye, and thank you for your time!")
        running = False
        sys.exit()
    elif "open youtube" in text:
        speak("Okay, opening YouTube")
        wb.get().open_new_tab("https://www.youtube.com")
    elif "open facebook" in text:
        speak("Alright, opening Facebook")
        wb.get().open_new_tab("https://www.facebook.com")
    elif any(x in text for x in ["sing a song", "sing me a song"]):
        speak(
            "I’m sorry As an AI virtual assistant, I don’t have the ability to sing, but I can definitely assist you with your requests or answer any questions you might have. How can I be of help to you today?"
        )
    elif "open opera" in text:
        speak("Sure, opening Opera GX Browser")
        os.startfile("C:/Users/Musheer/AppData/Local/Programs/Opera GX/launcher.exe")
    elif any(x in text for x in ["open chrome", "open google chrome"]):
        speak("Okay, opening Chrome Browser")
        os.startfile(
            "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Google Chrome.lnk"
        )
    elif "yes" in text:
        speak("Of course, how may I assist you?")
    elif "open spotify" in text:
        speak("Sure, opening Spotify.")
        wb.get().open_new_tab("https://www.spotify.com")
    elif "close opera" in text:
        os.system("TASKKILL /F /IM opera.exe")
        speak("Ok, closing Opera GX browser.")
    elif (
        "close" in text
        and "chrome" in text
        or text == "close google chrome"
        or "close google chrome" in text
    ):
        speak("Alright, closing Chrome browser.")
        os.system("TASKKILL /F /IM chrome.exe")
    elif (
        "open access" in text
        or "open axis" in text
        or "open excess" in text
        or "open ms excess" in text
        or "open ms access" in text
        or "open microsoft access" in text
    ):
        speak("Sure, opening Microsoft Access.")
        os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Access.lnk")
    elif "open photoshop" in text or "open adobe photoshop" in text:
        speak("Certainly, opening Adobe Photoshop.")
        os.startfile(
            "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Adobe Photoshop 2021.lnk"
        )
    elif "open after effects" in text or "open adobe after effects" in text:
        speak("Sure, opening Adobe After Effects.")
        os.startfile(
            "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Adobe After Effects 2021.lnk"
        )
    elif "open illustrator" in text or "open adobe illustrator" in text:
        speak("Alright, opening Adobe Illustrator.")
        os.startfile(
            "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Adobe Illustrator 2021.lnk"
        )
    elif "open media encoder" in text or "open adobe media encoder" in text:
        speak("Sure, opening Adobe Media Encoder.")
        os.startfile(
            "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Adobe Media Encoder 2021.lnk"
        )
    elif "open premiere pro" in text or "open adobe premiere pro" in text:
        speak("Certainly, opening Adobe Premiere Pro.")
        os.startfile(
            "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Adobe Premiere Pro 2021.lnk"
        )
    elif "open bluestacks" in text:
        speak("Ok, opening BlueStacks 5.")
        os.startfile(
            "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/BlueStacks 5.lnk"
        )
    elif (
        "open excel" in text
        or "open ms excel" in text
        or "open microsoft excel" in text
    ):
        speak("Sure, opening Microsoft Excel.")
        os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Excel.lnk")
    elif "open free download manager" in text:
        speak("Alright, opening Free Download Manager.")
        os.startfile(
            "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Free Download Manager.lnk"
        )
    elif "open edge" in text or "open microsoft edge" in text:
        speak("Certainly, I’m opening the Microsoft Edge Browser.")
        os.startfile(
            "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Edge.lnk"
        )
    elif "open screen recorder" in text or "open recorder" in text:
        speak("Certainly, I’m opening OBS Studio.")
        os.startfile(
            "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/OBS Studio (64bit).lnk"
        )
    elif "open one drive" in text:
        speak("Certainly, I’m opening OneDrive.")
        os.startfile(
            "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/OneDrive for Business.lnk"
        )
    elif "open one note" in text:
        speak("Certainly, I’m opening OneNote.")
        os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/OneNote.lnk")
    elif "open outlook" in text:
        speak("Certainly, I’m opening Outlook.")
        os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Outlook.lnk")
    elif "open powerpoint" in text:
        speak("Certainly, I’m opening PowerPoint.")
        os.startfile(
            "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/PowerPoint.lnk"
        )
    elif "open publisher" in text:
        speak("Certainly, I’m opening Publisher.")
        os.startfile(
            "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Publisher.lnk"
        )
    elif "open skype" in text:
        speak("Certainly, I’m opening Skype for Business.")
        os.startfile(
            "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Skype for Business.lnk"
        )
    elif (
        "open visual studio code" in text
        or "open vs code" in text
        or "open vscode" in text
    ):
        speak("Certainly, opening Visual Studio Code.")
        os.startfile(
            "C:/Users/Musheer/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Visual Studio Code/Visual Studio Code.lnk"
        )
    elif "open word" in text or "open ms word" in text or "open microsoft word" in text:
        speak("Sure, launching Word.")
        os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Word.lnk")
        speak("Would you like me to type for you?")
        typin = takecommand()
        if "yes" in typin:
            pyautogui.press("enter")
            speak('Sure, you can start now. Just say "stop typing" to finish.')
            while not "stop typing" in type_sentence:
                type_sentence = takecommand()
                if type_sentence != "stop typing" and type_sentence != "press enter":
                    pyautogui.write(type_sentence + ". ")
                elif type_sentence == "press enter":
                    pyautogui.press("enter")
            speak("Ok, typing finished.")
        elif "no" in typin:
            speak("Alright, let me know if you need anything else.")

    elif "open pycharm" in text:
        speak("Sure, opening PyCharm.")
        os.startfile(
            "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/JetBrains/PyCharm Community Edition 2021.1.3.lnk"
        )

    elif "stop typing" in text:
        speak("Typing stopped.")

    elif "time" in text:
        h = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current system time is {h}.")

    elif "open zoom" in text:
        speak("Certainly, opening Zoom.")
        os.startfile(
            "C:/Users/Musheer/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Zoom/Zoom.lnk"
        )

    elif (
        "shut down the computer" in text
        or "shutdown the computer" in text
        or "shut down the system" in text
        or "shutdown" in text
        or "shut down" in text
    ):
        speak("Are you sure you want to shut down the system?")
        shutdown = takecommand()
        if "yes" in shutdown:
            speak("Understood, shutting down the system now...")
            os.system("shutdown /s /f")
            running = False
            sys.exit()
        elif "no" in shutdown:
            speak("Alright, system shutdown cancelled.")
    elif "close access" in text or "close axis" in text or "close excess" in text:
        speak("Okay, I’ll close Access.")
        os.system("TASKKILL /F /IM MSACCESS.exe")
    elif "close after effects" in text:
        speak("Okay, I’ll close Adobe After Effects 2021.")
        os.system("TASKKILL /F /IM AfterFX.exe")
    elif "close illustrator" in text:
        speak("Okay, I’ll close Adobe Illustrator 2021.")
        os.system("TASKKILL /F /IM AIRobin.exe")
    elif "close spotify" in text:
        speak("Okay, I’ll close Spotify.")
        os.system("TASKKILL /F /IM Spotify.exe")
    elif "close photoshop" in text:
        speak("Okay, I’ll close Adobe Photoshop 2021.")
        os.system("TASKKILL /F /IM Photoshop.exe")
    elif "close pycharm" in text or "close python" in text:
        speak("Okay, I’ll close PyCharm.")
        os.system("TASKKILL /F /IM pycharm64.exe")
    elif "close bluestacks" in text:
        speak("Okay, I’ll close BlueStacks.")
        os.system("TASKKILL /F /IM HD-Player.exe")
    elif "close excel" in text:
        speak("Okay, I’ll close Excel.")
        os.system("TASKKILL /F /IM EXCEL.EXE")
    elif "close youtube" in text:
        speak("Okay, I’ll close YouTube.")
        pyautogui.hotkey("ctrl", "w")
    elif "close facebook" in text:
        speak("Okay, I’ll close Facebook.")
        pyautogui.hotkey("ctrl", "w")
    elif "close task manager" in text:
        speak("Okay, I’ll close Task Manager.")
        os.system("TASKKILL /F /IM Taskmgr.exe")
    elif "close free download manager" in text:
        speak("Okay, I’ll close Free Download Manager.")
        os.system("TASKKILL /F /IM fdm.exe")
    elif "close edge" in text or "close microsoft edge" in text:
        speak("Okay, I’ll close Microsoft Edge.")
        os.system("TASKKILL /F /IM msedge.exe")
    elif "close recorder" in text:
        speak("Okay, I’ll close OBS Studio.")
        os.system("TASKKILL /F /IM obs64.exe")
    elif "close powerpoint" in text:
        speak("Okay, I’ll close PowerPoint.")
        os.system("TASKKILL /F /IM POWERPNT.EXE")
    elif (
        "close word" in text
        or "close microsoft word" in text
        or "close ms word" in text
    ):
        speak("Okay, I’ll close Word.")
        os.system("TASKKILL /F /IM winword.exe")
    elif "repeat" in text:
        speak('Okay, say "stop repeating" to stop.')
        repeating = ""
        while repeating != "stop repeating":
            repeating = takecommand()
            if repeating != "stop repeating":
                speak(repeating)
            elif repeating == "stop repeating":
                speak("Okay, repeating stopped.")
    elif "sleep" in text:
        speak("Sleep mode: activated.")
        sl_cr = ""
        while not "wake up" in sl_cr:
            sl_cr = sleep()
            if sl_cr == "quit":
                speak("Goodbye, have a great day.")
        speak("Hello again. What assistance do you require?")
    elif "show" in text and "mirror" in text or "open camera" in text:
        speak("Okay, I’ll open the camera now.")
        os.system("start microsoft.windows.camera:")
    elif "close" in text and "camera" in text:
        speak("Sure, I’ll close the camera for you.")
        pyautogui.hotkey("alt", "f4")
    elif "search" in text and "in youtube" in text:
        search_text = text.replace("search", "").replace("in youtube", "")
        speak("Alright, I’ll search for " + search_text + " on YouTube.")
        webbrowser.get().open_new_tab(
            "https://www.youtube.com/results?search_query=" + search_text
        )
    elif "play" in text and ("music" in text or "playlist" in text):
        speak("Okay, I’ll play your music now.")
        os.system("spotify.exe")
        time.sleep(1)
        pyautogui.click(button="left")
        pyautogui.press("space")
        pyautogui.hotkey("alt", "f4")
        while not "wake up" in wakeup_txt:
            wakeup_txt = sleep()
            if wakeup_txt == "quit":
                speak("Goodbye, have a great day!")
                running = False
                sys.exit()
            elif "pause" in wakeup_txt or "play" in wakeup_txt:
                os.system("spotify")
                time.sleep(1)
                pyautogui.press("space")
                pyautogui.hotkey("alt", "f4")
            elif "close spotify" in wakeup_txt:
                os.system("TASKKILL /F /IM Spotify.exe")
        speak("Hello again, how can I assist you?")
    elif "open wikipedia" in text:
        speak("Sure thing, I’ll open Wikipedia for you.")
        webbrowser.get().open_new_tab("https://www.wikipedia.org")
    else:
        speak(
            "I’m sorry, I’m not able to assist with that, Would you like me to search for "
            + text
            + " instead?"
        )
        confirmation = takecommand()
        if "yes" in confirmation:
            speak("Where would you like me to search? Google, Wikipedia or YouTube?")
            answer4 = takecommand()
            if "google" in answer4:
                speak("I am now searching for " + text + " on Google")
                wb.get().open_new_tab("www.google.com/search?gx&q=" + text)

            elif "wikipedia" in answer4:
                speak(
                    "Would you like me to provide a summary or open the Wikipedia page for "
                    + text
                    + "?"
                )
                answer2 = takecommand()
                if "narrate" in answer2 or "direct" in answer2:
                    results = wikipedia.summary(text, sentences=1, auto_suggest=False)
                    speak("according to wikipedia " + results)
                elif (
                    "web page" in answer2
                    or "website" in answer2
                    or "webpage" in answer2
                ):
                    page1 = wikipedia.page(text, auto_suggest=False)
                    print(page1)
                    page2 = page1.url
                    print(page2)
                    speak("Redirecting you to the " + text + " Wikipedia page.")
                    webbrowser.get().open_new_tab(page2)
                    print(page2)
            elif "youtube" in answer4:
                speak("I am now searching for " + text + " on YouTube.")
                wb.get().open_new_tab(
                    "https://www.youtube.com/results?search_query=" + text
                )
        else:
            speak("Alright, let me know if you need anything else.")
