
import tkinter as tk

from variables_function import Variables


class KeyboardLogout():
    def __init__(self, win):
        self.__target= ''
        self.__keypad= tk.Frame(win)
    def __insert_text(self, text):
        """
        :param text : text to be insert into fild
        """
        self.__target.insert('end', text)


    def __create_keypad(self):
        """
        create the button of the keyboard
        :param win:
        :return:
        """

        for y in range(3):
            for x in range(3):
                val = y * 3 + x
                text = str(val)
                b = tk.Button(self.__keypad, text=text, command=lambda txt=text: self.__insert_text(txt))
                b.grid(row=y, column=x, sticky='news')

        return self.__keypad

    def __show_keypad(self, widget):
        """
        show the keyboard
        :param widget:
        :return:
        """

        self.__target = widget
        self.__keypad.place(relx=0.5, rely=0.5, anchor='s')




    def run_keyboard(self,win):
        """

        :param place_success: page if the password is correct
        :param place_fail: page if password is not right
        function to use keyboard logout
        :return:
        """
        self.__keypad = self.__create_keypad()
        # f = tk.Frame(win)
        # f.pack()

        e1 = tk.Entry()
        e1.grid(row=0, column=0)
        self.__show_keypad(e1)



        b1 = tk.Button(f, text='Log out', command=lambda: self.check_if_right_password(e1.get()))
        b1.grid(row=0, column=1)

    def check_if_right_password(self, password):
        if password == self.PASSWORD:
            exit()
        else:
            pass



if __name__=="__main__":
    pass
    # root = tk.Tk()
    # root.geometry('600x400')
    # k=KeyboardLogout(root)
    # k.run_keyboard(root)
    # root.mainloop()




