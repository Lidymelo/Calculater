from tkinter import *
from tkinter import ttk

color1 = "#292727" 
color2 = "#faf5f5" 
color3 = "#484759" 
color4 = "#e7e6f5" 
color5 = "#d65f1a" 


window =Tk()
window.title("Calculadora")
window.geometry("235x318")
window.config(bg=color1) 


frame_screen = Frame(window, width=235, height=50, bg=color3)
frame_screen.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=268)
frame_body.grid(row=1, column=0)


all_values = ''

text_value = StringVar()

def entry_value(event):

    global all_values

    all_values = all_values + str(event)




    text_value.set(all_values)


def calculate():
    result = eval(all_values)
    text_value.set(str(result))

def clean_screen():
    global all_values
    all_values = ""
    text_value.set("")




app_label = Label(frame_screen, textvariable=text_value, width= 15,height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font='Ivy 19', bg=color3, fg=color2)
app_label.place(x=0, y=0)

b_1 = Button(frame_body, command = clean_screen, text="C", width=11, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=1) 
b_2 = Button(frame_body, command = lambda: entry_value('%'), text="%", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=1)
b_3 = Button(frame_body, command = lambda: entry_value('/'), text="/", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=1)
b_4 = Button(frame_body, command = lambda: entry_value('7'), text="7", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=55)
b_5 = Button(frame_body, command = lambda: entry_value('8'), text="8", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=55)
b_6 = Button(frame_body, command = lambda: entry_value('9'), text="9", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=55)
b_7 = Button(frame_body, command = lambda: entry_value('*'), text="*", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=55)
b_8 = Button(frame_body, command = lambda: entry_value('4'), text="4", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=109)
b_9 = Button(frame_body, command = lambda: entry_value('5'), text="5", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=109)
b_10 = Button(frame_body, command = lambda: entry_value('6'), text="6", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=120, y=109)
b_11 = Button(frame_body, command = lambda: entry_value('+'), text="+", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=109)
b_12 = Button(frame_body, command = lambda: entry_value('1'), text="1", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=163)
b_13 = Button(frame_body, command = lambda: entry_value('2'), text="2", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=163)
b_14 = Button(frame_body, command = lambda: entry_value('3'), text="3", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=163)
b_15 = Button(frame_body, command = lambda: entry_value('-'), text="-", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=163)
b_16 = Button(frame_body, command = lambda: entry_value('0'), text="0", width=11, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=217)
b_17 = Button(frame_body, command = lambda: entry_value(','), text=",", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=217)
b_18 = Button(frame_body, command = calculate, text="=", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=217)




window.mainloop()





