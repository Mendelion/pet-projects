from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Игра 'Камень-ножницы-бумага'") #оглавление нашего приложения
root.geometry("800x600") #размер окна, если не нравится, поменяй разрешение, я поставил рандомное
root.resizable(False, False) #я думаю растягивать окно тоже не надо, пусть будет оконной игра. Если что, первый параметр - вертикаль, второй - горизонатль

label = ttk.Label(text="Добро пожаловать в нашу игру 'камень-ножницы-бумага'\nВам необходимо выбрать одно из трёх действий чтобы победить компьютер\nДля начала игры нажмите начать!", font=("Times New Roman", 14))
label.pack()

def click(): #новое окно после того как нажмём начать игру
    root.withdraw() #скрывается первое окно
    window = Tk()
    window.title("Игра 'Камень-ножницы-бумага'")
    window.geometry("800x600")
    window.resizable(False,False)
    #МАТВЕЙ!!! Теперь мы обязательно работаем только в этом окне, так как предудыщее окно закрыыто

    values = ["Камень", "Ножницы", "Бумага"]

btn_start = ttk.Button(text="Начать игру", command=click)
btn_start.place(relx=.5, rely=.5, anchor = "center", height= 80, width = 160)

root.mainloop()

