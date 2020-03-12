import datetime
import threading
import sys
import pygame

def ring_ring():
    pygame.init()
    pygame.mixer.init()
    sounda = pygame.mixer.Sound("/Users/leanne/Downloads/test.wav")
    sounda.play()
    # sys.stdout.write('ring ring\n')
    sys.stdout.flush()

class Clock:

    def __init__(self):
        self.alarm_time = None
        self._alarm_thread = None
        self.update_interval = 1
        self.event = threading.Event()

    def run(self):
        while True:
            self.event.wait(self.update_interval)
            if self.event.isSet():
                break
            now = datetime.datetime.now()
            if self._alarm_thread and self._alarm_thread.is_alive():
                alarm_symbol = '+'
                # print('yes: ')
            else:
                alarm_symbol = ' '
            sys.stdout.write("\r%02d:%02d:%02d %s"
                % (now.hour, now.minute, now.second, alarm_symbol))
            sys.stdout.flush()

    def set_alarm(self, hour, minute):
        now = datetime.datetime.now()
        print('now', now)
        alarm = now.replace(hour=int(hour), minute=int(minute))
        print('alarm',alarm) #alarm shows the current time now.
        delta = int((alarm - now).total_seconds())
        print('delta',delta)
        if delta <= 0:
            alarm = alarm.replace(day=alarm.day + 1)
            # print('delta.alarm',alarm)
            delta = int((alarm - now).total_seconds())
            # print('delta.delta', delta)
        if self._alarm_thread:
            self._alarm_thread.cancel()
            # print('self',self._alarm_thread.cancel())
        self._alarm_thread = threading.Timer(delta, ring_ring)
        self._alarm_thread.daemon = True
        self._alarm_thread.start()

clock = Clock()
#clock.set_alarm('13','40')
clock.set_alarm(sys.argv[1], sys.argv[2])
clock.run()
