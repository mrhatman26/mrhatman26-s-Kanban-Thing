import tkinter as t
from tkinter import *
from tkinter import font
from version_handler import version_read
from misc import out, outend

def gui_main():
    pname = "gui_main"
    out(pname, "Displaying main GUI")
    selected_proj = ""
    global rval
    rval = True
    #Functions go here
    def list_select_update(event):
        global selected_proj
        select_proj = gui_project_listbox.get(ACTIVE)
    def button_exit():
        global rval
        rval = False
        window.destroy()
        print("rval = " + str(rval))
    resolution = "680x720"
    title = "Kanbanthing - Main - " + version_read()
    window = t.Tk()
    window.title(title)
    window.geometry(resolution)
    window.resizable(False, False)
    gui_project_label = t.Label(window, text="Projects:", font=("Segoe UI", 25)).place(x=10, y=10)#.grid(row=0, column=0)
    gui_project_listbox = t.Listbox(window, height=40, width=60, bg="white")
    gui_project_listbox.insert(1, "Activity1") #Add function here for collecting ALL saved projects
    gui_project_listbox.insert(2, "testproj")
    gui_project_listbox.insert(3, "database")
    gui_project_listbox.insert(4, "cpptest")
    gui_project_listbox.insert(5, "etc")
    gui_project_listbox.bind("<<ListboxSelect>>", list_select_update)
    gui_project_listbox.place(x=10, y=65)
    gui_new_button = t.Button(window, text="New Project", width=21, font=("Segoe UI", 12)).place(x=470, y=60)
    gui_load_button = t.Button(window, text="Load Project", width=21, font=("Segoe UI", 12)).place(x=470, y= 110)
    gui_about_button = t.Button(window, text="About", width=21, font=("Segoe UI", 12)).place(x=470, y=160)
    gui_help_button = t.Button(window, text="Help", width=21, font=("Segoe UI", 12)).place(x=470, y=210)
    gui_exit_button = t.Button(window, text="Exit", width=21, font=("Segoe UI", 12), command=button_exit).place(x=470, y=671)
    window.mainloop()
    out(pname, "Exiting back to main.py with run = " + str(rval))
    return rval
