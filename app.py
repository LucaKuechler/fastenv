import tkinter as tk
import os



class shell():
    def __init__(self):
        self.cd = 'cd '
        self.cls = 'cls '
        self.start_env = "start \Scripts\\activate.bat"
        self.md = "md "
        self.off = "echo off" + "\n"
        self.on = "echo on"
        self.py = "python3 -m venv env\n"
        self.if_n = "IF NOT EXIST "



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
        two = s.if_n + self.env_path + "(\n"
        three = "GOTO :run_env\n"
        four = "\n"
        five = ") ELSE (\n"
        six = s.if_n + self.parent + " (\n"
        seven = s.md + self.parent + "\n"
        eight = ") ELSE ()\n"
        nine = "call :create_env\n"
        ten = ")\n"
        _one = "\n"
        _two = ":create_env\n"
        _three = self.letter
        _four = s.py
        _five = s.if_n + self.env_path + " (\n"
        _six = s.md + self.parent + "\\" + "build" + "\n"
        _seven = ")\n"
        _eight = "\n"
        _nine = ":run_env\n"
        _ten = s.cd + self.parent + "\\" + "build" + "\n"
        __one = s.start_env + "\n"
        __two = s.cls + "\n"
        __three = "\n"
        __four = s.off

        ultra_sting = ""
        elements = [one, two, three, four, five, six, seven, eight, nine, ten, _one, _two, _three, _four, _five, _six, _seven, _eight, _nine, _ten, __one, __two, __three, __four]
        for elem in elements:
            ultra_sting += elem

        return ultra_sting


    

    def create_bat_file(self):
        file_ = self.name + ".txt"  
        f= open(file_,"w+")
        ultra_string = self.create_bat_text()
        print("asd")
        f.write(ultra_string)
        f.close()



    def set_attributes(self, path, name):
        if os.path.exists(path):
            self.path = path
            self.parent = path + "\\" + name
            self.name = name
            self.letter = self.path[:2] + "\n"
            self.env_path = self.parent + "env"
            self.create_bat_file()




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



        button = tk.Button(text="OK", borderwidth="2", background="#1CFF14", command=lambda: self.logic.set_attributes(input_path.get(), input_name.get()))
        button.place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.15)

        root.mainloop()



if __name__ == "__main__":
    Visuel().display()