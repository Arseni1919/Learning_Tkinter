import tkinter as tk
import random

if __name__ == '__main__':
    window = tk.Tk()
    #
    # frame = tk.Frame()
    # frame.pack()

    # label = tk.Label(
    #     text="Hello, Tkinter",
    #     fg="white",
    #     bg="black",
    #     width=100,
    #     height=10
    # )
    # label.pack()
    #
    # button = tk.Button(
    #     text="Click me!",
    #     width=25,
    #     height=5,
    #     bg="blue",
    #     fg="black",
    # )
    # button.pack()
    #
    # entry = tk.Entry(fg="yellow", bg="blue", width=50)
    # entry.pack()
    #
    # text_box = tk.Text()
    # text_box.pack()



    # label = tk.Label(
    #     master=frame,
    #     text="Hello, Tkinter",
    #     fg="white",
    #     bg="black",
    #     width=100,
    #     height=10
    # )
    # label.pack()

    # border_effects = {
    #     "flat": tk.FLAT,
    #     "sunken": tk.SUNKEN,
    #     "raised": tk.RAISED,
    #     "groove": tk.GROOVE,
    #     "ridge": tk.RIDGE,
    # }
    #
    # for relief_name, relief in border_effects.items():
    #     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    #     choice = random.choice([tk.RIGHT, tk.LEFT, tk.BOTTOM, tk.TOP])
    #     print(choice)
    #     frame.pack(side=choice)
    #     label = tk.Label(master=frame, text=relief_name)
    #     label.pack()

    # entry = tk.Entry(width=40, bg="white", fg="black")
    # entry.pack()
    # entry.insert(0, "What is your name?")

    # frame1 = tk.Frame(master=window, width=300, height=100, bg="red")
    # frame1.pack(fill=tk.X)
    #
    # frame2 = tk.Frame(master=window, height=50, bg="yellow")
    # frame2.pack(fill=tk.X)
    #
    # frame3 = tk.Frame(master=window, height=25, bg="blue")
    # frame3.pack(fill=tk.X)
    # ---
    # frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
    # frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    #
    # frame2 = tk.Frame(master=window, width=100, bg="yellow")
    # frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    #
    # frame3 = tk.Frame(master=window, width=50, bg="blue")
    # frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    # ---
    # frame = tk.Frame(master=window, width=250, height=150)
    # frame.pack()
    #
    # label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
    # label1.place(x=0, y=0)
    #
    # label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
    # label2.place(x=75, y=75)
    # ---
    # for i in range(3):
    #     window.columnconfigure(i, weight=1, minsize=175)
    #     window.rowconfigure(i, weight=1, minsize=150)
    #
    #     for j in range(3):
    #         frame = tk.Frame(
    #             master=window,
    #             relief=tk.RAISED,
    #             borderwidth=1
    #         )
    #         frame.grid(row=i, column=j, padx=5, pady=5)
    #         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
    #         label.pack(padx=5, pady=5)
    # ---
    # window.rowconfigure(0, minsize=50)
    # window.columnconfigure([0, 1, 2, 3], minsize=50)
    #
    # label1 = tk.Label(text="1", bg="black", fg="white")
    # label2 = tk.Label(text="2", bg="black", fg="white")
    # label3 = tk.Label(text="3", bg="black", fg="white")
    # label4 = tk.Label(text="4", bg="black", fg="white")
    #
    # label1.grid(row=0, column=0)
    # label2.grid(row=0, column=1, sticky="ew")
    # label3.grid(row=0, column=2, sticky="ns")
    # label4.grid(row=0, column=3, sticky="nsew")
    #
    #
    # # Create an event handler
    # def handle_keypress(event):
    #     """Print the character associated to the key pressed"""
    #     print(event.char)
    #
    #
    # # Bind keypress event to handle_keypress()
    # window.bind("<Key>", handle_keypress)
    # ---


    # def increase():
    #     value = int(lbl_value["text"])
    #     lbl_value["text"] = f"{value + 1}"
    #
    #
    # def decrease():
    #     value = int(lbl_value["text"])
    #     lbl_value["text"] = f"{value - 1}"
    #
    #
    # window.rowconfigure(0, minsize=50, weight=1)
    # window.columnconfigure([0, 1, 2], minsize=50, weight=1)
    #
    # btn_decrease = tk.Button(master=window, text="-", command=decrease)
    # btn_decrease.grid(row=0, column=0, sticky="nsew")
    #
    # lbl_value = tk.Label(master=window, text="0")
    # lbl_value.grid(row=0, column=1)
    #
    # btn_increase = tk.Button(master=window, text="+", command=increase)
    # btn_increase.grid(row=0, column=2, sticky="nsew")
    # ---



    def fahrenheit_to_celsius():
        """Convert the value for Fahrenheit to Celsius and insert the
        result into lbl_result.
        """
        fahrenheit = ent_temperature.get()
        celsius = (5 / 9) * (float(fahrenheit) - 32)
        lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


    # # Create an event handler
    def handle_keypress(event):
        """Print the character associated to the key pressed"""
        print(event.keysym)
        if event.keysym == 'Return':
            fahrenheit_to_celsius()

    # Bind keypress event to handle_keypress()
    window.bind("<Key>", handle_keypress)


    window.title("Temperature Converter")
    frm_entry = tk.Frame(master=window)
    ent_temperature = tk.Entry(master=frm_entry, width=10)
    lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
    ent_temperature.grid(row=0, column=0, sticky="e")
    lbl_temp.grid(row=0, column=1, sticky="w")

    btn_convert = tk.Button(
        master=window,
        text="\N{RIGHTWARDS BLACK ARROW}",
        command=fahrenheit_to_celsius
    )
    lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
    frm_entry.grid(row=0, column=0, padx=10)
    btn_convert.grid(row=0, column=1, pady=10)
    lbl_result.grid(row=0, column=2, padx=10)




    window.mainloop()
