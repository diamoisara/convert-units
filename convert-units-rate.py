from tkinter import *
# Creating a GUI Window
window = Tk()
def from_cubicmeterhour():
    daily_cubicmeter = float(e2_value.get())*24
    daily_cubicfeet = float(e2_value.get())*847.55200131573
    dailybarrel = float(e2_value.get())*150.955
    t1.delete("1.0",END)
    t1.insert(END, daily_cubicmeter)
    t2.delete("1.0", END)
    t2.insert(END, daily_cubicfeet)
    t3.delete("1.0", END)
    t3.insert(END, dailybarrel)

e1 = Label(window, text="Input the rate in m3/h ")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text="daily_cubicmeter")
e4 = Label(window, text="daily_cubicfeet")
e5 = Label(window, text="dailybarrel")

t1 = Text(window, height=5, width=30)
t2 = Text(window, height=5, width=30)
t3 = Text(window, height=5, width=30)

b1 = Button(window, text="Convert", command=from_cubicmeterhour)

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)

window.mainloop()
