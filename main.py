import threading
import random
import math
import time

#                           1 задание

# # Глобальные переменные для хранения данных и результатов
# data_list = []
# sum_result = 0
# mean_result = 0

# # Функция для заполнения списка случайными числами
# def fill_list():
#     global data_list
#     data_list = [random.randint(1, 100) for _ in range(10)]
#     print(f"Список заполнен: {data_list}")

# # Функция для нахождения суммы элементов списка
# def calculate_sum():
#     global data_list, sum_result
#     sum_result = sum(data_list)
#     print(f"Сумма элементов списка: {sum_result}")

# # Функция для нахождения среднеарифметического значения списка
# def calculate_mean():
#     global data_list, mean_result
#     mean_result = sum(data_list) / len(data_list)
#     print(f"Среднеарифметическое значение списка: {mean_result}")

# # Основная функция, которая управляет потоками
# def main1():
#     # Создаем три потока
#     thread1 = threading.Thread(target=fill_list)
#     thread2 = threading.Thread(target=calculate_sum)
#     thread3 = threading.Thread(target=calculate_mean)

#     # Запускаем первый поток
#     thread1.start()

#     # Ждем, пока список будет заполнен
#     thread1.join()

#     # Запускаем оставшиеся два потока
#     thread2.start()
#     thread3.start()

#     # Ждем завершения работы всех потоков
#     thread2.join()
#     thread3.join()

#     # Выводим результаты
#     print(f"Итоговый список: {data_list}")
#     print(f"Сумма элементов списка: {sum_result}")
#     print(f"Среднеарифметическое значение списка: {mean_result}")


# main1()

#                                   2 задание

# Глобальные переменные для хранения данных и результатов
numbers = []
prime_numbers = []
factorials = []

user_path = input("Введите название тестового файла для заполнения числами: ") 

# Функция для чтения пути к файлу с числами
def read_input_file():
    global numbers
    global user_path
    with open(user_path, 'r') as file:
        numbers = [int(num) for num in file.read().strip().split()]
        
read_input_file()   # Вызываем функцию что бы заполнить массив numbers.

# Функция для заполнения файла случайными числами
def fill_file():
    global user_path
    with open(user_path, 'w') as file:
        for _ in range(10):
            num = random.randint(1, 100)
            file.write(f"{num}\n")

# Функция для нахождения простых чисел
def find_primes():
    global numbers, prime_numbers
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)

    # Запись найденных простых чисел в файл output_primes.txt
    with open('output_primes.txt', 'w') as file:
        file.write("\n".join(map(str, prime_numbers)))

# Функция для проверки числа на простоту
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Функция для вычисления факториалов чисел
def calculate_factorials():
    global numbers, factorials
    for num in numbers:
        factorial = math.factorial(num)
        factorials.append(factorial)

    # Запись вычисленных факториалов в файл output_factorials.txt
    with open('output_factorials.txt', 'w') as file:
        file.write("\n".join(map(str, factorials)))

# Основная функция, которая управляет потоками
def main2():
    # Поток для заполнения файла случайными числами
    fill_file_thread = threading.Thread(target=fill_file)

    # Потоки для нахождения простых чисел и вычисления факториалов
    find_primes_thread = threading.Thread(target=find_primes)
    calculate_factorials_thread = threading.Thread(target=calculate_factorials)

    # Запускаем поток для заполнения файла случайными числами
    fill_file_thread.start()
    fill_file_thread.join()  # Ждем завершения заполнения файла

    # Запускаем потоки для нахождения простых чисел и вычисления факториалов
    find_primes_thread.start()
    calculate_factorials_thread.start()

    # Ждем завершения работы всех потоков
    find_primes_thread.join()
    calculate_factorials_thread.join()

    # Выводим статистику выполненных операций
    print(f"Найденные простые числа: {prime_numbers}")
    print(f"Вычисленные факториалы: {factorials}")
    print(f"Количество найденных простых чисел: {len(prime_numbers)}")
    print(f"Количество вычисленных факториалов: {len(factorials)}")
    
main2()

