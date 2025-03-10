import time
import datetime
import pygame

class AlarmClock:
    def __init__(self, alarm_time, sound_file):
        self.alarm_time = alarm_time
        self.sound_file = sound_file
        self.is_running = True

    def start(self):
        print(f"Alarm set for {self.alarm_time}")
        while self.is_running:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time)

            if current_time == self.alarm_time:
                self.ring_alarm()

            time.sleep(1)

    def ring_alarm(self):
        print("Wake up booooy 👅")
        pygame.mixer.music.load(self.sound_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(1)

        self.is_running = False

if __name__ == "__main__":
    pygame.mixer.init()
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    
    #Change the sound file path if you want to change the music
    sound_file = "Projects/Alarm/Promise (Pragma Version).mp3"

    alarm_clock = AlarmClock(alarm_time, sound_file)
    alarm_clock.start()
