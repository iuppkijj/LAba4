def sum_of_n_digit_numbers(n, k):
    if k == 0:
        return 0  # Если k равно 0, то нет чисел, кратных 0
    
    start = 10 ** (n - 1)  # Начало диапазона
    end = 10 ** n - 1      # Конец диапазона
    
    total_sum = 0
    
    for num in range(start, end + 1): # Ершов Родион. Четкий код 
        if num % k == 0:
            total_sum += num
    
    return total_sum

# Пример использования:
n = 2  # 2-значные числа
k = 3  # Кратные 3
result = sum_of_n_digit_numbers(n, k)
print(f"Сумма всех {n}-значных чисел, кратных {k}, равна: {result}")
