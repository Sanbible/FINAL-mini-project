import tkinter as tk
from tkinter import *
import customtkinter
from yum import game_othello
from yum import game_othellopva

def open_pvp():
    game_othello() 

def open_pva():
    game_othellopva()

class window:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Othello")
        self.root.geometry("300x250")
        self.label = tk.Label(self.root, text="WELCOME TO OTHELLO", fg = 'Black', font=('Comic Sans MS', 18))
        self.label.grid(row=5, column=2, pady=5, padx=5, sticky=tk.NS)
        self.label = tk.Label(self.root, text="GAME MODE", fg = 'Black', font=('Comic Sans MS', 14))
        self.label.grid(row=10, column=2, pady=5, padx=5, sticky=tk.NS)
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("green")
        self.pvp_button = customtkinter.CTkButton(self.root, text="PvP", font=('Comic Sans MS', 20) , command=open_pvp)   
        self.pvp_button.grid(row=15, column=2, padx=5, pady=20)
        customtkinter.set_default_color_theme("green")
        self.pva_button = customtkinter.CTkButton(self.root, text="PvA", font=('Comic Sans MS', 20) ,command=open_pva)
        self.pva_button.grid(row=20, column=2, padx=20, pady=5)
        self.root.mainloop()

window()