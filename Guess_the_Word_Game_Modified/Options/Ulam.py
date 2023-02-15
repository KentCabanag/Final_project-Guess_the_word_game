from tkinter import *
from random import *
from tkinter import messagebox
import time

Ulam_WORD = ['DOBOA', 'TEKSIB', 'BIPOS', 'LADCETARE', 'TISONL', 'GIDUNUNA', 'HAWINI', 'GINAL', 'CHADOME', 'NUDOME', 'GALANI',
                'KAPTEB', 'SIWAKP', 'SAPNIT', 'SIGANING', 'PALUKANMANSI', 'GISSI', 'PAAT', 'LANOTI', 'SINOTU',]

Ulam_ANSWER = ['ADOBO', 'BISTEK', 'BOPIS', 'CALDERETA', 'LITSON', 'DINUGUAN', 'INIHAW', 'LAING', 'MECHADO', 'MENUDO', 'NILAGA',
                'PAKBET', 'PAKSIW', 'PANSIT', 'SINIGANG', 'SINAMPALUKAN', 'SISIG', 'TAPA', 'TINOLA', 'TUSINO']

ran_num = randrange(0, (len(Ulam_WORD)))
jumbled_rand_word = Ulam_WORD[ran_num]

points = 0

def main():
    def back():
        my_window.destroy()
        import Guess_the_Word_Modified
        Guess_the_Word_Modified.start_main_page()

    def change():
        global ran_num
        ran_num = randrange(0, (len(Ulam_WORD)))
        word.configure(text=Ulam_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def cheak():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == Ulam_ANSWER[ran_num]:
            points += 5
            score.configure(text="Score: " + str(points))
            messagebox.showinfo('Correct', "Correct Answer...Keep it Up!")
            ran_num = randrange(0, (len(Ulam_WORD)))
            word.configure(text=Ulam_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Incorrect Answer", "Incorrect Answer...Try your best!")
            get_input.delete(0, END)

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score: " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=Ulam_ANSWER[ran_num])
        else:
            ans_lab.configure(text='Not enough points')

    my_window = Tk()
    my_window.geometry("800x500")
    my_window.resizable(0, 0)
    my_window.title("Guess the Ulam Pinoy Word")
    my_window.configure(background="#4ce1de")

    img1 = PhotoImage(file="button.png")

    lab_img1 = Button(
        my_window,
        image=img1,
        bg='#4ce1de',
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    score = Label(
        text="Score: 0",
        pady=10,
        bg="#4ce1de",
        fg="#000000",
        font="Courier  20 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=jumbled_rand_word,
        pady=10,
        bg="#4ce1de",
        fg="#000000",
        font="Titillium  50 bold"
    )
    word.pack()

    get_input = Entry(
        font="none 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()

    submit = Button(
        text="Submit",
        width=18,
        borderwidth=8,
        font=("", 13),
        fg="#000000",
        bg="#4ce166",
        command=cheak,
    )
    submit.pack(pady=(10, 20))

    change = Button(
        text="Change Word",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#4ce166",
        font=("", 13),
        command=change,
    )
    change.pack()

    ans = Button(
        text="Hint",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#4ce166",
        font=("", 13),
        command=show_answer,
    )
    ans.pack(pady=(20, 10))

    ans_lab = Label(
        text="",
        bg="#4ce1de",
        fg="#000000",
        font="Courier 15 bold",
    )
    ans_lab.pack()

    my_window.mainloop()
