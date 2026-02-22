import tkinter as tk

app = tk.Tk()
app.title("My First App in Python :)")

"""button1 = tk.Button(text = "Click me!")
button1.pack()"""

"""def print_something():
    print("Button is working!")

button1 = tk.Button(text = "Click me", command = print_something)
button1.pack()"""

tk.Button(app, text = "+", bg = "red").grid(row = 0, column = 0, sticky = 'NSEW')
tk.Button(app, text = "-", bg = "orange").grid(row = 0, column = 1, sticky = 'NSEW')
tk.Button(app, text = "*", bg = "yellow").grid(row = 1, column = 0, sticky = 'NSEW')
tk.Button(app, text = "/", bg = "light green").grid(row = 1, column = 1, sticky = 'NSEW')

stop = tk.Button(text = "quit", command = app.destroy).grid(row = 5, sticky = "NSEW", columnspan = 2)


app.mainloop()
