from tkinter import *


def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            from Options import Prutas
            Prutas.main()
        elif args == 2:
            from Options import Hayop
            Hayop.main()
        elif args == 3:
            from Options import Ulam
            Ulam.main()

    def option():

        lab_img1 = Button(
            main_window,
            text="Select",
            bg='#e6fff5',
            border=0,
            justify='center',
            font=("Arial", 12)

        )
        sel_btn1 = Button(
            text="Prutas",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text="Hayop",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="Ulam",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(3),
        )
        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=0, column=4, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=1, column=4, pady=(10, 0), padx=50, )
        sel_btn3.grid(row=2, column=4, pady=(10, 0), padx=50, )


    def show_option():
        start_btn.destroy()

        lab_img.destroy()
        option()

    main_window = Tk()

    main_window.geometry("500x500+500+150")
    main_window.resizable(0, 0)
    main_window.title("Guess the Word Game Pinoy Concept")
    main_window.configure(background="#e6fff5")
    

    img1 = PhotoImage(file="button.png")

    lab_img = Label(
        main_window,
        text="Guess the Word Game Pinoy Concept",
        bg='#e6fff5',
        font=("Courier", 28)
    )
    lab_img.pack(pady=(50, 0))

    start_btn = Button(
        main_window,
        text="Start",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        cursor="hand2",
        command=show_option,
    )
    start_btn.pack(pady=(50, 20))

    main_window.mainloop()


start_main_page()