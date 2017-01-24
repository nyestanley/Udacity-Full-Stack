import time
import webbrowser


i = 1

while i < 4:
    time.sleep(10)
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    #open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    i = i+1
