import tkinter as tk
from db_sqlalchemy import db_init_sqlalchemy, get_data_sqlalchemy, db_delete_data, db_add_data
from tkinter import messagebox
from sk_constants import ADMIN, BODY_TEXT, HEADER_TEXT, BODY_TEXT_MED

pin = ""

def run_gui():   
    


    keys = [
        ['1', '2', '3'],    
        ['4', '5', '6'],    
        ['7', '8', '9'],    
        ['DEL', '0', 'OK'],    
    ]

    list_users = []
    list_pins = []


    if get_data_sqlalchemy() is not None:
        for user in get_data_sqlalchemy():
            list_users.append(f'{user.name}-{user.pin}-{user.is_active}')

    def button_refresh_list_handler():
        list_users = []
        for user in get_data_sqlalchemy():
            list_users.append(f'{user.name}-{user.pin}-{user.is_active}')
        lb_access_list_var.set(list_users)

    def lb_selected(event):
        indeks = lb_access_list.curselection()
        value1 = lb_access_list.get(indeks)

        entry_name_var.set(str(value1).split("-")[0])
        entry_pin1_var.set(str(value1).split("-")[1])
        entry_is_active_var.set(str(value1).split("-")[2])

    def button_delete_user_handler():
        name = entry_name_var.get()
        pin = entry_pin1_var.get()
        is_active = int(entry_is_active_var.get())

        user = [name, pin, is_active]

        db_delete_data(user)
        button_quit_handler()
        lbl_message_var.set("Korisnik je obrisan.")

    def button_info_message():
        messagebox.showinfo(title="Pozvoni", message="Zvono je aktivirano! Pričekajte da vam netko dođe otvoriti.")

    def button_frame_02():
        frame_02.pack(after=frame_01, padx=20, pady=20)

    def button_quit_handler():
        entry_name_var.set("")
        entry_pin1_var.set("")
        entry_is_active_var.set("")

    def button_save_handler():
        name = entry_name_var.get()
        pin = entry_pin1_var.get()
        is_active = entry_is_active_var.get()


        user = [name, pin, is_active]

        if len(pin) != 4:
            messagebox.showinfo(title="Pin error", message="Pin mora imati 4 znamenke!")
        else:
            db_add_data(user)
            lbl_message_var.set('Podaci su spremljeni')

    def keyboard(value):
        global pin

        if value == 'DEL':
            # remove last number from `pin`
            pin = pin[:-1]
            # remove all from `entry` and put new `pin`
            entry_pin.delete('0', 'end')
            entry_pin.insert('end', pin)

        elif value == 'OK':
            # check pin
             
            if pin == ADMIN:
                
                q = messagebox.askquestion(title="Admin PIN", message="Unijeli ste Admin PIN. Želite li pokrenuti administraciju sustava?")
                if q:
                    messagebox.showinfo(title="Admin PIN", message="Potvrda")
                    lbl_message_var.set('Dobrodošao Admin')
                    frame_03.pack(after=frame_02, padx=20, pady=20)
                else:
                    messagebox.showinfo(title="Admin PIN", message="Odgovorili ste ne")
            else:
                for user in get_data_sqlalchemy():
                    if pin == user.pin:
                        if user.is_active:
                            lbl_message_var.set(f'Dobrodošao {user.name}')
                            messagebox.showinfo(title="Pass", message=f"Dobrodosao {user.name}! Vrata su otkljucana.")
                        else:
                            messagebox.showinfo(title="User deactivated", message=f"{user.name}, deaktivirani ste i nemate prava ulaza!")
                            lbl_message_var.set(f'{user.name} je deaktiviran. Obratite se adminu.')


        else:
            # add number to pin
            pin += value
            # add number to `entry`
            entry_pin.insert('end', value)
    


    #main window
    main_window = tk.Tk()
    main_window.title("SmartKey")
    main_window.geometry("800x700")

    #Frame 1
    frame_01 = tk.Frame(main_window, highlightbackground="orange", highlightthickness=1)
    frame_01.pack(padx=20, pady=20)

    button_ring = tk.Button(frame_01,
                                text="Pozvoni",
                                font= HEADER_TEXT,
                                command= button_info_message) 
    button_ring.grid(row=0, column=0, padx=100, pady=15, sticky=tk.W)

    button_unlock = tk.Button(frame_01,
                                text="Otključaj",
                                font=HEADER_TEXT,
                                command= button_frame_02)
    button_unlock.grid(row=0, column=2, padx=100, pady=15, sticky=tk.E) 

    #region Frame 2
    frame_02 = tk.Frame(main_window, highlightbackground="orange", highlightthickness=1)


    # place to display pin
    entry_pin = tk.Entry(frame_02, show="*")
    entry_pin.grid(row=0, column=0, columnspan=3, ipady=5)

    # create buttons using `keys`
    for y, row in enumerate(keys, 1):
        for x, key in enumerate(row):
            # `lambda` inside `for` has to use `val=key:code(val)` 
            # instead of direct `code(key)`
            b = tk.Button(frame_02, text=key, command=lambda val=key:keyboard(val))
            b.grid(row=y, column=x, ipadx=10, ipady=10)

    lbl_message_var = tk.StringVar()
    lbl_message_var.set('Unesite PIN')
    lbl_message = tk.Label(frame_02,
                            textvariable=lbl_message_var,
                            font=BODY_TEXT)
    lbl_message.grid(row=4, column=5, padx=100, pady=15, sticky=tk.E) 

    button_close_app = tk.Button(frame_02,
                                text="Zatvori aplikaciju",
                                command=main_window.destroy,
                                font= HEADER_TEXT)
    button_close_app.grid(row=1, column=5, padx=5, pady=5) 

    #endregion

    #region Frame 3

    frame_03 = tk.Frame(main_window, highlightbackground="orange", highlightthickness=1)

    lb_access_list_var = tk.StringVar()
    lb_access_list_var.set(list_users)
    lb_access_list = tk.Listbox(frame_03, font=BODY_TEXT,
                           listvariable=lb_access_list_var)
    lb_access_list.grid(row=0, rowspan=5, column=0,
                   sticky=tk.EW,
                   padx=20, pady=20)
    lb_access_list.bind('<<ListboxSelect>>', lb_selected)
    
    
    lbl_name = tk.Label(frame_03,
                        text= "Ime i prezime:",
                        font= BODY_TEXT)
    lbl_name.grid(row=0, column=1, padx=5, pady=5, sticky=tk.E) 

    entry_name_var = tk.StringVar()
    entry_name = tk.Entry(frame_03,
                          textvariable=entry_name_var)
    entry_name.grid(row=0, column=2)

    lbl_pin = tk.Label(frame_03,
                        text= "PIN:",
                        font=BODY_TEXT)
    lbl_pin.grid(row=1, column=1, padx=5, pady=5, sticky=tk.E)   

    entry_pin1_var = tk.StringVar()
    entry_pin1 = tk.Entry(frame_03,
                          textvariable=entry_pin1_var)
    entry_pin1.grid(row=1, column=2)

    lbl_active = tk.Label(frame_03,
                        text= "Aktivan:",
                        font=BODY_TEXT)
    lbl_active.grid(row=2, column=1, padx=5, pady=5, sticky=tk.E)   

    entry_is_active_var = tk.IntVar()
    entry_is_active = tk.Checkbutton(frame_03,
                                     variable=entry_is_active_var,
                                     onvalue=1,
                                     offvalue=0)
    entry_is_active.grid(row=2, column=2, sticky=tk.W)

    button_save = tk.Button(frame_03,
                                text="Spremi",
                                command=button_save_handler,
                                foreground="#99004c",
                                font= BODY_TEXT)
    button_save.grid(row=3, column=1, padx=5, pady=5) 

    button_quit = tk.Button(frame_03,
                                text="Odustani",
                                font= BODY_TEXT,
                                foreground="#99004c",
                                command=button_quit_handler)
    button_quit.grid(row=3, column=2, padx=5, pady=5) 

    button_erase = tk.Button(frame_03,
                                text="Izbrisi",
                                command=button_delete_user_handler,
                                font= BODY_TEXT,
                                foreground="#99004c")
    button_erase.grid(row=3, column=3, padx=5, pady=5) 

    button_refresh = tk.Button(frame_03,
                                text="Refresh list",
                                command=button_refresh_list_handler,
                                font= BODY_TEXT_MED)
    button_refresh.grid(row=4, column=5, padx=5, pady=5) 
    #endregion

    
    #pokrecemo glavni prozor
    main_window.mainloop()

if __name__ == "__main__":
    db_init_sqlalchemy()
    run_gui()