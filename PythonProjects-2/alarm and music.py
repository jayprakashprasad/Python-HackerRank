"""import winsound
import time
from win10toast import ToastNotifier

def timer(message,minutes):
   #windows notification instantitor
   notificator = ToastNotifier()
   notificator.show_toast("Alarm",f"Alarm will go off in{minutes}minutes..",duration=10)

   time.sleep(minutes * 30)#pause script
   winsound.Beep(frequency=2500,duration=4000)#alarm sound
   notificator.show_toast(f"Alarm",message,duration=40)


if __name__ == "__main__":
    message="Post on github"
    minutes=1 #minutes
    timer(message,minutes)"""


#music
import winsound

def play_sound(frequency=3500, duration=5000):
    winsound.Beep(frequency, duration)

if __name__ == "__main__":
    frequency = 1000
    duration = 5000  # 5 sec
    play_sound(frequency, duration)
    play_sound()

