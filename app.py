import tkinter as tk
import os
import sys


ONEDRIVE_PATH = "C:\\Example\\Path\\OneDrive\\befehle\\pyenv\\"

class shell():
    def __init__(self):
        self.cd = 'cd '
        self.cls = 'cls '
        self.start_env = "\Scripts\\activate.bat"
        self.md = "md "
        self.off = "@echo off" + "\n"
        self.on = "@echo on"
        self.py = "python3 -m venv "
        self.if_n = "IF NOT EXIST "
        self.if_y = "IF EXIST "



class logic():
    def __init__(self):
        self.path = ""
        self.name = "" 
        self.letter = ""
        self.command_path = "E:\OneDrive\befehle\pyenv"
        self.shell = shell()



    def convert_list_to_string(self, org_list, seperator=','):
        return seperator.join(org_list)



    def create_bat_text(self):
        s =self.shell

        one = s.off
        two = s.if_y + self.env_path + " (\n"
        three = "GOTO:run_env\n"
        four = "\n"
        five = ") ELSE (\n"
        six = s.if_n + self.parent + " (\n"
        seven = s.md + self.parent + "\n"
        eight = ")\n"
        nine = "GOTO:create_env\n"
        ten = ")\n"
        _one = "\n"
        _two = ":create_env\n"
        _three = self.letter
        _four = s.py + self.env_path + "\n"
        _five = s.if_n + self.parent + "\\build" + " (\n"
        _six = s.md + self.parent + "\\build" + "\n"
        _seven = ")\n"
        _eight = "\n"
        _nine = ":run_env\n"
        _ten = self.letter
        __one = s.cd + self.parent + "\\build" + "\n"
        __two = "start " + self.env_path + s.start_env + "\n"
        __three = s.cls + "\n"
        __four = "GOTO:eof"
        __five = "\n"
        __six = s.on

        ultra_sting = ""
        elements = [one, two, three, four, five, six, seven, eight, nine, ten, _one, _two, _three, _four, _five, _six, _seven, _eight, _nine, _ten, __one, __two, __three, __four, __five, __six]
        for elem in elements:
            ultra_sting += elem

        return ultra_sting


    

    def create_bat_file(self):
        file_ = ONEDRIVE_PATH + self.name + ".bat"  
        f= open(file_,"w+")
        ultra_string = self.create_bat_text()
        print("File was made")
        f.write(ultra_string)
        f.close()



    def set_attributes(self, path, name, root):
        if os.path.exists(path):
            self.path = path
            self.parent = path + "\\" + name
            self.name = name
            self.letter = self.path[:2] + "\n"
            self.env_path = self.parent + "\\env"
            self.create_bat_file()
            root.quit()




class Visuel():
    def __init__(self):
        self.HEIGHT = 200
        self.WIDTH = 400
        self.TITLE = "fastenv"
        self.logic = logic()

    def display(self):

        root = tk.Tk()
        root.title(self.TITLE)

        canvas = tk.Canvas(root, height=self.HEIGHT, width=self.WIDTH)
        canvas.pack()


        name_label = tk.Label(text="Name:")
        name_label.place(relx=0.1, rely=0.1, relwidth=0.08, relheight=0.1)

        input_name = tk.Entry(canvas)
        input_name.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.1)



        path_label = tk.Label(text="Path:")
        path_label.place(relx=0.1, rely=0.4, relwidth=0.08, relheight=0.1)

        input_path = tk.Entry(canvas)
        input_path.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.1)



        button = tk.Button(text="OK", borderwidth="2", background="#1CFF14", command=lambda: self.logic.set_attributes(input_path.get(), input_name.get(), root))
        button.place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.15)

        root.mainloop()



if __name__ == "__main__":
    Visuel().display()