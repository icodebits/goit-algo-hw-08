import heapq

def minimize_cost(cable_lengths):
    # Ініціалізуємо купу
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    
    # Поки купа має більше одного елемента
    while len(cable_lengths) > 1:
        # Вибираємо два найдовші кабелі
        cable1 = heapq.heappop(cable_lengths)
        cable2 = heapq.heappop(cable_lengths)
        
        # Об'єднуємо кабелі та додаємо їх довжину до загальних витрат
        combined_length = cable1 + cable2
        total_cost += combined_length
        
        # Додаємо об'єднаний кабель назад до купи
        heapq.heappush(cable_lengths, combined_length)
    
    return total_cost

# Приклад використання
cable_lengths = [8, 4, 6, 12]
min_cost = minimize_cost(cable_lengths)
print("Загальні витрати на об'єднання кабелів:", min_cost)
