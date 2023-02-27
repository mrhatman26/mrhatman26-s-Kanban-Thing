import tkinter as t
from tkinter import *
from tkinter import font
from version_handler import version_read
from misc import out, outend

def gui_main():
    pname = "gui_main"
    outend(pname, "Creating main GUI")
    selected_proj = ""
    #Functions go here
    def list_select_update(event):
        global selected_proj
        select_proj = gui_project_frame_listbox.get(ACTIVE)
    resolution = "1280x720"
    title = "Kanbanthing - Main - " + version_read()
    window = t.Tk()
    window.title(title)
    window.geometry(resolution)
    window.resizable(False, False)
    gui_project_label = t.Label(window, text="Projects:", font=(font.nametofont("TkDefaultFont"), 25)).grid(row=0, column=0)
    gui_project_frame = t.Frame(window)
    gui_project_frame_listbox = t.Listbox(gui_project_frame, height=20, width=15, bg="white")
    gui_project_frame_listbox.insert(1, "Activity1")
    gui_project_frame_listbox.insert(2, "testproj")
    gui_project_frame_listbox.insert(3, "database")
    gui_project_frame_listbox.insert(4, "cpptest")
    gui_project_frame_listbox.insert(5, "etc")
    gui_project_frame_listbox.bind("<<ListboxSelect>>", list_select_update)
    gui_project_frame_listbox.pack()
    gui_project_frame.columnconfigure(0, weight=1)
    gui_project_frame.columnconfigure(1, weight=1)
    gui_project_frame.columnconfigure(2, weight=1)
    gui_project_frame.grid(row=1, column=0)
    window.mainloop()
