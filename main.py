import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("All in One Installer")
        #setting window size
        width=647
        height=907
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_871=tk.Button(root)
        GButton_871["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_871["font"] = ft
        GButton_871["fg"] = "#000000"
        GButton_871["justify"] = "center"
        GButton_871["text"] = "Exit"
        GButton_871.place(x=20,y=820,width=120,height=50)
        GButton_871["command"] = self.GButton_871_command

        GButton_264=tk.Button(root)
        GButton_264["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_264["font"] = ft
        GButton_264["fg"] = "#000000"
        GButton_264["justify"] = "center"
        GButton_264["text"] = "Update"
        GButton_264.place(x=170,y=820,width=120,height=50)
        GButton_264["command"] = self.GButton_264_command

        GButton_52=tk.Button(root)
        GButton_52["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=28)
        GButton_52["font"] = ft
        GButton_52["fg"] = "#000000"
        GButton_52["justify"] = "center"
        GButton_52["text"] = "Home"
        GButton_52.place(x=40,y=40,width=200,height=50)
        GButton_52["command"] = self.GButton_52_command

        GButton_405=tk.Button(root)
        GButton_405["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=28)
        GButton_405["font"] = ft
        GButton_405["fg"] = "#000000"
        GButton_405["justify"] = "center"
        GButton_405["text"] = "Utility Softwares"
        GButton_405.place(x=310,y=40,width=280,height=50)
        GButton_405["command"] = self.GButton_405_command

    def GButton_871_command(self):
        root.destroy()


    def GButton_264_command(self):
        print("command")


    def GButton_52_command(self):
        print("command")


    def GButton_405_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
