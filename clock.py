"""A simple live digital clock."""

import tkinter as tk
from datetime import datetime


class Clock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clock")
        self.geometry("420x280")
        self.minsize(320, 240)
        self.configure(bg="#101820")

        self.alarm_hour = None
        self.last_alarm_key = None
        self.alarm_ringing = False
        self.alarm_after_id = None

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

        alarm_frame = tk.Frame(self, bg="#101820")
        alarm_frame.pack(pady=(0, 4))

        tk.Label(
            alarm_frame,
            text="Alarm (HH):",
            font=("Segoe UI", 12),
            fg="#DCE3E8",
            bg="#101820",
        ).pack(side=tk.LEFT, padx=(0, 6))

        self.alarm_entry = tk.Entry(
            alarm_frame,
            width=3,
            font=("Segoe UI", 12),
            justify="center",
        )
        self.alarm_entry.pack(side=tk.LEFT, padx=(0, 8))

        tk.Button(
            alarm_frame,
            text="Set",
            command=self.set_alarm,
        ).pack(side=tk.LEFT, padx=(0, 6))

        tk.Button(
            alarm_frame,
            text="Stop",
            command=self.stop_alarm,
        ).pack(side=tk.LEFT)

        self.alarm_status_label = tk.Label(
            self,
            text="No alarm set",
            font=("Segoe UI", 10),
            fg="#DCE3E8",
            bg="#101820",
        )
        self.alarm_status_label.pack(pady=(2, 8))

        self.update_clock()

    def set_alarm(self):
        hour_text = self.alarm_entry.get().strip()
        if (
            len(hour_text) != 2
            or not hour_text.isascii()
            or not hour_text.isdigit()
            or not 0 <= int(hour_text) <= 23
        ):
            self.alarm_status_label.config(
                text="Enter a valid hour from 00 to 23"
            )
            return

        self.alarm_hour = int(hour_text)
        self.last_alarm_key = None
        self.stop_alarm()
        self.alarm_status_label.config(text=f"Alarm set for {hour_text}:00")

    def stop_alarm(self):
        if self.alarm_after_id is not None:
            self.after_cancel(self.alarm_after_id)
            self.alarm_after_id = None

        self.alarm_ringing = False
        self.alarm_status_label.config(text="Alarm stopped")

    def ring_alarm(self):
        if self.alarm_ringing:
            self.bell()
            self.alarm_after_id = self.after(1000, self.ring_alarm)

    def update_clock(self):
        now = datetime.now()
        self.time_label.config(text=now.strftime("%H:%M:%S"))
        self.date_label.config(text=now.strftime("%A, %B %d, %Y"))

        alarm_key = now.strftime("%Y-%m-%d-%H")
        if (
            self.alarm_hour == now.hour
            and self.last_alarm_key != alarm_key
        ):
            self.last_alarm_key = alarm_key
            self.alarm_ringing = True
            self.alarm_status_label.config(text="Alarm ringing - press Stop")
            self.ring_alarm()

        self.after(1000, self.update_clock)


if __name__ == "__main__":
    Clock().mainloop()