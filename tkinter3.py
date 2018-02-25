import tkinter as tk

root =tk.Tk()

name=""

def pressSubmit():
	name=e1.get()

tk.Label(root, text="""Enter Name""").grid(row=0)
e1=tk.Entry(root, text="""Enter your Name""").grid(row=0,column=1)

tk.Button(root,text='Submit',command=pressSubmit).grid(row=2)
root.mainloop()

print(name)