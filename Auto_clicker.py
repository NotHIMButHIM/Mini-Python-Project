import pyautogui
import time
import tkinter as tk
from threading import Thread
import keyboard

class AutoClickerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Auto Clicker")

        self.interval_var = tk.DoubleVar(value=1.0)
        self.running = False

        self.create_widgets()

    def create_widgets(self):
        interval_label = tk.Label(self.root, text="Interval (seconds):")
        interval_label.grid(row=0, column=0, padx=5, pady=5)

        interval_entry = tk.Entry(self.root, textvariable=self.interval_var)
        interval_entry.grid(row=0, column=1, padx=5, pady=5)

        start_button = tk.Button(self.root, text="Start (F6)", command=self.start_auto_clicker)
        start_button.grid(row=1, column=0, padx=5, pady=5)

        stop_button = tk.Button(self.root, text="Stop (F7)", command=self.stop_auto_clicker)
        stop_button.grid(row=1, column=1, padx=5, pady=5)

        self.root.bind("<F6>", lambda event: self.start_auto_clicker())
        self.root.bind("<F7>", lambda event: self.stop_auto_clicker())

    def start_auto_clicker(self):
        if not self.running:
            interval_seconds = self.interval_var.get()
            self.running = True
            self.auto_clicker_thread = Thread(target=self.auto_clicker, args=(interval_seconds,))
            self.auto_clicker_thread.start()

    def stop_auto_clicker(self):
        if self.running:
            self.running = False
            self.auto_clicker_thread.join()

    def auto_clicker(self, interval_seconds):
        try:
            while self.running:
                pyautogui.click()
                time.sleep(interval_seconds)
        except KeyboardInterrupt:
            pass

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = AutoClickerGUI()
    gui.run()
