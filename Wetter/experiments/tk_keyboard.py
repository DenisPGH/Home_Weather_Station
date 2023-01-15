import tkinter as tk

# def create_keypad(root):
#     keypad = tk.Frame(root)
#
#     for y in range(3):
#         for x in range(3):
#             val = y*3 + x
#             text = str(val)
#             b = tk.Button(keypad, text=text, command=lambda txt=text:insert_text(txt))
#             b.grid(row=y, column=x, sticky='news')
#
#     return keypad
#
# def insert_text(text):
#     target.insert('end', text)
#
# def show_keypad(widget):
#     global target
#     target = widget
#
#     keypad.place(relx=0.5, rely=0.5, anchor='s')
#
# def check_if_right_password(password):
#     print(password)






class KeyboardPassword:
    def __init__(self,win):
        self.target=''
        self.keypad= tk.Frame(win)
        self.__PASSWORD='1234'

    def insert_text(self,text):
        """
        :param text : text to be insert into fild
        """
        self.target.insert('end', text)


    def create_keypad(self):
        """
        create the button of the keyboard
        :param win:
        :return:
        """

        for y in range(3):
            for x in range(3):
                val = y * 3 + x
                text = str(val)
                b = tk.Button(self.keypad, text=text, command=lambda txt=text: self.insert_text(txt))
                b.grid(row=y, column=x, sticky='news')

        return self.keypad

    def show_keypad(self,widget):
        """
        show the keyboard
        :param widget:
        :return:
        """

        self.target = widget
        self.keypad.place(relx=0.5, rely=0.5, anchor='s')

    def check_if_right_password(self,password):
        if password==self.__PASSWORD:
            print(password)
            exit()
        else:
            self.run_keyboard()


    def run_keyboard(self):
        self.keypad = self.create_keypad(root)
        f = tk.Frame(root)
        f.pack()

        e1 = tk.Entry(f)
        e1.grid(row=0, column=0)
        self.show_keypad(e1)

        b1 = tk.Button(f, text='Log out', command=lambda: self.check_if_right_password(e1.get()))
        b1.grid(row=0, column=1)




if __name__=="__main__":
    root = tk.Tk()
    root.geometry('600x400')
    k=KeyboardPassword(root)
    k.run_keyboard()
    root.mainloop()

