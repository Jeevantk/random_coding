from tkinter import *


name=""



def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def getData():
	global name
	name = e1.get()




master = Tk()
master.title('Jarvis')

v = IntVar()

v.set('0')

Label(master, text="Name").grid(row=2)
# Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
# e2 = Entry(master)

e1.grid(row=2, column=1)
# e2.grid(row=1, column=1)

# Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Submit', command = combine_funcs(getData, master.quit)).grid(row=5, column=1, sticky=W, pady=4)

Radiobutton(master, text="HNI",padx = 20, variable=v, value=1).grid(row=4)

# Radiobutton(master, text="Not HNI",padx = 30, variable=v, value=2).grid(row=2)


mainloop( )

print (name)
print(v.get())