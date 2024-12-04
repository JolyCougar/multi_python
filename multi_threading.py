import threading
from tkinter import ttk
import tkinter as tk
from threading import Thread
import time


root =tk.Tk()
root.geometry('300x300+150+150')

def thread_sleep():
    time.sleep(10)
    lab['text'] = int(lab['text']) + 10


def new_thread():
    t1 = Thread(target=thread_sleep())
    t1.start()


btn = ttk.Button(root, text='Run', command=new_thread)
btn.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

lab = ttk.Label(root, text='0', font=5)
lab.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

root.mainloop()

# Многопоточность использует один процесс, но может использовать множество потоков
# Имеет, свои нюансы например проблема с синхронизацией потоков
# Например при изменении глобальной переменной тот поток который первый успел
# тот и будет с ней взаимодействовать для того что бы этого избежать
# необходимо блокировать использование другими потоками. Пример далее:

locker = threading.Lock()


def inc_value():
    print("блокируем поток")
    locker.acquire()


t1 = threading.Thread(target=inc_value)
t2 = threading.Thread(target=inc_value)
t1.start()
t2.start()

# Проблема такого исполнения в том, что любой другой поток может разблокировать поток
# Вариант решения проблемы: использование RLock вместо Lock
# тогда, только тот поток, который его заблокировал, сможет его разблокировать.
# Еще надо учесть что, при завершении работы основного потока,
# остальные продолжают работать, для исправления этой проблемы надо использовать
# .setDaemon(True)

