# from https://stackoverflow.com/questions/40949940/bind-not-working-for-shift-key-binds

import tkinter as tk

def test(event):
    print('keysym:', event.keysym)

root = tk.Tk()

root.bind('<Key>', test)

root.mainloop()