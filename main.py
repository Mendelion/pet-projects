from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Игра 'Камень-ножницы-бумага'") #оглавление нашего приложения
root.geometry("800x600") #размер окна, если не нравится, поменяй разрешение, я поставил рандомное
root.resizable(False, False) #я думаю растягивать окно тоже не надо, пусть будет оконной игра. Если что, первый параметр - вертикаль, второй - горизонатль

label = ttk.Label(text="Добро пожаловать в нашу игру 'камень-ножницы-бумага'\nВам необходимо выбрать одно из трёх действий чтобы победить компьютер\nДля начала игры нажмите начать!", font=("Times New Roman", 14))
label.pack()

root.mainloop()

