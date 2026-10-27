"""A simple live digital clock."""

import tkinter as tk
from datetime import datetime


class Clock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clock")
        self.geometry("420x220")
        self.minsize(320, 180)
        self.configure(bg="#101820")

        self.time_label = tk.Label(
            self,
            font=("Segoe UI", 52, "bold"),
            fg="#FEE715",
            bg="#101820",
        )
        self.time_label.pack(expand=True, pady=(24, 0))

        self.date_label = tk.Label(
            self,
            font=("Segoe UI", 16),
            fg="#DCE3E8",
            bg="#101820",
        )
        self.date_label.pack(pady=(0, 28))

        self.update_clock()

    def update_clock(self):
        now = datetime.now()
        self.time_label.config(text=now.strftime("%H:%M:%S"))
        self.date_label.config(text=now.strftime("%A, %B %d, %Y"))
        self.after(1000, self.update_clock)


if __name__ == "__main__":
    Clock().mainloop()