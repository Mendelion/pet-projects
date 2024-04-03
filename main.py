from tkinter import *
from tkinter import ttk

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

    label_game = ttk.Label(window, text="Выберите действие:", font=("Times New Roman", 16))
    label_game.pack()

    photo_rock = PhotoImage(file="C:\\Users\\User\\PycharmProjects\\pet-projects\\rock.png")
    photo_scissors = PhotoImage(file="C:\\Users\\User\\PycharmProjects\\pet-projects\\scissors.png")
    photo_paper = PhotoImage(file="C:\\Users\\User\\PycharmProjects\\pet-projects\\paper.png")
    btn_paper = ttk.Button(window, image=photo_paper)
    btn_rock = ttk.Button(window, image=photo_rock)
    btn_scissors = ttk.Button(window, image=photo_scissors)
    btn_paper.image = photo_paper
    btn_rock.image = photo_rock
    btn_scissors.image = photo_scissors
    btn_paper.grid(row=0, column=1, padx=10)
    btn_rock.grid(row=0, column=0, padx=10)
    btn_scissors.grid(row=0, column=2, padx=10)

    choices = ["Камень", "Ножницы", "Бумага"]

btn_start = ttk.Button(text="Начать игру", command=start_game)
btn_start.place(relx=.5, rely=.5, anchor = "center", height= 80, width = 160)

root.mainloop()