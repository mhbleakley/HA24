import time

class Timer:
    def __init__(self, seconds):
        self.seconds = seconds
        self.expired = False

    def start(self):
        self.expired = False
        self.start_time = time.time()

    def is_expired(self):
        if time.time() - self.start_time >= self.seconds:
            self.expired = True
        self.expired = False