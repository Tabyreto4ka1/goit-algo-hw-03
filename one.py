from datetime import datetime


def get_days_from_today(date): #Створюємо функцію
    try: 
        date = datetime.strptime(date, "%Y-%m-%d").date()#Дату з рядка переводимо в datetime у потрібному форматі
    except ValueError:
         return "Невірий формат" #Якщо при спробі отимати форма datetime трапиться помилка повертаємо  "невірний формат", щоб функція нне впала
    today = datetime.today() #Взнаємо поточну дату
    today_date= today.date() #Беремо саме дату без часу
    return (today_date - date).days # Повертаємо кількість днів від заданої дати до поточної


print(get_days_from_today('13.14.2000'))
