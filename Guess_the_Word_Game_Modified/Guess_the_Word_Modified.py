from tkinter import *
import pygame
pygame.mixer.init()
pygame.mixer.music.load("backgroundMusic.mp3")
pygame.mixer.music.play(-1)

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
        elif args == 4:
            from Options import Laro
            Laro.main()
        elif args == 5:
            from Options import Bahagi_ng_Katawan
            Bahagi_ng_Katawan.main()
        elif args == 6:
            from Options import Pangulo
            Pangulo.main()

    def option():

        lab_img1 = Button(
            main_window,
            text="Select  -> ",
            bg='#4ce1de',
            border=0,
            justify='center',
            font=("Segoe Script bold", 20)

        )
        sel_btn1 = Button(
            text="Prutas",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#4ce166",
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text="Hayop",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#4ce166",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="Ulam",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#4ce166",
            cursor="hand2",
            command=lambda: start_game(3),
        )

        sel_btn4 = Button(
            text="Laro",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#4ce166",
            cursor="hand2",
            command=lambda: start_game(4),
        )

        sel_btn5 = Button(
            text="Bahagi ng Katawan",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#4ce166",
            cursor="hand2",
            command=lambda: start_game(5),
        )

        sel_btn6 = Button(
            text="Pangulo",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#4ce166",
            cursor="hand2",
            command=lambda: start_game(6),
        )

        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=0, column=4, pady=(15, 0), padx=85, )
        sel_btn2.grid(row=1, column=4, pady=(15, 0), padx=85, )
        sel_btn3.grid(row=2, column=4, pady=(15, 0), padx=85, )
        sel_btn4.grid(row=3, column=4, pady=(15, 0), padx=85, )
        sel_btn5.grid(row=4, column=4, pady=(15, 0), padx=85, )        
        sel_btn6.grid(row=5, column=4, pady=(15, 0), padx=85, )      

    def show_option():
        start_btn.destroy()

        lab_img.destroy()
        option()

    main_window = Tk()

    main_window.geometry("800x500")
    main_window.resizable(0, 0)
    main_window.title("Guess the Pinoy Word Game")
    main_window.configure(background="#4ce1de")

    img1 = PhotoImage(file="button.png")

    lab_img = Label(
        main_window,
        text="Jumbled Pinoy Words",
        bg='#4ce1de',
        font=("Segoe Script bold", 45)
    )
    lab_img.pack(pady=(50, 0))

    start_btn = Button(
        main_window,
        text="Start",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#4ce166",
        font=("", 18),
        cursor="hand2",
        command=show_option,
    )
    start_btn.pack(pady=(50, 20))

    main_window.mainloop()


start_main_page()