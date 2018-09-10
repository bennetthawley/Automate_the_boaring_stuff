import webbrowser
import sys
import pyperclip

sys.argv

#Check for cmd line args
if len(sys.argv) > 1:
    #List object of cmd line args
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

#https://www.google.com/maps/place/
webbrowser.open('https://www.google.com/maps/place/' + address)

