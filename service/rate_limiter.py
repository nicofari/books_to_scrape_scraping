import time


class SimpleRateLimiter:
    def __init__(self, interval, verbose):
        self.interval = interval
        self.verbose = verbose

    def run(self):
        if self.verbose:
            print(f'Wait {self.interval}')
        time.sleep(self.interval)
