import os
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # hide main window

messagebox.showinfo("Message", "This is a popup message!")
os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")