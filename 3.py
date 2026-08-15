import re

def normalize_phone(phone_number):
    pattern = r"[^\d+]" #Створюємо патерн, де виділяємо все крім цифр та "+"
    repl=""
    phone_number=re.sub(pattern, repl, phone_number) #За допомогою патерна все крім цифр та "+" видаляємв
    match=re.search("\+38", phone_number)
    match_2=re.search("38", phone_number) #Створюємо дві перевіки на наявність на початку номера +38 або 38
    if match:
        return phone_number #Якщо на початку є"+38" - просто повртаємо
    elif match_2:
        return "+" + phone_number #Якщо на почаку є лише "38" додаємо + і повертаємо
    else:
        return "+38"+phone_number #Якщо на почаку немає нічого з вище вказаого додаємо +38
        
     
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
