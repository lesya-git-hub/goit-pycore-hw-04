#Функція total_salary(path) приймає один аргумент - шлях до текстового файлу (path), 
#який містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
def total_salary(path):
#Функція аналізує файл, обчислює загальну та середню суму заробітної плати.
#Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.
    total_salary = 0.0
    worker_count = 0
    worker_name = ''
    average_salary = 0.0
    try:
        with open(path, 'r', encoding='utf-8') as file:
           for line in file:
               try:
                   worker_name, salary = line.strip().split(',')
                   total_salary += float(salary)
                   worker_count += 1
               except ValueError:
                    continue
               if worker_count == 0:
                   print("Не знайдено списку робітників")
                   return 0, 0
           average_salary = float(total_salary/worker_count)
           return total_salary, average_salary
    except FileNotFoundError:
        print("File not found, please check the path to the file")
        return 0, 0 

total_salary, average_salary = total_salary('worker_salary.txt')
print(f'Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {average_salary}')


