import tkinter
from tkinter import messagebox

pin = ""

def button_info_message():
    messagebox.showinfo(title="Pozvoni", message="Zvono je aktivirano! Pričekajte da vam netko dođe otvoriti.")

def button_pin_frame():
    pin_frame.grid()
    



def enter_pin(button_number):

    global pin
    
    pin += button_number

    print(pin)

    


#inicijaliziramo glavni okvir
main_window = tkinter.Tk()
main_window.title("SmartKey")
main_window.geometry("600x400")

header_frame = tkinter.Frame(main_window, highlightbackground="orange", highlightthickness=1)
header_frame.grid(row=0, column=0, columnspan=5, padx=20, pady=20)

pin_frame = tkinter.Frame(main_window, highlightbackground="orange", highlightthickness=1)
pin_frame.grid(row=1, column=0, padx=20, pady=20)
pin_frame.grid_remove()



footer_frame = tkinter.Frame(main_window, highlightbackground="orange", highlightthickness=1)
footer_frame.grid(row=2, column=0, padx=20, pady=20)


button_ring = tkinter.Button(header_frame,
                             text="Pozvoni",
                             font=("Seqoe UI", 18),
                             command= button_info_message) #samo se navede f-ja (ne poziva se () jer bi se odmah izvrsila)
button_ring.grid(row=0, column=0, padx=100, pady=15, sticky=tkinter.W)

button_unlock = tkinter.Button(header_frame,
                               text="Otključaj",
                               font=("Seqoe UI", 18),
                               command= button_pin_frame)
button_unlock.grid(row=0, column=2, padx=100, pady=15, sticky=tkinter.E) 

button_1 = tkinter.Button(pin_frame,
                            text="1",
                            font=("Seqoe UI", 18),
                            command=enter_pin
                            )
button_1.grid(row=0, column=1, padx=10, pady=15, sticky=tkinter.SE)

button_2 = tkinter.Button(pin_frame,
                                text="2",
                                font=("Seqoe UI", 18),
                                command=enter_pin
                                )
button_2.grid(row=0, column=2, padx=10, pady=15, sticky=tkinter.SE)

button_3 = tkinter.Button(pin_frame,
                                text="3",
                                font=("Seqoe UI", 18)
                                )
button_3.grid(row=0, column=3, padx=10, pady=15, sticky=tkinter.SE)

button_4 = tkinter.Button(pin_frame,
                                text="4",
                                font=("Seqoe UI", 18)
                                )
button_4.grid(row=1, column=1, padx=10, pady=15, sticky=tkinter.SE)

button_5 = tkinter.Button(pin_frame,
                                text="5",
                                font=("Seqoe UI", 18)
                                )
button_5.grid(row=1, column=2, padx=10, pady=15, sticky=tkinter.SE)

button_6 = tkinter.Button(pin_frame,
                                text="6",
                                font=("Seqoe UI", 18)
                                )
button_6.grid(row=1, column=3, padx=10, pady=15, sticky=tkinter.SE)


button_7 = tkinter.Button(pin_frame,
                                text="7",
                                font=("Seqoe UI", 18)
                                )
button_7.grid(row=2, column=1, padx=10, pady=15, sticky=tkinter.SE)

button_8 = tkinter.Button(pin_frame,
                                text="8",
                                font=("Seqoe UI", 18)
                                )
button_8.grid(row=2, column=2, padx=10, pady=15, sticky=tkinter.SE)

button_9 = tkinter.Button(pin_frame,
                                text="9",
                                font=("Seqoe UI", 18)
                                )
button_9.grid(row=2, column=3, padx=10, pady=15, sticky=tkinter.SE)


button_0 = tkinter.Button(pin_frame,
                                text="0",
                                font=("Seqoe UI", 18)
                                )
button_0.grid(row=3, column=2, padx=10, pady=15, sticky=tkinter.SE)

button_c = tkinter.Button(pin_frame,
                                text="C",
                                font=("Seqoe UI", 18)
                                )
button_c.grid(row=3, column=3, padx=10, pady=15, sticky=tkinter.SE)



# region status frame
status_frame = tkinter.Frame(pin_frame, highlightbackground="orange", highlightthickness=1)
status_frame.grid(row=1, rowspan=5, column=5, columnspan=5, padx=20, pady=20)

label_display_message_var = tkinter.StringVar()
label_display_message_var.set("Unesite PIN od 4-znamenke")

label_display_message = tkinter.Label(status_frame,
                                        textvariable=label_display_message_var,
                                        font=("Segoe UI", 12))
label_display_message.grid(row=0, rowspan=2, column=6, columnspan=5,
                            padx=100, pady=70, sticky=tkinter.E)


entry_pin_var = tkinter.StringVar()
entry_pin = tkinter.Entry(status_frame,
                                 font=("Seqoe UI", 14),
                                 textvariable=entry_pin_var)
entry_pin.grid(row=1, column=6, columnspan=5, padx=10, pady=10)


#endregion
   


#pokrecemo glavni prozor
main_window.mainloop()