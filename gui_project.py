import tkinter as t
from tkinter import *
from tkinter import font
from version_handler import version_read
from misc import out, outend

def gui_project():
    pname = "gui_project"
    title = "Kanbanthing - Activity1 - " + version_read() #CHANGE THIS TO SHOW PROJECT NAME!
    window = t.Tk()
    window.title(title)
    window.geometry("846x720")
    window.resizable(False, False)
    gui_todo_label = t.Label(window, text="To Do:", font=("Segoe UI", 25)).place(x=10, y=10)
    gui_doing_label = t.Label(window, text="Doing:", font=("Segoe UI", 25)).place(x=300, y=10)
    gui_done_label = t.Label(window, text="Done:", font=("Segoe UI", 25)).place(x=590, y=10)
    gui_todo_listbox = t.Listbox(window, height=30, width=40, bg="white")
    gui_todo_listbox.place(x=10, y=65)
    gui_doing_listbox = t.Listbox(window, height=30, width=40, bg="white")
    gui_doing_listbox.place(x=300, y=65)
    gui_done_listbox = t.Listbox(window, height=30, width=40, bg="white")
    gui_done_listbox.place(x=590, y=65)
    gui_button_move_back = t.Button(window, text="<<", width=21, font=("Segoe UI", 12)).place(anchor="center", x=133, y=575)
    gui_button_move_forward = t.Button(window, text=">>", width=21, font=("Segoe UI", 12)).place(anchor="center", x=713, y=575)
    gui_button_add = t.Button(window, text="Add", width=21, font=("Segoe UI", 12)).place(anchor="center", x=423, y=575)
    gui_button_clear = t.Button(window, text="Clear", width=21, font=("Segoe UI", 12)).place(anchor="center", x=423, y=635)
    gui_button_back = t.Button(window, text="Back", width=21, font=("Segoe UI", 12)).place(anchor="center", x=423, y=695)
    window.mainloop()
    return False
