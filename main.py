from tkinter import *
import time


class DigitalClock:
    def init(self, root):
        self.root = root
        self.root.title("Digital Clock 🕒")
        self.root.geometry("450x200")
        self.root.config(bg="#0f172a")

        # Uhr
        self.time_label = Label(
            root,
            font=("Arial", 40, "bold"),
            fg="#00ffb3",
            bg="#0f172a"
        )
        self.time_label.pack(pady=10)

        # Datum
        self.date_label = Label(
            root,
            font=("Arial", 16),
            fg="white",
            bg="#0f172a"
        )
        self.date_label.pack()

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%A, %d %B %Y")

        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)

        self.root.after(1000, self.update_clock)


if name == "main":
    root = Tk()
    app = DigitalClock(root)
    root.mainloop()
