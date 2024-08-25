import time

class Timer:
    def __init__(self, seconds):
        self.seconds = seconds

    def start(self):
        self.start_time = time.time()

    def is_expired(self):
        if time.time() - self.start_time >= self.seconds:
            return True
        return False