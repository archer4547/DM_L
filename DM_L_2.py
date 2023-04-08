# Задача про покриття. Метод мінімального стовпчика - максимального рядка

# 7 підмножин A
N = 7

# варіант завдання - 8
A1 = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1]
A2 = [0, 1, 0, 1, 0, 0, 1, 0, 1, 3]
A3 = [0, 0, 0, 1, 1, 0 ,0, 1, 1, 2]
A4 = [0, 0, 1, 0, 0, 1, 0, 0, 1, 2]
A5 = [1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
A6 = [1, 0, 1, 1, 0, 0, 0, 0, 0, 2]
A7 = [1, 0, 1, 0, 1, 1, 0, 1, 0, 3]

# покриття
D = []

# Утворення списку з іменами A
A_names = []   
for key in range(1, N+1, 1):
    try:
        globals()[f"A{key}"]
        A_names.append(f"A{key}")
    except:
        pass

# Основний код
def main():
    
    # Знаходити мінімальні стовпчики й максимальні рядки поки не буде змін у покриттях
    while True:
        possible_rows = min_s()
        if max_r(possible_rows):
            break
    
    # Обчислити ціну покриття
    price = 0
    for i in D:
        price += globals()[i][0]
    
    # Вивести інформацію про покриття
    print("Покриття: {", ", ".join(D), "}")
    print(f"Кількість елементів: {len(D)}")
    print(f"Ціна: {price}")
        

# Функція для знаходження мінімального стовпця
def min_s():
    
    index = 0
     
    # Пошук стовпця з мінімальним числом одиниць 
    min_count = len(A_names)      
    for s in range(len(A1)):
        count = 0
        for A in A_names:
            if globals()[A][s]:
                count += 1
        if count < min_count:
            index = s
            min_count = count
    
    # Знаходження можливих максимальних рядків з цим стовпчиком
    possible_rows = []
    for A in A_names:
        if globals()[A][index] == 1:
            possible_rows.append(A)
        globals()[A].pop(index)
        
    return possible_rows
            
        
def max_r(possible_rows):
    
    # Пошук рядка з максимальним числом одиниць
    max_count = 0
    for row in possible_rows:
        if sum(globals()[row]) - globals()[row][len(globals()[row]) - 1] > max_count:
            max_count = sum(globals()[row]) - globals()[row][len(globals()[row]) - 1]
            max_row = row
      
    # Пошук стовпців які потрібно викреслити 
    try:
        indexes = [] 
        D.append(max_row)
        for index in range(len(globals()[max_row]) - 2):
            if globals()[max_row][index]:
                indexes.append(index)
    except:
        return True
         
    # Викреслення стовпців
    for index in reversed(indexes):
        for A in A_names:
            globals()[A].pop(index)

    
# Запуск програми
if __name__ == "__main__":
    main()
