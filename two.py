import random

def get_numbers_ticket(min, max, quantity):
    numbers=[]
    if min > max or min<1 or max > 1000 or quantity<1 or quantity > max-min+1: #перевірка усіх вимог параметрів функції
        return [] #Повертаємо просто пустий список
    else:
        numbers=list(range(min, max+1)) #Сворюємо список з вказаим діапазоном(+1 щоб було включно вказано параметра )
        lucky_numbers=random.sample(numbers, k=quantity)  # Отримуємо випадкові але унікальні числа зі списку
        return sorted(lucky_numbers)  #Сортуємо та повертаємо


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
