from tkinter import *
import time

window = Tk()
window.title("Digital Clock")
window.geometry("400x200")
window.config(bg="black")


def update_time():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %d %B %Y")

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    window.after(1000, update_time)


time_label = Label(
    window,
    font=("Arial", 40),
    fg="lime",
    bg="black"
)
time_label.pack(pady=10)

date_label = Label(
    window,
    font=("Arial", 14),
    fg="white",
    bg="black"
)
date_label.pack()

update_time()

window.mainloop()
