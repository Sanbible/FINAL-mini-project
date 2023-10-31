import tkinter as tk
from tkinter import PhotoImage
from tkinter import *
import customtkinter
from time import *
import random
from tkinter import messagebox
 
"""

ชื่อผู้จัดทำ 

นางสาวนวพร ทรายงาม รหัสนักศึกษา 6601012610059
นายรพีพงศ์ กุลศรีวัฒนา รหัสนักศึกษา 6601012610121


ชื่อที่ปรึกษาโครงงาน

นายศุภวิชญ์ สุขแดง รหัสนักศึกษา 6601012610164
กานต์ สุขสมกิจ รหัสนักศึกษา 6601012620011
นายชัยพล พรหมชาติ รหัสนักศึกษา 6601012630025
นายรัตนชัย เมธา รหัสนักศึกษา 6601012630084

"""

class game_othello:
    
    def __init__(self):
        self.root =tk.Toplevel(bg="#A2C19F")
        self.root.wm_geometry("900x475")
        self.bg = PhotoImage(file="bg.png") # "pyimage1"
        self.tb = PhotoImage(file="blackbg.png") # "pyimage2"
        self.tw = PhotoImage(file="whitebg.png") # "pyimage3"
        self.ck = PhotoImage(file="markk.png") # "pyimage4"
        self.gw = PhotoImage(file="globlawhite.png")
        self.tsw = PhotoImage(file="turnwhite.png")
        self.gb = PhotoImage(file="globalblack.png")
        self.tsb = PhotoImage(file="turnblack.png")
        self.another = "pyimage2"
        self.current = "pyimage3"
        self.check_coin_white = IntVar()
        self.check_coin_black = IntVar()
        self.check_coin_white.set(2)
        self.check_coin_black.set(2)
        self.time=StringVar()
        self.time.set(value="00:00:00")
        self.time_running = 0
        self.after_code = None
        self.TimeTicking()
        self.table = self.board()
        self.mark1() 
        self.marker()
        self.root.mainloop()

    def reset_game(self):
        for i in range(8):
            for j in range(8):
                self.table[i][j]["image"] = "pyimage1"
        self.time.set(value="00:00:00")
        self.time_running = 0
        self.mark1()
        self.current = "pyimage3"  # Reset the turn to white
        self.another = "pyimage2"  # Reset the other player's disk
        self.check_coin()
        self.marker()

    def board(self):
        boardall = []
        for row0 in range(8):
            board = []
            for column0 in range(8):
                button = tk.Button(self.root, image=self.bg)
                board.append(button)
                button.grid(row=row0+1, column=column0+1)
            boardall.append(board)
            tk.Label(self.root, text=chr(65+row0),bg="#A2C19F").grid(row=0, column=row0+1)
            tk.Label(self.root, text=(row0+1),bg="#A2C19F").grid(row=row0+1, column=0)

        blackpic = tk.Label(self.root,image=self.gb,bg="#A2C19F")
        blackpic.place(x=600,y=100)
        whitepic = tk.Label(self.root,image=self.tsw,bg="#A2C19F")
        whitepic.place(x=600,y=200)
        scoreblack = tk.Label(self.root,textvariable=self.check_coin_black,font=('Comic Sans MS', 20),fg="#000000",bg="#A2C19F")
        scoreblack.place(x=750,y=120)
        scorewhite = tk.Label(self.root,textvariable=self.check_coin_white,font=('Comic Sans MS', 20),fg="#000000",bg="#A2C19F")
        scorewhite.place(x=750,y=220)
        tk.Label(self.root,text="PvP MODE",font=('Comic Sans MS', 20),fg="#000000",bg="#A2C19F").place(x=635,y=40)
        tk.Label(self.root,textvariable=self.time,font=('Comic Sans MS', 20),fg="#000000",bg="#A2C19F").place(x=635,y=300)
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("blue")
        self.reset_button = customtkinter.CTkButton(self.root, text="Reset", font=('Comic Sans MS', 20) , command=lambda: self.reset_game()).place(x=625,y=380)
        
        return boardall

    def mark1(self):
        self.table[3][3]["image"]=self.tb
        self.table[3][4]["image"]=self.tw
        self.table[4][3]["image"]=self.tw
        self.table[4][4]["image"]=self.tb
        
    
    def marker(self): # ฟังก์ชันเช็คว่าสามารถวางจุดไหนได้บ้างแล้ว mark มัน
        for i in range(8):
            for j in range(8):
                if self.table[i][j]["image"] == self.another:
                    self.c_maker_top(i, j)
                    self.c_maker_bottom(i, j)
                    self.c_maker_left(i, j)
                    self.c_maker_right(i, j)
                    self.c_maker_top_left(i, j)
                    self.c_maker_top_right(i, j)
                    self.c_maker_bottom_left(i, j)
                    self.c_maker_bottom_right(i, j)

        if not self.has_valid_moves():
            self.check_game_over()

# ref นายศุภวิชญ์ สุขแดง , กานต์ สุขสมกิจ
    def c_maker_top(self,r,c): 
        for nrow in range(r-1,-1,-1):
            if self.table[nrow][c]["image"] == "pyimage1" or self.table[nrow][c]["image"] == "pyimage4":
                break
            elif self.table[nrow][c]["image"] == self.another:
                continue
            elif self.table[nrow][c]["image"] == self.current:    
                for irow in range(r+1,8): 
                    if self.table[irow][c]["image"] == "pyimage1":
                        self.table[irow][c]["image"] = "pyimage4"
                        self.table[irow][c].bind("<Button-1>",self.play_thegame)
                        break
                    elif self.table[irow][c]["image"] == "pyimage4":
                        break
                    elif self.table[irow][c]["image"] == self.current or self.table[irow][c]["image"] == "pyimage4":
                        break
                    elif self.table[irow][c]["image"] == self.another:
                        continue
    
    def c_maker_bottom(self,r,c):
        for nrow in range(r+1,8):
            if self.table[nrow][c]["image"] == "pyimage1" or self.table[nrow][c]["image"] == "pyimage4":
                break
            elif self.table[nrow][c]["image"] == self.another:
                continue
            elif self.table[nrow][c]["image"] == self.current:
                for irow in range(r-1,-1,-1):
                    if self.table[irow][c]["image"] == "pyimage1":
                        self.table[irow][c]["image"] = "pyimage4"
                        self.table[irow][c].bind("<Button-1>",self.play_thegame)
                        break
                    elif self.table[irow][c]["image"] == "pyimage4":
                        break
                    elif self.table[irow][c]["image"] == self.current or self.table[irow][c]["image"] == "pyimage4":
                        break
                    elif self.table[irow][c]["image"] == self.another:
                        continue

    def c_maker_left(self,r,c):
        for ncolumn in range(c-1,-1,-1):
            if self.table[r][ncolumn]["image"] == "pyimage1" or self.table[r][ncolumn]["image"] == "pyimage4":
                break
            elif self.table[r][ncolumn]["image"] == self.another:
                continue
            elif self.table[r][ncolumn]["image"] == self.current:
                for icolumn in range(c+1,8):
                    if self.table[r][icolumn]["image"] == "pyimage1":
                        self.table[r][icolumn]["image"] = "pyimage4"
                        self.table[r][icolumn].bind("<Button-1>",self.play_thegame)
                        break
                    elif self.table[r][icolumn]["image"] == "pyimage4":
                        break
                    elif self.table[r][icolumn]["image"] == self.current or self.table[r][icolumn]["image"] == "pyimage4":
                        break
                    elif self.table[r][icolumn]["image"] == self.another:
                        continue

    def c_maker_right(self,r,c):
        for ncolumn in range(c+1,8):
            if self.table[r][ncolumn]["image"] == "pyimage1" or self.table[r][ncolumn]["image"] == "pyimage4":
                break
            elif self.table[r][ncolumn]["image"] == self.another:
                continue
            elif self.table[r][ncolumn]["image"] == self.current:
                for icolumn in range(c-1,-1,-1):
                    if self.table[r][icolumn]["image"] == "pyimage1":
                        self.table[r][icolumn]["image"] = "pyimage4"
                        self.table[r][icolumn].bind("<Button-1>",self.play_thegame)
                        break
                    elif self.table[r][icolumn]["image"] == "pyimage4":
                        break
                    elif self.table[r][icolumn]["image"] == self.current or self.table[r][icolumn]["image"] == "pyimage4":
                        break
                    elif self.table[r][icolumn]["image"] == self.another:
                        continue

    def c_maker_top_left(self, r, c):
        for n in range(1, min(r, c)):
            if self.table[r - n][c - n]["image"] == "pyimage1" or self.table[r - n][c - n]["image"] == "pyimage4":
                break
            elif self.table[r - n][c - n]["image"] == self.another:
                continue
            elif self.table[r - n][c - n]["image"] == self.current:
                for i in range(1, min(7 - r, 7 - c)+1):
                    if self.table[r + i][c + i]["image"] == "pyimage1":
                        self.table[r + i][c + i]["image"] = "pyimage4"
                        self.table[r + i][c + i].bind("<Button-1>", self.play_thegame)
                        break
                    elif self.table[r + i][c + i]["image"] == "pyimage4":
                        break
                    elif self.table[r + i][c + i]["image"] == self.current or self.table[r + i][c + i]["image"] == "pyimage4":
                        break
                    elif self.table[r + i][c + i]["image"] == self.another:
                        continue

    def c_maker_top_right(self, r, c):
        for n in range(1, min(r, 7 - c) ):
            if self.table[r - n][c + n]["image"] == "pyimage1" or self.table[r - n][c + n]["image"] == "pyimage4":
                break
            elif self.table[r - n][c + n]["image"] == self.another:
                continue
            elif self.table[r - n][c + n]["image"] == self.current:
                for i in range(1, min(7 - r, c )+1):
                    if self.table[r + i][c - i]["image"] == "pyimage1":
                        self.table[r + i][c - i]["image"] = "pyimage4"
                        self.table[r + i][c - i].bind("<Button-1>", self.play_thegame)
                        break
                    elif self.table[r + i][c - i]["image"] == "pyimage4":
                        break
                    elif self.table[r + i][c - i]["image"] == self.current or self.table[r + i][c - i]["image"] == "pyimage4":
                        break
                    elif self.table[r + i][c - i]["image"] == self.another:
                        continue

    def c_maker_bottom_left(self, r, c):
        for n in range(1, min(7 - r, c) ):
            if self.table[r + n][c - n]["image"] == "pyimage1" or self.table[r + n][c - n]["image"] == "pyimage4":
                break
            elif self.table[r + n][c - n]["image"] == self.another:
                continue
            elif self.table[r + n][c - n]["image"] == self.current:
                for i in range(1, min(r , 7 - c)+1):
                    if self.table[r - i][c + i]["image"] == "pyimage1":
                        self.table[r - i][c + i]["image"] = "pyimage4"
                        self.table[r - i][c + i].bind("<Button-1>", self.play_thegame)
                        break
                    elif self.table[r - i][c + i]["image"] == "pyimage4":
                        break
                    elif self.table[r - i][c + i]["image"] == self.current or self.table[r - i][c + i]["image"] == "pyimage4":
                        break
                    elif self.table[r - i][c + i]["image"] == self.another:
                        continue

    def c_maker_bottom_right(self, r, c):
        for n in range(1, min(7 - r, 7 - c) ):
            if self.table[r + n][c + n]["image"] == "pyimage1" or self.table[r + n][c + n]["image"] == "pyimage4":
                break
            elif self.table[r + n][c + n]["image"] == self.another:
                continue
            elif self.table[r + n][c + n]["image"] == self.current:
                for i in range(1, min(r , c )+1):
                    if self.table[r - i][c - i]["image"] == "pyimage1":
                        self.table[r - i][c - i]["image"] = "pyimage4"
                        self.table[r - i][c - i].bind("<Button-1>", self.play_thegame)
                        break
                    elif self.table[r - i][c - i]["image"] == "pyimage4":
                        break
                    elif self.table[r - i][c - i]["image"] == self.current or self.table[r - i][c - i]["image"] == "pyimage4":
                        break
                    elif self.table[r - i][c - i]["image"] == self.another:
                        continue

    def play_thegame(self, event): # ฟังก์ชันการเล่นเกม ได้แก่ การกิน การเดิน การสลับสี 
        clicker = event.widget
        clicker["image"] = self.current
        for k in range(8):
            if clicker in self.table[k]:
                o = self.table[k].index(clicker)
                break
        self.play_top(k,o)
        self.play_bottom(k,o)
        self.play_left(k,o)
        self.play_right(k,o)
        self.play_top_left(k,o)
        self.play_top_right(k,o)
        self.play_bottom_left(k,o)
        self.play_bottom_right(k,o)

        for i in range(8):
            for j in range(8):
                self.table[i][j].unbind("<Button-1>")
                if self.table[i][j]["image"] == "pyimage4":
                    self.table[i][j]["image"] = "pyimage1"

        
        self.current= "pyimage2" if self.current == "pyimage3" else "pyimage3"
        self.another= "pyimage3" if self.another == "pyimage2" else "pyimage2"

       
        self.check_coin()

        if self.current == "pyimage3":
            tk.Label(self.root,image=self.tsw,bg="#A2C19F").place(x=600,y=200)
            tk.Label(self.root,image=self.gb,bg="#A2C19F").place(x=600,y=100)
            
        elif self.current == "pyimage2" :
            tk.Label(self.root,image=self.gw,bg="#A2C19F").place(x=600,y=200)
            tk.Label(self.root,image=self.tsb,bg="#A2C19F").place(x=600,y=100)
        
        self.marker()
        
    def play_top(self,r,c):
            memory = []
            for nrow in range(r-1,-1,-1):
                if self.table[nrow][c]["image"] == "pyimage1" or self.table[nrow][c]["image"] == "pyimage4":
                    break
                elif self.table[nrow][c]["image"] == self.another:
                    memory.append([nrow,c])
                    continue
                elif self.table[nrow][c]["image"] == self.current:
                    for i in memory:
                        self.table[i[0]][i[1]]["image"] = self.current
                    break

    def play_bottom(self,r,c):
        memory = []
        for nrow in range(r+1,8):
            if self.table[nrow][c]["image"] == "pyimage1" or self.table[nrow][c]["image"] == "pyimage4":
                break
            elif self.table[nrow][c]["image"] == self.another:
                memory.append([nrow,c])
                continue
            elif self.table[nrow][c]["image"] == self.current:
                for i in memory:
                    self.table[i[0]][i[1]]["image"] = self.current
                break        

    def play_left(self,r,c):
        memory = []
        for ncolumn in range(c-1,-1,-1):
            if self.table[r][ncolumn]["image"] == "pyimage1" or self.table[r][ncolumn]["image"] == "pyimage4":
                break
            elif self.table[r][ncolumn]["image"] == self.another:
                memory.append([r,ncolumn])
                continue
            elif self.table[r][ncolumn]["image"] == self.current:
                for i in memory:
                    self.table[i[0]][i[1]]["image"] = self.current
                break
    
    def play_right(self,r,c):
        memory = []
        for ncolumn in range(c+1,8):
            if self.table[r][ncolumn]["image"] == "pyimage1" or self.table[r][ncolumn]["image"] == "pyimage4":
                break
            elif self.table[r][ncolumn]["image"] == self.another:
                memory.append([r,ncolumn])
                continue
            elif self.table[r][ncolumn]["image"] == self.current:
                for i in memory:
                    self.table[i[0]][i[1]]["image"] = self.current
                break
    
    def play_top_left(self, r, c):
        memory = []
        for n in range(1, min(r, c) ):
            if self.table[r - n][c - n]["image"] == "pyimage1" or self.table[r - n][c - n]["image"] == "pyimage4":
                break
            elif self.table[r - n][c - n]["image"] == self.another:
                memory.append([r - n,c - n])
                continue
            elif self.table[r - n][c - n]["image"] == self.current:
                for i in memory:
                    self.table[i[0]][i[1]]["image"] = self.current
                break
    
    def play_top_right(self, r, c):
        memory = []
        for n in range(1, min(r, 7 - c) ):
            if self.table[r - n][c + n]["image"] == "pyimage1" or self.table[r - n][c + n]["image"] == "pyimage4":
                break
            elif self.table[r - n][c + n]["image"] == self.another:
                memory.append([r - n,c + n])
                continue
            elif self.table[r - n][c + n]["image"] == self.current:
                for i in memory:
                    self.table[i[0]][i[1]]["image"] = self.current
                break
    
    def play_bottom_left(self, r, c):
        memory = []
        for n in range(1, min(7 - r, c) ):
            if self.table[r + n][c - n]["image"] == "pyimage1" or self.table[r + n][c - n]["image"] == "pyimage4":
                break
            elif self.table[r + n][c - n]["image"] == self.another:
                memory.append([r + n,c - n])
                continue
            elif self.table[r + n][c - n]["image"] == self.current:
                for i in memory:
                    self.table[i[0]][i[1]]["image"] = self.current
                break
    
    def play_bottom_right(self, r, c):
        memory = []
        for n in range(1, min(7 - r, 7 - c) ):
            if self.table[r + n][c + n]["image"] == "pyimage1" or self.table[r + n][c + n]["image"] == "pyimage4":
                break
            elif self.table[r + n][c + n]["image"] == self.another:
                memory.append([r + n,c + n])
                continue
            elif self.table[r + n][c + n]["image"] == self.current:
                for i in memory:
                    self.table[i[0]][i[1]]["image"] = self.current
                break

    def TimeTicking(self):      
        converted = strftime("%H:%M:%S", gmtime(self.time_running)) # convert seconds to hour:minute:second
        self.time.set(converted) # change time display
        self.time_running += 1
        self.after_code = self.root.after(1000, self.TimeTicking)

    def StopTimer(self):
        global after_code
        if after_code is not None:
            self.root.after_cancel(after_code)
            after_code = None


    def check_coin(self): # นับตัวหมาก
        self.scorewhite = 0
        self.scoreblack = 0
        for i in range (8):
            for j in range(8):
                if self.table[i][j]["image"] == "pyimage3":
                    self.scorewhite += 1 
                elif self.table[i][j]["image"] == "pyimage2":
                    self.scoreblack += 1
        self.check_coin_black.set(self.scoreblack)
        self.check_coin_white.set(self.scorewhite)

    def check_game_over(self):
        black_moves = 0
        white_moves = 0

        # Count the number of valid moves for both players
        for i in range(8):
            for j in range(8):
                if self.table[i][j]["image"] == "pyimage4":
                    if self.current == "pyimage2":
                        black_moves += 1
                    elif self.current == "pyimage3":
                        white_moves += 1

    # Check if no more valid moves for both players
        if black_moves == 0 and white_moves == 0:
            if self.check_coin_black.get() > self.check_coin_white.get() and self.check_coin_black.get()+self.check_coin_white.get()!=64:
                winner = "Black Player Because no more valid moves"
            elif self.check_coin_black.get() < self.check_coin_white.get() and self.check_coin_black.get()+self.check_coin_white.get()!=64:
                winner = "White Player Because no more valid moves"
            elif self.check_coin_black.get() < self.check_coin_white.get():
                winner = "White Player"
            elif self.check_coin_black.get() > self.check_coin_white.get() :
                winner = "Black Player"
            else:
                winner = "It's a Tie!"
            messagebox.showinfo("Game Over", f"The winner is {winner}!")
    
    def has_valid_moves(self):
        for i in range(8):
            for j in range(8):
                if self.table[i][j]["image"] == "pyimage4":
                    return True

        return False





class game_othellopva:

    def __init__(self):
        self.root =tk.Toplevel(bg="#A2C19F")
        self.root.wm_geometry("900x475") 
        self.bg = PhotoImage(file="bg.png") # "pyimage1"
        self.tb = PhotoImage(file="blackbg.png") # "pyimage2"
        self.tw = PhotoImage(file="whitebg.png") # "pyimage3"
        self.ck = PhotoImage(file="markk.png") # "pyimage4"
        self.gw = PhotoImage(file="globlawhite.png")
        self.tsw = PhotoImage(file="turnwhite.png")
        self.gb = PhotoImage(file="globalblack.png")
        self.tsb = PhotoImage(file="turnblack.png")
        self.another = "pyimage2"
        self.current = "pyimage3"
        self.check_coin_white = IntVar()
        self.check_coin_black = IntVar()
        self.check_coin_white.set(2)
        self.check_coin_black.set(2)
        self.time=StringVar()
        self.time.set(value="00:00:00")
        self.time_running = 0
        self.after_code = None
        self.TimeTicking()
        self.game_loop()
        self.table = self.board()
        self.mark1() 
        self.marker()
        self.root.mainloop()

    def reset_game(self):
        for i in range(8):
            for j in range(8):
                self.table[i][j]["image"] = "pyimage1"
        self.time.set(value="00:00:00")
        self.time_running = 0
        self.mark1()
        self.current = "pyimage3"  # Reset the turn to white
        self.another = "pyimage2"  # Reset the other player's disk
        self.check_coin()
        self.marker()

        

    def board(self):
        boardall = []
        for row0 in range(8):
            board = []
            for column0 in range(8):
                button = tk.Button(self.root, image=self.bg)
                board.append(button)
                button.grid(row=row0+1, column=column0+1)
            boardall.append(board)
            tk.Label(self.root, text=chr(65+row0),bg="#A2C19F").grid(row=0, column=row0+1)
            tk.Label(self.root, text=(row0+1),bg="#A2C19F").grid(row=row0+1, column=0)

        blackpic = tk.Label(self.root,image=self.gb,bg="#A2C19F")
        blackpic.place(x=600,y=100)
        whitepic = tk.Label(self.root,image=self.tsw,bg="#A2C19F")
        whitepic.place(x=600,y=200)
        scoreblack = tk.Label(self.root,textvariable=self.check_coin_black,font=('Comic Sans MS', 20),fg="#000000",bg="#A2C19F")
        scoreblack.place(x=750,y=120)
        scorewhite = tk.Label(self.root,textvariable=self.check_coin_white,font=('Comic Sans MS', 20),fg="#000000",bg="#A2C19F")
        scorewhite.place(x=750,y=220)
        tk.Label(self.root,text="PvA MODE",font=('Comic Sans MS', 20),fg="#000000",bg="#A2C19F").place(x=635,y=40)
        tk.Label(self.root,textvariable=self.time,font=('Comic Sans MS', 20),fg="#000000",bg="#A2C19F").place(x=635,y=300)   
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("blue")
        self.reset_button = customtkinter.CTkButton(self.root, text="Reset", font=('Comic Sans MS', 20) , command=lambda: self.reset_game()).place(x=625,y=380)

        return boardall

    def mark1(self):
        self.table[3][3]["image"]=self.tb
        self.table[3][4]["image"]=self.tw
        self.table[4][3]["image"]=self.tw
        self.table[4][4]["image"]=self.tb
    
    def marker(self): # ฟังก์ชันเช็คว่าสามารถวางจุดไหนได้บ้างแล้ว mark
        for i in range(8):
            for j in range(8):
                if self.table[i][j]["image"] == self.another:
                    self.c_maker_top(i, j)
                    self.c_maker_bottom(i, j)
                    self.c_maker_left(i, j)
                    self.c_maker_right(i, j)
                    self.c_maker_top_left(i, j)
                    self.c_maker_top_right(i, j)
                    self.c_maker_bottom_left(i, j)
                    self.c_maker_bottom_right(i, j)
        if not self.has_valid_moves():
            self.check_game_over()

# ref นายศุภวิชญ์ สุขแดง , กานต์ สุขสมกิจ
    def c_maker_top(self,r,c): 
        for nrow in range(r-1,-1,-1):
            if self.table[nrow][c]["image"] == "pyimage1" or self.table[nrow][c]["image"] == "pyimage4":
                break
            elif self.table[nrow][c]["image"] == self.another:
                continue
            elif self.table[nrow][c]["image"] == self.current:    
                for irow in range(r+1,8):  # r = 4 , r - 1 = nrow = 3, nrow - 1 = irow = 2
                    if self.table[irow][c]["image"] == "pyimage1":
                        self.table[irow][c]["image"] = "pyimage4"
                        self.table[irow][c].bind("<Button-1>",self.play_thegame)
                        break
                    elif self.table[irow][c]["image"] == "pyimage4":
                        break
                    elif self.table[irow][c]["image"] == self.current or self.table[irow][c]["image"] == "pyimage4":
                        break
                    elif self.table[irow][c]["image"] == self.another:
                        continue
    
    def c_maker_bottom(self,r,c):
        for nrow in range(r+1,8):
            if self.table[nrow][c]["image"] == "pyimage1" or self.table[nrow][c]["image"] == "pyimage4":
                break
            elif self.table[nrow][c]["image"] == self.another:
                continue
            elif self.table[nrow][c]["image"] == self.current:
                for irow in range(r-1,-1,-1):
                    if self.table[irow][c]["image"] == "pyimage1":
                        self.table[irow][c]["image"] = "pyimage4"
                        self.table[irow][c].bind("<Button-1>",self.play_thegame)
                        break
                    elif self.table[irow][c]["image"] == "pyimage4":
                        break
                    elif self.table[irow][c]["image"] == self.current or self.table[irow][c]["image"] == "pyimage4":
                        break
                    elif self.table[irow][c]["image"] == self.another:
                        continue

    def c_maker_left(self,r,c):
        for ncolumn in range(c-1,-1,-1):
            if self.table[r][ncolumn]["image"] == "pyimage1" or self.table[r][ncolumn]["image"] == "pyimage4":
                break
            elif self.table[r][ncolumn]["image"] == self.another:
                continue
            elif self.table[r][ncolumn]["image"] == self.current:
                for icolumn in range(c+1,8):
                    if self.table[r][icolumn]["image"] == "pyimage1":
                        self.table[r][icolumn]["image"] = "pyimage4"
                        self.table[r][icolumn].bind("<Button-1>",self.play_thegame)
                        break
                    elif self.table[r][icolumn]["image"] == "pyimage4":
                        break
                    elif self.table[r][icolumn]["image"] == self.current or self.table[r][icolumn]["image"] == "pyimage4":
                        break
                    elif self.table[r][icolumn]["image"] == self.another:
                        continue

    def c_maker_right(self,r,c):
        for ncolumn in range(c+1,8):
            if self.table[r][ncolumn]["image"] == "pyimage1" or self.table[r][ncolumn]["image"] == "pyimage4":
                break
            elif self.table[r][ncolumn]["image"] == self.another:
                continue
            elif self.table[r][ncolumn]["image"] == self.current:
                for icolumn in range(c-1,-1,-1):
                    if self.table[r][icolumn]["image"] == "pyimage1":
                        self.table[r][icolumn]["image"] = "pyimage4"
                        self.table[r][icolumn].bind("<Button-1>",self.play_thegame)
                        break
                    elif self.table[r][icolumn]["image"] == "pyimage4":
                        break
                    elif self.table[r][icolumn]["image"] == self.current or self.table[r][icolumn]["image"] == "pyimage4":
                        break
                    elif self.table[r][icolumn]["image"] == self.another:
                        continue

    def c_maker_top_left(self, r, c):
        for n in range(1, min(r, c)):
            if self.table[r - n][c - n]["image"] == "pyimage1" or self.table[r - n][c - n]["image"] == "pyimage4":
                break
            elif self.table[r - n][c - n]["image"] == self.another:
                continue
            elif self.table[r - n][c - n]["image"] == self.current:
                for i in range(1, min(7 - r, 7 - c)+1):
                    if self.table[r + i][c + i]["image"] == "pyimage1":
                        self.table[r + i][c + i]["image"] = "pyimage4"
                        self.table[r + i][c + i].bind("<Button-1>", self.play_thegame)
                        break
                    elif self.table[r + i][c + i]["image"] == "pyimage4":
                        break
                    elif self.table[r + i][c + i]["image"] == self.current or self.table[r + i][c + i]["image"] == "pyimage4":
                        break
                    elif self.table[r + i][c + i]["image"] == self.another:
                        continue

    def c_maker_top_right(self, r, c):
        for n in range(1, min(r, 7 - c) ):
            if self.table[r - n][c + n]["image"] == "pyimage1" or self.table[r - n][c + n]["image"] == "pyimage4":
                break
            elif self.table[r - n][c + n]["image"] == self.another:
                continue
            elif self.table[r - n][c + n]["image"] == self.current:
                for i in range(1, min(7 - r, c )+1):
                    if self.table[r + i][c - i]["image"] == "pyimage1":
                        self.table[r + i][c - i]["image"] = "pyimage4"
                        self.table[r + i][c - i].bind("<Button-1>", self.play_thegame)
                        break
                    elif self.table[r + i][c - i]["image"] == "pyimage4":
                        break
                    elif self.table[r + i][c - i]["image"] == self.current or self.table[r + i][c - i]["image"] == "pyimage4":
                        break
                    elif self.table[r + i][c - i]["image"] == self.another:
                        continue

    def c_maker_bottom_left(self, r, c):
        for n in range(1, min(7 - r, c) ):
            if self.table[r + n][c - n]["image"] == "pyimage1" or self.table[r + n][c - n]["image"] == "pyimage4":
                break
            elif self.table[r + n][c - n]["image"] == self.another:
                continue
            elif self.table[r + n][c - n]["image"] == self.current:
                for i in range(1, min(r , 7 - c)+1):
                    if self.table[r - i][c + i]["image"] == "pyimage1":
                        self.table[r - i][c + i]["image"] = "pyimage4"
                        self.table[r - i][c + i].bind("<Button-1>", self.play_thegame)
                        break
                    elif self.table[r - i][c + i]["image"] == "pyimage4":
                        break
                    elif self.table[r - i][c + i]["image"] == self.current or self.table[r - i][c + i]["image"] == "pyimage4":
                        break
                    elif self.table[r - i][c + i]["image"] == self.another:
                        continue

    def c_maker_bottom_right(self, r, c):
        for n in range(1, min(7 - r, 7 - c) ):
            if self.table[r + n][c + n]["image"] == "pyimage1" or self.table[r + n][c + n]["image"] == "pyimage4":
                break
            elif self.table[r + n][c + n]["image"] == self.another:
                continue
            elif self.table[r + n][c + n]["image"] == self.current:
                for i in range(1, min(r , c )+1):
                    if self.table[r - i][c - i]["image"] == "pyimage1":
                        self.table[r - i][c - i]["image"] = "pyimage4"
                        self.table[r - i][c - i].bind("<Button-1>", self.play_thegame)
                        break
                    elif self.table[r - i][c - i]["image"] == "pyimage4":
                        break
                    elif self.table[r - i][c - i]["image"] == self.current or self.table[r - i][c - i]["image"] == "pyimage4":
                        break
                    elif self.table[r - i][c - i]["image"] == self.another:
                        continue

    def play_top(self,r,c):
            memory = []
            for nrow in range(r-1,-1,-1):
                if self.table[nrow][c]["image"] == "pyimage1" or self.table[nrow][c]["image"] == "pyimage4":
                    break
                elif self.table[nrow][c]["image"] == self.another:
                    memory.append([nrow,c])
                    continue
                elif self.table[nrow][c]["image"] == self.current:
                    for i in memory:
                        self.table[i[0]][i[1]]["image"] = self.current
                    break

    def play_bottom(self,r,c):
        memory = []
        for nrow in range(r+1,8):
            if self.table[nrow][c]["image"] == "pyimage1" or self.table[nrow][c]["image"] == "pyimage4":
                break
            elif self.table[nrow][c]["image"] == self.another:
                memory.append([nrow,c])
                continue
            elif self.table[nrow][c]["image"] == self.current:
                for i in memory:
                    self.table[i[0]][i[1]]["image"] = self.current
                break

    def play_left(self,r,c):
        memory = []
        for ncolumn in range(c-1,-1,-1):
            if self.table[r][ncolumn]["image"] == "pyimage1" or self.table[r][ncolumn]["image"] == "pyimage4":
                break
            elif self.table[r][ncolumn]["image"] == self.another:
                memory.append([r,ncolumn])
                continue
            elif self.table[r][ncolumn]["image"] == self.current:
                for i in memory:
                    self.table[i[0]][i[1]]["image"] = self.current
                break
    
    def play_right(self,r,c):
        memory = []
        for ncolumn in range(c+1,8):
            if self.table[r][ncolumn]["image"] == "pyimage1" or self.table[r][ncolumn]["image"] == "pyimage4":
                break
            elif self.table[r][ncolumn]["image"] == self.another:
                memory.append([r,ncolumn])
                continue
            elif self.table[r][ncolumn]["image"] == self.current:
                for i in memory:
                    self.table[i[0]][i[1]]["image"] = self.current
                break
    
    def play_top_left(self, r, c):
        memory = []
        for n in range(1, min(r, c) ):
            if self.table[r - n][c - n]["image"] == "pyimage1" or self.table[r - n][c - n]["image"] == "pyimage4":
                break
            elif self.table[r - n][c - n]["image"] == self.another:
                memory.append([r - n,c - n])
                continue
            elif self.table[r - n][c - n]["image"] == self.current:
                for i in memory:
                    self.table[i[0]][i[1]]["image"] = self.current
                break
    
    def play_top_right(self, r, c):
        memory = []
        for n in range(1, min(r, 7 - c) ):
            if self.table[r - n][c + n]["image"] == "pyimage1" or self.table[r - n][c + n]["image"] == "pyimage4":
                break
            elif self.table[r - n][c + n]["image"] == self.another:
                memory.append([r - n,c + n])
                continue
            elif self.table[r - n][c + n]["image"] == self.current:
                for i in memory:
                    self.table[i[0]][i[1]]["image"] = self.current
                break
    
    def play_bottom_left(self, r, c):
        memory = []
        for n in range(1, min(7 - r, c) ):
            if self.table[r + n][c - n]["image"] == "pyimage1" or self.table[r + n][c - n]["image"] == "pyimage4":
                break
            elif self.table[r + n][c - n]["image"] == self.another:
                memory.append([r + n,c - n])
                continue
            elif self.table[r + n][c - n]["image"] == self.current:
                for i in memory:
                    self.table[i[0]][i[1]]["image"] = self.current
                break
    
    def play_bottom_right(self, r, c):
        memory = []
        for n in range(1, min(7 - r, 7 - c) ):
            if self.table[r + n][c + n]["image"] == "pyimage1" or self.table[r + n][c + n]["image"] == "pyimage4":
                break
            elif self.table[r + n][c + n]["image"] == self.another:
                memory.append([r + n,c + n])
                continue
            elif self.table[r + n][c + n]["image"] == self.current:
                for i in memory:
                    self.table[i[0]][i[1]]["image"] = self.current
                break
    
    def TimeTicking(self):
        
        converted = strftime("%H:%M:%S", gmtime(self.time_running)) # convert seconds to hour:minute:second
        self.time.set(converted) # change time display
        self.time_running += 1
        self.after_code = self.root.after(1000, self.TimeTicking)

    def StopTimer(self):
        global after_code
        if after_code is not None:
            self.root.after_cancel(after_code)
            after_code = None



    def check_coin(self): # นับตัวหมาก
        self.scorewhite = 0
        self.scoreblack = 0
        for i in range (8):
            for j in range(8):
                if self.table[i][j]["image"] == "pyimage3":
                    self.scorewhite += 1 
                elif self.table[i][j]["image"] == "pyimage2":
                    self.scoreblack += 1
        self.check_coin_black.set(self.scoreblack)
        self.check_coin_white.set(self.scorewhite)
        
    def game_loop(self):
        if  self.current == "pyimage2":  # ถ้าเป็นตาของผู้เล่นสีดำ
            self.place_black_piece()
            self.current, self.another = self.another, self.current  # สลับตา
            self.marker()  # ทำเครื่องหมายที่ตำแหน่งที่สามารถเลือกได้

        # เรียกฟังก์ชัน game_loop อีกครั้งหลัง delay (ปรับ delay)
        self.root.after(1000, self.game_loop)

    def place_black_piece(self):
        valid_positions = []

        # เก็บตำแหน่งที่สามารถเลือกได้ทั้งหมดจากฟังก์ชัน 'marker'
        for i in range(8):
            for j in range(8):
                if self.table[i][j]["image"] == "pyimage4":
                    valid_positions.append((i, j))

        if valid_positions:
            # เลือกตำแหน่งที่สามารถเลือกได้แบบสุ่มเพื่อวางตัวสีดำ
            row, col = random.choice(valid_positions)
            tk.Label(self.root,image=self.tsw,bg="#A2C19F").place(x=600,y=200)
            tk.Label(self.root,image=self.gb,bg="#A2C19F").place(x=600,y=100)
           

            # วางตัวสีดำในตำแหน่งที่เลือก
            self.table[row][col]["image"] = "pyimage2"
            
            # สลับตาของฝ่ายตรงข้าม
            self.play_top(row, col)
            self.play_bottom(row, col)
            self.play_left(row, col)
            self.play_right(row, col)
            self.play_top_left(row, col)
            self.play_top_right(row, col)
            self.play_bottom_left(row, col)
            self.play_bottom_right(row, col)
            self.check_coin()

    def play_thegame(self, event): # ฟังก์ชันการเล่นเกม ได้แก่ การกิน การเดิน การสลับสี 
        clicker = event.widget
        clicker["image"] = self.current
        for k in range(8):
            if clicker in self.table[k]:
                o = self.table[k].index(clicker)
                break
        self.play_top(k,o)
        self.play_bottom(k,o)
        self.play_left(k,o)
        self.play_right(k,o)
        self.play_top_left(k,o)
        self.play_top_right(k,o)
        self.play_bottom_left(k,o)
        self.play_bottom_right(k,o)

        for i in range(8):
            for j in range(8):
                self.table[i][j].unbind("<Button-1>")
                if self.table[i][j]["image"] == "pyimage4":
                    self.table[i][j]["image"] = "pyimage1"


        self.current= "pyimage2" if self.current == "pyimage3" else "pyimage3"
        self.another= "pyimage3" if self.another == "pyimage2" else "pyimage2"
     
        
        self.check_coin()
        
        if self.current == "pyimage2":
            tk.Label(self.root,image=self.gw,bg="#A2C19F").place(x=600,y=200)
            tk.Label(self.root,image=self.tsb,bg="#A2C19F").place(x=600,y=100)
            # Call your function to place a black piece
            self.place_black_piece()

        self.marker()

    def check_game_over(self):
        black_moves = 0
        white_moves = 0

        # Count the number of valid moves for both players
        for i in range(8):
            for j in range(8):
                if self.table[i][j]["image"] == "pyimage4":
                    if self.current == "pyimage2":
                        black_moves += 1
                    elif self.current == "pyimage3":
                        white_moves += 1

    # Check if no more valid moves for both players
        if black_moves == 0 and white_moves == 0:
            if self.check_coin_black.get() > self.check_coin_white.get() and self.check_coin_black.get()+self.check_coin_white.get()!=64:
                winner = "Black Player Because no more valid moves"
            elif self.check_coin_black.get() < self.check_coin_white.get() and self.check_coin_black.get()+self.check_coin_white.get()!=64:
                winner = "White Player Because no more valid moves"
            elif self.check_coin_black.get() < self.check_coin_white.get():
                winner = "White Player"
            elif self.check_coin_black.get() > self.check_coin_white.get() :
                winner = "Black Player"
            else:
                winner = "It's a Tie!"
            messagebox.showinfo("Game Over", f"The winner is {winner}!")

    def has_valid_moves(self):
        for i in range(8):
            for j in range(8):
                if self.table[i][j]["image"] == "pyimage4":
                    return True

        return False

       




    