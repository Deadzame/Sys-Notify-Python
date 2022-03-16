import win10toast # Импортируем системный уведомления 10 винды
import sys # Импортируем системный ЯП Питона

notify1 = win10toast.ToastNotifier()
notify2 = win10toast.ToastNotifier()
notify3 = win10toast.ToastNotifier()
# toast4 = win10toast.ToastNotifier() подобная переменная сверху
notify1.show_toast(title='System', msg='Работа системы началась!', duration=5)
notify2.show_toast(title='System', msg='Удачного и продуктивного днря, Сергей!)', duration=5)
notify3.show_toast(title='System', msg='Система Запущена!', duration=5) #выполняем команду