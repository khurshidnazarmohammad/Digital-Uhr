from tkinter import *
import time


window = Tk()
window.title('digital Uhr')
window.geometry('600*400')


def myTime():
    hour = time.strftime('%I')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    am_pm = time.strftime("%p")
    day = time.strftime("%A")
    zone = time.strftime("%z")

    myText = hour + ":" + minute + ":" + second + " " + am_pm
    myText2 = day + ", " + zone
    myLabel.config(text=myText)
    myLabel.after(1000, myTime)



myLabel = Label(window, text='HELLO WORLD',font=(
    'Arial', 72), fg='white', bg='green')
myLabel.pack()

myLabel2 = Label(window, text='',font=('Arial', 24))
myLabel2.pack()

myTime()

window.mainloop()