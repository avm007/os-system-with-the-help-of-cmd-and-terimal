import os
import pyttsx3 as ps

ps.speak("HEY!WARM WELCOME TO MY APPLICATION")
ps.speak("How Can AMIT Help You")

while True:

    p = input('Tell Me what u want! :')


    if ("don't" in p.lower() or 'not' in p.lower() or 'dont' in p.lower()):
         ps.speak('You denied Me to open Application')

    elif ('chrome' in p.lower() or 'browser' in p.lower()) and ('run' in p.lower() or 'open' in p.lower()):
        ps.speak("Opening Chrome")
        os.system('chrome')

    elif ('chrome' in p.lower() or 'browser' in p.lower()) and ('run' in p.lower() or 'open' in p.lower()):
        ps.speak("Opening Notepad")
        os.system('notepad')

    elif ('wmplayer' in p.lower() or 'media player' in p.lower() or 'music player' in p.lower()) and (
            'run' in p.lower() or 'open' in p.lower()):
        ps.speak("Opening Windows media player")
        os.system('wmplayer')

    elif ('zoom' in p.lower() or 'zoomapp' in p.lower() or 'video' in p.lower() or 'conferencing' in p.lower()) and (
            'run' in p.lower() or 'open' in p.lower()):
        ps.speak("Opening Zoom")
        os.system('zoom')

    elif ('paint' in p.lower() or 'mspaint' in p.lower() or 'draw' in p.lower()) and (
            'run' in p.lower() or 'open' in p.lower()):
        ps.speak("Opening Paint")
        os.system('mspaint')

    elif ('telegram' in p.lower() or 'telegram desktop' in p.lower() or 'telegram messenger' in p.lower()) and (
            'run' in p.lower() or 'open' in p.lower()):
        ps.speak("Opening Telegram")
        os.system('Telegram')

    elif ('whatsapp' in p.lower() or 'whatapp desktop' in p.lower() or 'whatsapp messenger' in p.lower()) and (
            'run' in p.lower() or 'open' in p.lower()):
        ps.speak("Opening WhatsApp")
        os.system('WhatsApp')

    elif ( 'firefox' in p.lower() or 'firefox browser' in p.lower() or 'mozilla' in p.lower() or 'mozilla firefox' in p.lower()) and (
            'run' in p.lower() or 'open' in p.lower()):
        ps.speak("Opening Firefox")
        os.system('Firefox')

    elif ('cmd' in p.lower() or 'command' in p.lower() or 'command prompt' in p.lower() or 'terminal' in p.lower()) and (
            'run' in p.lower() or 'open' in p.lower()):
        ps.speak("Opening Command prompt")
        os.system('cmd')

    elif ('control' in p.lower() or 'control panel' in p.lower() or 'settings' in p.lower()) and (
            'run' in p.lower() or 'open' in p.lower()):
        ps.speak("Opening control panel")
        os.system('control')

    elif ('git' in p.lower() or 'git bash' in p.lower() or 'bash' in p.lower()) and (
            'run' in p.lower() or 'open' in p.lower()):
        ps.speak("Opening Git Bash")
        os.system('git bash')

    elif ('quit' in p.lower() or 'exit' in p.lower()):
        ps.speak("GONNA MISS U!")
        ps.speak("BY THE WAY! Thank You,Please Visit Again")
        exit()
    else :
        ps.speak("Sorry,Please enter a valid Choice")