from tkinter import *
from tkinter import ttk
import random

def finish():
    root.destroy()
    print("Закрытие приложения")

root = Tk()
root.title("Игра 'Камень-ножницы-бумага'") #оглавление нашего приложения
root.geometry("800x600") #размер окна, если не нравится, поменяй разрешение, я поставил рандомное
root.resizable(False, False) #я думаю растягивать окно тоже не надо, пусть будет оконной игра. Если что, первый параметр - вертикаль, второй - горизонатль
root.protocol("WM_DELETE_WINDOW", finish)

label = ttk.Label(text="Добро пожаловать в нашу игру 'камень-ножницы-бумага'\nВам необходимо выбрать одно из трёх действий чтобы победить компьютер\nДля начала игры нажмите начать!", font=("Times New Roman", 16))
label.pack()

def start_game(): #новое окно после того как нажмём начать игру
    root.withdraw() #скрывается первое окно
    window = Toplevel()
    window.title("Игра 'Камень-ножницы-бумага'")
    window.geometry("800x600")
    window.resizable(False,False)

    def close_window():
        window.destroy()
        root.deiconify()
    window.protocol("WM_DELETE_WINDOW", close_window)

    label_game = ttk.Label(window, text="Выберите действие:", font=("Times New Roman", 16))
    label_game.pack()

    photo_rock = PhotoImage(file="C:\\Users\\User\\PycharmProjects\\pet-projects\\rock.png").subsample(8, 12)
    photo_scissors = PhotoImage(file="C:\\Users\\User\\PycharmProjects\\pet-projects\\scissors.png").subsample(8, 12)
    photo_paper = PhotoImage(file="C:\\Users\\User\\PycharmProjects\\pet-projects\\paper.png").subsample(8, 12)
    btn_paper = ttk.Button(window, image=photo_paper, command = lambda: human_choise("Бумага"))
    btn_rock = ttk.Button(window, image=photo_rock, command = lambda: human_choise("Камень"))
    btn_scissors = ttk.Button(window, image=photo_scissors, command = lambda: human_choise("Ножницы"))
    btn_paper.image = photo_paper
    btn_rock.image = photo_rock
    btn_scissors.image = photo_scissors
    btn_paper.place(relx=0.5, rely=0.7, anchor = "center", height= 80, width = 160)
    btn_rock.place(relx=0.2, rely=0.7, anchor="center", height=80, width=160)
    btn_scissors.place(relx=0.8, rely=0.7, anchor="center", height=80, width=160)

    human_result = None
    def human_choise(figure):
        nonlocal human_result
        if human_result is None:
            human_result = figure
            label_game.destroy()
            label_choise = ttk.Label(window, text=f"Вы выбрали фигуру: {figure}", font=("Times New Roman", 16))
            label_choise.pack()
            window.after(2000, computer_choise) #после двух секунд будет выбор компьютера
            label_choise.destroy()


    computer_result = None
    def computer_choise():
        nonlocal computer_result
        global label_computer_choise
        label_computer_choise = ttk.Label(window, text=f"Компьютер сделал свой выбор", font=("Times New Roman", 16))
        label_computer_choise.pack()
        choicess = ["Бумага", "Камень", "Ножницы"]
        computer_result = random.choice(choicess)
        window.after(2000, comparison, human_result, computer_result)
        #почему-то так передаём результаты функции

    def comparison(human_result, computer_result):
        label_computer_choise.destroy()
        result = ""
        if human_result == computer_result:
            result = "Ничья"
        elif (human_result == "Камень" and computer_result == "Ножницы") or\
            (human_result == "Ножницы" and computer_result == "Бумага") or\
            (human_result == "Бумага" and computer_result == "Камень"):
            result = "Вы победили!"
        else:
            result = "Победил компьютер!"
        label_result = ttk.Label(window, text=f"{result}", font=("Times New Roman", 16))
        label_result.pack()

btn_start = ttk.Button(text="Начать игру", command=start_game)
btn_start.place(relx=.5, rely=.5, anchor = "center", height= 80, width = 160)

root.mainloop()